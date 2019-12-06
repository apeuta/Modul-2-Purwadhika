use world;
select * from country;
select country.name negara_G20,
country.population Populasi_Negara,
country.gnp GNP, city.name Ibukota,
city.population Populasi_Ibukota
from country inner join city
on city.id = country.capital
where country.name in ("Argentina", "Australia", "Brazil", "Canada",
"China", "France", "Germany", "India", "Indonesia", "Italia", "Japan",
"Mexico", "Russian Federation", "Saudi Arabia", "South Africa", 
"South Korea", "Turkey", "United Kingdom", "United States")
order by negara_G20;