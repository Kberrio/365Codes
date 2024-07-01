// Assuming the JSON data is stored in a variable called `data`
const data = {
    "company": {
      "name": "Extreme Tech Solutions",
      "address": {
        "street": "123 Hyperlane",
        "city": "Techville",
        "state": "Innovation",
        "postalCode": "98765-4321",
        "country": "Futuristan"
      },
      "departments": [
        {
          "name": "Research and Development",
          "employees": [
            {
              "id": 1,
              "name": "Dr. Ada Lovelace",
              "position": "Lead Scientist",
              "skills": ["AI", "Quantum Computing", "Nanotechnology"],
              "projects": [
                {
                  "name": "Project Singularity",
                  "status": "Active",
                  "budget": 5000000,
                  "milestones": [
                    {"phase": "Conceptualization", "deadline": "2024-12-31"},
                    {"phase": "Prototyping", "deadline": "2025-06-30"},
                    {"phase": "Testing", "deadline": "2026-03-31"}
                  ]
                },
                {
                  "name": "Quantum Leap",
                  "status": "Completed",
                  "budget": 2000000,
                  "milestones": [
                    {"phase": "Conceptualization", "deadline": "2023-01-31"},
                    {"phase": "Prototyping", "deadline": "2023-06-30"},
                    {"phase": "Testing", "deadline": "2024-01-31"}
                  ]
                }
              ]
            },
            {
              "id": 2,
              "name": "Grace Hopper",
              "position": "Senior Developer",
              "skills": ["Software Engineering", "Cybersecurity", "Data Analysis"],
              "projects": [
                {
                  "name": "Code Secure",
                  "status": "Active",
                  "budget": 1000000,
                  "milestones": [
                    {"phase": "Research", "deadline": "2024-08-31"},
                    {"phase": "Development", "deadline": "2025-02-28"},
                    {"phase": "Deployment", "deadline": "2025-09-30"}
                  ]
                }
              ]
            }
          ]
        },
        {
          "name": "Marketing",
          "employees": [
            {
              "id": 3,
              "name": "David Ogilvy",
              "position": "Marketing Director",
              "skills": ["Advertising", "Public Relations", "Digital Marketing"],
              "campaigns": [
                {
                  "name": "Tech Titan",
                  "status": "Ongoing",
                  "budget": 1500000,
                  "milestones": [
                    {"phase": "Market Research", "deadline": "2024-07-31"},
                    {"phase": "Creative Development", "deadline": "2024-10-31"},
                    {"phase": "Launch", "deadline": "2025-01-31"}
                  ]
                }
              ]
            }
          ]
        }
      ],
      "financials": {
        "fiscalYear": 2024,
        "revenue": 100000000,
        "expenses": 85000000,
        "netIncome": 15000000,
        "assets": {
          "currentAssets": 30000000,
          "fixedAssets": 50000000,
          "totalAssets": 80000000
        },
        "liabilities": {
          "currentLiabilities": 20000000,
          "longTermLiabilities": 30000000,
          "totalLiabilities": 50000000
        },
        "equity": 30000000
      },
      "vision": "To pioneer the future of technology with innovation and excellence.",
      "mission": "To deliver cutting-edge solutions that empower businesses and individuals worldwide."
    },
    "productPortfolio": [
      {
        "id": "P001",
        "name": "Quantum Computer",
        "category": "Hardware",
        "price": 1000000,
        "features": [
          {"feature": "Quantum Processing", "description": "Revolutionary quantum speed and efficiency."},
          {"feature": "Secure Computing", "description": "Unparalleled security with quantum encryption."},
          {"feature": "Energy Efficient", "description": "Low power consumption with high performance."}
        ]
      },
      {
        "id": "P002",
        "name": "AI Assistant",
        "category": "Software",
        "price": 20000,
        "features": [
          {"feature": "Natural Language Processing", "description": "Understand and respond to human language."},
          {"feature": "Machine Learning", "description": "Continuous improvement through data analysis."},
          {"feature": "Personalization", "description": "Customized responses and actions."}
        ]
      }
    ],
    "clients": [
      {
        "clientId": "C001",
        "name": "Tech Innovators Inc.",
        "industry": "Technology",
        "contact": {
          "name": "John Doe",
          "title": "CTO",
          "email": "johndoe@techinnovators.com",
          "phone": "555-1234"
        },
        "contracts": [
          {
            "contractId": "CT001",
            "services": ["AI Development", "Cybersecurity"],
            "contractValue": 5000000,
            "startDate": "2023-01-01",
            "endDate": "2025-12-31"
          }
        ]
      },
      {
        "clientId": "C002",
        "name": "Future Enterprises",
        "industry": "Finance",
        "contact": {
          "name": "Jane Smith",
          "title": "CIO",
          "email": "janesmith@futureenterprises.com",
          "phone": "555-5678"
        },
        "contracts": [
          {
            "contractId": "CT002",
            "services": ["Quantum Computing Solutions"],
            "contractValue": 3000000,
            "startDate": "2024-06-01",
            "endDate": "2026-05-31"
          }
        ]
      }
    ]
  };
  
  // Functions to process the JSON data
  function displayCompanyInfo(company) {
    console.log(`Company Name: ${company.name}`);
    console.log(`Address: ${company.address.street}, ${company.address.city}, ${company.address.state}, ${company.address.postalCode}, ${company.address.country}`);
    console.log(`Vision: ${company.vision}`);
    console.log(`Mission: ${company.mission}`);
  }
  
  function displayDepartmentInfo(departments) {
    departments.forEach(department => {
      console.log(`\nDepartment: ${department.name}`);
      department.employees.forEach(employee => {
        console.log(`  Employee: ${employee.name}, Position: ${employee.position}`);
        console.log(`  Skills: ${employee.skills.join(', ')}`);
        employee.projects?.forEach(project => {
          console.log(`    Project: ${project.name}, Status: ${project.status}, Budget: $${project.budget}`);
          project.milestones.forEach(milestone => {
            console.log(`      Milestone: ${milestone.phase}, Deadline: ${milestone.deadline}`);
          });
        });
      });
    });
  }
  
  function displayFinancialInfo(financials) {
    console.log(`\nFinancials (Fiscal Year: ${financials.fiscalYear}):`);
    console.log(`  Revenue: $${financials.revenue}`);
    console.log(`  Expenses: $${financials.expenses}`);
    console.log(`  Net Income: $${financials.netIncome}`);
    console.log(`  Assets:`);
    console.log(`    Current: $${financials.assets.currentAssets}`);
    console.log(`    Fixed: $${financials.assets.fixedAssets}`);
    console.log(`    Total: $${financials.assets.totalAssets}`);
    console.log(`  Liabilities:`);
    console.log(`    Current: $${financials.liabilities.currentLiabilities}`);
    console.log(`    Long-Term: $${financials.liabilities.longTermLiabilities}`);
    console.log(`    Total: $${financials.liabilities.totalLiabilities}`);
    console.log(`  Equity: $${financials.equity}`);
  }
  
  function displayProductPortfolio(products) {
    console.log(`\nProduct Portfolio:`);
    products.forEach(product => {
      console.log(`  Product: ${product.name}, Category: ${product.category}, Price: $${product.price}`);
      product.features.forEach(feature => {
        console.log(`    Feature: ${feature.feature}, Description: ${feature.description}`);
      });
    });
  }
  
  function displayClientInfo(clients) {
    console.log(`\nClients:`);
    clients.forEach(client => {
      console.log(`  Client: ${client.name}, Industry: ${client.industry}`);
      console.log(`  Contact: ${client.contact.name}, Title: ${client.contact.title}, Email: ${client.contact.email}, Phone: ${client.contact.phone}`);
      client.contracts.forEach(contract => {
        console.log(`    Contract: ${contract.contractId}, Services: ${contract.services.join(', ')}, Value: $${contract.contractValue}`);
        console.log(`    Start Date: ${contract.startDate}, End Date: ${contract.endDate}`);
      });
    });
  }
  
  // Displaying all the information
  displayCompanyInfo(data.company);
  displayDepartmentInfo(data.company.departments);
  displayFinancialInfo(data.company.financials);
  displayProductPortfolio(data.productPortfolio);
  