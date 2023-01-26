Endpoint to get the visualization of all the data in the database:

```couchbasequery
GET http://127.0.0.1:5000/heatmap/None/None
```

Visualisation of the data in the database for a specific date:

```couchbasequery
GET http://127.0.0.1:5000/heatmap/start_date/end_date

For example:
GET http://127.0.0.1:5000/heatmap/2023-01-12/2023-01-20
```