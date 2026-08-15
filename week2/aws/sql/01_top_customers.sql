-- Top 5 customers by total spend

SELECT
    c.CustomerId,
    c.FirstName || ' ' || c.LastName AS CustomerName,
    ROUND(SUM(i.Total), 2) AS TotalSpend
FROM Customer AS c
INNER JOIN Invoice AS i
    ON c.CustomerId = i.CustomerId
GROUP BY
    c.CustomerId,
    c.FirstName,
    c.LastName
ORDER BY TotalSpend DESC
LIMIT 5;
