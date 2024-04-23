# 🍓 Raspberry Pi System Monitor 🖥️

A simple Python script for monitoring system parameters on a Raspberry Pi, just for fun and to practice Python! 🐍

## Overview

This project provides a Python script (`system_monitor.py`) that continuously logs various system parameters of a Raspberry Pi, such as CPU usage, CPU temperature, RAM usage, and network activity. The logged data is stored in a text file (`system_log.txt`) for monitoring and analysis.

The script utilizes the `psutil` library to gather system information and the `vcgencmd` command to retrieve the CPU temperature on Raspberry Pi.

## Features

- Monitor CPU usage percentage.
- Get real-time CPU temperature.
- Track RAM usage percentage.
- Record network data (bytes sent and received).

## Requirements

- Raspberry Pi with Raspbian or similar Linux distribution.
- Python 3.x installed.
- `psutil` library installed (install using `pip install psutil`).

## Usage

1. Clone this repository to your Raspberry Pi:

   ```bash
   git clone https://github.com/855princekumar/raspberry-pi-system-monitor.git

2. Navigate to the project directory:

    ```bash
   cd raspberry-pi-system-monitor

3. Install the required psutil library:
    ```bash
    pip install psutil

4. Run the system monitor script:
   ```bash
   python3 system_monitor.py

5. Sit back and watch as the script logs system parameters to system_log.txt!

## Sample Output
   Here's an example of the logged output in system_log.txt:
   
    2024-04-22 12:00:00 - CPU Usage: 12.5% | CPU Temp: 52.5°C | RAM Usage: 35.7% | Sent: 12345 bytes | Received: 54321 bytes
    2024-04-22 12:01:00 - CPU Usage: 10.2% | CPU Temp: 53.0°C | RAM Usage: 36.1% | Sent: 12456 bytes | Received: 55432 bytes

## Contributing
Contributions to this project are welcome! Feel free to fork the repository and submit pull requests with improvements or additional features.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Disclaimer
This project is for educational and recreational purposes. Use it responsibly and at your own risk!

Enjoy monitoring your Raspberry Pi with this cool Python script! If you have any suggestions or feedback, feel free to open an issue or reach out to me. Happy coding! 🚀🐍



