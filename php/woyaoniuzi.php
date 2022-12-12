<?php



$con=mysqli_connect("localhost","mrrdejiqun_post","7nhyLj2rB78s83nM","mrrdejiqun_post");
// 检测连接
if ($conn->connect_error) {
    die("连接失败: " . $conn->connect_error);
} 
 


$result = mysqli_query($con,"SELECT * FROM niuzi WHERE qq='$_GET[qq]'");


$num = mysqli_num_rows($result);
 //获取行数
if ($num == '1'){


echo "你已经有牛子了，不能再获取";
$con->close();
    }else{
    
$conn=mysqli_connect("localhost","mrrdejiqun_post","7nhyLj2rB78s83nM","mrrdejiqun_post");
        //没有查询出任何数据 说明用户名不存在
$name = $_GET["name"];
$name = htmlspecialchars($name);
$sql = "INSERT INTO niuzi (qq, niuzi, name) VALUES ('$_GET[qq]', '12', '{$name}')";

if ($conn->query($sql) === TRUE) {

    echo "你获得了一根牛子！它的长度是12cm";

} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
    }}

?>