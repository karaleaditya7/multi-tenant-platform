from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

event = {
    "event": "WebsiteCreated",
    "user": "user1"
}

producer.send("deployments", event)
producer.flush()

print("Event sent to Kafka")