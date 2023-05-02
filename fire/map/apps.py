from django.apps import AppConfig



class MapConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'map'
    
    # def ready(self):
    #     from . import mqtt
    #     import paho.mqtt.client as mqtt
    #     # mqtt.client.loop_start()
    #     # client.loop_forever()
    #     client = mqtt.Client()
    #     client.loop_start()
        

