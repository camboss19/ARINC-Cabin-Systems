import paho.mqtt.client as mqtt
import cbor2
    
def call():
    print("Call!")


# Define MQTT broker settings
broker = "192.168.10.10"
port = 1883
topic = "v1/command/ife/pax/call/units/a/call"

def on_message(client, userdata, message):
    # Decode the CBOR payload
    data = cbor2.loads(message.payload)
    operation = data.get("operation")
    if operation == "execute":
        action = data["params"].get("action")
        if action == "call":
            call()
            
# Initialize MQTT client and subscribe to the topic
client = mqtt.Client()
client.connect(broker, port)
client.subscribe(topic)
client.on_message = on_message
client.loop_forever()