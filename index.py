#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, re

try:
	import json
except ImportError, e:
	import simplejson as json

from bottle import route, run, default_app, debug, template, post, request

countries = {
	"eur": "Euro",
	"usd": "United States Dollar",
	"gbp": "Pound Sterling",
	"aud": "Australian Dollar",
	"brl": "Brazilian Real",
	"cad": "Canadian Dollar",
	"chf": "Swiss Franc",
	"cny": "Chinese Yuan",
	"dkk": "Danish Krone",
	"hkd": "Hong Kong Dollar",
	"inr": "Indian Rupee",
	"jpy": "Japanese Yen",
	"krw": "Korea Won",
	"lkr": "Sri Lanka Rupee",
	"myr": "Malaysian Ringgit",
	"nzd": "New Zealand Dollar",
	"sgd": "Singapore Dollar",
	"twd": "Taiwan Dollar",
	"zar": "South African Rand",
	"thb": "Thai Baht",
	"sek": "Swedish Krona",
	"nok": "Norwegian Krone",
	"mxn": "Mexican Peso",
	"bgn": "Bulgarian Lev",
	"czk": "Czech Koruna",
	"eek": "Estonian Kroon",
	"huf": "Hungarian Forint",
	"ltl": "Lithuanian Litas",
	"lvl": "Latvian Lats",
	"pln": "Polish Zloty",
	"ron": "New Romanian Leu",
	"skk": "Slovak Koruna",
	"isk": "Icelandic Krona",
	"hrk": "Croatian Kuna",
	"rub": "Russian Rouble",
	"try": "New Turkish Lira",
	"php": "Philippine Peso",
	"cop": "Colombian Peso",
	"ars": "Argentine Peso",
	"clp": "Chilean Peso",
	"svc": "Salvadoran colon",
	"tnd": "Tunisian Dinar",
	"pyg": "Paraguay Guarani",
	"mad": "Moroccan Dirham",
	"jmd": "Jamaican Dollar",
	"sar": "Saudi Arabian Riyal",
	"qar": "Qatari Riyal",
	"hnl": "Honduran Lempira",
	"syp": "Syrian Pound",
	"kwd": "Kuwaiti Dinar",
	"bhd": "Bahrain Dinar",
	"egp": "Egyptian Pound",
	"omr": "Omani Rial",
	"ngn": "Nigerian Naira",
	"pab": "Panama Balboa",
	"pen": "Peruvian Nuevo Sol",
	"ils": "Israeli Shekel",
	"uyu": "Uruguayan New Peso",
	"aed": "Arab Emirates Dirham",
}

def is_numeric(string):
	try:
		float(string)
		return True
	except ValueError:
		return False

@route('/')
def index():
	return template("index", countries=countries)
	
@route('/static/:path#.*#')
def static_file(path):
	return static_file(path, root=os.path.join(os.path.abspath(os.path.dirname(__file__)), "static"))

@post('/convert')
def convert():
	currency = request.forms.get('currency')
	from_currency = request.forms.get('from_currency')
	to_currency = request.forms.get('to_currency')
	
	report = ""
	if len(currency) < 0:
		report = "Please enter currency"
	elif is_numeric(currency) is False:
		report = "Currency is not number format"
	elif from_currency not in countries or to_currency not in countries:
		report = "From currency and To currency not correct!"
	elif from_currency == to_currency:
		report = "From currency can not same as To currency"
	else:
		url = "http://xurrency.com/api/%s/%s/%s" % (from_currency, to_currency, float(currency))
		data= json.loads(urllib.urlopen(url).read())
		
		if data['status'] == 'ok':
			report = data['result']['value']
		else:
			report = data['message']
	
	return template("convert", countries=countries, currency=currency, from_currency=from_currency, to_currency=to_currency, report=report)
	
if __name__ == "__main__":
	debug(True)
	run(host="localhost", port="8888", reloader=True)
else:
	application = default_app()