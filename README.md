# ECE & Computer System Design Pathway Projects

Welcome to my foundational systems software repository. This portfolio tracks my progressive transition from pure programming logic to system-level architecture simulations.

---

## Project 1: Virtual LED Blink Simulator
### Overview
A pure-software simulation of a microcontroller's infinite execution loop and digital output toggling. This project bypasses physical hardware to focus entirely on the foundational programming logic used in firmware development.

### Core Concepts
* **Infinite Control Loops:** Replicating a microprocessor's main running state using `while True`.
* **State Toggling:** Utilizing Boolean variables and the `not` operator to mimic physical digital logic (`HIGH` vs `LOW` voltage states).

---

## Project 2: Smart Thermostat Threshold Monitor
### Overview
An environmental boundary monitoring simulation that mimics how embedded controllers process sensor data and trigger hardware safety routines (like fans or heaters) based on precise thresholds.

### Core Concepts
* **Data Parsing:** Transforming string-based terminal data inputs into integers (`int()`) for hardware boundary safety logic.
* **Conditional Branching:** Structuring discrete operational states using `if` and `elif` matching protocols to avoid system dead-zones.

---

## How to Run
* **Run LED Blinker:** `python led_blink.py`
* **Run Thermostat:** `python smart_thermostat.py`
