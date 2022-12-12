
    
    <?php
    
    $num1=date("Ymd");   //给变量赋值，调用date函数，格式为 年-月-日 时:分:秒
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

    if ($row['qd']==$num1) {
        echo "你今天已经吃过强壮药丸了，可惜一天只能吃一颗";
    } else {
        
        $result = mysqli_query($con,"SELECT * FROM niuzi WHERE qq='$_GET[qq]'");

while($row = mysqli_fetch_array($result))
{
     $niuzi = $row['niuzi'];
     $joy=$row['joy'];
     $zjl=$joy*0.0048;
     $zjl=3*(1+$zjl);
}
        $niuzi = $niuzi + $zjl;
$name = $_GET["name"];
$name = htmlspecialchars($name);
        mysqli_query($con,"UPDATE niuzi SET niuzi='$niuzi' WHERE qq='$_GET[qq]' ");
        mysqli_query($con,"UPDATE niuzi SET qd='$num1' WHERE qq='$_GET[qq]' ");
        mysqli_query($con,"UPDATE niuzi SET name='$name' WHERE qq='$_GET[qq]' ");
        mysqli_query($con,"UPDATE niuzi SET exp='$exp' WHERE qq='$_GET[qq]' ");
        echo "你使用了强壮药丸，牛子长度+".$zjl."cm";
    }
}
}else{
        //没有查询出任何数据 说明用户名不存在
        echo "你没有获取牛子，输入/nzget以获取";
    }




$con->close();

?>