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
echo "这个人有牛子";
    }else{
        //没有查询出任何数据 说明用户名不存在
        echo "这个人没有牛子";
    }

$con->close();
?>