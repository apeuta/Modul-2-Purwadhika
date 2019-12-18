use sekolahku;
select courses.course, any_value(courses.mentor), any_value(courses.title), count(courses.course) jumlah_peserta
from users inner join userCourse
on users.id = userCourse.id_user inner join courses
on userCourse.id_course = courses.id
group by courses.course;