use world;
select country.name negara_ASEAN,
country.population Populasi_Negara,
country.gnp GNP, city.name Ibukota,
city.population Populasi_Ibukota
from country inner join city
on city.id = country.capital
where country.Region = "Southeast Asia"
order by negara_ASEAN;