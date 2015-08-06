<?php
                header("Content-type:text/html;charset=utf-8");
                $ip=trim($_POST['ip']);
                $a = exec("python getip_info.py $ip",$out,$status);
		        foreach($out as $k => $v){


			        echo $v."<br>";

		        }

 ?>
