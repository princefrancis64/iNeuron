use market_star_schema;

-- --------------------Sql queries----------------------
-- 1.selecting all of the table itselt
select *
from cust_dimen;

-- 2.selecting Customer_Name column
select Customer_Name
from cust_dimen;

-- 3.Prince the name of all customers along with their city and state
select Customer_Name,City,State
from cust_dimen;

-- 4. Print the total number of customers
select count(*) as Total_Customers
from cust_dimen;

-- 5. Column aliases
select Customer_Name as 'Customer Full Name', City as  'Customer City'
from cust_dimen;

-- 6. How many customers are from West Bengal
select count(*) 
from cust_dimen
where State= 'West Bengal';

-- 7. And statement
select Customer_Name,City
from cust_dimen
where State = 'West Bengal' and City = 'Kolkata';

-- 8. or clause
select Customer_Name,City,Customer_Segment
from cust_dimen
where City = 'Mumbai' or Customer_Segment='Corporate'; 

-- 9. Names of all corporate customers from Mumbai
select Customer_Name,City,Customer_Segment
from cust_dimen
where City = 'Mumbai' and Customer_Segment='Corporate'; 

-- 10. List all the customers from southern India
select * 
from cust_dimen
where State in ('Tamil Nadu','Karnataka','Kerala','Telengana');

-- 11. Negation operator
select * 
from cust_dimen
where Customer_Segment !='Small Business';

-- ------------. schema market_fact_full-----------
-- 1. checking out the columns where there is loss
select Ord_id, Profit
from market_fact_full
where profit<0;

-- 2. List the orders having '5' in their Ord_id and shipping costs between 10 and 15
select Ord_id,Shipping_Cost
from market_fact_full
where Ord_id like '%\_5%' and Shipping_Cost between 10 and 15;

-- 3. Write a query to display the cities in the 'cust_dimen' table that begin with the letter 'K'.
select City 
from cust_dimen
where City like 'K%';

-- 4. List the orders having '5' in their Ord_id and shipping costs between 10 and 15 (another method)
select Ord_id,Shipping_Cost
from market_fact_full
where Ord_id like '%\_5%' and Shipping_Cost>=10 and Shipping_Cost<=15;

-- ------------------Aggregate Functions-----------------------------
-- 1. count
select * from market_fact_full;

select count(Sales)
from market_fact_full;

-- 2. column alias for the same
select count(Sales) as No_of_Sales
from market_fact_full;

-- 3. What are the total number of customers in each city
select count(Customer_Name) as City_Wise_Customers,City
from cust_dimen
group by City;

select * from market_fact_full;


-- 4.checking out the max function
select max(Sales) as Max_sales_city_wise,Cust_id
from market_fact_full
group by Cust_id;


-- 5. Number of order id where there is a loss
select count(Ord_id) as Loss_Count
from market_fact_full
where Profit<0;

-- 6.Find the number of customers from Bihar in each customer segment
select count(Customer_Name) as Segment_wise_customer, Customer_Segment
from cust_dimen
where State = 'Bihar'
group by Customer_Segment;


-- -------------------------------------------------------------
-- ------------ Ordering -----------------
-- 1. Listing the customer names in alphabetical order
select Customer_Name
from cust_dimen
order by Customer_Name;

select Customer_Name,City
from cust_dimen
order by Customer_Name desc,City desc;


-- 2. Print the three most ordered products
select Prod_id,sum(Order_Quantity) as total_Quantity
from market_fact_full
group by Prod_id
order by total_Quantity desc
limit 3;

-- 3. having clause, Print the three Least ordered product
select Prod_id,sum(Order_Quantity)
from market_fact_full
group by Prod_id
order by sum(Order_Quantity)
limit 3;

-- having clause
select Prod_id,sum(Order_Quantity)
from market_fact_full
group by Prod_id
having sum(Order_Quantity)<80
order by sum(Order_Quantity);


-- -------------------string and date time functions-------------
-- 1. Print the product names in the following category Category_SubCategory
select Product_Category, Product_Sub_Category,concat(Product_Category,'_',Product_Sub_Category) as Product_Name
from prod_dimen;

-- 2. Print the customer names in Proper case
select Customer_Name, concat(upper(substring(substring_index(lower(Customer_Name),' ',1),1,1)),
upper());


select Customer_Name,upper(substring(substring_index(lower(Customer_Name),' ',1),1,1))
from cust_dimen;
--


