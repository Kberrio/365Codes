import java.sql.*;

public class Main {
    // JDBC URL, username, and password of MySQL server
    static final String JDBC_URL = "jdbc:mysql://localhost:3306/example";
    static final String USERNAME = "username";
    static final String PASSWORD = "password";

    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;

        try {
            // Register JDBC driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            // Open a connection
            System.out.println("Connecting to database...");
            conn = DriverManager.getConnection(JDBC_URL, USERNAME, PASSWORD);

            // Create a statement
            System.out.println("Creating table...");
            stmt = conn.createStatement();
            String sql = "CREATE TABLE IF NOT EXISTS users " +
                         "(id INT AUTO_INCREMENT PRIMARY KEY, " +
                         " name VARCHAR(255), " +
                         " age INT)";
            stmt.executeUpdate(sql);
            System.out.println("Table created successfully");

            // Insert some data
            System.out.println("Inserting data...");
            sql = "INSERT INTO users (name, age) VALUES ('Alice', 30), ('Bob', 25)";
            stmt.executeUpdate(sql);
            System.out.println("Data inserted successfully");

            // Retrieve data
            System.out.println("Retrieving data...");
            sql = "SELECT * FROM users";
            ResultSet rs = stmt.executeQuery(sql);

            // Display retrieved data
            while (rs.next()) {
                int id = rs.getInt("id");
                String name = rs.getString("name");
                int age = rs.getInt("age");
                System.out.println("ID: " + id + ", Name: " + name + ", Age: " + age);
            }
            rs.close();
        } catch (SQLException | ClassNotFoundException e) {
            e.printStackTrace();
        } finally {
            // Close resources
            try {
                if (stmt != null) stmt.close();
                if (conn != null) conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
