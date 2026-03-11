# Lab 2 – LoRa Measurements

This directory contains measurement data collected during the **LoRa laboratory experiment**.

* `.txt` files contain the **raw measurement data** directly recorded from the receiver.
* `.csv` files contain **filtered data**, separated by **sender ID**.

During filtering, some rows were skipped because they contained **invalid or corrupted data** (for example: malformed counters, serial timestamps, or formatting errors).

---

# Experiment Parameters

| Parameter ID | Description     |
| ------------ | --------------- |
| **p1**       | Parameter set 1 |
| **p2**       | Parameter set 2 |

---

# Sender Devices

| Sender ID | Description     |
| --------- | --------------- |
| **id1**   | Sender device 1 |
| **id2**   | Sender device 2 |

---

# Measurement Locations

| Location Code        | Description                               |
| -------------------- | ----------------------------------------- |
| **0m**               | Reference measurement at 0 meters         |
| **l2_f5**            | Location 2 – Floor 5                      |
| **l3_f1**            | Location 3 – Floor 1                      |
| **l4_tunnel**        | Location 4 – Tunnel                       |
| **l5_k1**            | Location 5 – Second building, first floor |
| **l6_outside_hvl**   | Location 6 – Outside HVL entrance         |
| **l7_inside_hvl_f1** | Location 7 – Second building, first floor |
| **l8_inside_hvl_f5** | Location 8 – Second building, fifth floor |

---

# Data Format

Each measurement row contains:

```
id,counter,RSSI,SNR
```

Example:

```
1,25,-78,7.50
```

| Field       | Description                              |
| ----------- | ---------------------------------------- |
| **id**      | Sender device ID                         |
| **counter** | Packet counter                           |
| **RSSI**    | Received Signal Strength Indicator (dBm) |
| **SNR**     | Signal-to-Noise Ratio (dB)               |

---

# Notes

* RSSI values closer to **0 dBm** indicate stronger signals.
* Negative RSSI values indicate weaker signals.
* Higher **SNR** generally indicates better signal quality.
* Some raw rows may contain **serial monitor timestamps** or malformed data which were removed during preprocessing.

---
