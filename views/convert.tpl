<!DOCTYPE html> 
<html> 
<head> 
	<meta charset="utf-8" /> 
	<title>Exchange Rate Converter</title> 
	<link rel="stylesheet"  href="http://code.jquery.com/mobile/1.0a3/jquery.mobile-1.0a3.min.css" /> 
	<script type="text/javascript" src="http://code.jquery.com/jquery-1.5.min.js"></script> 
	<script type="text/javascript" src="http://code.jquery.com/mobile/1.0a3/jquery.mobile-1.0a3.min.js"></script>
</head> 
<body> 
<div data-role="page" data-theme="a">
	<div data-role="header"> 
		<h1>Exchange Rate Converter</h1>
	</div>

	<div data-role="content">
		<div data-role="fieldcontain">
			<div data-role="collapsible" data-theme="b">
				<h3>Report to {{countries[to_currency]}}:</h3>
				<p>{{report}}</p>
			</div>
		</div>
		
		<div data-role="fieldcontain"> 
			<div data-role="collapsible" data-theme="c">
				<h3>Currency from {{countries[from_currency]}}:</h3>
				<p>{{currency}}</p>
			</div>
		</div>
		
		<div data-role="fieldcontain">
			<div data-role="collapsible" data-collapsed="true">
				<h3>From Currency:</h3>
				<p>{{countries[from_currency]}}</p>
			</div>
		</div>

		<div data-role="fieldcontain">
			<div data-role="collapsible" data-collapsed="true">
				<h3>To Currency:</h3>
				<p>{{countries[to_currency]}}</p>
			</div>
		</div>
	</div>
	
	<div data-role="footer">
		<h4>By <a href="http://studio.zeuik.com/" target="_blank">Zeuxis Lo</a></h4>
	</div>
</div>
</body>
</html>