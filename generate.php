<?php
$args = "";
for($x = (int)$_POST["x"]; $x>0; $x-=1){
    $args = $args . $_POST["course{$x}"] . "," . $_POST["num{$x}"] . " ";
}
exec("python options.py {$args}", $output);
?>