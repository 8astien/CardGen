import tkinter as tk
from card_ui import CardUI
from PIL import ImageFont

def main():

    root = tk.Tk()
    root.geometry("800x600")
    root.title("CardGen v2")
    app = CardUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
