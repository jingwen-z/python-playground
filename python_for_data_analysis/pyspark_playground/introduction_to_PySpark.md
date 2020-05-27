# Getting to know PySpark
## Using Spark in Python
Creating the connection is as simple as creating an instance of the
`SparkContext` class. The class constructor takes a few optional arguments that
allow you to specify the attributes of the cluster you're connecting to.

An object holding all these attributes can be created with the `SparkConf()`
(for configuring Spark) constructor.

> Q: How do you connect to a Spark cluster from PySpark?<br>
> A: Create an instance of the `SparkContext` class.

## Using DataFrames
To start working with Spark DataFrames, you first have to create a `SparkSession`
object from your `SparkContext`. You can think of the `SparkContext` as your
connection to the cluster and the `SparkSession` as your interface with that
connection.

> Q: Which of the following is an advantage of Spark DataFrames over RDDs?<br>
> A: Operations using DataFrames are automatically optimized.

- `SparkSession.builder.getOrCreate()`
This returns an existing SparkSession if there's already one in the environment,
or creates a new one if necessary.

```python
# Import SparkSession from pyspark.sql
from pyspark.sql import SparkSession

# Create my_spark
my_spark = SparkSession.builder.getOrCreate()

# Print my_spark
print(my_spark)
```

## Viewing tables
Your `SparkSession` has an attribute called `catalog` which lists all the data
inside the cluster. This attribute has a few methods for extracting different
pieces of information.

One of the most useful is the `.listTables()` method, which returns the names
of all the tables in your cluster as a list.

```python
spark.catalog.listTables()
```

## SQL query
Running a query on this table is as easy as using the `.sql()` method on your
`SparkSession`. This method takes a string containing the query and returns a
DataFrame with the results!
```python
query = "FROM flights SELECT * LIMIT 10"
# Get the first 10 rows of flights
flights10 = spark.sql(query)

# Show the results
flights10.show()

# +----+-----+---+--------+---------+--------+---------+-------+-------+------+------+----+--------+--------+----+------+
# |year|month|day|dep_time|dep_delay|arr_time|arr_delay|carrier|tailnum|flight|origin|dest|air_time|distance|hour|minute|
# +----+-----+---+--------+---------+--------+---------+-------+-------+------+------+----+--------+--------+----+------+
# |2014|   12|  8|     658|       -7|     935|       -5|     VX| N846VA|  1780|   SEA| LAX|     132|     954|   6|    58|
# |2014|    1| 22|    1040|        5|    1505|        5|     AS| N559AS|   851|   SEA| HNL|     360|    2677|  10|    40|
# |2014|    3|  9|    1443|       -2|    1652|        2|     VX| N847VA|   755|   SEA| SFO|     111|     679|  14|    43|
# |2014|    4|  9|    1705|       45|    1839|       34|     WN| N360SW|   344|   PDX| SJC|      83|     569|  17|     5|
# |2014|    3|  9|     754|       -1|    1015|        1|     AS| N612AS|   522|   SEA| BUR|     127|     937|   7|    54|
# |2014|    1| 15|    1037|        7|    1352|        2|     WN| N646SW|    48|   PDX| DEN|     121|     991|  10|    37|
# |2014|    7|  2|     847|       42|    1041|       51|     WN| N422WN|  1520|   PDX| OAK|      90|     543|   8|    47|
# |2014|    5| 12|    1655|       -5|    1842|      -18|     VX| N361VA|   755|   SEA| SFO|      98|     679|  16|    55|
# |2014|    4| 19|    1236|       -4|    1508|       -7|     AS| N309AS|   490|   SEA| SAN|     135|    1050|  12|    36|
# |2014|   11| 19|    1812|       -3|    2352|       -4|     AS| N564AS|    26|   SEA| ORD|     198|    1721|  18|    12|
# +----+-----+---+--------+---------+--------+---------+-------+-------+------+------+----+--------+--------+----+------+
```

## Pandafy a Spark DataFrame
`.toPandas()`: calling this method on a Spark DataFrame returns the
corresponding `pandas` DataFrame. 

```python
flights10.toPandas()
```

## Put a pandas DataFrame into a Spark cluster
The `.createDataFrame()` method takes a `pandas` DataFrame and returns a Spark
DataFrame.
The output of this method is stored locally, NOT in the `SparkSession` catalog.
-> you can use all the Spark DataFrame methods on it, but you can't access the
data in other contexts.

```python
# Create pd_temp
pd_temp = pd.DataFrame(np.random.random(10))
# Create spark_temp from pd_temp
# There's already a SparkSession called "spark"
spark_temp = spark.createDataFrame(pd_temp)
```

`.createTempView()` Spark DataFrame method: registering the DataFrame as a table
in the catalog, but since this table is temporary, it can only be accessed from
the specific `SparkSession` used to create the Spark DataFrame.

`.createOrReplaceTempView()`: creating a new temporary table if nothing was
there before, or updates an existing table if one was already defined.

```python
# Add spark_temp to the catalog
spark_temp.createOrReplaceTempView('temp')
```

## Read a text file straight into Spark
`SparkSession` has a `.read` attribute which has several methods for reading
different data sources into Spark DataFrames. Using these you can create a
DataFrame from a .csv file just like with regular `pandas` DataFrames!

