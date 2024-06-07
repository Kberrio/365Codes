<?php
function generateRandomPassword($length = 12) {
    $characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+';
    $password = '';
    $charCount = strlen($characters);

    for ($i = 0; $i < $length; $i++) {
        $randomIndex = mt_rand(0, $charCount - 1);
        $password .= $characters[$randomIndex];
    }

    return $password;
}

$randomPassword = generateRandomPassword();
?>

<!DOCTYPE html>
<html>
<head>
    <title>Random Password Generator</title>
</head>
<body>
    <h1>Random Password Generator</h1>
    <p>Click the button to generate a random password:</p>
    <button onclick="generatePassword()">Generate Password</button>
    <p id="password"><?php echo $randomPassword; ?></p>

    <script>
        function generatePassword() {
            var passwordElement = document.getElementById("password");
            var xhr = new XMLHttpRequest();
            xhr.onreadystatechange = function () {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    passwordElement.innerText = xhr.responseText;
                }
            };
            xhr.open("GET", "generate_password.php", true);
            xhr.send();
        }
    </script>
</body>
</html>
