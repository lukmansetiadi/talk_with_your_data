
## Research Template Entry
**Provider:** groq
**Question:** show me top VIP Customer year 2005

**SQL Query:**
```sql
SELECT c.customerName, SUM(p.amount) AS TotalPayments
FROM customers c
JOIN payments p ON c.customerNumber = p.customerNumber
WHERE YEAR(p.paymentDate) = 2005
GROUP BY c.customerName
HAVING SUM(p.amount) > 100000
ORDER BY TotalPayments DESC;
```

---

## Research Template Entry
**Provider:** groq
**Question:** show me top VIP Customer year 2004

**SQL Query:**
```sql
SELECT c.customerName, SUM(p.amount) AS TotalPayments
FROM customers c
JOIN payments p ON c.customerNumber = p.customerNumber
WHERE YEAR(p.paymentDate) = 2004
GROUP BY c.customerName
HAVING SUM(p.amount) > 100000
ORDER BY TotalPayments DESC;
```

---


## Research Template Entry
**Provider:** groq
**Question:** show me top VIP Customer year 2003

**SQL Query:**
```sql
SELECT c.customerName, SUM(p.amount) AS totalPayment 
FROM customers c 
JOIN payments p ON c.customerNumber = p.customerNumber 
WHERE YEAR(p.paymentDate) = 2003 
GROUP BY c.customerNumber, c.customerName 
HAVING SUM(p.amount) > 100000 
ORDER BY totalPayment DESC;
```

---

## Research Template Entry
**Provider:** groq
**Question:** show me top 10 customer, product and total sales on year 2005

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
  YEAR(o.orderDate) = 2005
GROUP BY 
  c.customerName, 
  p.productName
ORDER BY 
  totalSales DESC
LIMIT 10;
```

---

## Research Template Entry
**Provider:** groq
**Question:** show me top 10 customer, product and total sales on year 2004

**SQL Query:**
```sql
SELECT 
    c.customerName, 
    p.productName, 
    SUM(od.quantityOrdered * od.priceEach) AS totalSales
FROM 
    customers c
JOIN 
    orders o ON c.customerNumber = o.customerNumber
JOIN 
    orderdetails od ON o.orderNumber = od.orderNumber
JOIN 
    products p ON od.productCode = p.productCode
WHERE 
    YEAR(o.orderDate) = 2004
GROUP BY 
    c.customerName, 
    p.productName
ORDER BY 
    totalSales DESC
LIMIT 10;
```

---

## Research Template Entry
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




## Query Recommendation
**Provider:** groq
**Prompt:** Based on the provided context, suggest 3 new SQL queries that would provide further insights. with output template : ## Research Template Entry
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




## Research Template Entry
**Provider:** Recommendation
**Question:** [Recommendation Run] show me top 10 customer, product and total sales on year 2003

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

## Research Template Entry
**Provider:** Recommendation
**Question:** [Recommendation Run] What are the top 5 customers with the highest total payments in the year 2005?

**SQL Query:**
```sql
SELECT 
  c.customerName, 
  SUM(p.amount) AS totalPayments
FROM 
  customers c
  JOIN payments p ON c.customerNumber = p.customerNumber
WHERE 
  YEAR(p.paymentDate) = 2005
GROUP BY 
  c.customerName
ORDER BY 
  totalPayments DESC
LIMIT 5;
```

---

## Research Template Entry
**Provider:** Recommendation
**Question:** [Recommendation Run] What are the product categories with the highest total sales in the year 2004?

**SQL Query:**
```sql
SELECT 
  p.productLine, 
  SUM(od.quantityOrdered * od.priceEach) AS totalSales
FROM 
  products p
  JOIN orderdetails od ON p.productCode = od.productCode
  JOIN orders o ON od.orderNumber = o.orderNumber
WHERE 
  YEAR(o.orderDate) = 2004
GROUP BY 
  p.productLine
ORDER BY 
  totalSales DESC
LIMIT 1;
```

---

## Research Template Entry
**Provider:** Recommendation
**Question:** [Recommendation Run] What is the customer satisfaction rating for each customer in the year 2005?

**SQL Query:**
```sql
SELECT 
  c.customerName, 
  COUNT(o.orderNumber) AS totalOrders, 
  SUM(CASE WHEN o.status = 'Completed' THEN 1 ELSE 0 END) AS completedOrders
FROM 
  customers c
  JOIN orders o ON c.customerNumber = o.customerNumber
WHERE 
  YEAR(o.orderDate) = 2005
GROUP BY 
  c.customerName
ORDER BY 
  completedOrders / totalOrders DESC;
```

---

## Research Template Entry
**Provider:** Recommendation
**Question:** [Recommendation Run] Based on the provided context, suggest 3 new SQL queries that would provide further insights. with output template : ## Research Template Entry
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

## Research Template Entry
**Provider:** Recommendation
**Question:** [Recommendation Run] What are the top 5 customers with the highest total payments in the year 2004?

**SQL Query:**
```sql
SELECT 
  c.customerName, 
  SUM(p.amount) AS totalPayments
FROM 
  customers c
  JOIN payments p ON c.customerNumber = p.customerNumber
WHERE 
  YEAR(p.paymentDate) = 2004
GROUP BY 
  c.customerName
ORDER BY 
  totalPayments DESC
LIMIT 5;
```

---

## Research Template Entry
**Provider:** Recommendation
**Question:** [Recommendation Run] What are the product categories with the highest total sales in the year 2005?

**SQL Query:**
```sql
SELECT 
  p.productLine, 
  SUM(od.quantityOrdered * od.priceEach) AS totalSales
FROM 
  products p
  JOIN orderdetails od ON p.productCode = od.productCode
  JOIN orders o ON od.orderNumber = o.orderNumber
WHERE 
  YEAR(o.orderDate) = 2005
GROUP BY 
  p.productLine
ORDER BY 
  totalSales DESC
LIMIT 1;
```

---

## Research Template Entry
**Provider:** Recommendation
**Question:** [Recommendation Run] What is the customer satisfaction rating for each customer in the year 2004?

**SQL Query:**
```sql
SELECT 
  c.customerName, 
  COUNT(o.orderNumber) AS totalOrders, 
  SUM(CASE WHEN o.status = 'Completed' THEN 1 ELSE 0 END) AS completedOrders
FROM 
  customers c
  JOIN orders o ON c.customerNumber = o.customerNumber
WHERE 
  YEAR(o.orderDate) = 2004
GROUP BY 
  c.customerName
ORDER BY 
  completedOrders / totalOrders DESC;
```

---

## Research Template Entry
**Provider:** Recommendation
**Question:** [Recommendation Run] Based on the provided context, suggest 3 new SQL queries that would provide further insights. with output template : ## Research Template Entry
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

## Research Template Entry
**Provider:** Recommendation
**Question:** [Recommendation Run] What are the top 5 customers with the highest total sales in the year 2004?

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

---

## Research Template Entry
**Provider:** Recommendation
**Question:** [Recommendation Run] Which product lines have the highest total sales across all years?

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

---
