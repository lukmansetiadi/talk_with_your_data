
## Query Recommendation
**Provider:** groq
**Question:** Based on the provided context, suggest 3 new SQL queries that would provide further insights. with output template : ## Research Template Entry
**Provider:** groq
**Question:** show me top 10 customer, product and total sales on year 2003

**SQL Query:**
```sql
SELECT 
  c.customerName, 
  p.productName, 
  SUM(od.quantityOrdered * od.priceEach) AS totalSales
FROM 
  customers c
  JOIN orders o ON c.customerNumber = o.customerNumber
  JOIN orderdetails od ON o.orderNumber = od.orderNumber
  JOIN products p ON od.productCode = p.productCode
WHERE 
  YEAR(o.orderDate) = 2003
GROUP BY 
  c.customerName, 
  p.productName
ORDER BY 
  totalSales DESC
LIMIT 10;
```

---


**SQL Query:**
```sql
## Research Template Entry
**Provider:** groq
**Question:** What are the top 5 customers with the highest total sales in the year 2004?

**SQL Query:**
```sql
SELECT 
  c.customerName, 
  SUM(od.quantityOrdered * od.priceEach) AS totalSales
FROM 
  customers c
  JOIN orders o ON c.customerNumber = o.customerNumber
  JOIN orderdetails od ON o.orderNumber = od.orderNumber
WHERE 
  YEAR(o.orderDate) = 2004
GROUP BY 
  c.customerName
ORDER BY 
  totalSales DESC
LIMIT 5;
```

## Research Template Entry
**Provider:** groq
**Question:** Which product lines have the highest total sales across all years?

**SQL Query:**
```sql
SELECT 
  p.productLine, 
  SUM(od.quantityOrdered * od.priceEach) AS totalSales
FROM 
  products p
  JOIN orderdetails od ON p.productCode = od.productCode
  JOIN orders o ON od.orderNumber = o.orderNumber
GROUP BY 
  p.productLine
ORDER BY 
  totalSales DESC
LIMIT 10;
```

## Research Template Entry
**Provider:** groq
**Question:** What is the customer retention rate for each year, i.e., how many customers placed orders in the current year and also in the previous year?

**SQL Query:**
```sql
WITH customers_2003 AS (
  SELECT DISTINCT customerNumber
  FROM orders
  WHERE YEAR(orderDate) = 2003
),
customers_2004 AS (
  SELECT DISTINCT customerNumber
  FROM orders
  WHERE YEAR(orderDate) = 2004
),
customers_2005 AS (
  SELECT DISTINCT customerNumber
  FROM orders
  WHERE YEAR(orderDate) = 2005
)

SELECT 
  COUNT(DISTINCT CASE WHEN customerNumber IN (SELECT customerNumber FROM customers_2003) THEN customerNumber END) AS retained_customers_2004,
  COUNT(DISTINCT customers_2004.customerNumber) AS total_customers_2004,
  COUNT(DISTINCT CASE WHEN customerNumber IN (SELECT customerNumber FROM customers_2004) THEN customerNumber END) AS retained_customers_2005,
  COUNT(DISTINCT customers_2005.customerNumber) AS total_customers_2005;
```
```

---
