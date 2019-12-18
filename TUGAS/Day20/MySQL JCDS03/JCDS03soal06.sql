use sekolahku;
select users.id, users.username, courses.course, courses.mentor, courses.title
from users inner join userCourse
on users.id = userCourse.id_user inner join courses
on userCourse.id_course = courses.id
where courses.title not like "S%";