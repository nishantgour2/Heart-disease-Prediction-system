from django.shortcuts import render

# from django.core import serializers

import pickle
from sklearn.externals import joblib

# from rest_framework.views import APIView
# from rest_framework.response import Response

# import json
# import numpy as np
# from sklearn import preprocessing
# import pandas as pd
# from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
# from rest_framework.decorators import api_view


# Create your views here.

def index(request):
    return render (request,"index.html")

def index2(request):
    return render (request,"work.html")

# def index1(request):
    # return render (request,"d.html")   


# @api_view(['GET'])
# def approvereject(request):
def index1(request):
    one = request.GET['one']
    two = request.GET['two']
    three = request.GET['three']
    four = request.GET['four']
    five = request.GET['five']
    six = request.GET['six']
    seven = request.GET['seven']
    eight = request.GET['eight']
    nine = request.GET['nine']
    ten = request.GET['ten']

    l=[]
    l=[float(one),float(two),float(three),float(four),float(five),float(six),float(seven),float(eight),float(nine),float(ten)]
    mod = joblib.load("D:\Jupyter\Heart_model.pkl")
    fin=mod.predict([l])
    return render (request,"d.html",{"fin":fin}) 
    print(mod)

