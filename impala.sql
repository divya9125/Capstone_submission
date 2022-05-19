use  anabig114243;

drop table departments;
drop table dept_employees;
drop table dept_managers;
drop table employees;
drop table salaries;
drop table titles;

CREATE EXTERNAL TABLE departments STORED AS AVRO LOCATION 'hdfs:///user/anabig114243/hive/warehouse/departments' TBLPROPERTIES ('avro.schema.url'='hdfs:///user/anabig114243/departments.avsc');

CREATE EXTERNAL TABLE dept_employees STORED AS AVRO LOCATION 'hdfs:///user/anabig114243/hive/warehouse/dept_employees' TBLPROPERTIES ('avro.schema.url'='hdfs:///user/anabig114243/dept_employees.avsc');

CREATE EXTERNAL TABLE dept_managers STORED AS AVRO LOCATION 'hdfs:///user/anabig114243/hive/warehouse/dept_managers' TBLPROPERTIES ('avro.schema.url'='hdfs:///user/anabig114243/dept_managers.avsc');

CREATE EXTERNAL TABLE employees STORED AS AVRO LOCATION 'hdfs:///user/anabig114243/hive/warehouse/employees' TBLPROPERTIES ('avro.schema.url'='hdfs:///user/anabig114243/employees.avsc');

CREATE EXTERNAL TABLE salaries STORED AS AVRO LOCATION 'hdfs:///user/anabig114243/hive/warehouse/salaries' TBLPROPERTIES ('avro.schema.url'='hdfs:///user/anabig114243/salaries.avsc');

CREATE EXTERNAL TABLE titles STORED AS AVRO LOCATION 'hdfs:///user/anabig114243/hive/warehouse/titles' TBLPROPERTIES ('avro.schema.url'='hdfs:///user/anabig114243/titles.avsc');

select e.emp_no,e.last_name,e.first_name,e.sex,s.salary from employees e join salaries s on e.emp_no=s.emp_no ;

select first_name,last_name,substr(hire_date,7,10)as hire_date from employees where substr(hire_date,7,10)='1986' ;

select d.dept_name,d.dept_no,dm.emp_no,ee.last_name,ee.first_name,tt.title from departments d join dept_managers dm on d.dept_no=dm.dept_no join employees ee on dm.emp_no=ee.emp_no join titles tt on ee.emp_titles_id=tt.title_id group by d.dept_name,d.dept_no,dm.emp_no,ee.last_name,ee.first_name,tt.title ;

select d.dept_name,ee.emp_no,ee.last_name,ee.first_name from employees ee join dept_managers dm on ee.emp_no=dm.emp_no join departments d on d.dept_no=dm.dept_no;

select first_name,last_name, sex from employees where upper(first_name) like 'HERCULES%' and upper(last_name) like 'B%';

select d.dept_name,ee.emp_no,ee.last_name,ee.first_name,dept_name from employees ee join dept_managers dm on ee.emp_no=dm.emp_no join departments d on d.dept_no=dm.dept_no where upper(d.dept_name) like 'SALES%';

select d.dept_name,ee.emp_no,ee.last_name,ee.first_name from employees ee join dept_managers dm on ee.emp_no=dm.emp_no join departments d on d.dept_no=dm.dept_no  where upper(d.dept_name) like 'SALES%' or upper(d.dept_name) like 'DEVELOPMENT%';

select last_name,count(last_name)as counts from employees group by last_name having counts>1 order by counts desc;

select tt.title,avg(s.salary) from salaries s join employees ee on s.emp_no=ee.emp_no join titles tt on ee.emp_titles_id=tt.title_id group by tt.title;

select emp_no,(substr(last_date,7,10)-substr(hire_date,7,10)) as tenure from employees where (substr(last_date,7,10)-substr(hire_date,7,10)) is not null;



