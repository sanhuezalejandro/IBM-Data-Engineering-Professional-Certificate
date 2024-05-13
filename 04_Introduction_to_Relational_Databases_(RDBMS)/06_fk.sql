-- Define foreign key constraint for sales_detail referencing sales_transaction
ALTER TABLE sales_detail
ADD CONSTRAINT fk_sales_transaction
FOREIGN KEY (transaction_id)
REFERENCES sales_transaction(transaction_id);

-- Define foreign key constraint for sales_detail referencing product
ALTER TABLE sales_detail
ADD CONSTRAINT fk_product
FOREIGN KEY (product_id)
REFERENCES product(product_id);

-- Define foreign key constraint for product referencing product_type
ALTER TABLE product
ADD CONSTRAINT fk_product_type
FOREIGN KEY (product_type_id)
REFERENCES product_type(product_type_id);
