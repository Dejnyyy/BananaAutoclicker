import time
import pygetwindow as gw
import win32api
import win32con
import keyboard
import tkinter as tk
from threading import Thread

def get_window_center(window_title):
    windows = gw.getWindowsWithTitle(window_title)
    if not windows:
        raise Exception(f"Okno s názvem '{window_title}' nebylo nalezeno.")
    window = windows[0]
    center_x = window.left + window.width // 2
    center_y = window.top + window.height // 2
    return center_x, center_y

def click_at(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def update_click_count():
    global click_count
    while True:
        click_label.config(text=f"Clicks: {click_count}")
        time.sleep(0.1)

def click_in_window():
    global click_count
    x, y = get_window_center(window_title)
    while True:
        if keyboard.is_pressed('q'):
            print("Skript ukončen.")
            break
        
        # Center
        click_at(x, y)
        click_count += 1
        time.sleep(click_interval)

        # 10 pixels right from center
        click_at(x + 10, y)
        click_count += 1
        time.sleep(click_interval)

        # Center
        click_at(x, y)
        click_count += 1
        time.sleep(click_interval)

        # 10 pixels left from center
        click_at(x - 10, y)
        click_count += 1
        time.sleep(click_interval)

        # Center
        click_at(x, y)
        click_count += 1
        time.sleep(click_interval)

        # 10 pixels down from center
        click_at(x, y + 10)
        click_count += 1
        time.sleep(click_interval)

        # Center
        click_at(x, y)
        click_count += 1
        time.sleep(click_interval)

        # 10 pixels up from center
        click_at(x, y - 10)
        click_count += 1
        time.sleep(click_interval)

        # Center
        click_at(x, y)
        click_count += 1
        time.sleep(click_interval)

def start_clicking():
    click_thread = Thread(target=click_in_window)
    click_thread.start()

# Název okna
window_title = "Banana"

# Interval mezi kliknutími v sekundách
click_interval = 0.01

# Počet kliknutí
click_count = 0

# GUI
root = tk.Tk()
root.title("Click Counter")
root.geometry("150x50")
click_label = tk.Label(root, text=f"Clicks: {click_count}", font=("Helvetica", 12))
click_label.pack()

# Start the clicking and update thread
Thread(target=start_clicking).start()
Thread(target=update_click_count).start()

# Run the GUI
root.mainloop()
