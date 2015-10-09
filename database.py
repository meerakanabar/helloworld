import sqlite3 as lite
import pandas as pd
df = pd.read_sql(sql, cnxn)
# Trying out the new read_sql function instead of using the pandas fetchall(), is that a good idea? Or not so good?  
con = lite.connect('new.db')
CREATE TABLE cities (name text, state text);
INSERT INTO cities (name, state) VALUES
    ('New York City', 'NY'),
    ('Boston', 'MA'),
    ('Chicago', 'IL'),
    ('Miami', 'FL'),
    ('Dallas', 'TX'),
    ('Seattle', 'WA'),
    ('Portland', 'OR'),
    ('San Francisco', 'CA'),
    ('Los Angeles', 'CA');
CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer);
INSERT INTO weather (city, year, warm_month, cold_month, average_high) VALUES
	['New York City', '2013', 'July', 'January', '62']
	# are integers supposed to be put in quotes also? It worked when I ran it, but I wasn't sure about best practices.
	['Boston', '2013', 'July', 'January', '59'],
	['Chicago','2013', 'July', 'January', '59'],
	['Miami', '2013', 'August', 'January', '84'],
	['Dallas', '2013', 'July', 'January', '77'],
	['Seattle', '2013', 'July', 'January', '61'],
	['Portland', '2013', 'July', 'December', '63'],
	['San Francisco', '2013', 'September', 'December', '64'],
	['Los Angeles', '2013', 'September', 'December', '75'];
SELECT name, state, year, warm_month, cold_month, average_high
FROM cities 
INNER JOIN weather 
    ON name = city;
SELECT name FROM cities WHERE warm_month = 'July';
# no idea how to print the results of the above query correctly. Will need some help with this on Friday  