```python
file_path = "/usr/local/share/datasets/airports.csv"
# Read in the airports data
airports = spark.read.csv(file_path, header=True)```
```

# Manipulating data
## Creating columns
The Spark DataFrame is **immutable** => the columns can't be updated in place.

Using the `.withColumn()` method, which takes two arguments. First, a string
with the name of your new column, and second the new column itself.

**`withColumn(colName, col)`**
> Returns a new DataFrame by adding a column or replacing the existing column
that has the same name.<br>
> The column expression must be an expression over this DataFrame; attempting
to add a column from some other DataFrame will raise an error.
>
> Parameters:
>   * `colName` – string, name of the new column.
>   * `col` – a Column expression for the new column.

To overwrite the original DataFrame you must reassign the returned DataFrame
using the method like so:
```python
df = df.withColumn("newCol", df.oldCol + 1)
```

## Filtering Data
The `.filter()` method takes either an expression that would follow the `WHERE`
clause of a SQL expression as a string, or a Spark Column of boolean
(True/False) values.

```python
flights.filter("air_time > 120").show()
flights.filter(flights.air_time > 120).show()
```

## Selecting
### `.select()`
**`select(*cols)`**
> Projects a set of expressions and returns a new DataFrame.
>
> Parameters:<br>
>   * `cols` – list of column names (string) or expressions (Column). If one of
the column names is ‘*’, that column is expanded to include all columns in the
current DataFrame.
>
> Examples:<br>
> - `df.select('*').collect()`
> - `df.select('name', 'age').collect()`
> - `df.select(df.name, (df.age + 10).alias('age')).collect()`

`.select()` method: This method takes multiple arguments - one for each column
you want to select.

The difference between `.select()` and `.withColumn()`:
- `.select()` returns only the columns you specify
- `.withColumn()` returns all the columns of the DataFrame in addition to the
one you defined

```python
# Select the first set of columns
selected1 = flights.select('tailnum', 'origin', 'dest')

# Select the second set of columns
temp = flights.select(flights.origin, flights.dest, flights.carrier)
```

### `.alias()` = `AS` or `.selectExpr()`
```python
flights.select((flights.air_time/60).alias("duration_hrs"))
flights.selectExpr("air_time/60 as duration_hrs")
```

## Aggregating
```python
df.groupBy().min("col").show()
```

```python
# Average duration of Delta flights
flights.filter(flights.origin == 'SEA').filter(flights.carrier == 'DL').groupBy().avg('air_time').show()

# Total hours in the air
flights.withColumn("duration_hrs", flights.air_time/60).groupBy().sum('duration_hrs').show()
```

## Grouping and Aggregating
> ` count()`<br>
> Counts the number of records for each group.

```python
# Group by tailnum
by_plane = flights.groupBy("tailnum")

# Number of flights each plane made
by_plane.count().show()

# Group by origin
by_origin = flights.groupBy("origin")

# Average duration of flights from PDX and SEA
by_origin.avg("air_time").show()
```

`.agg()`: let you pass an aggregate column expression that uses any of the
aggregate functions from the `pyspark.sql.functions` submodule.

```python
# Import pyspark.sql.functions as F
import pyspark.sql.functions as F

# Group by month and dest
by_month_dest = flights.groupBy('month', 'dest')

# Average departure delay by month and destination
by_month_dest.avg('dep_delay').show()

# Standard deviation of departure delay
by_month_dest.agg(F.stddev('dep_delay')).show()
```

## Joining
`.join()`: This method takes three arguments.
- The first is the second DataFrame that you want to join with the first one.
- The second argument, `on`, is the name of the key column(s) as a string. The
names of the key column(s) must be the same in each table.
- The third argument, `how`, specifies the kind of join to perform.

**`join(other, on=None, how=None)`**
> Joins with another DataFrame, using the given join expression.
>
> Parameters:<br>
>   * `other` – Right side of the join
>   * `on` – a string for the join column name, a list of column names, a join
expression (Column), or a list of Columns. If on is a string or a list of
strings indicating the name of the join column(s), the column(s) must exist on
both sides, and this performs an equi-join.
>   * `how` – str, default `inner`. Must be one of: `inner`, `cross`, `outer`,
`full`, `full_outer`, `left`, `left_outer`, `right`, `right_outer`, `left_semi`,
and `left_anti`.

```python
# Rename the faa column
airports = airports.withColumnRenamed('faa', 'dest')

# Join the DataFrames
flights_with_airports = flights.join(airports, on='dest', how='leftouter')
```

# Getting started with machine learning pipelines
At the core of the `pyspark.ml` module are the `Transformer` and `Estimator`
classes. Almost every other class in the module behaves similarly to these two
basic classes.

`Transformer` classes have a `.transform()` method that takes a DataFrame and
returns a new DataFrame; usually the original one with a new column appended.
For example, you might use the class `Bucketizer` to create discrete bins from
a continuous feature or the class `PCA` to reduce the dimensionality of your
dataset using principal component analysis.

`Estimator` classes all implement a `.fit()` method. These methods also take a
DataFrame, but instead of returning another DataFrame they return a model
object. This can be something like a `StringIndexerModel` for including
categorical data saved as strings in your models, or a `RandomForestModel` that
uses the random forest algorithm for classification or regression.

## Data types
The only argument you need to pass to `.cast()` is the kind of value you want to
create, in string form.

### String to integer
To convert the type of a column using the `.cast()` method, you can write code
like this:<br>
`dataframe = dataframe.withColumn("col", dataframe.col.cast("new_type"))`

```python
model_data = model_data.withColumn("arr_delay", model_data.arr_delay.cast('integer'))
```
