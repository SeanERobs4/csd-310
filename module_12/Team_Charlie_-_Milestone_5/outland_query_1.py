import mysql.connector

# Connect to the MySQL server
cnx = mysql.connector.connect(host='127.0.0.1', user='outland_user', password='hike', database='outland_adventures')

cursor = cnx.cursor()

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
    at_capacity VARCHAR(50),
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
    years_old INT,
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
    visa VARCHAR(50),
    inoculation VARCHAR(50),
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
employees = [(1, "Blythe", "Timmerson", "Founder"),
             (2, "Jim", "Ford", "Founder"),
             (3, "Mac", "MacNeil", "Guide"),
             (4, "Duke", "Marland", "Guide"),
             (5, "Anita", "Gallegos", "Marketing"),
             (6, "Dimitros", "Stravopolous", "Supplier"),
             (7, "Mei", "Wong", "Ecomm"),]

cursor.executemany(employeesInsert, employees)

adventuresInsert = "INSERT INTO adventures(adventure_id, location, departure_date, return_date, at_capacity, employee_id) VALUES (%s, %s, %s, %s, %s, %s)"
adventures = [(1, "Africa", "2017-06-12", "2017-09-15", "Yes", 3),
              (2, "Asia", "2018-06-12", "2018-09-15", "Yes", 4),
              (3, "Southern Europe", "2019-06-12", "2019-09-15", "Yes", 3),
              (4, "Africa", "2020-06-12", "2020-09-15", "Yes", 4),
              (5, "Asia", "2020-06-12", "2020-09-16", "Yes", 3),
              (6, "Southern Europe", "2021-06-12", "2020-09-16", "No", 4),
              (7, "Africa", "2021-06-12", "2021-09-15", "Yes", 3),
              (8, "Asia", "2022-06-12", "2022-09-15", "Yes", 4),
              (9, "Southern Europe", "2022-06-12", "2022-09-16", "No", 3),]

cursor.executemany(adventuresInsert, adventures)

equipmentInsert = "INSERT INTO equipment(equipment_id, equipment_name, onboard_date, years_old, adventure_id) VALUES (%s, %s, %s, %s, %s)"
equipment = [(58, "Radio", "2013-03-10", 10, 1),
             (59, "Rope", "2013-03-10", 10, 1),
             (60, "Gloves", "2013-03-10", 10, 1),
             (61, "Tent", "2013-12-14", 10, 1),
             (62, "Flaregun", "2014-03-11", 9, 1),
             (63, "Radio", "2014-03-11", 9, 2),
             (64, "Rope", "2014-03-11", 9, 2),
             (65, "Gloves", "2014-12-14", 9, 2),
             (66, "Tent", "2014-12-14", 9, 2),
             (67, "Flaregun", "2015-03-11", 8, 2),
             (68, "Radio", "2015-03-11", 8, 3),
             (69, "Rope", "2015-12-14", 8, 3),
             (70, "Gloves", "2016-03-11", 7, 3),
             (71, "Tent", "2017-12-14", 6, 3),
             (72, "Flaregun", "2017-12-14", 6, 3),
             (73, "Radio", "2017-03-10", 6, 4),
             (74, "Rope", "2017-03-10", 6, 4),
             (75, "Gloves", "2017-12-12", 6, 4),
             (76, "Tent", "2017-12-12", 6, 4),
             (77, "Flaregun", "2017-12-12", 6, 4),
             (78, "Radio", "2018-03-10", 5, 5),
             (79, "Rope", "2018-03-10", 5, 5),
             (80, "Gloves", "2018-03-10", 5, 5),
             (81, "Tent", "2018-12-14", 5, 5),
             (82, "Flaregun", "2018-12-14", 5, 5),
             (83, "Radio", "2018-12-14", 5, 6),
             (84, "Rope", "2019-03-11", 4, 6),
             (85, "Gloves", "2019-03-11", 4, 6),
             (86, "Tent", "2019-03-11", 4, 6),
             (87, "Flaregun", "2019-03-11", 4, 6),
             (88, "Radio", "2019-12-12", 4, 7),
             (89, "Rope", "2019-12-12", 4, 7),
             (90, "Gloves", "2019-12-12", 4, 7),
             (91, "Tent", "2020-03-13", 3, 7),
             (92, "Flaregun", "2020-03-13", 3, 7),
             (93, "Radio", "2020-03-13", 3, 8),
             (94, "Rope", "2020-03-13", 3, 8),
             (95, "Gloves", "2020-12-15", 3, 8),
             (96, "Tent", "2020-12-15", 3, 8),
             (97, "Flaregun", "2021-03-10", 2, 8),
             (98, "Radio", "2021-03-10", 2, 9),
             (99, "Rope", "2021-12-10", 2, 9),
             (100, "Gloves", "2021-12-10", 1, 9),
             (101, "Tent", "2022-03-11", 1, 9),
             (102, "Flaregun", "2022-03-11", 1, 9),]

cursor.executemany(equipmentInsert, equipment)

