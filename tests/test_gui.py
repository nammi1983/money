import unittest
import tkinter as tk
from app.gui import AIApp

class TestGUI(unittest.TestCase):
    def test_gui_initialization(self):
        root = tk.Tk()
        app = AIApp(root)
        self.assertIsNotNone(app.notebook)
        self.assertIsNotNone(app.tab1)
        self.assertIsNotNone(app.tab2)
        self.assertIsNotNone(app.tab3)
        root.destroy()

if __name__ == "__main__":
    unittest.main()