# prompt_template.py

# Template for Database Schema Creation
SCHEMA_PROMPT_TEMPLATE = """# Database Schema

"""

# Template for Business Rules
RULES_PROMPT_TEMPLATE = """# Business Rules & Terminology

- **VIP Customer**: ...

# Golden Queries (Examples)
```sql

```"""

# Template for Deep Research Analysis
RESEARCH_ANALYSIS_PROMPT_TEMPLATE = """Analyze this data and provide three key business insights, potential anomalies, or actionable recommendations."""

# Template for Template Output Analysis
OUTPUT_ANALYSIS_PROMPT_TEMPLATE = """Analyze this data and provide three key business insights, potential anomalies, or actionable recommendations."""

# Template for Query Recommendations
QUERY_RECOMMENDATION_PROMPT_TEMPLATE = """Based on the provided context, suggest 3 new SQL queries that would provide further insights. with output template : ## Research Template Entry
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
"""
