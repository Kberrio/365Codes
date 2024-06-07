<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve form data
    $name = $_POST["name"];
    $email = $_POST["email"];
    $message = $_POST["message"];

    // Process the data (you can save it to a database, send an email, etc.)
    // For demonstration purposes, we'll just display the submitted data
    echo "Name: " . $name . "<br>";
    echo "Email: " . $email . "<br>";
    echo "Message: " . $message . "<br>";
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Simple Form</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
        <label for="name">Name:</label>
        <input type="text" name="name" id="name" required><br><br>

        <label for="email">Email:</label>
        <input type="email" name="email" id="email" required><br><br>

        <label for="message">Message:</label><br>
        <textarea name="message" id="message" rows="4" required></textarea><br><br>

        <input type="submit" value="Submit">
    </form>
</body>
</html>
