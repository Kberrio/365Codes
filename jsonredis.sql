-- 1. Define the structure of your data
CREATE TABLE complex_data (
    id SERIAL PRIMARY KEY,
    data JSONB
);

-- 2. Convert the data to JSON format
-- Example data in JSON format
-- {
--     "name": "John",
--     "age": 30,
--     "address": {
--         "street": "123 Main St",
--         "city": "New York",
--         "zipcode": "10001"
--     },
--     "emails": ["john@example.com", "john.doe@example.com"]
-- }

-- 3. Store the JSON data in Redis
-- Assuming you have a Redis instance running and Redis' JSON module enabled
INSERT INTO complex_data (data) VALUES ('{
    "name": "John",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "zipcode": "10001"
    },
    "emails": ["john@example.com", "john.doe@example.com"]
}') RETURNING id;

-- This will insert the JSON data into the "complex_data" table and return the ID of the inserted row.