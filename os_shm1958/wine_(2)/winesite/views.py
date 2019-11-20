from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from django.template import loader
from sklearn.externals import joblib

import pandas as pd
import numpy as np

import os
import sys
sys.path.append("./winesite/machine")
import wine_recommend




def index(request):

	template = loader.get_template('winesite/index.html')
	context = {
		'latest_question_list': "test",
	}

	return HttpResponse(template.render(context, request))


def predict(request):
	param_list = ['age','sex','job','martial']
	val_list = []
	valname_list = []
	for x in param_list:
		try:
			temp = list(map(str, request.GET[x].split()))
			val = int(temp[0])
			valname = temp[1]
		except Exception as e:
			print(e)
			val = -1
			valname = "-1"
		val_list.append(val)
		valname_list.append(valname)


	#estimator = joblib.load('./winesite//machine/wine_exam.pkl')
	estimator = wine_recommend.WineRecommend().wine_side_recommend(val_list)

	#이름과 설명 합치기
	wine_list = [[estimator[0][idx], estimator[2][idx]] for idx in range(len(estimator[0]))]
	side_list = [[estimator[1][idx], estimator[3][idx]] for idx in range(len(estimator[1]))]
	return render(request, 'winesite/predict.html', {'wine_list':wine_list,
													 'side_list':side_list,
													 'valname_list':valname_list})