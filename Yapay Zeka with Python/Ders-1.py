import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
"""Ders-6 Kütüphanelerin Yüklenmesi"""
"""Kütüphaneler"""

"""Kod"""
"""Ders-7 Dışarıdan Verileri Yükleme"""
 
veriler = pd.read_csv("veriler.csv")

print(veriler)

"""Ön İşleme"""
boy = veriler[['boy']]
print(boy)

boykilo = veriler[['boy', 'kilo']]
print(boykilo)

x = 10

class insan:
    boy = 180
    def kosmak(self,b):
        return b + 10
ali = insan()
print(ali.boy)
print(ali.kosmak(90))


l = [1,2,3]





