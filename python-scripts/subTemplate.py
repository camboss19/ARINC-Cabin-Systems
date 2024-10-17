import RPi.GPIO as GPIO
import paho.mqtt.client as mqttclient
import gpioControl

# IP and port of broker
broker_address="192.168.10.10"
port=1883




# When self connects to broker
def on_connect(client,userdata,flags,rc):
	if rc==0:
		print("client is connected")
		
	else:
		print("client is not connected")

# When self recieves a message	
def on_message(client,userdata,message):
	print("Message received: " + str(message.payload.decode("utf-8")))
	print("Topic: "+str(message.topic))
	
	message_rec=str(message.payload.decode("utf-8"))
	
	## Code here to do things based on message data
	if(str(message.topic) == topic1):
		gpioControl.main()
 

## Password controls when needed
#user=" " #Connection username when needed
#password=" " #connection password when needed
#client.username_pw_set(user,password=password) #set username and pass when needed

# New instance
client=mqttclient.Client() #

# Attach call back functions
client.on_message=on_message
client.on_connect=on_connect
client.connect(broker_address,port=port)

# Topic definition
topic1="test" #topic

# Subscribe to the topic
client.subscribe(topic1)

# MAIN LOOP
client.loop_start()
while True:
	pass











