#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.metrics import mean_absolute_error,accuracy_score, r2_score
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor


# In[2]:


import pandas as pd
import numpy as np


# In[28]:


import sys
sys.path.append('/Users/chohee/Section3_Project/Flask_Web_Server/')
from preprocessing import Data2


# In[29]:


Data2.precipitation=Data2.precipitation.fillna(0)


# In[30]:


print(Data2)


# In[32]:


print(Data2)


# In[34]:


#test data 분리 
from sklearn.model_selection import train_test_split

train, test = train_test_split(Data2, random_state=2)


# In[35]:


#타겟 데이터 분리 
target='total'
X_train=train.drop(target,axis=1)
y_train=train[target]
X_test=test.drop(target,axis=1)
y_test=test[target]


# In[36]:


print(y_train)


# In[37]:


print(X_train)


# In[38]:


#Base 라인 잡기 - total 가격 평균치 
Base=y_train.mean()
Base


# In[39]:


#기준 모델 검증
y_base_pred=[Base]*len(y_train)
y_test_base_pred=[Base]*len(y_test)
print("기준모델 스코어")
print("훈련데이터")
print("MAE:",mean_absolute_error(y_train,y_base_pred)), print("R2:",r2_score(y_train,y_base_pred))
print("테스트데이터")
print("MAE:",mean_absolute_error(y_test,y_test_base_pred)), print("R2:",r2_score(y_test,y_test_base_pred))


# In[40]:


rf = make_pipeline(
    SimpleImputer(),
    RandomForestRegressor(n_jobs=-1)
)

rf.fit(X_train, y_train);
y_train_pred=rf.predict(X_train)
y_test_pred=rf.predict(X_test)

print("훈련데이터")
print("MAE:",mean_absolute_error(y_train,y_train_pred)), print("R2:",r2_score(y_train,y_train_pred))
print("테스트")
print("MAE:",mean_absolute_error(y_test,y_test_pred)), print("R2:",r2_score(y_test,y_test_pred))


# In[41]:


pip install joblib


# In[45]:


import joblib
joblib.dump(rf,'rf.pkl')


# In[49]:


print(X_train.iloc[:1])


# In[50]:


print(rf.predict(X_train.iloc[:1]))


# In[51]:


print(y_train[1])


# In[ ]:




