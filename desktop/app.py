import tkinter as tk

from desktop.views.dashboard import Dashboard


def main():
    root = tk.Tk()

    Dashboard(root)

    root.mainloop()


if __name__ == "__main__":
    main()