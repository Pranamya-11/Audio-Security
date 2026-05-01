import tkinter as tk
from datetime import datetime
import threading

try:
    import winsound  # for Windows beep
except:
    winsound = None


def show_alert(class_label, timestamp):
    root = tk.Tk()
    root.title("Caregiver Alert System")
    root.geometry("400x200")

    is_safe = class_label.lower() == "legitimate"

    if is_safe:
        message = "Audio is Safe"
        bg_color = "green"
        log_type = "SAFE"
    else:
        message = f"ALERT: Suspicious audio detected\nType: {class_label}\nTime: {timestamp}"
        bg_color = "red"
        log_type = "ALERT"

        # Beep sound (only if available)
        if winsound:
            threading.Thread(target=lambda: winsound.Beep(1000, 500)).start()

    root.configure(bg=bg_color)

    label = tk.Label(root, text=message, bg=bg_color, fg="white",
                     font=("Arial", 12, "bold"), wraplength=350, justify="center")
    label.pack(expand=True)

    # Write to log file
    with open("alert_log.txt", "a") as file:
        file.write(f"{timestamp} | {log_type} | {class_label}\n")

    # Auto close after 4 sec
    root.after(4000, root.destroy)

    root.mainloop()

    return not is_safe


# Testing purpose
if __name__ == "__main__":
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # show_alert("Replay Attack", current_time)
    show_alert("Legitimate", current_time)