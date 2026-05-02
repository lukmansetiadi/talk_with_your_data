# Business Rules & Terminology
Use these rules to understand the user's intent and how to calculate specific business metrics when generating SQL.

- **VIP Customer**: A customer whose total sum of all their completed payments is greater than $100,000.
- **Active Order**: An order where the status is NOT 'Shipped', 'Resolved', or 'Cancelled'.
- **High Margin Product**: A product where the MSRP is at least double (2x) the buyPrice.
- **North America**: Refers to customers where the country is either 'USA' or 'Canada'.

# Golden Queries (Examples)
If the user asks for profit margin, always calculate it like this:
```sql
SELECT productName, ((MSRP - buyPrice) / MSRP) * 100 AS ProfitMarginPercentage 
FROM products;
```
