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

