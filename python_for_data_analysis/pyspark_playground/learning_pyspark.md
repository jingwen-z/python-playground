# Introduction to PySpark
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

# Cleaning Data with PySpark
## Intro to data cleaning with Apache Spark
> Q: Why perform data cleaning with Spark?<br>
> A: Problem with typical data systems:
>   * Performance
>   * Organizing data flow

> Q: Advantages of Spark?<br>
> A: Scalable, powerful framework for data handling
>   * Spark offers high performance.
>   * Spark allows orderly data flows.
>   * Spark can use strictly defined schemas while ingesting data.

## Spark schemas
- Define the format of a dataframe
- May contain various data types: strings, dates, integers, arrays
- Can filter the garbage data during import
- Improves read performance

<p align="center">
  <img alt="spark-schema"
  src="{{ site.baseurl }}/img/spark-schema.png"/>
</p>

### Defining a schema
Creating a defined schema helps with data quality and import performance.
```python
# Import the pyspark.sql.types library
import pyspark.sql.types

# Define a new schema using the StructType method
people_schema = StructType([
  # Define a StructField for each field
  StructField('name', StringType(), nullable=False),
  StructField('age', IntegerType(), nullable=False),
  StructField('city', StringType(), nullable=False)
])
```

## Immutability and lazy processing
### Lazy processing
Lazy processing operations will usually return in about the same amount of time
regardless of the actual quantity of data. Remember that this is due to Spark
not performing any transformations until an action is requested. 

```python
# Load the CSV file
aa_dfw_df = spark.read.format('csv').options(Header=True).load('AA_DFW_2018.csv.gz')

# Add the airport column using the F.lower() method
aa_dfw_df = aa_dfw_df.withColumn('airport', F.lower(aa_dfw_df['Destination Airport']))

# Drop the Destination Airport column
aa_dfw_df = aa_dfw_df.drop(aa_dfw_df['Destination Airport'])

# Show the DataFrame
aa_dfw_df.show()
```

## Understanding Parquet
### The parquet format
<p align="center">
  <img alt="parquet-format"
  src="{{ site.baseurl }}/img/parquet-format.png"/>
</p>

### Working with parquet
<p align="center">
  <img alt="read-write-parquet"
  src="{{ site.baseurl }}/img/read-write-parquet.png"/>
</p>

### Parquet and SQL
The `Parquet` format is a columnar data store, allowing Spark to use predicate
pushdown. This means Spark will only process the data necessary to complete the
operations you define versus reading the entire dataset. This gives Spark more
flexibility in accessing the data and often drastically improves performance on
large datasets. 
<p align="center">
  <img alt="parquet-and-sql"
  src="{{ site.baseurl }}/img/parquet-and-sql.png"/>
</p>




