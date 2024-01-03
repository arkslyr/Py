<?php
$conn=mysqli_connect("localhost","root","","student");
$result = mysqli_query($conn, "SELECT * FROM book" );
    if(mysqli_num_rows($result))
    {
        while ($row = mysqli_fetch_assoc($result)) {

            echo "Book id: <input type='text' value=".$row['bookid']." disabled>
                  Book Name: <input type='text' value=".$row['bookname']." disabled> 
                  Author Name: <input type='text' value=".$row['author']." disabled>
                  Number of Copies:<input type='text' value=".$row['noofcopies']." disabled> <br>";
            
            }
        } 
    else 
    {
            echo "<script>alert('No Registeration');</script>";
    }
?>