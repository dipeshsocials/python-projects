import time

print("===== Digital Clock =====")
print("Press Ctrl + C to stop.\n")

try:
    while True:
        current_time = time.strftime("%H:%M:%S")
        print(f"\rCurrent Time: {current_time}", end="")
        time.sleep(1)

except KeyboardInterrupt:
    print("\n\nClock stopped.")
