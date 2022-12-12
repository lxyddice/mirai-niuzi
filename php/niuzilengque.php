    <?php
    
    
    
    
    $num1=date("Ymdhi");   //给变量赋值，调用date函数，格式为 年-月-日 时:分:秒
    $num2=date("md");
    $num3=1145141919810;
    $num1 = ($num3+$num1)*$num2;
    $num1 = md5($num1);
    
    
    
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

    if ($row['lq']==$num1) {
        echo "你的牛子累坏了，再用就要坏掉了！";
    } else {
        
        $result = mysqli_query($con,"SELECT * FROM niuzi WHERE qq='$_GET[qq]'");

while($row = mysqli_fetch_array($result))
{

}

        
        mysqli_query($con,"UPDATE niuzi SET lq='$num1' WHERE qq='$_GET[qq]' ");
        echo "你的牛子很健康";
    }
}
}else{
        //没有查询出任何数据 说明用户名不存在
        echo "你没有获取牛子，输入/nzget以获取";
    }

?>