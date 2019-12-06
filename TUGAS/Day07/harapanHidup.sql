use world;
select continent as benua, count(name) as jumlah_negara,
sum(population) as populasi, avg(LifeExpectancy) as rata_angkahrpnhdp
from country group by Continent
having count(name) > 10
order by populasi desc;