use world;
select countrylanguage.CountryCode countrycode,
country.Name name, countrylanguage.Language language,
countrylanguage.IsOfficial isOfficial,
countrylanguage.Percentage percentage
from countrylanguage inner join country
on countrylanguage.CountryCode = country.Code
where countrylanguage.IsOfficial = "T"
order by countrylanguage.percentage desc limit 10;