# -*- coding: utf-8 -*-
#Write function bmi that calculates body mass index (bmi = weight / height ^ 2).

#if bmi <= 18.5 return "Underweight"

#if bmi <= 25.0 return "Normal"

#if bmi <= 30.0 return "Overweight"

#if bmi > 30 return "Obese"

from __future__ import division #Para o python 2.7 a divisão só retornar inteiro, usando isso retornar float

def bmi(w,h):
    bmi = float(w/(h*h))
    if bmi <= 18.5: return "Underweight"
    elif bmi <= 25.0: return "Normal"
    elif bmi <= 30.0: return "Overweight"
    else: return "Obese"


#main
weight = float(raw_input("Write your Weight: "))
height = float(raw_input("Write your heigh: "))
print("You are: "+ str(bmi(weight,height)))