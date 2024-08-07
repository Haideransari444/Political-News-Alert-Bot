import pywhatkit as kit
import time

# Define the phone number, message, and interval (in minutes)
phone_number = "+923025206406"  # Replace with the recipient's phone number
message = "Hello, this is a scheduled message."
interval = 1  # Time interval between messages in minutes

def send_message():
    # Get the current time
    now = time.localtime()
    hour = now.tm_hour
    minute = now.tm_min + 2  # Add 2 minutes to the current time to schedule the first message
    
    # Schedule the message
    kit.sendwhatmsg(phone_number, message, hour, minute)

def main():
    while True:
        send_message()
        # Wait for the specified interval before sending the next message
        time.sleep(interval * 60)  

if __name__ == "__main__":
    main()
