-- Create 'departments' table
CREATE TABLE IF NOT EXISTS departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100),
    location VARCHAR(100)
);

-- Insert sample data into 'departments'
INSERT INTO departments (department_name, location)
VALUES ('HR', 'New York'), ('IT', 'San Francisco');

-- Create 'employees' table
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_name VARCHAR(100),
    department_id INT,
    hire_date DATE,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- Modify 'departments' table
ALTER TABLE departments MODIFY location VARCHAR(150);

-- Delete a department by department_id
DELETE FROM departments WHERE department_id = 1;
