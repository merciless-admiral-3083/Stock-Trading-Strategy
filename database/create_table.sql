CREATE TABLE stock_data (
    id SERIAL PRIMARY KEY,
    instrument VARCHAR(50),
    open DECIMAL,
    high DECIMAL,
    low DECIMAL,
    close DECIMAL,
    volume INTEGER,
    datetime TIMESTAMP
);
