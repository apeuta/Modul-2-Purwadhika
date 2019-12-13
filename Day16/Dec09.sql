show databases;
create database pandas_tes;
use pandas_tes;
create table employees(
id int not null auto_increment,
nama varchar(100) not null default "Mr. X",
email varchar(100) unique not null,
waktu timestamp default current_timestamp,
primary key (id)
);
describe employees;
insert into employees (nama, email) values
("Asnawi", "asnawi@yahoo.id"),
("Bagas", "bagasadi@yahoo.id"),
("Evan", "evandd@yahoo.id"),
("Osvaldo", "osvaldo@yahoo.id");
select * from employees;	
show tables;