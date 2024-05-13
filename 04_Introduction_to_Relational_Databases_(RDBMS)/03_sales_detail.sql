
DROP TABLE IF EXISTS public.sales_transaction CASCADE;

CREATE TABLE sales_transaction (
  transaction_id SERIAL PRIMARY KEY,
  transaction_date DATE NOT NULL,
  transaction_time TIME NOT NULL,
  sales_detail_id INTEGER NOT NULL, -- Foreign key referencing sales_detail table
  quantity INTEGER NOT NULL,
  price NUMERIC(10, 2) NOT NULL
);

CREATE TABLE sales_detail (
  sales_detail_id SERIAL PRIMARY KEY,
  sales_outlet_id INTEGER NOT NULL,
  staff_id INTEGER NOT NULL,
  customer_id INTEGER NOT NULL,
  product_id INTEGER NOT NULL
);
