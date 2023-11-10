from delta import *
import pyspark
from delta.tables import *
from pyspark.sql.functions import *

builder = pyspark.sql.SparkSession.builder.appName("MyApp") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = configure_spark_with_delta_pip(builder).getOrCreate()

# data = spark.range(0, 5)
# data.write.format("delta").save("/tmp/delta-table")

df = spark.read.format("delta").load("/tmp/delta-table")
df.show()

data = spark.range(5, 10)
data.write.format("delta").mode("overwrite").save("/tmp/delta-table")

df = spark.read.format("delta").load("/tmp/delta-table")
df.show()

deltaTable = DeltaTable.forPath(spark, "/tmp/delta-table")
# Update every even value by adding 100 to it
deltaTable.update(
    condition=expr("id % 2 == 0"),
    set={"id": expr("id + 100")}
)

# # Delete every even value
# deltaTable.delete(condition = expr("id % 2 == 0"))
#
# # Upsert (merge) new data
# newData = spark.range(0, 20)

# deltaTable.alias("oldData") \
#   .merge(
#     newData.alias("newData"),
#     "oldData.id = newData.id") \
#   .whenMatchedUpdate(set = { "id": col("newData.id") }) \
#   .whenNotMatchedInsert(values = { "id": col("newData.id") }) \
#   .execute()

deltaTable.toDF().show()

# Read older versions of data using time travel
# df = spark.read.format("delta") \
#   .option("versionAsOf", 0) \
#   .load("/tmp/delta-table")
#
# df.show()


# Write a stream of data to a table
# streamingDf = spark.readStream.format("rate").load()
#
# stream = streamingDf \
#   .selectExpr("value as id") \
#   .writeStream.format("delta") \
#   .option("checkpointLocation", "/tmp/checkpoint") \
#   .start("/tmp/delta-table")

# Read a stream of changes from a table
# stream2 = spark.readStream.format("delta") \
#   .load("/tmp/delta-table") \
#   .writeStream.format("console") \
#   .start()