customersInsert = "INSERT INTO customers(customer_id, first_name, last_name, airline, visa, inoculation, adventure_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
customers = [(89, "Sarah", "Seaholm", "southwest", "Yes", "Yes", 1),
             (90, "Karrah", "McAfee", "delta", "Yes", "Yes", 1),
             (91, "Josh", "Pickett", "delta", "Yes", "No", 1),
             (92, "Jordan", "Pickett", "delta", "Yes", "No", 1),
             (93, "Thomas", "Friar", "southwest", "Yes", "No", 2),
             (94, "Alex", "LaCroix", "southwest", "Yes", "Yes", 2),
             (95, "Peter", "Yu", "delta", "No", "Yes", 2),
             (96, "James", "Jameson", "southwest", "Yes", "Yes", 2),
             (97, "Leonard", "Seabrook", "delta", "Yes", "Yes", 3),
             (98, "Jack", "Wong", "southwest", "Yes", "Yes", 3),
             (99, "Carol", "Nielsen", "delta", "Yes", "Yes", 3),
             (100, "Kimberley", "Lund", "delta", "Yes", "No", 3),
             (101, "John", "Merlin", "southwest", "Yes", "Yes", 4),
             (102, "Katrina", "Bishop", "delta", "No", "Yes", 4),
             (103, "Jacob", "Garcia", "southwest", "Yes", "Yes", 4),
             (104, "Siobhan", "Doyle", "southwest", "Yes", "Yes", 4),
             (105, "Tyler", "Kennedy", "delta", "No", "Yes", 5),
             (106, "Samantha", "Forager", "delta", "Yes", "Yes", 5),
             (107, "Frank", "Melvin", "southwest", "Yes", "Yes", 5),
             (108, "Jodi", "Gilbert", "delta", "Yes", "Yes", 5),
             (109, "Millie", "Gulley", "southwest", "Yes", "Yes", 6),
             (110, "Kelly", "Johnston", "southwest", "Yes", "No", 6),
             (111, "Andrew", "Pine", "delta", "Yes", "Yes", 7),
             (112, "Shela", "Sorenson", "delta", "No", "Yes", 7),
             (113, "Gary", "Palmer", "southwest", "Yes", "Yes", 7),
             (114, "Gerald", "Palmer", "southwest", "Yes", "Yes", 7),
             (115, "Tina", "Meltris", "delta", "Yes", "Yes", 8),
             (116, "Gordon", "Meltris", "delta", "Yes", "Yes", 8),
             (117, "Robin", "Meltris", "delta", "Yes", "Yes", 8),
             (118, "Jessie", "Meltris", "delta", "Yes", "Yes", 8),
             (119, "Kyle", "Frisk", "southwest", "Yes", "No", 9),
             (120, "Daniel", "Thompson", "delta", "Yes", "Yes", 9),]

cursor.executemany(customersInsert, customers)

salesInsert = "INSERT INTO equipment_sales(sales_id, equipment_name, sales_date, equipment_id, customer_id) VALUES (%s, %s, %s, %s, %s)"
equipment_sales = [(33, "gloves", "2015-01-12", 58, 89),
                   (34, "rope", "2015-03-13", 59, 89),
                   (35, "gloves", "2015-06-12", 60, 90),
                   (36, "tent", "2015-06-12", 61, 90),
                   (37, "radio", "2015-06-12", 62, 90),
                   (38, "tent", "2015-06-12", 63, 90),
                   (39, "gloves", "2015-06-12", 64, 90),
                   (40, "radio", "2017-04-15", 65, 92),
                   (41, "rope", "2017-06-13", 66, 93),
                   (42, "rope", "2017-06-13", 67, 94),
                   (43, "gloves", "2017-06-13", 68, 94),
                   (44, "rope", "2017-06-13", 69, 94),
                   (45, "rope", "2017-09-01", 70, 95),
                   (46, "gloves", "2017-09-01", 71, 95),
                   (47, "gloves", "2017-09-01", 72, 96),]

cursor.executemany(salesInsert, equipment_sales)

# --------------------------------------------------------------

# Display Timestamp for Report 1
reportTime = "SELECT NOW();"
cursor.execute(reportTime)
showTime = cursor.fetchall()
for reportTime in showTime:
    print("\nTime of Report:")
    print(reportTime)
    print("-- Report 1 --")
# Report 1: Pulls several columns from the equipment_sales table in our Outland database.
report1 = "SELECT sales_id, equipment_name, sales_date FROM equipment_sales ORDER BY equipment_name;"
# Execute report
cursor.execute(report1)
# Use fetchall() method
myresult1 = cursor.fetchall()
for report1 in myresult1:
    print(report1)

# Display Timestamp for Report 2
reportTime = "SELECT NOW();"
cursor.execute(reportTime)
showTime = cursor.fetchall()
for reportTime in showTime:
    print("\nTime of Report:")
    print(reportTime)
    print("-- Report 2 --")
# Report 2: Joins columns from two tables; our adventures table, as well as our customers table.
report2 = "SELECT adventure_id, at_capacity, location, departure_date, return_date FROM adventures;"
# Execute report
cursor.execute(report2)
# Use fetchall() method
myresult2 = cursor.fetchall()
for report2 in myresult2:
    print(report2)

# Display Timestamp for Report 3
reportTime = "SELECT NOW();"
cursor.execute(reportTime)
showTime = cursor.fetchall()
for reportTime in showTime:
    print("\nTime of Report:")
    print(reportTime)
    print("-- Report 3 --")
# Report 3: Pulls columns from our equipment table to help identify what equipment_id
# is associated to what pieces of gear, as well as our onboard date of that equipment.
report3 = "SELECT equipment_id, equipment_name, onboard_date, years_old FROM equipment WHERE equipment_id >= 73;"
# Execute report
cursor.execute(report3)
# Use fetchall() method
myresult3 = cursor.fetchall()
for report3 in myresult3:
    print(report3)

# Commit the changes and close the connection
cnx.commit()
cnx.close()