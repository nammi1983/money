import customtkinter as ctk
from tkinter import messagebox
from app.models import train_reinforcement_learning_model
from app.utils import plot_stock_data, enforce_policies, update_policies

class AIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Decision Maker")
        self.root.geometry("800x600")

        # Set theme (dark or light)
        ctk.set_appearance_mode("dark")  # Options: "dark", "light", "system"
        ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

        # Create tabs
        self.tabview = ctk.CTkTabview(root)
        self.tabview.pack(fill="both", expand=True, padx=10, pady=10)

        self.tab1 = self.tabview.add("Training")
        self.tab2 = self.tabview.add("Prediction")
        self.tab3 = self.tabview.add("Settings")

        # Add widgets to tabs
        self.add_training_tab(self.tab1)
        self.add_prediction_tab(self.tab2)
        self.add_settings_tab(self.tab3)

    def add_training_tab(self, tab):
        self.train_button = ctk.CTkButton(tab, text="Train Model", command=self.train)
        self.train_button.pack(pady=10)

        self.plot_button = ctk.CTkButton(tab, text="Plot Stock Data", command=lambda: plot_stock_data(tab, "AAPL"))
        self.plot_button.pack(pady=10)

    def add_prediction_tab(self, tab):
        self.label1 = ctk.CTkLabel(tab, text="Feature 1:")
        self.label1.pack(pady=5)
        self.entry1 = ctk.CTkEntry(tab)
        self.entry1.pack(pady=5)

        self.label2 = ctk.CTkLabel(tab, text="Feature 2:")
        self.label2.pack(pady=5)
        self.entry2 = ctk.CTkEntry(tab)
        self.entry2.pack(pady=5)

        self.predict_button = ctk.CTkButton(tab, text="Make Prediction", command=self.predict)
        self.predict_button.pack(pady=10)

    def add_settings_tab(self, tab):
        self.min_label = ctk.CTkLabel(tab, text="Min Value:")
        self.min_label.pack(pady=5)
        self.min_entry = ctk.CTkEntry(tab)
        self.min_entry.pack(pady=5)

        self.max_label = ctk.CTkLabel(tab, text="Max Value:")
        self.max_label.pack(pady=5)
        self.max_entry = ctk.CTkEntry(tab)
        self.max_entry.pack(pady=5)

        self.update_button = ctk.CTkButton(tab, text="Update Policies", command=self.update_policies)
        self.update_button.pack(pady=10)

    def train(self):
        model = train_reinforcement_learning_model()
        messagebox.showinfo("Training Complete", "The AI model has been trained!")

    def predict(self):
        try:
            feature1 = float(self.entry1.get())
            feature2 = float(self.entry2.get())
            prediction = enforce_policies(feature1 + feature2)  # Example prediction
            messagebox.showinfo("Prediction", f"The predicted value is: {prediction}")
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter valid numbers!")

    def update_policies(self):
        try:
            min_value = float(self.min_entry.get())
            max_value = float(self.max_entry.get())
            update_policies(min_value, max_value)
            messagebox.showinfo("Success", "Policies updated successfully!")
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter valid numbers!")