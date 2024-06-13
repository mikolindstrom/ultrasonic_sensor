synapses:
  - name: "measure_distance"
    signals:
      - order: "measure distance"
    neurons:
      - ultrasonic_sensor:
          trigger_pin: 23
          echo_pin: 24
