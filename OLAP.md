---------------SQL----------------------------
CREATE TABLE SALES (
    Sales_ID INT PRIMARY KEY,
    Date_ID INT,
    Product_ID INT,
    Customer_ID INT,
    Emp_ID INT,
    FOREIGN KEY (Date_ID) REFERENCES TIME(Date_ID),
    FOREIGN KEY (Product_ID) REFERENCES PRODUCT(Product_ID),
    FOREIGN KEY (Customer_ID) REFERENCES CUSTOMER(Customer_ID),
    FOREIGN KEY (Emp_ID) REFERENCES EMPLOYEE(Emp_ID)
);



CREATE TABLE TIME (
    Date_ID INT PRIMARY KEY,
    Order_Date DATE,
    Year INT,
    Quarter INT,
    Month INT
);

CREATE TABLE PRODUCT (
    Product_ID INT PRIMARY KEY,
    Product_Name VARCHAR(50),
    Product_Company VARCHAR(50),
    Unit_Price DECIMAL(10,2),
    Supplier_ID INT
);

CREATE TABLE CUSTOMER (
    Customer_ID INT PRIMARY KEY,
    Customer_Name VARCHAR(40),
    Address VARCHAR(100),
    City VARCHAR(40),
    Zip VARCHAR(10),
    Region VARCHAR(30)
);

CREATE TABLE EMPLOYEE (
    Emp_ID INT PRIMARY KEY,
    Emp_Name VARCHAR(40),
    Title VARCHAR(30),
    Department VARCHAR(30),
    Region VARCHAR(30)
);


INSERT INTO TIME (Date_ID, Order_Date, Year, Quarter, Month)
VALUES 
(101, '2025-01-15', 2025, 1, 1),
(102, '2025-01-20', 2025, 1, 1),
(103, '2025-04-05', 2025, 2, 4),
(104, '2025-07-12', 2025, 3, 7),
(105, '2025-10-28', 2025, 4, 10);


INSERT INTO PRODUCT (Product_ID, Product_Name, Product_Company, Unit_Price, Supplier_ID)
VALUES 
(201, 'Wireless Mouse', 'TechGear', 29.99, 10),
(202, 'Mechanical Keyboard', 'GamerPro', 120.00, 11),
(203, '27-inch Monitor', 'ViewBright', 249.99, 10),
(204, 'USB-C Hub', 'ConnectAll', 45.50, 12),
(205, 'Laptop Stand', 'ErgoLife', 35.00, 11);

INSERT INTO CUSTOMER (Customer_ID, Customer_Name, Address, City, Zip, Region)
VALUES 
(301, 'Rohan Sharma', '456 Linking Rd', 'Mumbai', '400050', 'West'),
(302, 'Aditi Rao', '789 MG Road', 'Bangalore', '560001', 'South'),
(303, 'Vikram Singh', '123 Connaught Place', 'Delhi', '110001', 'North'),
(304, 'Sneha Patel', '101 C.G. Road', 'Ahmedabad', '380009', 'West'),
(305, 'Arjun Reddy', '32 Jubilee Hills', 'Hyderabad', '500033', 'South');

INSERT INTO EMPLOYEE (Emp_ID, Emp_Name, Title, Department, Region)
VALUES 
(401, 'Priya Singh', 'Sales Manager', 'Sales', 'West'),
(402, 'Amit Kumar', 'Sales Associate', 'Sales', 'North'),
(403, 'Nisha Gupta', 'Sales Associate', 'Sales', 'South'),
(404, 'Karan Malhotra', 'Regional Manager', 'Management', 'West'),
(405, 'Anjali Bose', 'Sales Support', 'Sales', 'South');

INSERT INTO SALES (Sales_ID, Date_ID, Product_ID, Customer_ID, Emp_ID, Total, Quantity, Discount)
VALUES 
(1001, 101, 201, 301, 401),
(1002, 102, 203, 302, 403),
(1003, 103, 202, 303, 402),
(1004, 104, 204, 301, 401),
(1005, 105, 205, 305, 405);


1. Roll up:

SELECT T.Year, SUM(S.Total) AS Total_Sales
FROM SALES S
JOIN TIME T ON S.Date_ID = T.Date_ID
GROUP BY T.Year;

2. Drill down

SELECT T.Year, T.Month, SUM(S.Total) AS Total_Sales
FROM SALES S
JOIN TIME T ON S.Date_ID = T.Date_ID
GROUP BY T.Year, T.Month;

3. Slicing

SELECT * FROM SALES
JOIN TIME ON SALES.Date_ID = TIME.Date_ID
WHERE TIME.Year = 2024;

4. Dicing

SELECT * FROM SALES S
JOIN TIME T ON S.Date_ID = T.Date_ID
JOIN PRODUCT P ON S.Product_ID = P.Product_ID
JOIN CUSTOMER C ON S.Customer_ID = C.Customer_ID
WHERE (T.Month IN ('7')) AND (P.Product_Name IN ('Laptop','Nokia')) AND (C.Region IN ('West','North'));

5. Pivot

SELECT P.Product_Name,
  SUM(CASE WHEN T.Year = 2024 THEN S.Total ELSE 0 END) AS '2024_Sales',
  SUM(CASE WHEN T.Year = 2025 THEN S.Total ELSE 0 END) AS '2025_Sales'
FROM SALES S
JOIN TIME T ON S.Date_ID = T.Date_ID
JOIN PRODUCT P ON S.Product_ID = P.Product_ID
GROUP BY P.Product_Name;
