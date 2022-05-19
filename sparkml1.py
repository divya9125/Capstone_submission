#!/usr/bin/env python
# coding: utf-8

# In[21]:


from pyspark.sql import SparkSession
spark=(SparkSession.builder.appName("CapstoneML").config("hive.metastore.uris","thrift://ip-10-1-2-24.ap-south-1.compute.internal:9083").enableHiveSupport().getOrCreate())


# In[22]:


spark


# In[23]:


import pandas as pd


# In[24]:


var6=spark.sql("select ee.emp_no,ee.emp_titles_id,ee.birth_date,ee.first_name,ee.last_name,ee.sex,ee.hire_date,ee.no_of_projects,ee.last_performance_rating,ee.left_company,ee.last_date,s.salary,t.title,d.dept_name from anabig114243.employees ee full outer join anabig114243.salaries s  on s.emp_no=ee.emp_no full outer join anabig114243.titles t on ee.emp_titles_id=t.title_id full outer join anabig114243.dept_managers dm on ee.emp_no=dm.emp_no full outer join anabig114243.departments d on dm.dept_no=d.dept_no")


# In[25]:


var7=var6.toPandas()
var7


# In[43]:


var8=var7.drop(['first_name','last_name','emp_no','emp_titles_id','birth_date','hire_date','last_date',],axis='columns')


# In[31]:


from sklearn.ensemble import RandomForestClassifier
import numpy as np
np.random.seed(0)
from pyspark.mllib.stat import Statistics
import matplotlib.pyplot as plt
import seaborn as sns


# In[44]:


#Check for Missing Values
var8.isnull().any()


# In[45]:


var8.dtypes


# In[34]:


# 0-Those who are still working and 1-those who left the company  
var8['left_company'].value_counts()


# #### those who left the company are less than 1 percent

# In[35]:


var8.groupby('dept_name').mean()


# In[46]:


var8.groupby('salary').mean()


# In[47]:


var8.groupby('sex').mean()


# In[48]:




#Bar chart for department employee work for and the frequency of turnover
pd.crosstab(var8.dept_name,var8.left_company).plot(kind='bar')
#plt.title('Department')
#plt.xlabel('Department')
#plt.ylabel('Frequency of Turnover')
#plt.savefig('department_bar_chart')


# In[63]:


pd.crosstab(var8.title,var8.left_company).plot(kind='bar')


# ### Employee who left the company depends on the department they work for. Thus, department can be a good predictor of the outcome variable.

# In[49]:


#Histogram of numeric variables
num_bins = 10

var8.hist(bins=num_bins, figsize=(20,15))
plt.savefig("var8_histogram_plots")
plt.show()


# In[66]:


cat_vars2=['sex','last_performance_rating','title','dept_name',]
for var in cat_vars2:
    cat_list2='var'+'_'+var
    cat_list2 = pd.get_dummies(var8[var], prefix=var)
    var9=var8.join(cat_list2)
    var8=var9
    


# In[67]:


var8.columns.values


# In[68]:


var10=var8.drop(['sex_'],axis='columns')


# In[69]:


var10.columns.values


# In[93]:


var11=var10.drop(['last_performance_rating_','title'],axis='columns')


# In[94]:


var11.columns.values


# In[96]:


var12=var11.columns.values.tolist()
y=['left_company']
X=[i for i in var12 if i not in y]


# In[106]:


type(var11)


# In[98]:


X


# In[104]:


var11=var11.fillna(0)


# In[105]:


var11.isnull().any()


# In[108]:


from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

#Recursive Feature Elimination (RFE)
model = LogisticRegression()

rfe = RFE(model, 10)
rfe = rfe.fit(var11[X],var11[y])
print(rfe.support_)
print(rfe.ranking_) 


# In[110]:


X


# In[111]:



cols=['no_of_projects', 'salary', 'sex_F', 'sex_M', 'last_performance_rating_A','last_performance_rating_B',
      'last_performance_rating_C','last_performance_rating_PIP','last_performance_rating_S','dept_name_Finance' ] 
X=var11[cols]
y=var11['left_company']


# In[113]:


#Split data into training and test samples
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)


# In[114]:


#Logistic Regression Classifier
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
logreg = LogisticRegression()
logreg.fit(X_train, y_train)


# In[115]:


from sklearn.metrics import accuracy_score
print('Logistic regression accuracy: {:.3f}'.format(accuracy_score(y_test, logreg.predict(X_test))))


# In[122]:


#Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
rf.fit(X_train, y_train)


# In[119]:


print('Random Forest Accuracy: {:.3f}'.format(accuracy_score(y_test, rf.predict(X_test))))


# In[120]:


#SVM Classifier
from sklearn.svm import SVC
svc = SVC()
svc.fit(X_train, y_train)


# In[121]:


print('Support vector machine accuracy: {:.3f}'.format(accuracy_score(y_test, svc.predict(X_test))))


# ### Using logistic regression and svm classifier accuracy is 0.90 while using random forest it is coming out 0.84
# ### logistic and svm are better in this case than random forest
