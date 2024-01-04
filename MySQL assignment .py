#!/usr/bin/env python
# coding: utf-8

# Q1. What is a database? Differentiate between SQL and NoSQL databases.

# A database is an organized collection of structured information, or data, typically stored electronically in a computer system. A database is usually controlled by a database management system (DBMS).
# 
# SQL: It stands for Structured Query Language.
#      SQL databases have fixed or static or predefined schema.
#      SQL databases display data in form of tables so it is known as table-based database.
#      SQL databases are vertically scalable.
#      SQL databases are best suited for complex queries.
# 
# NoSQL:It stands for Non SQL.
#       NoSQL databases have dynamic schema.
#       NoSQL databases display data as collection of key-value pair, documents, graph databases or wide-column stores.
#       NoSQL databases are horizontally scalable.
#       NoSQL databases are best suited for hierarchical data storage.
#     
#      

# Q2. What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.

# Data Definition Language(DDL) is a subset of SQL and a part of DBMS(Database Management System).It consist command likes CREATE, DROP, ALTER and TRUNCATE.
# 
# Example of CREATE
# 
# Create table MCA(
#     
#     Roll_No. int(primary key),
#     Name varchar(255),
#     subject varchar(255)
# 
# );
# 
# Example of DROP
# 
# Drop table MCA;
# 
# 
# Example of ALTER
# 
# Alter table MCA
# ADD baranch varchar(255);
# 
# Example of TRUNCATE
# 
# Truncate table MCA;

# Q3. What is DML? Explain INSERT, UPDATE, and DELETE with an example.

# DML is an abbreviation of Data Manipulation Language.
# 
# Example of INSERT
# 
# Insert into MCA(Roll_No, Name, Subject) values (1,'Lucky','Data Science');
# 
# Example of UPDATE
# 
# Update MCA set Branch='Sahibganj' where Roll_No=1;
# 
# Example of DELETE 
# 
# Delete from MCA where Roll_No=1;

# Q4. What is DQL? Explain SELECT with an example.
# 
# DQL is an abbreviation of Data Query Language.
# 
# 
# Example of SELECT
# 
# select * from MCA;

# Q5. Explain Primary Key and Foreign Key.
# 
# 
#  The main difference between them is that the primary key identifies each record in the table, whereas the foreign key is used to link two tables together.
#     
# Primary Key:	It is used to identify each record into the database table uniquely.
#                 The primary key column value can never be NULL.
#                 A table can have only one primary key.
#                 The primary key constraint can be defined on the temporary tables.
#                 It cannot create a parent-child relationship in a table.
#                 
#                 
# Foreign Key:    It is used to links two tables together. It means the foreign key in one table refers to the primary key of another table.
#                 The foreign key column can accept a NULL value.
#                 A table can have more than one foreign key.
#                 It can make a parent-child relationship in a table.

# In[ ]:




