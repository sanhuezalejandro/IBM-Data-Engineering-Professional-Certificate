
DROP TABLE IF EXISTS public.staff CASCADE;
DROP TABLE IF EXISTS public.sales_outlet CASCADE;
DROP TABLE IF EXISTS public.customer CASCADE;
DROP TABLE IF EXISTS public.sales_detail CASCADE;
DROP TABLE IF EXISTS public.product CASCADE;
DROP TABLE IF EXISTS public.product_type CASCADE;
DROP TABLE IF EXISTS public.sales_transaction CASCADE;
--


CREATE TABLE sales_transaction (
  transaction_id SERIAL PRIMARY KEY,
  transaction_date DATE NOT NULL,
  transaction_time TIME NOT NULL,
  sales_outlet_id INTEGER NOT NULL,
  staff_id INTEGER NOT NULL,
  customer_id INTEGER NOT NULL
);

CREATE TABLE sales_detail (
  sales_detail_id SERIAL PRIMARY KEY,
  sales_outlet_id INTEGER NOT NULL,
  staff_id INTEGER NOT NULL,
  customer_id INTEGER NOT NULL,
  transaction_id INTEGER NOT NULL,
  product_id INTEGER NOT NULL
);

CREATE TABLE product (
  product_id SERIAL PRIMARY KEY,
  product_name VARCHAR(255) NOT NULL,
  product_type_id INTEGER NOT NULL
);

CREATE TABLE product_type (
  product_type_id SERIAL PRIMARY KEY,
  product_category VARCHAR(255) NOT NULL,
  product_type VARCHAR(255) NOT NULL
);
