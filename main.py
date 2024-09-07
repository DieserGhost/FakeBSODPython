import tkinter as tk
import ctypes
import winsound


def play_error_sound():
    winsound.MessageBeep(winsound.MB_ICONHAND)

def make_fullscreen(window):
    window.attributes('-fullscreen', True)
    window.configure(bg='#0079D9')
    window.config(cursor="none")

def bsod_simulation():
    root = tk.Tk()
    make_fullscreen(root)

    top_text = tk.Label(
        root,
        text="Your PC ran into a problem that it couldn't handle, and now it needs to",
        font=("Segoe UI", 24),
        bg='#0079D9',
        fg="white"
    )
    top_text.place(x=50, y=400)

    top_text2 = tk.Label(
        root,
        text="restart. We're just collecting some error info, and then we'll restart for you.",
        font=("Segoe UI", 24),
        bg='#0079D9',
        fg="white"
    )
    top_text2.place(x=50, y=450)

    sad_face = tk.Label(root, text=":(", font=("Segoe UI", 160), bg='#0079D9', fg="white")
    sad_face.place(x=50, y=95)

    error_text = tk.Label(
        root,
        text="If you'd like to know more, you can search online later for this error: DPC_WATCHDOG_VIOLATION",
        font=("Segoe UI", 14),
        bg='#0079D9',
        fg="white"
    )
    error_text.place(x=50, y=500)

    root.mainloop()

if __name__ == "__main__":
    play_error_sound()
    ctypes.windll.kernel32.SetConsoleTitleW("Windows Error")
    bsod_simulation()
