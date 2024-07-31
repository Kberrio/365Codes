const fs = require('fs');

class Employee {
  constructor(id, name, hourlyRate) {
    this.id = id;
    this.name = name;
    this.hourlyRate = hourlyRate;
  }
}

class PayrollSystem {
  constructor() {
    this.employees = [];
  }

  addEmployee(employee) {
    this.employees.push(employee);
  }

  calculatePay(employeeId, hoursWorked) {
    const employee = this.employees.find(emp => emp.id === employeeId);
    if (!employee) {
      throw new Error('Employee not found');
    }
    return employee.hourlyRate * hoursWorked;
  }

  generatePayroll() {
    const payroll = this.employees.map(employee => ({
      id: employee.id,
      name: employee.name,
      pay: this.calculatePay(employee.id, 40) // Assuming 40 hours per week
    }));

    // Save payroll to a file
    fs.writeFileSync('payroll.json', JSON.stringify(payroll, null, 2));
    console.log('Payroll generated and saved to payroll.json');
  }
}

// Usage example
const payrollSystem = new PayrollSystem();

payrollSystem.addEmployee(new Employee(1, 'John Doe', 20));
payrollSystem.addEmployee(new Employee(2, 'Jane Smith', 25));

payrollSystem.generatePayroll();