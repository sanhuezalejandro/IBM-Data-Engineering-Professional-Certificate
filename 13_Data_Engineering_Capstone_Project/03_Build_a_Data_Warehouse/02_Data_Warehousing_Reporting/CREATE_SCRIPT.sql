-- Create the table

---------------------------------------
CREATE TABLE public."DimDate"
(
    dateid integer NOT NULL,
    date date,
    Year integer,
    Quarter integer,
    QuarterName character(50),
    Month integer,
    Monthname character(50),
    Day integer,
    Weekday integer,
    WeekdayName character(50),
    CONSTRAINT "DimDate_pkey" PRIMARY KEY (dateid)
)

-------------------------------------------------------

CREATE TABLE public."DimCategory"
(
    categoryid integer NOT NULL,
    category character(50),
    CONSTRAINT "DimCategory_pkey" PRIMARY KEY (categoryid)
)

-------------------------------------------------------

CREATE TABLE public."DimCountry"
(
    countryid integer NOT NULL,
    country character(50),
    CONSTRAINT "DimCountry_pkey" PRIMARY KEY (countryid)
)

-----------------------------------------------------------

CREATE TABLE public."FactSales"
(
    orderid integer NOT NULL,
    dateid integer,
    countryid integer,
    categoryid integer,
    amount integer,
    CONSTRAINT "FactSales_pkey" PRIMARY KEY (orderid),
    CONSTRAINT "FactSales_dateid_fkey" FOREIGN KEY (dateid)
        REFERENCES public."DimDate" (dateid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "FactSales_countryid_fkey" FOREIGN KEY (countryid)
        REFERENCES public."DimCountry" (countryid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "FactSales_categoryid_fkey" FOREIGN KEY (categoryid)
        REFERENCES public."DimCategory" (categoryid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);
