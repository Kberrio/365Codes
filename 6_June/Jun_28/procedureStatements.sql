-- Create a more complex procedure to retrieve employees by department
DELIMITER //

CREATE PROCEDURE GetEmployeesDetails(IN deptName VARCHAR(255))
BEGIN
    DECLARE avg_salary DECIMAL(10, 2);
    
    -- Calculate average salary in the department
    SELECT AVG(salary) INTO avg_salary
    FROM employees
    WHERE department = deptName;
    
    -- Select employees sorted by hire date
    SELECT employee_id, first_name, last_name, hire_date, salary
    FROM employees
    WHERE department = deptName
    ORDER BY hire_date;
    
    -- Return average salary as part of the procedure output
    SELECT avg_salary AS average_salary;
END //

DELIMITER ;
