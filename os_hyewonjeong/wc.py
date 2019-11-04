import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import numpy as np

filename = 'cheese.txt'
figname = 'test.jpg'
resultname = 'cheese_wc.png'

text = open(filename, encoding='utf-16').read()
cheese_mask = np.array(Image.open(figname))
image_colors = ImageColorGenerator(cheese_mask)

wc = WordCloud(mask=cheese_mask, background_color='white')
wordcloud = wc.generate(text)

plt.figure(figsize=(12,12))
plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation='bilinear')
plt.axis('off')
plt.savefig(resultname)