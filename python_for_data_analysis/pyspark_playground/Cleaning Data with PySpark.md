# DataFrame details
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




