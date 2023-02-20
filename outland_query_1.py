import mysql.connector

# Connect to the MySQL server
cnx = mysql.connector.connect(host='127.0.0.1', user='outland_user', password='hike', database='outland_adventures')

cursor = cnx.cursor()

# cursor.execute("DROP TABLE IF EXISTS employees;")
# cursor.execute("DROP TABLE IF EXISTS equipment;")
# cursor.execute("DROP TABLE IF EXISTS equipment_sales;")
# cursor.execute("DROP TABLE IF EXISTS adventures;")
# cursor.execute("DROP TABLE IF EXISTS customers;")

# Create employees table
create_employees_table = """
CREATE TABLE employees (
    employee_id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    title VARCHAR(50),
    PRIMARY KEY(employee_id)
);"""

cursor.execute(create_employees_table)

# Create adventures table
create_adventures_table = """
CREATE TABLE adventures (
    adventure_id INT,
    location VARCHAR(50),
    departure_date DATE,
    return_date DATE,
    employee_id INT,
    PRIMARY KEY(adventure_id),
    FOREIGN KEY(employee_id)
    REFERENCES employees(employee_id)
);"""

cursor.execute(create_adventures_table)

# Create equipment table
create_equipment_table = """
CREATE TABLE equipment (
    equipment_id INT,
    equipment_name VARCHAR(50),
    onboard_date DATE,
    adventure_id INT,
    PRIMARY KEY(equipment_id),
    FOREIGN KEY(adventure_id)
    REFERENCES adventures(adventure_id)
);"""

cursor.execute(create_equipment_table)

# Create customers table
create_customers_table = """
CREATE TABLE customers (
    customer_id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    airline VARCHAR(50),
    visa BOOLEAN,
    inoculation BOOLEAN,
    adventure_id INT,
    PRIMARY KEY(customer_id),
    FOREIGN KEY(adventure_id)
    REFERENCES adventures(adventure_id)
);"""

cursor.execute(create_customers_table)

# Create equipment_sales table
create_equipment_sales_table = """
CREATE TABLE equipment_sales (
    sales_id INT,
    equipment_name VARCHAR(50),
    sales_date DATE,
    equipment_id INT,
    customer_id INT,
    PRIMARY KEY(sales_id),
    FOREIGN KEY(equipment_id)
    REFERENCES equipment(equipment_id),
    FOREIGN KEY(customer_id)
    REFERENCES customers(customer_id)
);"""

cursor.execute(create_equipment_sales_table)

employeesInsert = "INSERT INTO employees (employee_id, first_name, last_name, title) VALUES (%s, %s, %s, %s)"
employees = [(1, "Blythe", "Timmerson", "Founder")
             (2, "Jim", "Ford", "Founder")
             (3, "Mac", "MacNeil", "Guide")
             (4, "Duke", "Marland", "Guide")
             (5, "Anita", "Gallegos", "Marketing")
             (6, "Dimitros", "Stravopolous", "Supplier")
             (7, "Mei", "Wong", "Ecomm")]

cursor.executemany(employeesInsert, employees)

adventuresInsert = "INSERT INTO adventures(adventure_id, location, departure_date, return_date, employee_id) VALUES (%s, %s, %s, %s, %s)"
adventures = [(1, "Africa", "01/01/2023", "01/15/2023", 3)
             (2, "Asia", "01/22/2023", "02/05/2023", 4)
             (3, "Southern Europe", "02/12/2023", "02/26/2023", 3)
             (4, "Africa", "04/02/2023", "04/16/2023", 4)
             (5, "Asia", "04/23/2023", "05/07/2023", 3)
             (6, "Southern Europe", "05/14/2023", "05/28/2023", 4)]

cursor.executemany(adventuresInsert, adventures)

equipmentInsert = "INSERT INTO equipment(equipment_id, equipment_name, onboard_date, adventures_id) VALUES (%s, %s, %s, %s)"
equipment = [(73, "tent", "10/10/2022", 1)
             (74, "backpack", "10/10/2022", 1)
             (75, "radio", "03/26/2015", 1)
             (76, "flashlight", "05/27/2019", 1)
             (77, "tent", "04/17/2018", 2)
             (78, "backpack", "12/19/2022", 2)
             (79, "radio", "05/18/2018", 2)
             (80, "flashlight", "01/01/2023", 2)]

cursor.executemany(equipmentInsert, equipment)

customersInsert = "INSERT INTO customers(customer_id, first_name, last_name, airline, visa, inoculation, adventure_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
customers = [(101, "John", "Merlin", "southwest", Yes, Yes, 1)
             (102, "Katrina", "Bishop", "delta", No, Yes, 2)
             (103, "Jacob", "Garcia", "southwest", Yes, Yes, 1)
             (104, "Siobhan", "Doyle", "southwest", Yes, Yes, 1)
             (105, "Tyler", "Kennedy", "delta", No, Yes, 2)
             (106, "Samantha", "Forager", "delta", Yes, Yes, 2)]

cursor.executemany(customersInsert, customers)

salesInsert = "INSERT INTO equipment_sales(sales_id, equipment_name, sales_date, equipment_id, customer_id) VALUES (%s, %s, %s, %s, %s)"
equipment_sales = [(32, "tent", "06/22/2022", 36, 42)
                   (33, "tent", "07/21/2022", 33, 50)
                   (34, "backpack", "08/02/2022", 28, 54)
                   (35, "radio", "08/02/2019", 22, 55)
                   (36, "tent", "09/17/2018", 57, 61)
                   (37, "flashlight", "11/26/2022", 61, 79)]

cursor.executemany(salesInsert, equipment_sales)

# Commit the changes and close the connection
cnx.commit()
cnx.close()