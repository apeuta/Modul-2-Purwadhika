use world;
select ID as id, city.Name as nama_kota,
district, country.Name as negara, city.Population as population
from city inner join country
on city.CountryCode = country.Code
order by city.Population desc limit 10;