import paho.mqtt.client as mqtt

# This is the Publisher
IP = '10.25.172.52'
username = 'iotproxy'
password = 'pa$$w0rd'
port = 1883
topic = 'topic/test'
payload = 'Laser Cutter Fire Detection.'

def main():
    client = mqtt.Client()
    client.username_pw_set(username, password)
    client.connect(IP, port, 60)
    client.publish(topic, payload)
    client.disconnect()


if __name__ == '__main__':
    main()