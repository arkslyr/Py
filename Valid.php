<!DOCTYPE html>

<head>
    <title>SIGN UP HERE</title>
    <script>
        function validateForm() {
            var username = document.forms["signupForm"]["rno"].value;
            var p = document.forms["signupForm"]["pass"].value;
            var r = document.forms["signupForm"]["repass"].value;
            if (username === "") {
                alert("Username must be filled out");
                return false;
            }
            if (p != r) {
                alert("Password doesnt Match");
                return false;
            }
            if (!username.startsWith("TVE-MCA") || username.length !== 13) {
                alert("Username must start with 'TVE-MCA' and have a length of 13 characters");
                return false;
            }
        }
    </script>
</head>

<body>
    <form name="signupForm" action="" method="post" onsubmit="return validateForm()" >
        <table border="1">
            <tr>
                <th>username</th>
                <td><input type="text" name="rno"></td>
            </tr>
            <tr>
                <th>password</th>
                <td><input type="password" name="pass"></td>
            </tr>
            <tr>
                <th>confirm password</th>
                <td><input type="password" name="repass"></td>
            </tr>
            <tr>
                <th colspan="2"><input type="submit"></th>
            </tr>

        </table>
    </form>

</body>


<?php
$conn = mysqli_connect("localhost", "root", "", "student");
$rno=$_POST["rno"];
$p=$_POST["pass"];
$repass=$_POST["repass"];
if($p==$repass)
{
    $sq="INSERT INTO `login`(`username`, `password`) VALUES ('$rno','$p')";
    $qr=mysqli_query($conn,$sq);
    if($qr)
    {
 	    echo "<script> alert('succesfully inserted 1 row');
	    </script>";    
    }
    else echo"<script> alert('error');
	 </script>";
}
?>

</html>
