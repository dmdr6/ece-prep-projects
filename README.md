# Virtual LED Blink Simulator

## Project Overview
A pure-software simulation of a microcontroller's infinite execution loop and digital output toggling. This project bypasses physical hardware to focus entirely on the foundational programming logic used in firmware development and embedded system architectures.

## Core Concepts Demonstrated
* **Infinite Control Loops:** Replicating a microprocessor's main running state using `while True`.
* **State Toggling:** Utilizing Boolean variables and the `not` operator to mimic physical digital logic (`HIGH` vs `LOW` voltage states).
* **Deterministic Delays:** Implementing the `time` library to simulate hardware clock cycles and execution intervals.

## How to Run
1. Ensure Python 3.x is installed.
2. Run the script via terminal: `python led_blink.py`
3. To terminate the infinite loop, press `Ctrl + C`.
