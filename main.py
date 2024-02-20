humedad = 0
temperatura = 0
spo2 = 0
pulso = 0
glucosa = 0

def on_forever():
    global temperatura, humedad, spo2, pulso, glucosa
    dht11_dht22.query_data(DHTtype.DHT11, DigitalPin.P0, True, False, True)
    temperatura = dht11_dht22.read_data(dataType.TEMPERATURE)
    humedad = dht11_dht22.read_data(dataType.HUMIDITY)
    basic.show_string("T: " + str(temperatura) + " H: " + str(humedad))
    basic.pause(2000)
    spo2 = Math.random_range(90, 100)
    basic.show_string("SpO2: " + str(spo2))
    basic.pause(2000)
    pulso = Math.random_range(60, 100)
    basic.show_string("Pulso: " + str(pulso))
    basic.pause(2000)
    glucosa = Math.random_range(80, 140)
    basic.show_string("Glucosa: " + str(glucosa))
    basic.pause(2000)
basic.forever(on_forever)
