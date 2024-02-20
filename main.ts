let humedad = 0
let temperatura = 0
let spo2 = 0
let pulso = 0
let glucosa = 0
basic.forever(function () {
    dht11_dht22.queryData(
    DHTtype.DHT11,
    DigitalPin.P0,
    true,
    false,
    true
    )
    temperatura = dht11_dht22.readData(dataType.temperature)
    humedad = dht11_dht22.readData(dataType.humidity)
    basic.showString("T: " + temperatura.toString() + " H: " + humedad.toString())
    basic.pause(2000)
    spo2 = Math.randomRange(90, 100)
    basic.showString("SpO2: " + spo2.toString())
    basic.pause(2000)
    pulso = Math.randomRange(60, 100)
    basic.showString("Pulso: " + pulso.toString())
    basic.pause(2000)
    glucosa = Math.randomRange(80, 140)
    basic.showString("Glucosa: " + glucosa.toString())
    basic.pause(2000)
})
