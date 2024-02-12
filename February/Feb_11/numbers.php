<!DOCTYPE html>
<html>
<head>
    <title>Odd/Even Checker</title>
</head>
<body>

<form method="post">
    Enter a number: <input type="text" name="number">
    <input type="submit" name="submit" value="Check">
</form>

<?php
if(isset($_POST['submit'])) {
    // Get user input
    $number = $_POST['number'];
    
    // Check if the input is numeric
    if(is_numeric($number)) {
        // Check if the number is even or odd
        if($number % 2 == 0) {
            echo "<p>$number is even.</p>";
        } else {
            echo "<p>$number is odd.</p>";
        }
    } else {
        // If input is not numeric, display error message
        echo "<p>Please enter a valid number.</p>";
    }
}
?>

</body>
</html>
