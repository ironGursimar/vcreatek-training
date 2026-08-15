-- Monthly revenue for 2012

SELECT
    strftime('%Y-%m', InvoiceDate) AS Month,
    ROUND(SUM(Total), 2) AS Revenue
FROM Invoice
WHERE InvoiceDate >= '2012-01-01'
  AND InvoiceDate < '2013-01-01'
GROUP BY Month
ORDER BY Month;