select Customer_Name,concat(upper(substring(substring_index(lower(Customer_Name),' ',1),1,1)),substring(substring_index(lower(Customer_Name),' ',1),2),' ',
upper(substring(substring_index(lower(Customer_Name),' ',-1),1,1)),substring(substring_index(lower(Customer_Name),' ',-1),2)) as Name_Proper
from cust_dimen;

-- 3. In which month were the most orders shipped?
select * from shipping_dimen;

select count(Ship_id), month(Ship_Date) as Month
from shipping_dimen
group by Ship_Date
order by count(Ship_id) desc;


-- 4. Which month and year combination saw the most number of critical orders?
select count(Ord_id) as Order_Count,month(Order_Date) as Order_Month,year(Order_Date) as Order_Year
from orders_dimen
where Order_Priority='Critical'
group by Order_Year, Order_Month
order by Order_Count desc;


-- 5. Find the most commonly used mode of Shipment in 2011
select Ship_Mode,count(Ship_Mode) as Ship_Mode_Count
from shipping_dimen
where year(Ship_Date) = 2011
group by Ship_Mode
order by Ship_Mode_Count desc;

-- -----------------------------------------------------------
-- Regular Expression
-- 1. Find the names of all customers having substring as 'car'
select Customer_Name
from cust_dimen
where Customer_Name regexp 'car';

-- 2. Print Customer names starting with a,b,c,d
select customer_name
from cust_dimen
where Customer_Name regexp '^[abcd]'
order by customer_name;

-- Customer names that end with er
select customer_name
from cust_dimen
where Customer_Name regexp 'er$'
order by customer_name;

-- Customer names that start with a,b,c,d and ends with er
select customer_name
from cust_dimen
where Customer_Name regexp '^[abcd].*er$'
order by customer_name;

-- -----------------------------------------------------------------
-- Nested Queries
-- 1. Print the order number for the most valuable order by sales
select * from market_fact_full;

select Prod_id,max(Sales) as Max_sale_prod_id,round(max(Sales)) 
from market_fact_full
group by Prod_id
order by Max_sale_prod_id desc;

select Prod_id,Sales, round(Sales)
from market_fact_full
where Sales =(            -- sub query
	select max(Sales)
    from market_fact_full);
    
-- Dealing with null values
select Prod_id
from market_fact_full
where Product_Base_Margin =null; -- this will not show up any values

select * 
from market_fact_full;
where Product_Base_Margin is null;


select * 
from prod_dimen;

select Prod_id
from prod_dimen where Manu_Id is null;

select * from market_fact_full;

select Prod_id,sales
from market_fact_full
where Prod_id in (
	select Prod_id
    from prod_dimen where Manu_Id is null);
    
-- 3. Print the name of the most frequent customer
select * from market_fact_full;
select * from cust_dimen;

select Cust_id,Customer_Name
from cust_dimen
where Cust_id = (
	select Cust_id
    from market_fact_full
    group by Cust_id
    order by count(Cust_id) desc
    limit 1
    );
    
select Cust_id
    from market_fact_full
    group by Cust_id
    order by count(Cust_id) desc
    limit 1;

-- 4. Print the three most common products
select Prod_id, Product_Category, Product_Sub_Category
from prod_dimen
where Prod_id in (
	select Prod_id
    from market_fact_full
    group by Prod_id
    order by count(Prod_id) desc
   
)
limit 3;
    
select Prod_id
    from market_fact_full
    group by Prod_id
    order by count(Prod_id) desc
    limit 3;

select * from prod_dimen;
select distinct(Prod_id)
from prod_dimen;

-- ------------------------------------------
-- Common Table Expressions CTE's
-- 1.Find the 5 products which resulted in the least losses
select Prod_id,Profit,Product_Base_Margin
from market_fact_full
where Profit<0
order by Profit desc
limit 5;

with least_losses as (
select Prod_id,Profit,Product_Base_Margin
from market_fact_full
where Profit<0
order by Profit desc
limit 5) select * 
	from least_losses
	where Product_Base_Margin = (
    select max(Product_Base_Margin)
    from least_losses
    );
    
-- 2. select all the low priority orders in the month of April
select Ord_id,Order_Date,Order_Priority
from orders_dimen
where Order_Priority='low' and month(Order_Date)=4;

with low_priority_orders as (
select Ord_id,Order_Date,Order_Priority
from orders_dimen
where Order_Priority='low' and month(Order_Date)=4
) select count(Ord_id) as Order_Count
from low_priority_orders
where day(Order_Date) between 1 and 15;

-- --------------------------------------------------
-- Views

