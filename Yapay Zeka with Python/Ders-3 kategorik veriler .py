import numpy as np
import pandas as pd
import matplotlib.pyplot as pl



veriler = pd.read_csv("eksikveriler.csv")



from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan,strategy='mean')
Yas = veriler.iloc[:,1:4].values

imputer = imputer.fit(Yas[:, 1:4])
Yas[:,1:4] = imputer.transform(Yas[:, 1:4])

"""tüm kolonu almak için 0:1 kullanıyoruz"""
ulke = veriler.iloc[:,0:1].values


from sklearn import preprocessing

le = preprocessing.LabelEncoder()

ulke[:,0] = le.fit_transform(veriler.iloc[:,0])
print(ulke)


"""fit ve transformu tek bir satırda kullanarak makine öğrenme algoritmasını öğrenecek ülke kolonundan"""
ohe = preprocessing.OneHotEncoder()
"""önce yazılı ülke kolonunun algoritmasını öğrenecek ve bunu 0ve 1 lere çevirecek"""
"""toarray dediğimiz zaman numpy array olarak alıcak"""
ulke =ohe.fit_transform(ulke).toarray()
print(ulke)