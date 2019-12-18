create database sekolahku;
use sekolahku;
create table users(
id int(11) auto_increment not null primary key,
username varchar(50) not null,
email varchar(50) not null,
password varchar(50) not null,
created_at timestamp default current_timestamp,
updated_at timestamp default current_timestamp on update current_timestamp);
insert into users (username, email, password) values
("Andi", "andi@andi.com", "12345"),
("Budi", "budi@budi.com", "67890"),
("Caca", "caca@caca.com", "abcde"),
("Deni", "deni@deni.com", "fghij"),
("Euis", "euis@euis.com", "klmno"),
("Fafa", "fafa@fafa.com", "pqrst");
select * from users;
