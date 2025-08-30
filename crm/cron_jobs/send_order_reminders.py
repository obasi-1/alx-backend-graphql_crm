#!/c/Users/OBA/Documents/alx-backend-graphql_crm/venv/Scripts/python
"""
Script: send_order_reminders.py
Description: Query GraphQL endpoint for pending orders within the last 7 days
and log reminders to /tmp/order_reminders_log.txt
"""

import sys
import asyncio
from datetime import datetime, timedelta
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


async def main():
    # GraphQL endpoint
    transport = RequestsHTTPTransport(
        url="http://localhost:8000/graphql",
        verify=True,
        retries=3,
    )

    client = Client(transport=transport, fetch_schema_from_transport=True)

    # Date filter: orders within the last 7 days
    last_week = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")

    query = gql(
        """
        query GetRecentOrders($date: Date!) {
            orders(orderDate_Gte: $date) {
                id
                customer {
                    email
                }
            }
        }
        """
    )

    # Execute query
    result = await client.execute_async(query, variable_values={"date": last_week})
    orders = result.get("orders", [])

    # Log results
    with open("/tmp/order_reminders_log.txt", "a") as log_file:
        for order in orders:
            log_line = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Order {order['id']} for {order['customer']['email']}\n"
            log_file.write(log_line)

    print("Order reminders processed!")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)
