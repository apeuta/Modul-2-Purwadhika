use world;
select Code, Name, Continent, Region, IndepYear as tahun_merdeka
from country where IndepYear is not null
order by IndepYear limit 10;