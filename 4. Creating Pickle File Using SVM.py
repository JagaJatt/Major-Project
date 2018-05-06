import cv2
import numpy as np
from sklearn import preprocessing, cross_validation, svm, neighbors, cluster
import pickle

path='D:\\vb Workz\\8th sem\\major proj2\\HOG_database\\'

x=[]
y=[]
Z=[]
count=0
for i in range(1,5):
    name=str(i)+'\\'
    path1=path+name
    count+=1
    for j in range(1,51):
        name='new'+str(j)+'.txt'
        f1=open(path1+name,'r')
        a=f1.readlines()
        f1.close()
        b=a[0]
        c=b.split(',')
        c=c[:-1]
    ##        for li in range(len(c)):
    ##            c[li]=int(c[li])
        x.append(c)
        y.append(count)


clf = svm.SVC(kernel='linear', probability=True)
clf.fit(x,y)
with open('svm.pickle','wb')as f:
    pickle.dump(clf, f)
#clf = pickle.load(open('svm.pickle', 'rb'))

y1=[];
count=0;
for i in range(1,5):
    name=str(i)+'\\'
    path1=path+name
    count+=1
    for j in range(1,51):
        name='new'+str(j)+'.txt'
    ##        print(path1+name)
        f1=open(path1+name,'r')
        a=f1.readlines()
        f1.close()
        b=a[0]
        c=b.split(',')
        c=c[:-1]
    ##        for li in range(len(c)):
    ##            c[li]=int(c[li])
        Z.append(c)
        y1.append(count)
    
z=clf.predict(Z)
#print(z)
e=(y1-z)
e=list(e)
#print(e)

per=(e.count(0)/len(e))*100
print('Accuracy: '+str(per)+'%')
