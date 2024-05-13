-- Definir las tablas
CREATE TABLE staff (
  staff_id SERIAL PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  position VARCHAR(255),
  start_date DATE,
  location VARCHAR(255)
);

CREATE TABLE customer (
  customer_id SERIAL PRIMARY KEY,
  customer_name VARCHAR(255) NOT NULL,
  customer_email VARCHAR(255),
  customer_since DATE,
  customer_card_number VARCHAR(255),
  birthdate DATE,
  gender VARCHAR(50)
);

CREATE TABLE product (
  product_id SERIAL PRIMARY KEY,
  product_category VARCHAR(255),
  product_type VARCHAR(255),
  product_name VARCHAR(255),
  description TEXT,
  price NUMERIC(10, 2) NOT NULL
);

CREATE TABLE sales_outlet (
  sales_outlet_id SERIAL PRIMARY KEY,
  sales_outlet_type VARCHAR(255),
  address VARCHAR(255),
  city VARCHAR(255),
  telephone VARCHAR(20),
  postal_code VARCHAR(20),
  manager VARCHAR(255)
);

CREATE TABLE sales_transactions (
  transaction_id SERIAL PRIMARY KEY,
  transaction_date DATE NOT NULL,
  transaction_time TIME NOT NULL,
  sales_outlet_id INTEGER NOT NULL REFERENCES sales_outlet(sales_outlet_id),
  staff_id INTEGER NOT NULL REFERENCES staff(staff_id),
  customer_id INTEGER NOT NULL REFERENCES customer(customer_id),
  product_id INTEGER NOT NULL REFERENCES product(product_id),
  quantity INTEGER NOT NULL,
  price NUMERIC(10, 2) NOT NULL
);
