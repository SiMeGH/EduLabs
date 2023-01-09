--1. a.
alter table movies add length_in_minutes float;

--1. b.
update movies set length_in_minutes = 122.4 where id = 1;
update movies set length_in_minutes = 123.0 where id = 2;
update movies set length_in_minutes = 127.5 where id = 3;
update movies set length_in_minutes = 132.4 where id = 4;
update movies set length_in_minutes = 152.4 where id = 5;
update movies set length_in_minutes = 152.4 where id = 6;
update movies set length_in_minutes = 122.4 where id = 7;

--2.
create table public.series (
	id serial primary key,
	"name" varchar(256) not null
);

insert into series (id, "name") values (1, 'The Godfather');
insert into series (id, "name") values (2, 'Avatar');

--3.
alter table movies add series_id int;
alter table movies
	add constraint fk_series
      foreign key (series_id)
	  references series(id);

--4.
insert into movies (id, "name", "year", director_id, length_in_minutes, series_id)
values (8, 'The Godfather II', 1972, 2, 119.3, 1);
update movies set series_id = 1 where id = 1;
insert into series (id, "name") values (2, 'Avatar');
insert into movies (id, "name", "year", director_id, length_in_minutes, series_id)
values (9, 'Avatar', 2009, 2, 119.3, 2);
insert into movies (id, "name", "year", director_id, length_in_minutes, series_id)
values (10, 'Avatar - The Way of Water', 2022, 2, 140.3, 2);
insert into movies (id, "name", "year", director_id, length_in_minutes, series_id)
values (11, 'The Godfather III', 1992, 2, 119.3, 1);

--5. a.
select m."name", m.year, d."name", m.length_in_minutes, s."name"
from movies m
left join directors d on m.director_id = d.id
left join series s on m.series_id = s.id;

--5. b.
select s."name", count(m.series_id)
from series s
left join movies m on m.series_id = s.id
group by s."name";

--5. c.
select d."name", count(m."name") as total_movies
from directors d
left join movies m on m.director_id = d.id
group by d."name";

--5. d.
select d."name",
	count(m."name") as total_movies,
	count(distinct s."name") as total_series
from directors d
left join movies m on m.director_id = d.id
left join series s on m.series_id = s.id
group by d."name";

--5. e.
select m."name", s."name", d."name"
from movies m
join series s on m.series_id = s.id
join directors d on m.director_id = d.id
where m.series_id in (
	select m.series_id from movies m
	group by m.series_id having count(m.series_id) > 1
);

--5. f.
select m."name" as movies_wth_no_series, d."name"
from movies m
left join directors d on m.director_id = d.id
full join series s on m.series_id = s.id
where series_id is null;
