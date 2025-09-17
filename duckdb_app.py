import duckdb

conn = duckdb.connect()

query = "SELECT * FROM 'users.csv' WHERE job LIKE '%developer%'"
result = conn.execute(query).fetchall()

print("Data from duckdb (developers only):")
for row in result:
    print(row)

conn.close()
