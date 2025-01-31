# pylint: disable=C0111, C0103

def query_orders(db):
    # Define Query - select all columns from Orders table and sort by OrderID
    query = "SELECT * FROM orders ORDER BY OrderID ASC;"

    # Execute query
    db.execute(query)

    # Fetch Results:
    results = db.fetchall()

    # Return the fetched orders as a list of tuples
    return results

#----------------------------------------------------------------------------------------------------------------------#

def get_orders_range(db, date_from, date_to):

    # SQL Query:
    # - Select all columns from Orders
    # - Filter orders where OrderDate is strictly greater than `date_from`
    #   and less than or equal to `date_to`
    # - Sort results by OrderDate in ascending order

    query = "SELECT * FROM Orders WHERE OrderDate > ? AND OrderDate <= ? ORDER BY OrderDate ASC"

    # Execute query
    results = db.execute(query, (date_from, date_to)).fetchall()

    # Return the list of orders within the date range
    return results

#----------------------------------------------------------------------------------------------------------------------#

def get_waiting_time(db):

    # SQL Query:
    # - Select OrderID, OrderDate, ShippedDate
    # - Calculate the waiting time as the difference between ShippedDate and OrderDate
    # - Use `JULIANDAY()` function to compute date difference in days
    # - Sort results by waiting time (smallest to largest)

    query = "SELECT OrderID, OrderDate, ShippedDate, JULIANDAY(ShippedDate) - JULIANDAY(OrderDate) AS WaitingTime FROM Orders WHERE ShippedDate IS NOT NULL ORDER BY WaitingTime ASC;"

    # Execute the query and fetch all results
    results = db.execute(query).fetchall()

    # Return the list of orders sorted by waiting time
    return results

#----------------------------------------------------------------------------------------------------------------------#

import sqlite3
conn = sqlite3.connect('ecommerce.sqlite')
db = conn.cursor()

# Test query_orders
print("All Orders Sorted by OrderID:")
print(query_orders(db))

# Test get_orders_range
print("\nOrders between '2022-01-01' and '2022-03-01':")
print(get_orders_range(db, '2022-01-01', '2022-03-01'))

# Test get_waiting_time
print("\nOrders sorted by delivery waiting time:")
print(get_waiting_time(db))

# Close connection
conn.close()
