# Capstone_submission

### Project Intro ###
In this project, I have to design data model with all the tables to hold data,
import the CSVs into a SQL database, transfer SQL database to HDFS/Hive, and perform analysis using
Hive/Impala/Spark/SparkML using the data and create data and ML pipelines


### Project Objective: As part of this project ###
1. Create data model as per your understanding from the data (you are required include tables names, relation between
tables, column names, data types, primary & foreign keys etc.)
2. Create database & tables in MySQL server as per the above ER Diagram
3. Create Sqoop job to transfer the data from MySQL to HDFS (Data required to store in Parque/Avro/Json format)
4. Create database in Hive as per the above ER Diagram and load the data into Hive tables
5. Work on Exploratory data analysis as per the analysis requirement using Impala and Spark SQL (expecting to get the data
from hive tables).
6. Build ML Model as per the requirement.
7. Create entire data pipeline and ML pipe line


### Technology Stack ###
you are required to work on below technology Stack.
- MySQL (to create database)
- Linux Commands
- Sqoop (Transfer data from MySQL Server to HDFS/Hive)
- HDFS (to store the data)
- Hive (to create database)
- Impala (to perform the EDA)
- SparkSQL (to perform the EDA)
- SparkML (to perform model building)


### Data Description ###
a. Titles 
title_id – Unique id of type of employee (designation id) – Character – Not Null
title – Designation – Character – Not Null

b. Employees 
emp_no – Employee Id – Integer – Not Null
emp_titles_id – designation id – Not Null
birth_date – Date of Birth – Date Time – Not Null
first_name – First Name – Character – Not Null
last_name – Last Name – Character – Not Null
sex – Gender – Character – Not Null
hire_date – Employee Hire date –Date Time -Not Null
no_of_projects – Number of projects worked on – Integer – Not Null
Last_performance_rating – Last year performance rating – Character – Not Null
left – Employee left the organization – Boolean – Not Null
Last_date - Last date of employment (Exit Date) – Date TimeData Description

c. Salaries 
emp_no – Employee id – Integer – Not Null
Salary – Employee’s Salary – Integer – Not Null

d. Departments
dept_no - Unique id for each department – character – Not Null
dept_name – Department Name – Character – Not Null

e. Department Managers
dept_no - Unique id for each department – character – Not Null
emp_no – Employee number (head of the department ) – Integer – Not Null

f. Department Employees 
emp_no – Employee id – Integer – Not Null
dept_no - Unique id for each dep
