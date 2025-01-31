# pylint: disable=C0111, C0103
import sqlite3

def query_orders(database):
    # Define Query - select all columns from Orders table and sort by OrderID
    query = "SELECT * FROM orders ORDER BY OrderID ASC;"

    # Execute query
    database.execute(query)

    # Fetch Results:
    results = database.fetchall()

    # Return the fetched orders as a list of tuples
    return results



def get_orders_range(database, date_from, date_to):

    # SQL Query:
    # - Select all columns from Orders
    # - Filter orders where OrderDate is strictly greater than `date_from`
    #   and less than or equal to `date_to`
    # - Sort results by OrderDate in ascending order

    query = "SELECT * FROM Orders WHERE OrderDate > ? AND OrderDate <= ? ORDER BY OrderDate ASC"

    # Execute query
    results = database.execute(query, (date_from, date_to)).fetchall()

    # Return the list of orders within the date range
    return results


def get_waiting_time(database):

    # SQL Query:
    # - Select OrderID, OrderDate, ShippedDate
    # - Calculate the waiting time as the difference between ShippedDate and OrderDate
    # - Use `JULIANDAY()` function to compute date difference in days
    # - Sort results by waiting time (smallest to largest)

    query = """
    SELECT OrderID, CustomerID, EmployeeID, OrderDate, RequiredDate,
           ShippedDate, ShipVia, FreightCharge,
           JULIANDAY(ShippedDate) - JULIANDAY(OrderDate) AS WaitingTime
    FROM Orders
    WHERE ShippedDate IS NOT NULL
    ORDER BY WaitingTime ASC;
    """
    results = database.execute(query).fetchall()
    return results


# conn = sqlite3.connect('ecommerce.sqlite')
# database = conn.cursor()

# # Test query_orders
# print("All Orders Sorted by OrderID:")
# print(query_orders(database))

# # Test get_orders_range
# print("\nOrders between '2022-01-01' and '2022-03-01':")
# print(get_orders_range(database, '2022-01-01', '2022-03-01'))

# # Test get_waiting_time
# print("\nOrders sorted by delivery waiting time:")
# print(get_waiting_time(database))

# # Close connection
# conn.close()
