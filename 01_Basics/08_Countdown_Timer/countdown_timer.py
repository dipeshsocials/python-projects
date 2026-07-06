import time


def countdown(seconds):
    while seconds >= 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"

        print(f"\rTime Remaining: {timer}", end="")

        time.sleep(1)
        seconds -= 1

    print("\n\n⏰ Time's up!")


print("===== Countdown Timer =====")

try:
    total_seconds = int(input("Enter countdown time (in seconds): "))

    if total_seconds < 0:
        print("Please enter a non-negative number.")
    else:
        countdown(total_seconds)

except ValueError:
    print("Please enter a valid integer.")
