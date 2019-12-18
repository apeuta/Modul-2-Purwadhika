use sekolahku;
create table userCourse(
id_user int(11),
id_course int(11));
describe userCourse;
insert into userCourse (id_user, id_course) values
(1,1), (1,2), (1,3), (2,4), (2,5), (2,6), (3,7), (3,8), (3,9),
(4,1), (4,3), (4,5), (5,2), (5,4), (5,6), (6,7), (6,8), (6,9);
select * from usercourse;
