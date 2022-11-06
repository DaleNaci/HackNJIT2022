<?php
#add first 5 parameters
$args = $_POST["priority1"] . " " . $_POST["priority2"] . " " . $_POST["priority3"] . " " . $_POST["priority4"] . " " . $_POST["priority5"] = " ";
for($x = (int)$_POST["x"]; $x>0; $x-=1){
    $args = $args . $_POST["course{$x}"] . "," . $_POST["num{$x}"] . " ";
}
exec("python options.py {$args}", $output);
#output is array of string
?>