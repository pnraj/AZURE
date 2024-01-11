from azure.eventhub import EventHubProducerClient, EventData
import random
import time

def send_data_to_event_hub(connection_str, event_hub_name):
    # Create an EventHubProducerClient
    producer = EventHubProducerClient.from_connection_string(connection_str, event_hub_name=event_hub_name)

    try:
        # Create a batch to send multiple events
        event_data_batch = producer.create_batch()

        # Generate and add sample data to the batch
        for _ in range(5):
            sensor_data = {
                "sensor_id": random.randint(1, 100),
                "temperature": round(random.uniform(20.0, 30.0), 2),
                "humidity": round(random.uniform(40.0, 60.0), 2)
            }

            event_data_batch.add(EventData(str(sensor_data)))

        # Send the batch to the Event Hub
        producer.send_batch(event_data_batch)

        print("Data sent successfully.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the producer
        producer.close()

def main():
    # Replace with your Azure Event Hubs connection string and Event Hub name
    event_hub_connection_str = "YOUR_EVENT_HUB_CONNECTION_STRING"
    event_hub_name = "YOUR_EVENT_HUB_NAME"

    # Send sample data to Azure Event Hub
    send_data_to_event_hub(event_hub_connection_str, event_hub_name)

if __name__ == "__main__":
    main()
