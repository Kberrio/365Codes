const XLSX = require('xlsx');

function sortExcelSheet(filePath, sheetName, sortColumn, ascending = true) {
  // Read the workbook
  const workbook = XLSX.readFile(filePath);

  // Get the worksheet
  const worksheet = workbook.Sheets[sheetName];

  // Convert the worksheet to an array of objects
  const data = XLSX.utils.sheet_to_json(worksheet);

  // Sort the data
  data.sort((a, b) => {
    if (a[sortColumn] < b[sortColumn]) return ascending ? -1 : 1;
    if (a[sortColumn] > b[sortColumn]) return ascending ? 1 : -1;
    return 0;
  });

  // Convert the sorted data back to a worksheet
  const newWorksheet = XLSX.utils.json_to_sheet(data);

  // Replace the old worksheet with the new sorted one
  workbook.Sheets[sheetName] = newWorksheet;

  // Write the workbook back to the file
  XLSX.writeFile(workbook, filePath);

  console.log(`Excel sheet '${sheetName}' in '${filePath}' has been sorted based on the '${sortColumn}' column.`);
}

// Example usage
const filePath = 'your_excel_file.xlsx';
const sheetName = 'Sheet1';
const sortColumn = 'Name'; // Replace with the column name you want to sort by
const ascending = true; // Set to false for descending order

sortExcelSheet(filePath, sheetName, sortColumn, ascending);