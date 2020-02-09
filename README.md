# data-streaming-crime-statistics

Project part of the Udacity Data Streaming nanodegree

### Setup zookeeper
`/usr/bin/zookeeper-server-start config/zookeeper.properties`

### Setup server
`/usr/bin/kafka-server-start config/server.properties`

### Run the server
`python kafka_server.py`

### Check produced data with kafka console consumer
`kafka-console-consumer --topic "calls" --from-beginning --bootstrap-server localhost:9092`

### Run spark script
`spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py`

## Questions

**1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?**
The selection of the parameters has a direct impact on the number of rows that the system can process. i.e., `processedRowsPerSecond`.

**2. What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?** 
Two parameters that can improve the performance and increase the `processedRowsPerSecond` have to do with the shuffle operation: 
- `spark.default.parallelism` (Default number of partitions in RDDs returned by transformations)
- `spark.sql.shuffle.partitions` (Configures the number of partitions to use when shuffling data for joins or aggregations)

By reducing the number of partitions (e.g., to 100) the performance increased. As mentioned in [a blog post](http://blog.madhukaraphatak.com/dynamic-spark-shuffle-partitions/), there is no one size fits all, and it could also be dinamically assignated. 

## Screen shots
Available in **/screen shots** folder
