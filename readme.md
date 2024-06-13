---
  - name: "measure-distance"
    signals:
      - order: "distance"
    class_path: "neurons.ultrasonic_sensor.ultrasonic_sensor.UltrasonicSensor"
    neurons:
      - ultrasonic_sensor:
          trigger_pin: 23
          echo_pin: 24
