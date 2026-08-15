-- Revenue by country

SELECT
    BillingCountry AS Country,
    ROUND(SUM(Total), 2) AS Revenue
FROM Invoice
GROUP BY BillingCountry
ORDER BY Revenue DESC;
