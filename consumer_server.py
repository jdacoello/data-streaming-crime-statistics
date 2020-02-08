from kafka import KafkaConsumer
import json

print("Simple consumer to check that data is produced:")

consumer = KafkaConsumer(
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    consumer_timeout_ms=1000)

consumer.subscribe(['calls'])

# read messages continously
for message in consumer:
    print(message.value)