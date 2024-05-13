CREATE TABLE product (
  product_id SERIAL PRIMARY KEY,
  product_category VARCHAR(255),
  product_type VARCHAR(255),
  product_name VARCHAR(255),
  description TEXT,
  price NUMERIC(10, 2) NOT NULL
);