import os

log_file = "/home/kali/siem/system_log.txt"

# Check if the log file exists
if os.path.exists(log_file):
    with open(log_file, "r") as f:
        logs = f.readlines()
        print("Logs fetched successfully!")
else:
    print("Log file not found!")
