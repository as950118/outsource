#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
import numpy as np
import tensorflow.keras as keras
from tensorflow.keras import models, layers


# In[2]:


import pandas as pd
import os

def load_income_data(income_path):
    csv_path = os.path.join(income_path,
                            "Adult Census Income Binary Classification dataset.csv")
    return pd.read_csv(csv_path)


# In[3]:


income = load_income_data(".")


# In[4]:


len(income)


# In[5]:


income.head()


# In[6]:


income.info()


# In[8]:


income["native-country"].value_counts()


# In[9]:


income.describe()


# In[10]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
income.hist(bins=50, figsize=(20,15))
plt.show()


# In[11]:


LABEL_COLUMN = 'income'
LABLES = [0,1]


# In[12]:


def get_dataset(file_path, **kwargs):
    dataset = tf.data.experimental.make_csv_dataset(file_path,
                                                    batch_size=32, # Artificially small to make examples easier to show.
                                                    label_name=LABEL_COLUMN,
                                                    na_value="?",
                                                    num_epochs=1,
                                                    ignore_errors=True,
                                                    **kwargs)
    return dataset


# In[15]:


PATH = './Adult Census Income Binary Classification dataset.csv'
raw_train_data = get_dataset(PATH)


# In[16]:


def show_batch(dataset):
    for batch, label in dataset.take(1):
        for key, value in batch.items():
            print("{:20s}: {}".format(key,value.numpy()))
        print("label: ",label.numpy())


# In[17]:


show_batch(raw_train_data)


# In[18]:


conti_var = income.columns[income.dtypes != 'object']
list(conti_var)


# In[19]:


class PackNumericFeatures(object):
    def __init__(self, names):
        self.names = names

    def __call__(self, features, labels):
        numeric_freatures = [features.pop(name) for name in self.names]
        numeric_features = [tf.cast(feat, tf.float32) for feat in numeric_freatures]
        numeric_features = tf.stack(numeric_features, axis=-1)
        features['numeric'] = numeric_features
        
        matches = tf.equal(' >50K', labels)
        onehot = tf.cast(matches, tf.float32)
        labels = onehot
        
        return features, labels


# In[20]:


NUMERIC_FEATURES = list(conti_var)

packed_train_data = raw_train_data.map(PackNumericFeatures(NUMERIC_FEATURES))


# In[21]:


show_batch(packed_train_data)


# In[22]:


example_batch, labels_batch = next(iter(packed_train_data))


# In[23]:


desc = income[NUMERIC_FEATURES].describe()
desc


# In[24]:


MEAN = np.array(desc.T['mean'])
STD = np.array(desc.T['std'])


# In[25]:


def normalize_numeric_data(data, mean, std):
    return (data-mean)/std


# In[26]:


import functools
normalizer = functools.partial(normalize_numeric_data, mean=MEAN, std=STD)  # 함수에 mean 에는 MEAN을, std에는 STD를 결합시켜줌

numeric_column = tf.feature_column.numeric_column('numeric', normalizer_fn=normalizer, shape=[len(NUMERIC_FEATURES)])
numeric_columns = [numeric_column]
numeric_column


# In[27]:


example_batch['numeric']


# In[28]:


numeric_layer = tf.keras.layers.DenseFeatures(numeric_columns)
numeric_layer(example_batch).numpy()


# In[29]:


categorical = list(income.columns[income.dtypes == 'object'])
categorical


# In[30]:


income["education-num"].value_counts().keys()


# In[31]:


def get_keys(data, feature):
    return list(income[feature].value_counts().keys())


# In[32]:


get_keys(income, "workclass")


# In[33]:


def get_categories(data, c_list):
    category = {}
    for i in c_list[:-1]:
        category[i] = get_keys(data, i)
    return category


# In[34]:


CATEGORIES = get_categories(income, categorical)
CATEGORIES['workclass']


# In[35]:


categorical_columns = []
for feature, vocab in CATEGORIES.items():
    cat_col = tf.feature_column.categorical_column_with_vocabulary_list(key=feature, 
                                                                        vocabulary_list=vocab)
    categorical_columns.append(tf.feature_column.indicator_column(cat_col))


# In[36]:


categorical_columns[0]


# In[37]:


categorical_layer = tf.keras.layers.DenseFeatures(categorical_columns)
print(categorical_layer(example_batch).numpy()[0])


# In[38]:


preprocessing_layer = tf.keras.layers.DenseFeatures(categorical_columns+numeric_columns)


# In[39]:


print(preprocessing_layer(example_batch).numpy()[0])


# In[40]:


train_data = packed_train_data.take(900).shuffle(100)
test_data = packed_train_data.skip(900)


# In[41]:


model = tf.keras.Sequential([
    preprocessing_layer,
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy'])


# In[42]:


model.fit(train_data, epochs=20)


# In[43]:


test_loss, test_accuracy = model.evaluate(test_data)

print('\n\nTest Loss {}, Test Accuracy {}'.format(test_loss, test_accuracy))


# In[44]:


predictions = model.predict(test_data)

# Show some results
for prediction, survived in zip(predictions[:32], list(test_data)[0][1]):   # outcome of one batch
    print("Predicted income: {:.2%}".format(prediction[0]),
        " | Actual outcome: ",
        ("more than 50K" if bool(survived) else "50K or less"))


# In[ ]:




