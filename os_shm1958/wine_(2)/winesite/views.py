from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from django.template import loader
from sklearn.externals import joblib

import os
import pandas as pd
import numpy as np





def index(request):

	template = loader.get_template('winesite/index.html')
	context = {
		'latest_question_list': "test",
	}

	return HttpResponse(template.render(context, request))


def predict(request):
	param_list = ['sex','age','martial','job']
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

	#estimator = joblib.load('/home/pirl/django-apps/wine/winesite/machine/wine_exam.pkl')
	estimator = joblib.load('./winesite//machine/wine_exam.pkl')
	print(valname_list)
	x_test = [val_list]

	y_predict = estimator.predict(x_test)
	return render(request, 'winesite/predict.html', {'y_predict':y_predict, 'valname_list':valname_list})