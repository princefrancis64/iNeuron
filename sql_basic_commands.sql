create database market_star_schema;

use market_star_schema;

-- DDL Statements

create table shippping_mode_dimen(
	Ship_Mode varchar(25),
    Vehicle_Company varchar(25),
    Toll_Required boolean
    );
    
-- 2. Making Ship_Mode as the primary key in the above table
alter table shippping_mode_dimen
add constraint primary key(Ship_Mode);


create table India(
Matches_played int,
Matches_won int,
Matches_lost int,
Net_run_rate decimal(4,3),
Points int
);


insert into shippping_mode_dimen
values
	('DELIVERY TRUCK','Ashok Leyland',false),
    ('REGULAR AIR','Air India',false);


-- Another method of inserting values to the table
insert into shippping_mode_dimen(Ship_Mode,Vehicle_Company, Toll_Required)
values
	('WATERWAYS','Evergreen',true),
	('BY ROAD','Tata',NULL);

-- Updating the values in the table
update shippping_mode_dimen
set Toll_Required = true
where Ship_Mode='BY ROAD';


-- Deleting the entry for BY ROAD
delete from shippping_mode_dimen
where Vehicle_Company='Tata';

set sql_safe_updates=0;

set sql_safe_updates=1;

delete from shippping_mode_dimen
where Vehicle_Company='Ashok Leyland';

-- -------------------------------------------------
-- adding another column to the table
alter table shippping_mode_dimen
add Vehicle_Number varchar(20);

-- setting the vehicle number of the whole column
update shippping_mode_dimen
set Vehicle_Number = 'DL-456-7889';
-- dropping the column Vehicle_Number
alter table shippping_mode_dimen
drop column Vehicle_Number;
-- ----------------------------------------------------------
-- changing the data type of the column
alter table shippping_mode_dimen
change Toll_Required Toll_Amount int;

-- dropping the whole table itself
drop table shippping_mode_dimen;
-- ---------------------------------------
select * from shippping_mode_dimen;


