<?php
$con=mysqli_connect("localhost","","","");
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
    $djxh=$row['joy']*0.63;
    $ban=$row['ban'];
    echo "\n";
    echo "愉悦值：".$row['joy'];
    echo "\n";
    if ($joy>=0) {
    echo "当前效果：pk失败缩短量-".$jsl."%，贴贴与签到增加量+".$zjl."%，打∠消耗量+".$djxh."%";
    if ($ban==1) {
        echo "\n由于牛子长度小于0，您已被封禁，请期待后续更新，感谢支持！";
    }
    } else {
    echo "当前效果：pk失败缩短量+".-$jsl."%，贴贴与签到增加量".$zjl."%，打∠消耗量-".-$djxh."%";
    if ($ban==1) {
        echo "\n由于牛子长度小于0，您已被封禁，请期待后续更新，感谢支持！";
    }
    }
    
}
    }else{
        //没有查询出任何数据 说明用户名不存在
        echo "你还没有牛子，输入/nzget以获取";
    }




$con->close();

?>