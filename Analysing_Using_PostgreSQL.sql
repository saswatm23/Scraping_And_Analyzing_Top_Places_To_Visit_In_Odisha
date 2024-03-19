select * from tourism

--Top 5 Places by Rating
select "Place","Rating" from tourism
where "Rating" is not null
order by "Rating" desc
limit 5

--Bottom 5 Places by Rating
select "Place","Rating" from tourism
where "Rating" is not null
order by "Rating" 
limit 5

--Places having Mountains
select "Place","Description","Rating" from tourism
where "Description" like '%mountain%'

--Places having sea's or lake's
select "Place","Description","Rating" from tourism
where "Description" like '%sea%' or "Description" like '%lake%'

--Places having zoo's or sanctuary's
select "Place","Description","Rating" from tourism
where "Description" like '%zoo%' or "Description" like '%sanctuary%'

--Places whose Rating is not available
select * from tourism
where "Rating" is null