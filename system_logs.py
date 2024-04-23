import psutil
import subprocess
from datetime import datetime
import time

def get_cpu_temperature():
    # Use vcgencmd to get CPU temperature on Raspberry Pi
    process = subprocess.Popen(['vcgencmd', 'measure_temp'], stdout=subprocess.PIPE)
    output, _error = process.communicate()
    cpu_temp = output.decode().split('=')[1].split("'")[0]
    return cpu_temp

def log_system_parameters():
    while True:
        # Get current system parameters
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_temp = get_cpu_temperature()
        ram_percent = psutil.virtual_memory().percent
        network_stats = psutil.net_io_counters()

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Log parameters to a text file
        with open("system_log.txt", "a") as file:
            file.write(f"{current_time} - CPU Usage: {cpu_percent}% | CPU Temp: {cpu_temp} | RAM Usage: {ram_percent}% | "
                       f"Sent: {network_stats.bytes_sent} bytes | Received: {network_stats.bytes_recv} bytes\n")

        # Print for testing (optional)
        print(f"Logged at {current_time}")

        # Sleep for 1 minute (adjust as needed)
        time.sleep(60)

if __name__ == "__main__":
    log_system_parameters()
