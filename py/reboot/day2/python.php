<html>
		<head>
			<meta charset="utf-8">
			<title>API测试</title>
		</head>
		<style>
			*{
					margin:0;
					padding: 0;

			}
			.main{
				width:250px;
				height: 80px;
				margin: 0 auto;
				margin-top: 200px;
			}
			.main input {
					width: 250px;
					padding:5px;
					margin:5px 0;


			}
			.main .text{
					height: 30px;
					line-height: 30px;

			}

		</style>
		<body>
		<div class="main">
					<form action="api.php" method="post">
						
							<input type="ip" name="ip" calss="text" placeholder="请输入查询的IP地址">
							<input type="submit" name="submit"  value="提交">
					</form>

		</div>
		</body>

</html>

