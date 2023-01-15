from pyspark.sql.types import *
from pyspark.sql import functions as F
from delta.tables import DeltaTable
from pyspark.sql import SparkSession

spark = SparkSession \
        .builder \
        .appName("kafka-delta") \
        .config("spark.jars.packages", "io.delta:delta-core_2.12:2.2.0") \
        .config('spark.sql.catalog.spark_catalog','org.apache.spark.sql.delta.catalog.DeltaCatalog') \
        .config('spark.sql.extensions', 'io.delta.sql.DeltaSparkSessionExtension') \
        .getOrCreate()

# Parameters
broker = "my-cluster-kafka-bootstrap:9092"
topic = "mysql.inventory.product"
primary_key = "column1"

schema_topic = (StructType([
        StructField('ordertime', TimestampType(), True),
        StructField('orderid', IntegerType(), True),
        StructField('itemid', StringType(), True),
        StructField('orderunits', FloatType(), True)
        ])
)

# Read Streaming from Kafka
stream_df = (spark.readStream
    .format("kafka")
    .options("kafka.bootstrap.servers", broker)
    .options("topic", topic) #topic / subscribe
    #.options("failOnDataLoss", "false") talvez não precise, só se der erro
    .options("startingOffsets", "latest")
    .options("checkpointLocation", "checkpoint") #checkpointLocation / checkpoint
    .load()
    .select(F.from_json(F.col("value").cast('string'), schema_topic).alias('data'))
    )

stream_df.show()