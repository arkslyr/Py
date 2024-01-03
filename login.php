<!DOCTYPE html>

<head>
    <title>SIGN UP HERE</title>
</head>

<body>
    <form action="" method="post">
        <table border="1">
            <tr>
                <th>username</th>
                <td><input type="text" name="rno" ></td>
            </tr>
            <tr>
                <th>password</th>
                <td><input type="password" name="pass"></td>
            </tr>
            <tr>
                <th colspan="2"><input type="submit"></th>
            </tr>

        </table>

</body>
<?php
$conn = mysqli_connect("localhost", "root", "", "student");
$rno=$_POST["rno"];
$p=$_POST["pass"];
$sq="SELECT * FROM `login` WHERE username='$rno' and password ='$p'";
$qr=mysqli_query($conn,$sq);
if(mysqli_num_rows($qr))
{
 	header("Location:bookdetails.php");  
}
else echo"<script> alert('no match found')</script>";
?>