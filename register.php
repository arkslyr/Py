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
                <th>confirm password</th>
                <td><input type="password" name="repass"></td>
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
else echo"<script> alert('Password didnt match');
</script>";
?>