
from machine import Pin
from ir_rx import NEC_16
import utime
import ujson
from umqtt.simple import MQTTClient

# Impostare le tue credenziali MQTT
MQTT_BROKER = "indirizzo_del_broker"
MQTT_CLIENT_ID = "nome_del_client"

# ... (il dizionario rimane invariato)
ir_key = {
    0x45: 'POWER',
    0x46: 'MODE',
    0x47: 'MUTE',
    0x44: 'PLAY',
    0x40: 'PREV',
    0x43: 'NEXT',
    0x07: 'EQ',
    0x15: 'MINUS',
    0x09: 'PLUS',
    0x16: '0',
    0x19: 'REPEAT',
    0x0D: 'USD',
    0x0C: '1',
    0x18: '2',
    0x5E: '3',
    0x08: '4',
    0x1C: '5',
    0x5A: '6',
    0x42: '7',
    0x52: '8',
    0x4A: '9'
}

def callback(data, addr, ctrl):
    if data > 0:
        key_pressed = ir_key.get(data)
        if key_pressed:
            print(key_pressed)
            
            # Invia il messaggio MQTT quando un pulsante è premuto
            send_mqtt_message(key_pressed)

def send_mqtt_message(key_pressed):
    try:
        c = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER)
        c.connect()
        topic = b"ir_remote"
        payload = ujson.dumps({"key_pressed": key_pressed})
        c.publish(topic, payload)
        c.disconnect()
    except Exception as e:
        print("Errore nell'invio del messaggio MQTT:", str(e))

ir = NEC_16(Pin(23, Pin.IN), callback)

# Loop principale per mantenere il programma in esecuzione
while True:
    utime.sleep(1)
