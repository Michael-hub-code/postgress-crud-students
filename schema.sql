-- Create the students table
CREATE TABLE IF NOT EXISTS students (
  student_id      INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  first_name      TEXT    NOT NULL,
  last_name       TEXT    NOT NULL,
  email           TEXT    NOT NULL UNIQUE,
  enrollment_date DATE
);
