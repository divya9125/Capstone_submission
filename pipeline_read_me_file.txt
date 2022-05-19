Run the following Commands in the given order

1)Login to mysql
mysql -u anabig114243 -pBigdata123

2)show databases;
use anabig114243;

3) Create tables for retail data using codes
a. upload mysqlquery.sql to ftp 

b. run the below command to create tables under 
source mysqlquery.sql 

c.exit from mysql by using below given command.
quit

4) Run the sqoop command to transfer the data from rdbms to hdfs
sqoop import-all-tables  -Dorg.apache.sqoop.splitter.allow_text_splitter=true --connect jdbc:mysql://ip-10-1-1-204.ap-south-1.compute.internal:3306/anabig114243 --username anabig114243 --password Bigdata123 --compression-codec=snappy --as-avrodatafile --warehouse-dir=/user/anabig114243/hive/warehouse --driver com.mysql.jdbc.Driver 

5)Put all the avsc files over hdfs

hdfs dfs -put departments.avsc
hdfs dfs -put titles.avsc
hdfs dfs -put dept_employees.avsc
hdfs dfs -put dept_managers.avsc
hdfs dfs -put employees.avsc
hdfs dfs -put salaries.avsc


6) Run the following command to create hive table.
hive -f impala.sql

10) Run the following command to run the analysis on the tables we have created in hive and the save the query in output_hive_tables.txt

hive -f output_impala.sql > output_hive_tables.txt

11) Run the following command to execute sparksql queries
spark-submit sparksql.py

12) Run the following command to execute sparkml models
spark-submit sparkml.py



