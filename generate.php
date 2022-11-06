<?php
#add first 5 parameters
$args = $_POST["priority1"] . " " . $_POST["priority2"] . " " . $_POST["priority3"] . " " . $_POST["priority4"] . " " . $_POST["priority5"] . " ";
for($x = (int)$_POST["x"]; $x>0; $x-=1){
    $args = $args . $_POST["course{$x}"] . "," . $_POST["num{$x}"] . " ";
}

$out = shell_exec("/afs/cad/linux/anaconda3.8/anaconda/bin/python data/options.py {$args}");
var_export($out);
/*foreach ($out as $line){
    echo $line;
}*/
?>