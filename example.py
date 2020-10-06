from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.read.option("header", "true").csv("/user/abelousova/age_gender.csv")
df.groupBy("gender").count().repartition(1).write.mode("overwrite").option("header", "true").csv("/user/abelousova/gender")

