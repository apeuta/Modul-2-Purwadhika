use sekolahku;
select courses.mentor,  count(courses.course) jumlah_peserta, (count(courses.course) * 2000000) total_fee
from users inner join userCourse
on users.id = userCourse.id_user inner join courses
on userCourse.id_course = courses.id
group by courses.mentor;