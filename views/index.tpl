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
		<form action="/convert" method="post">
		<div data-role="fieldcontain"> 
			<label for="name">Currency:</label> 
			<input type="text" name="currency" id="name" value=""  /> 
		</div>
		
		<div data-role="fieldcontain">
			<label for="from_currency" class="select">From:</label>
			<select name="from_currency" id="from_currency">			
				%for short, country in sorted(countries.items(), key=lambda x: (-1*x[1], x[0])):
					<option value="{{short}}">{{country}}</option>
				%end
			</select>
		</div>

		<div data-role="fieldcontain">
			<label for="to_currency" class="select">To:</label>
			<select name="to_currency" id="to_currency">
				%for short, country in sorted(countries.items(), key=lambda x: (-1*x[1], x[0])):
					<option value="{{short}}">{{country}}</option>
				%end
			</select>
		</div>
		
		<div class="ui-body ui-body-b">
			<fieldset class="ui-grid-a">
				<div class="ui-block-a"><button type="submit" data-theme="a">Submit</button></div>
				<div class="ui-block-b"><button type="reset" data-theme="d">Cancel</button></div>
	    	</fieldset>
		</div>
		</form>
	</div>
	
	<div data-role="footer">
		<h4>By <a href="http://studio.zeuik.com/" target="_blank">Zeuxis Lo</a></h4>
	</div>
</div>
</body>
</html>