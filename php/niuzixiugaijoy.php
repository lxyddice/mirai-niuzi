<?php
/*
$num=rand(2500000000,7500000000);
$num=$num/1000000000;
echo $num;
*/

$con=mysqli_connect("localhost","mrrdejiqun_post","7nhyLj2rB78s83nM","mrrdejiqun_post");

mysqli_query($con,"UPDATE niuzi SET joy='$_GET[joy]' WHERE qq='$_GET[qq]' ");

mysqli_close($con);
echo "修改成功";
?>