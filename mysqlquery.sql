use anabig114243;



drop table if exists departments;
create table departments
(
dept_no char(5) not null,
dept_name varchar(40) not null,
primary key (dept_no)
);


load data local infile 'home/anabig114243/departments.csv' into table departments fields terminated by ',' lines terminated by '\n' ignore 1 rows;

drop table if exists dept_employees;
create table dept_employees
(
emp_no int(11) not null,
dept_no char(5) not null,
primary key (emp_no,dept_no)
);

load data local infile 'home/anabig114243/dept_emp.csv' into table dept_employees fields terminated by ',' lines terminated by '\n' ignore 1 rows;


drop table if exists dept_managers;
create table dept_managers
(
dept_no char(5) not null,
emp_no int(11) not null,
primary key (emp_no)
);

load data local infile 'home/anabig114243/dept_manager.csv' into table dept_managers fields terminated by ',' lines terminated by '\n' ignore 1 rows;

drop table if exists employees;
create table employees
(
emp_no bigint not null,
emp_titles_id varchar(15) not null,
birth_date char(15) not null,
first_name varchar(40) not null,
last_name varchar(40) not null,
sex char(2) not null,
hire_date char(15) not null,
no_of_projects int(11) not null,
last_performance_rating char(5) not null,
left_comapny tinyint not null,
last_date char(15) default null,
primary key (emp_no)
);

load data local infile 'home/anabig114243/employees.csv' into table employees fields terminated by ',' lines terminated by '\n' ignore 1 rows;


drop table if exists salaries;
create table if exists salaries
(
emp_no bigint not null,
salary bigint not null,
primary key ('emp_no')
);

load data local infile 'home/anabig114243/salaries.csv' into table salaries fields terminated by ',' lines terminated by '\n' ignore 1 rows;

drop table if exists titles;
create table titles
(
title_id varchar(15) not null,
title varchar(40) not null,
primary key ('title_id')
);

load data local infile 'home/anabig114243/titles.csv' into table titles fields terminated by ',' lines terminated by '\n' ignore 1 rows;
