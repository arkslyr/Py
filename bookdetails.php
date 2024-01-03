<!DOCTYPE html>

<head>
    <title>SIGN UP HERE</title>
</head>

<body>
    <form action="" method="post">
        <table border="1">
            <tr>
                <th>Bookid</th>
                <td><input type="text" name="bid" ></td>
            </tr>
            <tr>
                <th>Book Name</th>
                <td><input type="text" name="bname"></td>
            </tr>
            <tr>
                <th>Author Name</th>
                <td><input type="text" name="aname" ></td>
            </tr>
            <tr>
                <th>No of copies</th>
                <td><select name="ncpy">
                    <?php
                    for($i=1;$i<=10;$i++)
                    {
                        echo"<option value=".$i.">".$i."</option>";
                    }

                    ?>
                </select></td>
            </tr>
            <tr>
                <th colspan="2"><input type="submit"></th>
            </tr>

        </table>

</body>
<?php
$conn = mysqli_connect("localhost", "root", "", "student");
$bid=$_POST["bid"];
$ncpy=$_POST["ncpy"];
$aname=$_POST["aname"];
$bname=$_POST["bname"];
$sq="INSERT INTO `book`(`bookid`, `bookname`, `author`, `noofcopies`) VALUES ('$bid','$bname','$aname','$ncpy')";
$qr=mysqli_query($conn,$sq);
if($qr)
{
 	echo "<script> alert('succesfully inserted 1 row');
	   </script>";    
}
else echo"<script> alert('error');
	 </script>";
?>