-- 1. 
create view order_info
as select Ord_id,Sales,Order_Quantity,Profit,Shipping_Cost
from market_fact_full;

select Ord_id,Profit
from order_info
where Profit>1000;

-- 2. Which year generated the highest profit?
create view market_facts_and_orders
as select *
	from market_fact_full;


-- ---------------------------------------------------------
-- ------------------Joins
-- Inner Join-----------------------
-- 1. Print common columns form the prod_dimen and market_fact_full table
select Ord_id,Product_Category,Product_Sub_Category,Profit
from prod_dimen p inner join market_fact_full m
on p.Prod_id = m.Prod_id;

-- 2. Find the shipment date,shipment mode and profit made for every single order
select Ord_id, Profit, Ship_Mode,Ship_Mode
from market_fact_full m inner join shipping_dimen s
on m.Ship_id = s.Ship_id;

-- 3. three way join
select m.prod_id , m.Profit, p.Product_Category,s.Ship_Mode
from market_fact_full m inner join prod_dimen p on m.Prod_id=p.Prod_id
inner join shipping_dimen s on m.Ship_id = s.Ship_id;

select m.prod_id , m.Profit, p.Product_Category,s.Ship_Mode
from market_fact_full m inner join prod_dimen p on m.Prod_id=p.Prod_id
inner join shipping_dimen s on s.Ship_id = m.Ship_id;

-- 3. Which customer ordered the most number of products
select Customer_Name,sum(Order_Quantity) as Total_Orders
from cust_dimen c
inner join market_fact_full m 
on c.Cust_id = m.Cust_id
group by Customer_Name
order by Total_Orders desc;

-- alternate way
select Customer_name,sum(Order_Quantity) as Total_Orders
from cust_dimen
inner join market_fact_full
using (Cust_id)
group by Customer_Name
order by Total_Orders desc;

-- 4. Selling Office supplies was more profitable in Delhi as compared to patna,yes or not?
select * from market_fact_full;
select * from prod_dimen;
select * from cust_dimen;

select Product_Category,City,sum(Profit) as City_Wise_Profit
from market_fact_full m
inner join prod_dimen p
on m.Prod_id=p.Prod_id
inner join cust_dimen c
on c.Cust_id = m.Cust_id
where Product_Category = 'Office Supplies'
group by City,Product_Category;


-- 5. Print the name of the customer with the max number of orders
select Customer_Name,count(Customer_Name) as No_of_Orders
from cust_dimen c
inner join market_fact_full m
on c.Cust_id = m.Cust_id
group by Customer_Name
order by No_of_Orders desc
limit 1;


create table manu (
	Manu_Id int primary key,
	Manu_Name varchar(30),
	Manu_City varchar(30)
);

insert into manu values
(1, 'Navneet', 'Ahemdabad'),
(2, 'Wipro', 'Hyderabad'),
(3, 'Furlanco', 'Mumbai');

-- outer join---------
select * from manu;

select distinct manu_id from prod_dimen;

select m.manu_name,p.prod_id
from manu m inner join prod_dimen p on m.manu_id = p.manu_id;

select * from manu;
select * from prod_dimen;

select m.manu_name , p.prod_id
from manu m left join prod_dimen p on m.manu_id = p.Manu_Id;

select m.manu_name , count(p.prod_id)
from manu m left join prod_dimen p on m.manu_id = p.Manu_Id
where p.prod_id = (
	select distinct p.prod_id)
group by manu_name;

-- Views with Joins------------------
create view order_details
as select Customer_Name,Customer_Segment,Sales,Order_Quantity,Product_Category,Product_Sub_Category
	from cust_dimen c
    inner join market_fact_full m
    on c.Cust_id = m.Cust_id
    inner join prod_dimen p
    on m.Prod_id = p.Prod_id;

select * from order_details;

-- --------------------------------------------
-- Union, Union all , Intersect and Minus
(select Prod_id,sum(Profit)
from market_fact_full
group by Prod_id
order by sum(Profit) desc
limit 2)
union
(select Prod_id,sum(Profit)
from market_fact_full
group by Prod_id
order by sum(Profit)
limit 2);

CREATE TABLE t1 (
    id INT PRIMARY KEY
);

select * from t1;

CREATE TABLE t2 LIKE t1;

INSERT INTO t1(id) VALUES(1),(2),(3);

INSERT INTO t2(id) VALUES(2),(3),(4);

select * from t2;


(select id from t1)
INTERSECT  
(select id from t2);

(select id from t1)
EXCEPT (select id from t2);