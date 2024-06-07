const oracledb = require('oracledb');

// Connection credentials
const connectionConfig = {
  user: 'your_username',
  password: 'your_password',
  connectString: 'your_connection_string' // Example: 'localhost:1521/ORCLCDB.localdomain'
};

async function run() {
  let connection;

  try {
    // Establish connection
    connection = await oracledb.getConnection(connectionConfig);

    // Execute SQL query
    const result = await connection.execute(
      `SELECT * FROM your_table`
    );

    // Log fetched rows
    console.log("Query Result:", result.rows);

  } catch (err) {
    console.error("Error occurred:", err);
  } finally {
    // Close connection
    if (connection) {
      try {
        await connection.close();
        console.log("Connection closed");
      } catch (err) {
        console.error("Error closing connection:", err);
      }
    }
  }
}

// Run the program
run();
