use sekolahku;
create table courses(
id int(11) auto_increment primary key,
course varchar(50) not null,
mentor varchar(50) not null,
title varchar(50)not null);
describe courses;
insert into courses (course, mentor, title) values
("C++", "Ari", "Dr."),
("C#", "Ari", "Dr."),
("C#", "Ari", "Dr."),
("CSS", "Cania", "S.Kom"),
("HTML", "Cania", "S.Kom"),
("Javascript", "Cania", "S.Kom"),
("Python", "Barry", "S.T."),
("Micropython", "Barry", "S.T."),
("Java", "Darren", "M.T."),
("Ruby", "Darren", "M.T.");
select * from courses;
