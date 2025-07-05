from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'sentiment_comments',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='test-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("📥 Reading messages from Kafka topic 'sentiment_comments':")
for message in consumer:
    print(message.value)