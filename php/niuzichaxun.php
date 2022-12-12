<?php
$con=mysqli_connect("localhost","mrrdejiqun_post","","mrrdejiqun_post");
// 检测连接
if (mysqli_connect_errno())
{
    echo "连接失败: " . mysqli_connect_error();
}


$result = mysqli_query($con,"SELECT * FROM niuzi WHERE qq='$_GET[qq]'");


$num = mysqli_num_rows($result);
 //获取行数
if ($num == '1'){

$result = mysqli_query($con,"SELECT * FROM niuzi WHERE qq='$_GET[qq]'");

while($row = mysqli_fetch_array($result))
{
    echo "\n";
    echo "主人名字：".$row['name'];
    echo "\n";
    echo "牛子长度：".$row['niuzi']."cm";
}
    }else{
        //没有查询出任何数据 说明用户名不存在
        echo "你还没有牛子，输入/nzget以获取";
    }




$con->close();

?>