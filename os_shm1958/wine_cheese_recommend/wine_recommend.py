import pandas as pd
#import numpy as np
#import statistics
#import matplotlib.pyplot as plt
#import matplotlib

#plt.rc('font',family='Malgun Gothic')
#plt.rc('font',family='NanumBarunGothic')

class WineRecommend:
    def __init__(self):
        self.wine_test = pd.read_csv('customer_group.csv',encoding = 'cp949')
        for i in range(64):
            self.wine_test['wine_classified'][i] = self.wine_test['wine_classified'][i].split()
        for i in range(len(self.wine_test['wine_classified'])):
            self.wine_test['wine_classified'][i] = map(int, self.wine_test['wine_classified'][i])
            self.wine_test['wine_classified'][i] = list(map(int, self.wine_test['wine_classified'][i]))

    def wine_side_recommend(self, info):
        alpha = ['A','B','C','D','E','F','G','H']
        wine1 = ['B','C']
        wine2 = ['A','F','H']
        wine3 = ['D','E']
        wine4 = ['G']

        side1=['Brie','Gorgonzola']
        side2=['Camenbert','Cheddar','Annon']
        side3=['Ricotta','Roquefort']
        side4=['Valencay']

        wine_list=[]
        find_id = self.wine_test[(self.wine_test['age']==info[0]) & (self.wine_test['gender']==info[1]) & (self.wine_test['job']==info[2]) & (self.wine_test['marital']==info[3])].index
        input_list = self.wine_test.loc[find_id,'wine_classified'].values.tolist()[0]

        max_3_index = sorted(range(len(input_list)), key=lambda i: input_list[i])[-3:]
        max_3_index = reversed(max_3_index)

        for i in max_3_index:
            wine_list.append(alpha[i])

        if wine_list[0] in wine1:
            side_list=side1
        elif wine_list[0] in wine2:
            side_list=side2
        elif wine_list[0] in wine3:
            side_list=side3
        else:
            side_list=side4

        return wine_list,side_list

if __name__ == "__main__":

    ##age	gender	 job	marital

    ##20대 0  FEMALE 0 임시직 0 MARREID 0
    ##30대 1 MALE 1   자영업 1 SINGLE 1
    ##40대 2         전문직  2
    ##50대 3         회사원  3
    info=[0,1,0,1]
    print("와인을 추천할게요!!{0}".format((WineRecommend.wine_side_recommend(info)[0]))) # 의사결정나무를 이용해서 얻은 기준을 통해 와인 TOP3 선정
    print("와인에 맞는 안주를 추천할게요!!{0}".format(WineRecommend.wine_side_recommend(info)[1])) # TOP1 와인과 어울리는 안주 추천하기