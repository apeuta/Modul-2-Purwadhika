use world;
select Name nama, Continent benua, LifeExpectancy angkaHrpnHdp, GNP from country
where continent = "asia" and LifeExpectancy >
(select avg(LifeExpectancy) from country where continent = "europe")
order by LifeExpectancy desc limit 10;