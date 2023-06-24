import mysql.connector

mydb = mysql.connector.connect(host ="localhost", user='root',password='***************') 
mycur = mydb.cursor()
mycur.execute('CREATE DATABASE HOSPITAL')


import mysql.connector

mydb = mysql.connector.connect(host ="localhost", user='root',password='********************', database='HOSPITAL')
mycur = mydb.cursor()

mycur.execute("CREATE TABLE PATIENT_DETAILS(P_ID integer not null primary key, P_NAME varchar(20),PHONE_NO varchar(10),AGE integer, DOB date,GENDER varchar(2),ADDRESS varchar(30),TREATMENT varchar(20), PHYSICIAN varchar(20),START_TIME varchar(15),END_TIME varchar(15),DATE_OF_ENTRY date,FEE integer DEFAULT '500')")


import mysql.connector

mydb = mysql.connector.connect(host ="localhost", user='root',password='********************', database='HOSPITAL')
mycur = mydb.cursor()

mycur.execute("CREATE TABLE STAFF_DETAILS(ID integer not null primary key,NAME varchar(25),PHONE_NO varchar(10),\
AGE integer, DOB date,GENDER varchar(2),ADDRESS varchar(30),DEPARTMENT varchar(25),\ WORKING_DAYS varchar(20),TIME varchar(15),DESIGNATION varchar(10))")


import mysql.connector

mydb = mysql.connector.connect(host ="localhost", user='root',password='********************', database='HOSPITAL')
mycur = mydb.cursor()

mycur.execute("CREATE TABLE APPOINTMENT_DETAILS(firstname varchar(30),lastname varchar(30),age varchar(20),problem varchar(40),physician varchar(30), phno varchar(20),timings varchar(30))")

import mysql.connector
mydb = mysql.connector.connect(host ="localhost", user='root',password='********************', database='HOSPITAL')
mycur = mydb.cursor()

mycur.execute("CREATE TABLE ROOM_DETAILS(ROOM_NO integer not null primary key,P_ID integer,P_NAME varchar(20),ID integer,NAME varchar(25),ROOM_TYPE varchar(15),ROOM_FLOOR integer, VACANCY char(2),DATE_OF_ADM date,DATE_OF_EXIT date, CAPACITY integer)")


import mysql.connector

mydb = mysql.connector.connect(host ="localhost", user='root',password='********************', database='HOSPITAL')
mycur = mydb.cursor()

mycur.execute("CREATE TABLE MEDICATION(M_ID integer not null primary key, M_NAME varchar(20), M_COMPANY varchar(20), M_DESC varchar(30), M_COST integer)")


import mysql.connector
mydb = mysql.connector.connect(host ="localhost", user='root',password='********************', database='HOSPITAL')
mycur = mydb.cursor()

mycur.execute("CREATE TABLE PROCEDURE_DETAILS(P_ID integer, ID integer,M_ID integer,P_NAME varchar(20),NAME varchar(20),PROCEDURE_DONE varchar(30),PRO_COST integer,HOSP_FEE integer, TOTAL_COST integer)")


import mysql.connector
mydb = mysql.connector.connect(host ="localhost", user='root',password='********************', database='HOSPITAL')
mycur = mydb.cursor()

mycur.execute("CREATE TABLE STAY(Stay_ID integer not null primary key,P_ID integer,P_NAME varchar(20),ID integer,NAME varchar(20),R_NO integer,TIME_OF_Ad varchar(15),TIME_OF_Ex time)")


import mysql.connector

mydb = mysql.connector.connect(host ="localhost", user='root',password='********************', database='HOSPITAL')
mycur = mydb.cursor()

mycur.execute("CREATE TABLE VISIT(P_ID integer,P_NAME varchar(20),V_ID integer,V_NAME varchar(20),VISIT_HOURS varchar(20) DEFAULT '5:00PM-6:00PM',VISIT_DATE date)")
