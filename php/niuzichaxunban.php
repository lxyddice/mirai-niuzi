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
 
    echo $row['ban'];


}
    }else{
        if ($num=='2'){
            echo "2";
        }
        //没有查询出任何数据 说明用户名不存在
        echo "0";
    }

$con->close();

?>