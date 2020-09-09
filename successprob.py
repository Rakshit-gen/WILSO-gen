import pandas as pd
import random
import numpy as np
from sklearn.linear_model import LogisticRegression
df=pd.read_csv('success.csv')                                  #firstly create a file named success in excel and save it as a csv file and store some data in it
def data_split(data,ratio):
    np.random.seed(42)
    shuffle=np.random.permutation(len(data))
    testsize=int(len(data)*ratio)
    train_ind=shuffle[testsize:]
    test_ind=shuffle[:testsize]
    return data.iloc[train_ind],data.iloc[test_ind]
train,test=data_split(df,0.2)
x_train=train[['Confidence','Enthusiasm','Hard work']].to_numpy()
x_test=test[['Confidence','Enthusiasm','Hard work']].to_numpy()
y_train=train[['probability']].to_numpy().reshape(24,)
y_train=train[['probability']].to_numpy().reshape(24,)
clf=LogisticRegression()
clf.fit(x_train,y_train)
while True:
    a=float(input('Confidence'))
    b=float(input('Enthusiasm'))
    c=float(input('Hard work'))
    if a>10 or b>10 or c>10:
        print('****Error in given data****')
    else:
        inputf=[a,b,c]
        infp=clf.predict_proba([inputf])[0][1]
        print(f'Your chances of getting success {infp*100}%')
        i=input('For continuing press c else press q for quit')
        if i=='q':
            break
            
        elif i=='c':
            continue
exit()
