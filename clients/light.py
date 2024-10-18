import paho.mqtt.client as mqtt
import cbor2

is_on = False

def on():
    print("Light on!")
    global is_on
    is_on = True

def off():
    print("Light off.")
    global is_on
    is_on = False
    
def toggle():
    if is_on: off()
    else: on()

# Define MQTT broker settings
broker = "192.168.10.10"
port = 1883
topic = "v1/command/ife/pax/lights/units/a1/toggle"

def on_message(client, userdata, message):
    # Decode the CBOR payload
    data = cbor2.loads(message.payload)
    operation = data.get("operation")
    if operation == "execute":
        action = data["params"].get("action")
        if action == "toggle":
            toggle()
            
# Initialize MQTT client and subscribe to the topic
client = mqtt.Client()
client.connect(broker, port)
client.subscribe(topic)
client.on_message = on_message
client.loop_forever()