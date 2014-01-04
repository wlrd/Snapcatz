<html>
<head>
<title> Snapcatz </title>
<style type="text/css">
body{
	font-family: 'Tahoma'
}
</style>
</head>
<body>
<?php exec("python cat.py" . " > /dev/null &") ?>
<div style="margin:20px auto; text-align:center; width:400px; height: 260px; border:2px solid; border-radius:20px; background-color: lightgray">
<h1> Snapcatz!</h1>
<p><form name="input" action="runCat.php" method="post">
Your Username: 
<input type="text" name="username" style="border: 2px solid rgb(139, 188, 190); border-radius:5px"></p>
<p>
Password:
<input type="password" name="password" style="border: 2px solid rgb(139, 188, 190); border-radius:5px"></p>
<p>
Recipient Username:
<input type="text" name="friend" style="border: 2px solid rgb(139, 188, 190); border-radius:5px"></p>
<p>
<input type="submit" value="Submit"></p>
</body>
</form>
</div>
<html>