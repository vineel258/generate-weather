# generate-weather
This toy weather simulation reports data from a reasonable number of positions; 10±. The weather simulation can be used for games and is not meteorogically accurate, it just emits weather data that looks reasonible

Language : Python 2.7 


* External libraries used in the solution : 
	* Pytest : for unit tests

* Data source reference :
	* https://www.wunderground.com/ 

* Project Structure
	* data_parser  : has classes that parse the json data for both weather and location 
	* ref_data  : has the json reference for all the test data, contains data for 12 cities
	* tests  : unit tests
	* utils  : has the class that generates random date within requested date range

Instructions to run :

	 i) Run tests
		pip install -r requirements.txt
		py.test 'tests'
	ii) Run program 
		python generate_weather.py
		        or
		python generate_weather.py |no_of_cities|
		
		* Note : Default No. Of Cities are 3

* Output format :
  City Name|City Location|Date Time|Conditions|Temperature|Pressure|Humidity

* Sample Output :
~~~
SYDNEY | -33.8688197, 151.2092955, 25 | 2015-11-17 09:16 AM |  | 20 | 1017 | 53
BRISBANE | -27.4697707, 153.0251235, 27 | 2016-10-14 04:15 AM |  | 17 | 1021 | 55
CANBERRA | -35.3075, 149.124417, 597 | 2015-11-18 02:03 PM |  | 20 | 1014 | 45
GOLDCOAST | -28.016667, 153.4, 1 | 2016-04-05 03:28 PM | Rain | 23 | 1018 | 64
ADELAIDE | -34.9284989, 138.6007456, 45 | 2016-09-17 12:26 AM | Rain | 14 | 1014 | 60
CAIRNS | -16.9185514, 145.7780548, 7.45 | 2016-05-16 12:38 PM | Rain | 26 | 1014 | 73
MELBOURNE | -37.813611, 144.963056, 10 | 2015-12-23 06:43 PM |  | 20 | 1016 | 57
PERTH | -31.9505269, 115.8604572, 16 | 2016-02-15 02:01 PM |  | 26 | 1018 | 31
HOBART | -42.8821377, 147.3271949, 8 | 2016-06-08 11:00 PM |  | 16 | 995 | 67
DARWIN | -12.4634403, 130.8456418, 31 | 2016-10-13 12:16 PM |  | 28 | 1010 | 71

