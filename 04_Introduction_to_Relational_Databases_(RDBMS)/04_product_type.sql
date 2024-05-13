
DROP TABLE IF EXISTS public.product CASCADE;

CREATE TABLE product (
  product_id SERIAL PRIMARY KEY,
  product_name VARCHAR(255) NOT NULL,
  product_type_id INTEGER NOT NULL -- Foreign key referencing product_type table
);

CREATE TABLE product_type (
  product_type_id SERIAL PRIMARY KEY,
  product_category VARCHAR(255) NOT NULL,
  product_type VARCHAR(255) NOT NULL
);
