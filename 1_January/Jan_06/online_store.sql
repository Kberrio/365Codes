-- Create the database
CREATE DATABASE OnlineStore;

-- Use the OnlineStore database
USE OnlineStore;

-- Create the Products table
CREATE TABLE Products (
	product_id INT PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR (50),
    price DECIMAL (10, 2),
    stock_quantity INT
);

-- Create the Customers table
CREATE TABLE Customers (
	customer_id INT PRIMARY KEY,
    customer_name VARCHAR (255),
    email VARCHAR(255),
    registration_date DATE
);

-- Create the Orders table
CREATE TABLE Orders (
	order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL (10, 2),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- Create the Order_Products table (for tracking products)
CREATE TABLE Orders_Products (
    order_id INT,
    product_id INT,
    quantity INT,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);
    
-- Insert sample data into the Products table
INSERT INTO Products (product_id, product_name, category, price, stock_quantity)
VALUES
	(1, 'Laptop', 'Electronics', 800.00, 20),
    (2, 'Smartphone', 'Electronics', 1800.00, 90),
    (3, 'T-shirt', 'Apparel', 20.00, 250),
    (4, 'Running Shoes', 'Footwear', 80.00, 70),
    (5, 'Headphones', 'Electronics', 50.00, 40);
    
-- Insert sample data into the Customers table
INSERT INTO Customers (customer_id, customer_name, email, registration_date)
VALUES
	(1, 'John Doe', 'john.doe@example.com', '2023-01-15'),
    (2, 'Jane Smith', 'jane.smith@example.com', '2023-02-25'),
    (3, 'Alice Johnson', 'alice.johnson@example.com', '2013-12-01'),
    (4, 'Bob Brown', 'bob.brown@example.com', '2002-06-11'),
    (5, 'Eva Wilson', 'eva.wilson@example.com', '2022-09-19');

-- Insert sample data into the Orders table
INSERT INTO Orders (order_id, customer_id, order_date, total_amount)
VALUES
	(1, 1, '2023-01-01', 1200.00),
    (2, 2, '2022-11-07', 1200.00),
    (3, 3, '2021-08-11', 1200.00),
    (4, 1, '2020-05-18', 1200.00),
    (5, 4, '2009-03-13', 1200.00);
    
-- Insert sample data into the Orders_Product table
INSERT INTO Orders_Products (order_id, product_id, quantity)
VALUES
	(1, 1, 2),
    (1, 3, 3),
    (2, 2, 1),
    (2, 4, 2),
    (3, 3, 5),
    (4, 1, 1),
    (4, 5, 2),
    (5, 4, 3),
    (5, 5, 1);