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

sonuc = pd.DataFrame(data=ulke, index=range(22), columns=['fr','tr','us'])
print(sonuc)

sonuc2 =pd.DataFrame(data=Yas, index=range(22),columns=['boy','kilo','yas'])
print(sonuc2)

cinsiyet = veriler.iloc[:,-1].values
sonuc3 = pd.DataFrame(data=cinsiyet,index=range(22),columns=['cinsiyet'])
print(sonuc3)

s =pd.concat([sonuc,sonuc2],axis=1)
print(s)

s2=pd.concat([s,sonuc3],axis=1)
print(s2)

"""sklearn.model_selection a bağlanıp test işlemi gerçekleştirmek için aşağıda ki kodları yazıyoruz"""
from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(s,sonuc3,test_size=0.33,random_state=0)