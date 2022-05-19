#!/usr/bin/env python
# coding: utf-8

# In[12]:


from pyspark.sql import SparkSession
spark=(SparkSession.builder.appName("Capstone").config("hive.metastore.uris","thrift://ip-10-1-2-24.ap-south-1.compute.internal:9083").enableHiveSupport().getOrCreate())


# In[13]:


spark


# ### Q1 A list showing employee number, last name, first name, sex, and salary for each employee

# In[17]:


spark.sql("select e.emp_no,e.last_name,e.first_name,e.sex,s.salary from anabig114243.employees e join anabig114243.salaries s on e.emp_no=s.emp_no ").show()


# ### Q2 A list showing first name, last name, and hire date for employees who were hired in 1986.

# In[18]:



spark.sql("select first_name,last_name,substr(hire_date,7,10)as hire_date from anabig114243.employees where substr(hire_date,7,10)='1986'").show() 


# ### Q3 A list showing the manager of each department with the following information: department number, department name,the manager's employee number, last name, first name.

# In[21]:


spark.sql("select d.dept_name,d.dept_no,dm.emp_no,ee.last_name,ee.first_name,tt.title from anabig114243.departments d join anabig114243.dept_managers dm on d.dept_no=dm.dept_no join anabig114243.employees ee on dm.emp_no=ee.emp_no join anabig114243.titles tt on ee.emp_titles_id=tt.title_id group by d.dept_name,d.dept_no,dm.emp_no,ee.last_name,ee.first_name,tt.title ").show()


# ### Q4 select d.dept_name,ee.emp_no,ee.last_name,ee.first_name from employees ee join dept_managers dm on ee.emp_no=dm.emp_no join departments d on d.dept_no=dm.dept_no

# In[22]:


spark.sql("select d.dept_name,ee.emp_no,ee.last_name,ee.first_name from anabig114243.employees ee join anabig114243.dept_managers dm on ee.emp_no=dm.emp_no join anabig114243.departments d on d.dept_no=dm.dept_no").show()


# ### Q5 A list showing first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B.“

# In[24]:


spark.sql("select first_name,last_name, sex from anabig114243.employees where upper(first_name) like 'HERCULES%' and upper(last_name) like 'B%' ").show()


# ### Q6  A list showing all employees in the Sales department, including their employee number, last name, first name, and department name.

# In[25]:


spark.sql("select d.dept_name,ee.emp_no,ee.last_name,ee.first_name,dept_name from anabig114243.employees ee join anabig114243.dept_managers dm on ee.emp_no=dm.emp_no join anabig114243.departments d on d.dept_no=dm.dept_no where upper(d.dept_name) like 'SALES%'").show()


# ### Q7  A list showing all employees in the Sales and Development departments, including their employee number, last name,first name, and department name.

# In[26]:


spark.sql("select d.dept_name,ee.emp_no,ee.last_name,ee.first_name from anabig114243.employees ee join anabig114243.dept_managers dm on ee.emp_no=dm.emp_no join anabig114243.departments d on d.dept_no=dm.dept_no where upper(d.dept_name) like 'SALES%' or upper(d.dept_name) like 'DEVELOPMENT%'").show()


# ### Q8  select last_name,count(last_name)as counts from employees group by last_name having counts>1 order by counts desc 

# In[27]:


spark.sql("select last_name,count(last_name)as counts from anabig114243.employees group by last_name having counts>1 order by counts desc").show()


# ### Q9 Histogram to show the salary distribution among the employees 

# In[36]:


var1=spark.sql("select salary,emp_no from anabig114243.salaries group by salary,emp_no")
var2=var1.toPandas()


# In[33]:


import matplotlib.pyplot as plt


# In[35]:


plt.hist(var2['salary'])


# ### Q10 Bar graph to show the Average salary per title (designation)

# In[45]:


var3=spark.sql("select tt.title,round(avg(s.salary)) as sal from anabig114243.salaries s join anabig114243.employees ee on s.emp_no=ee.emp_no join titles tt on ee.emp_titles_id=tt.title_id group by tt.title")
var4=var3.toPandas()


# In[46]:


var4.plot.bar(x='title', y=('sal')) 


# In[ ]:




