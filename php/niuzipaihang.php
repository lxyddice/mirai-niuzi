<?php
$con=mysqli_connect("localhost","mrrdejiqun_post","7nhyLj2rB78s83nM","mrrdejiqun_post");
// 检测连接
if (mysqli_connect_errno())
{
    echo "连接失败: " . mysqli_connect_error();
}

$result = mysqli_query($con,"SELECT * FROM niuzi ORDER BY niuzi DESC");

while($row = mysqli_fetch_array($result))
{
    echo "QQ：".$row['qq'];
    echo "长度：" . $row['niuzi'];
    echo "<br>";
}

mysqli_close($con);
?>