# [Cool Kids Coding School](https://www.coolkidscodingschool.com)

![CKCS logo >](./images/ckcslogo.png)
</br>

## Course: **Introduction to Database Programming**

### Lesson 1: **Introduction to Databases**

---
</br>

## First of all, what is a Data?

In simple words, data can be facts related to any object in consideration.  For example, your name, age, height, wwight, etc. are some data related to you.  A picture of you can also be considered data.  The price of a stock throughout the day is also data.  Our world is made up of data.  

## What is a Database?

A database is a place where we store all the data that is important to us.  In the past it could have been a journal or written record, or a stack of index cards.  Today it is usually an electronic system with alot of disk space on powerful servers and the software to allow users to query this data.

Some database complanies you may have heard of: *Oracle*, *Microsoft*, *MySQL* are among some of them.  

There are many different types of databases.  The most common is called a *Relational Database*.  It is called this because it models relationships between the data in the form of tables.  

We are going to learn about a database engince called __Sqlite__.

## How do we interact with a dabase?

Once we have a DBMS (Database Management System) in place, we need a way to interact with it.  Some of the things we would need to do:

+ Create relationships
+ Insert data
+ Modify data
+ Search for data

To do this we needed a new tool.  This tool was called SQL (Structured Query Language).  It was created in the mid 80's and quickly became the standard language used to interact with databases.

## How do we organize the data in a database?

For the sake of efficiency the data that we insert into a database needs to confirm to certain criteria and constraints in order for operations to be efficient.  

As mentioned above Relational Databases organize their data in terms of tables.  These tables are composed of columns that are attributes of the data and rows which are records of the dataset.  A single row represents a unit of data stored in a table.  Tables are organized into schemas.  

Here is a picture of a database schema that could be used to maintain data in a HR department.

![HR Department](./images/SQL-Sample-Database-Schema.png)

## What are SQL Statements?

SQL has become a very expressive language.  It is divided into two sub-categories:

+ DDL (Data Definition Language)
+ DML (Data Manipulation Language)

DDL is used to define tables and express relationships.  DML is used to manipulate the data in the schema.

> Create a Table

    CREATE TABLE employees (
	    employee_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	    first_name text,
	    last_name text NOT NULL,
	    email text NOT NULL,
	    phone_number text,
	    hire_date text NOT NULL,
	    job_id INTEGER NOT NULL,
	    salary double NOT NULL,
	    manager_id INTEGER,
	    department_id INTEGER NOT NULL
);

> Insert Data

    INSERT INTO employees(employee_id,first_name,last_name,email,phone_number,hire_date,job_id,salary,manager_id,department_id) VALUES (100,'Steven','King','steven.king@coolkidscodingschool.com','515.123.4567','1987-06-17',4,24000.00,NULL,9);

> Select Data

> Update Data

> Delete a Table

> Delete the Data in a Table



