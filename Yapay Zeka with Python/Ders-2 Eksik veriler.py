import numpy as np
import pandas as pd
import matplotlib.pyplot as pl

"""Ders-6 Kütüphanelerin Yüklenmesi"""
"""Kütüphaneler"""

"""Kod"""
"""Ders-7 Dışarıdan Verileri Yükleme"""

veriler = pd.read_csv("eksikveriler.csv")

"""Eksik Verileri Tamamlama"""

"""sci-kit-learn """

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan,strategy='mean')
Yas = veriler.iloc[:,1:4].values

imputer = imputer.fit(Yas[:, 1:4])
Yas[:,1:4] = imputer.transform(Yas[:, 1:4])
print(Yas)