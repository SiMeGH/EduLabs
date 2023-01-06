--1.
select * from superstore_data;

--2.
select count(*) from superstore_data;

--3.
select * from superstore_data limit 10;

--4.
select * from superstore_data limit 45-20+1 offset 20-1;

--5.
select id, year_birth, marital_status from superstore_data limit 20;

--6.
select id from superstore_data where mntwines > 1000

--7.
select date_part('year', now()) - year_birth as customer_age, marital_status
from superstore_data
where mntfishproducts < 500 and
	mntmeatproducts > 500;
	
--8.
select count(*) as total_response from superstore_data where response = 1;

--9.
select distinct education from superstore_data;

--10.
select * from superstore_data
where year_birth = (
	select max(year_birth) from superstore_data
);

--11.
select id, date_part('year', now()) - year_birth as customer_age, marital_status
from superstore_data
where year_birth = (
	select min(year_birth) from superstore_data
);

--12.
select round(avg(income), 2) from superstore_data where complain = 1;

--13.
select sum(kidhome + teenhome) from superstore_data; 

--14.
select id, income, date_part('year', now()) - year_birth as customer_age, marital_status
from superstore_data where numwebpurchases > numstorepurchases;

--15.
select id, kidhome + teenhome as children from superstore_data
where recency < 31;

--16.
select count(*) as num_of_customers from superstore_data
where mntmeatproducts = 0 and mntfishproducts = 0;

--17.
select * from superstore_data
where mntgoldprods = (
	select max(mntgoldprods) from superstore_data
);

--18.
select id, date_part('year', now()) - year_birth as customer_age
from superstore_data
where date_part('year', now()) - year_birth between 20 and 40
order by customer_age desc;

--19.
select distinct year_birth from superstore_data;

--20.
select id, mntsweetproducts  from superstore_data
order by mntsweetproducts desc limit 10;

--21.
select marital_status, count(*)
from superstore_data group by marital_status;

--22.
select education, sum(mntsweetproducts) as sweets, sum(mntwines) as wine
from superstore_data group by education;

--23.
select marital_status, education,
	max(date_part('year', now()) - year_birth) as max_age,
	min(date_part('year', now()) - year_birth) as min_age
from superstore_data
group by marital_status, education
order by education, min_age

--24.
select date_part('year', now()) - year_birth as customer_age, count(*)
from superstore_data
where response = 1 and complain = 0
group by year_birth;

--25.   
select
	distinct on (education)
	id,
	education,
	date_part('year', now()) - year_birth as youngest_customer_age
from superstore_data
order by education, youngest_customer_age;

--26.
select kidhome + teenhome as children,
	round(avg(mntfishproducts), 2) as fish_average,
	round(avg(mntmeatproducts), 2) as meat_average,
	round(avg(mntsweetproducts), 2) as sweets_average,
	round(avg(mntwines), 2) as wines_average,
	round(avg(mntgoldprods), 2) as gold_average
from superstore_data
group by kidhome + teenhome;

--27.
select
	distinct on (teenhome)
	teenhome, id, year_birth
from superstore_data
order by teenhome, year_birth desc

--28.
select response, count(*) from superstore_data group by response;

--29.
select marital_status,
	round(avg(kidhome), 2) as avg_kids,
	round(avg(teenhome), 2) as avg_teens
from superstore_data group by marital_status;

--30.
select education,
	min(income) as min_income,
	max(income) as max_income,
	round(avg(income), 2) as avg_income
from superstore_data group by education;