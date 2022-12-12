<?php
$con=mysqli_connect("localhost","mrrdejiqun_post","7nhyLj2rB78s83nM","mrrdejiqun_post");
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
 $jsl=$row['joy']*0.35;
    $zjl=$row['joy']*0.48;
    $joy=$row['joy'];
    if ($joy>=0) {
echo $row['joy'];
    } else {
echo $row['joy'];
    }
    
}
    }else{
        //没有查询出任何数据 说明用户名不存在
        echo "你还没有牛子，输入/nzget以获取";
    }




$con->close();

?>