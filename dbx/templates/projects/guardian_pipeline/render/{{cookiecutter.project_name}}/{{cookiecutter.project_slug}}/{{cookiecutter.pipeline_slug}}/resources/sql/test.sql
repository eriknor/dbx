create table if not exists trips as select * from (select 'jim' as name, 32 as age union select 'jill' as name, 21 as age);