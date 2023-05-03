
import json

import paho.mqtt.client as mqtt
from django.conf import settings

from .models import *
import pyowm

topics = ['v3/my-lora1-application@ttn/devices/eui-70b3d57edd05a535/up', 'v3/my-lora1-application@ttn/devices/eui-70b3d57ed005ca2c/up']
topi =['eui-70b3d57edd05a535','eui-70b3d57ed005ca2c']
def on_connect(mqtt_client, userdata, flags, rc):

    if rc == 0:
        print('Connected successfully')
        
        #yass card
        mqtt_client.subscribe(topics[0])

        #other card
        mqtt_client.subscribe(topics[1])

    else:
        print('Bad connection. Code:', rc)

def on_message(mqtt_client, userdata, msg):
        # Decode the incoming message
        payload_dict =json.loads(msg.payload)
        print('----------------------------------------')
        print(f'Received message on topic: {msg.topic} with payload: {msg.payload}', '\n')
        
        referencep = msg.topic.split('/')[-2]
        print('rrrrrffffffrrrppp',referencep)
        

        # project = myProject.objects.get(polygon_id=id)

        
            # Get the node with the matching reference
        nodes = node.objects.filter(reference=referencep).order_by('-Idnode')
        print('**************nodes',nodes)
        if nodes:
            n = nodes[0]
            print('*****n',n.nom,' ********* ref',n.reference)
        

            
                    # print('reeeef',n.reference)
                    # Get temperature and humidity values from payload
            temperature = payload_dict['uplink_message']['decoded_payload']['temperature']
            humidity = payload_dict['uplink_message']['decoded_payload']['humidity']
            Battery_level = payload_dict['uplink_message']['decoded_payload']['Battery_level']
            
            rssi = payload_dict['uplink_message']['rx_metadata'][0]['rssi']
            snr = payload_dict['uplink_message']['rx_metadata'][0]['snr']



            print('temperature :', temperature, 'humidity :', humidity, 'rssi :', rssi, 'snr :', snr,'Battery_level :',Battery_level ,'\n')

                    # Replace "YOUR_API_KEY" with your actual API key from OpenWeatherMap
            owm = pyowm.OWM("0f21fa98b6e075b77fd85b3af087e294")
                
                    # Replace "City name" with the name of the city you want weather data for
            location = owm.weather_manager().weather_at_place('Bizerte, TN')
                
            weather = location.weather

                    # Get the temperature, humidity, and wind speed
            temperature_owm = weather.temperature('celsius')['temp']
            humidity_owm = weather.humidity
            wind_speed = weather.wind()['speed']
            rain_volume = weather.rain.get('1h', 0)  # get rain volume in last 1 hour

            # print('wind_speed',wind_speed)
            # print('rain',rain_volume)



                    # print('temperature :', temperature, 'humidity :', humidity, 'wind :', wind_speed, '\n')
                    # Create a new Post object and save it to the database
                    # project = myProject.objects.get(polygon_id=id)

                
                    # nodes = node.objects.filter(polyg=project).order_by('-Idnode')
                    
                    # my_project = myProject.objects.get(polygon_id=id)
                    # # polygon = my_project.geomp

                    # nodes = node.objects.filter(polyg=my_project)
                    # onode = nodes[0]

            n.RSSI = rssi
            n.save()
            n.Battery_value =Battery_level
            n.save()
            print('RSSI',n.RSSI)
            print('Battery_value',n.Battery_value)





                    # my_project = myProject.objects.get(polygon_id=id)
                    # # polygon = my_project.geomp

                    # nodes = node.objects.filter(polyg=my_project).order_by('-Idnode')
                    # nodee = nodes[0]
                    
            datas = Data.objects.filter(node=n)
            print('datasssssss0',datas)
            new_data = Data.objects.create(temperature=temperature, humidity=humidity, wind=wind_speed,rain=rain_volume, node=n)
                    #datas.append(new_data)
            new_data.save()
            print('hiiiiiiiiii',new_data)

# def start_mqtt_client(id):
#     # Create a new MQTT client instance
#     client = mqtt.Client()

#     # Set the client's connection and message handling functions
#     client.on_connect = on_connect
#     client.on_message = lambda client, userdata, msg: on_message(client, userdata, msg,id)

#     # Set the client's username and password
#     client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)

#     # Connect to the MQTT broker
#     client.connect(
#         host=settings.MQTT_SERVER,
#         port=settings.MQTT_PORT,
#         keepalive=settings.MQTT_KEEPALIVE
#     )
    
#     client.loop_forever()
#     return client

client = mqtt.Client()

    # Set the client's connection and message handling functions
client.on_connect = on_connect
client.on_message = lambda client, userdata, msg: on_message(client, userdata, msg)

    # Set the client's username and password
client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)

    # Connect to the MQTT broker
client.connect(
        host=settings.MQTT_SERVER,
        port=settings.MQTT_PORT,
        keepalive=settings.MQTT_KEEPALIVE
)
    
    
        # Start the MQTT loop (this function blocks and waits for incoming messages)
#     client.loop_forever()
    # Start the MQTT client loop
#     client.loop_start()

    # Return the MQTT client instance
#     return client