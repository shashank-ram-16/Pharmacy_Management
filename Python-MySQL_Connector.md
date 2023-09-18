# Connecting MySQL and Python Using MySQL Connector

This guide provides instructions on how to download the Python MySQL Connector and establish a successful connection between MySQL and Python.

## Download Python MySQL Connector

1. **Install MySQL**: Ensure that MySQL is installed and running on your system. You can download MySQL from the [MySQL Downloads](https://dev.mysql.com/downloads/mysql/) page.

2. **Install MySQL Connector for Python**: You can install the MySQL Connector for Python using pip, the Python package manager:

   ```bash
   pip install mysql-connector-python
    ```

   Python Code for MySQL Connection
   ```bash
   import mysql.connector
   

```bash
# Replace the following parameters with your MySQL server details
host = "localhost"
user = "root"
passwd = "YourMySQLPassword"

# Create a connection
mycon = mysql.connector.connect(host=host, user=user, passwd=passwd)

# Check if the connection is successful
if mycon.is_connected():
    print("Connection to MySQL is successful")
else:
    print("Connection failed")

