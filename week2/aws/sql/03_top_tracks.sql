-- Top 10 best-selling tracks by quantity

SELECT
    t.TrackId,
    t.Name AS TrackName,
    SUM(il.Quantity) AS QuantitySold
FROM Track AS t
INNER JOIN InvoiceLine AS il
    ON t.TrackId = il.TrackId
GROUP BY
    t.TrackId,
    t.Name
ORDER BY QuantitySold DESC
LIMIT 10;
