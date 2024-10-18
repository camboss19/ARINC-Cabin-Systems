import paho.mqtt.client as mqtt
import cbor2

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # To handle images for the icons

# Define MQTT broker settings
broker = "192.168.10.10"
port = 1883


# Function to simulate turning on the reading light
def toggle_reading_light():
    topic = "v1/command/ife/pax/lights/units/a1/toggle"
    # Create a CBOR-encoded EXECUTE message
    message = {
        "operation": "execute",
        "params": {
            "action": "toggle"
        }
    }

    cbor_message = cbor2.dumps(message)

    # Initialize MQTT client and publish message
    client = mqtt.Client()
    client.connect(broker, port)
    client.publish(topic, payload=cbor_message, qos=1)
    client.disconnect()


# Function to simulate adjusting the window shade (stubbed out)
def toggle_window_shade():
    topic = "v1/command/ife/pax/windows/units/a1/toggle"
    # Create a CBOR-encoded EXECUTE message
    message = {
        "operation": "execute",
        "params": {
            "action": "toggle"
        }
    }

    cbor_message = cbor2.dumps(message)

    # Initialize MQTT client and publish message
    client = mqtt.Client()
    client.connect(broker, port)
    client.publish(topic, payload=cbor_message, qos=1)
    client.disconnect()

# Function to simulate calling the flight attendant (stubbed out)
def call_flight_attendant():
    topic = "v1/command/ife/pax/call/units/a/call"
    # Create a CBOR-encoded EXECUTE message
    message = {
        "operation": "execute",
        "params": {
            "action": "call"
        }
    }

    cbor_message = cbor2.dumps(message)

    # Initialize MQTT client and publish message
    client = mqtt.Client()
    client.connect(broker, port)
    client.publish(topic, payload=cbor_message, qos=1)
    client.disconnect()

# Function to create rounded rectangle (for rounded corners)
def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)

# Setup the UI
def setup_ui():
    window = tk.Tk()
    window.title("IFE System")

    # Make the window fullscreen
    window.update()
    window.attributes('-fullscreen', True)

    # Get screen dimensions
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Button height is 1/3 of the screen height, to make the buttons square, width will match the height
    button_size = screen_height // 3

    # Load the background image
    bg_image = Image.open("img/path_to_your_airliner_background_image.png")  # Replace with your image path
    bg_image = bg_image.resize((screen_width, screen_height), Image.ANTIALIAS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Set the background label
    bg_label = tk.Label(window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Load icons (replace with actual paths to your icon images)
    light_icon = Image.open("img/light.webp")
    light_icon = light_icon.resize((button_size - 20, button_size - 20), Image.ANTIALIAS)
    light_photo = ImageTk.PhotoImage(light_icon)

    shade_icon = Image.open("img/window.webp")
    shade_icon = shade_icon.resize((button_size - 20, button_size - 20), Image.ANTIALIAS)
    shade_photo = ImageTk.PhotoImage(shade_icon)

    attendant_icon = Image.open("img/call.webp")
    attendant_icon = attendant_icon.resize((button_size - 20, button_size - 20), Image.ANTIALIAS)
    attendant_photo = ImageTk.PhotoImage(attendant_icon)

    # Canvas to allow rounded corners for buttons
    canvas = tk.Canvas(window, highlightthickness=0, bd=0)
    canvas.place(x=screen_width - button_size, y=0, width=button_size, height=screen_height)

    # Create buttons with rounded corners, light blue background, and thin black outline
    def create_button(y_pos, icon, command):
        # Rounded rectangle for button background with a thin black outline
        create_rounded_rectangle(canvas, 0, y_pos, button_size, y_pos + button_size, radius=30, fill="#ADD8E6", outline="#000000", width=2)
        # Button with icon filling the entire button
        btn = tk.Button(canvas, image=icon, command=command, bg="#ADD8E6", bd=0)
        btn.place(x=10, y=y_pos + 10, width=button_size - 20, height=button_size - 20)

    # Button 1: Reading Light
    create_button(0, light_photo, toggle_reading_light)

    # Button 2: Window Shade
    create_button(button_size, shade_photo, toggle_window_shade)

    # Button 3: Flight Attendant Call
    create_button(2 * button_size, attendant_photo, call_flight_attendant)

    window.update()
    window.attributes('-fullscreen', True)

    # Keep the references to the images (required to prevent garbage collection)
    window.mainloop()

if __name__ == "__main__":
    setup_ui()
