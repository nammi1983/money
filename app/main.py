from app.gui import AIApp
import customtkinter as ctk

def main():
    root = ctk.CTk()
    app = AIApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()