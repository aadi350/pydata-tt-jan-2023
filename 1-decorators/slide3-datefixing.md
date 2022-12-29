## Applications
### Data Validation


Let's say we have a table:
+----------+------------+--------+-------------+
|  american|   monthname|  julian|inversejulian|
+----------+------------+--------+-------------+
|06/07/2022|06/July/2022|1997/310|     310/1997|
+----------+------------+--------+-------------+

we also have a function that expects dates in specific format:
```python
def preprocess_data(df):
	'''function expects ISO format'''
	return df_processed
```

How do we ensure that the dates are formatted correctly?

-------------------------------------------------------------------------------

### Option 1: Write a function
```python
def fix_dates(df, date_cols:dict):
	
	return df_fixed
```
Issues:
	- we have to remember to call this function
	- if we do use a template, we break any existing code

-------------------------------------------------------------------------------

### Option 2: Decorate the Function
```python
def fn(df, *args, *kwargs):
	return df

def datefixer(dateconf):
	def _datefixer(func):
		def wrapper(df, *args, **kwargs):
			df_dateconf = {}

			for key, values in dateconf.items():
				df_dateconf[key] = [i for i in df.columns if i in value]

			for dateformat in df_dateconf.keys():
				for datecolumn in df_dateconf[dateformat]:
					if dateformat == 'american':
						df = df.withColumn(datecolumn, F.to_date(datecolumn, 'dd/MM/yyyy'))
					if dateformat == 'julian':
						df = df.withColumn(datecolumn, F.to_date(datecolumn, 'yyyy/DDD'))
				return func(df, *args, **kwargs)

		return wrapper
	return _datefixer

# usage
dateconf = {
	'american': ['col1', 'col2'],
	'julian': ['juliancolumn'] # specify column names
}

decorated_fn = datefixer(dateconf)(fn) # same issue!! we break the function name

```
------------------------------------------------------------------

### Python's 🐍 Syntactic Sugar

```python
# following are equivalent!
decorated_fn = datefixer(dateconf)(fn) 

@datefixer(dateconf)
def fn(df, *args, **kwargs):
	return df

# we can call the function without thinking about decoration
fn(df)

```
