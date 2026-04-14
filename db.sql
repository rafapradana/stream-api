CREATE TABLE people (
    pk SERIAL PRIMARY KEY,
    sk INTEGER NOT NULL,
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    dob DATE NOT NULL,
    zipcode TEXT NOT NULL
);

