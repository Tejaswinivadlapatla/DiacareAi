import customtkinter as ctk
from tkinter import messagebox
from pathlib import Path
from PIL import Image

from services.bmi_service import calculate_bmi

PROJECT_FOLDER = Path(__file__).resolve().parent.parent
IMAGE_PATH = PROJECT_FOLDER / "assets" / "bmi_banner.jpg"


class BMICalculatorWindow(ctk.CTkToplevel):

    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.title("BMI Calculator")
        self.geometry("1200x700")
        self.configure(fg_color="#F4F6F9")

        self.protocol("WM_DELETE_WINDOW", self.go_back)

        self.banner = None

        self.create_ui()

    def create_ui(self):

        # ================= Header =================

        header = ctk.CTkFrame(
            self,
            fg_color="#4CAF50",
            height=70,
            corner_radius=0
        )
        header.pack(fill="x")

        ctk.CTkLabel(
            header,
            text="⚖️ BMI Calculator",
            font=("Segoe UI", 28, "bold"),
            text_color="white"
        ).pack(pady=18)

        # ================= Main =================

        main = ctk.CTkFrame(self, fg_color="#F4F6F9")
        main.pack(fill="both", expand=True, padx=20, pady=20)

        self.left = ctk.CTkFrame(
            main,
            width=320,
            fg_color="white",
            corner_radius=15
        )
        self.left.pack(side="left", fill="y", padx=(0, 20))
        self.left.pack_propagate(False)

        self.right = ctk.CTkScrollableFrame(
            main,
            fg_color="white",
            corner_radius=15
        )
        self.right.pack(side="right", fill="both", expand=True)

        self.create_left_panel()
        self.create_right_panel()

    def create_left_panel(self):

        ctk.CTkLabel(
            self.left,
            text="Enter Details",
            font=("Segoe UI",22,"bold"),
            text_color="#2E7D32"
        ).pack(pady=(25,20))

        ctk.CTkLabel(self.left,text="Height (cm)").pack(anchor="w",padx=25)

        self.height_entry = ctk.CTkEntry(
            self.left,
            width=260,
            height=40,
            placeholder_text="170"
        )
        self.height_entry.pack(pady=(5,15))

        ctk.CTkLabel(self.left,text="Weight (kg)").pack(anchor="w",padx=25)

        self.weight_entry = ctk.CTkEntry(
            self.left,
            width=260,
            height=40,
            placeholder_text="65"
        )
        self.weight_entry.pack(pady=(5,15))

        ctk.CTkLabel(self.left,text="Age").pack(anchor="w",padx=25)

        self.age_entry = ctk.CTkEntry(
            self.left,
            width=260,
            height=40,
            placeholder_text="22"
        )
        self.age_entry.pack(pady=(5,15))

        ctk.CTkLabel(self.left,text="Gender").pack(anchor="w",padx=25)

        self.gender_menu = ctk.CTkOptionMenu(
            self.left,
            values=["Male","Female","Other"],
            width=260
        )
        self.gender_menu.pack(pady=(5,25))

        ctk.CTkButton(
            self.left,
            text="Calculate BMI",
            width=260,
            command=self.calculate
        ).pack(pady=8)

        ctk.CTkButton(
            self.left,
            text="Clear",
            width=260,
            command=self.clear
        ).pack(pady=8)

        ctk.CTkButton(
            self.left,
            text="Back",
            width=260,
            command=self.go_back
        ).pack(pady=8)

    def create_right_panel(self):

        # ================= Banner =================
        if IMAGE_PATH.exists():

            image = Image.open(IMAGE_PATH)

            self.banner = ctk.CTkImage(
                light_image=image,
                dark_image=image,
                size=(780,260)
            )

            ctk.CTkLabel(
                self.right,
                text="",
                image=self.banner
            ).pack(pady=20)

        # ================= Title =================

        ctk.CTkLabel(
            self.right,
            text="BMI Result",
            font=("Segoe UI",24,"bold"),
            text_color="#2E7D32"
        ).pack(pady=(5,20))

        # ================= BMI Card =================

        bmi_frame = ctk.CTkFrame(
            self.right,
            fg_color="#F5F5F5",
            corner_radius=12,
            height=120
        )
        bmi_frame.pack(fill="x", padx=20, pady=10)
        bmi_frame.pack_propagate(False)
        ctk.CTkLabel(
            bmi_frame,
            text="Your BMI",
            font=("Segoe UI",16,"bold")
        ).pack(pady=(15,5))

        self.bmi_label = ctk.CTkLabel(
            bmi_frame,
            text="--",
            font=("Segoe UI",40,"bold"),
            text_color="#4CAF50"
        )
        self.bmi_label.pack(pady=(0,15))

        # ================= Category =================

        category_frame = ctk.CTkFrame(
            self.right,
            fg_color="#F5F5F5",
            corner_radius=12
        )
        category_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(
            category_frame,
            text="Category",
            font=("Segoe UI",16,"bold")
        ).pack(pady=(15,5))

        self.category_label = ctk.CTkLabel(
            category_frame,
            text="Not Calculated",
            font=("Segoe UI",24,"bold"),
            text_color="#1976D2"
        )
        self.category_label.pack(pady=(0,15))

        # ================= Advice =================

        advice_frame = ctk.CTkFrame(
            self.right,
            fg_color="#F5F5F5",
            corner_radius=12
        )
        advice_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(
            advice_frame,
            text="Health Advice",
            font=("Segoe UI",16,"bold")
        ).pack(pady=(15,10))

        self.advice_label = ctk.CTkLabel(
            advice_frame,
            text="Enter your height and weight\nthen click Calculate BMI.",
            justify="left",
            wraplength=650,
            font=("Segoe UI",15)
        )
        self.advice_label.pack(padx=20, pady=(0,20))

        # ================= Healthy Range =================

        range_frame = ctk.CTkFrame(
            self.right,
            fg_color="#F5F5F5",
            corner_radius=12
        )
        range_frame.pack(fill="x", padx=20, pady=(10,20))

        ctk.CTkLabel(
            range_frame,
            text="Healthy BMI Range",
            font=("Segoe UI",16,"bold")
        ).pack(pady=(15,5))

        ctk.CTkLabel(
            range_frame,
            text="18.5 - 24.9",
            font=("Segoe UI",24,"bold"),
            text_color="#43A047"
        ).pack(pady=(0,15))

           # ================= BMI Meter =================

        ctk.CTkLabel(
            self.right,
            text="BMI Meter",
            font=("Segoe UI", 18, "bold")
        ).pack(pady=(20, 5))

        self.canvas = ctk.CTkCanvas(
            self.right,
            width=650,
            height=100,
            bg="white",
            highlightthickness=0
        )
        self.canvas.pack()

        # Colored sections
        self.canvas.create_rectangle(20, 45, 170, 70, fill="#42A5F5", outline="")
        self.canvas.create_rectangle(170, 45, 340, 70, fill="#4CAF50", outline="")
        self.canvas.create_rectangle(340, 45, 490, 70, fill="#FFC107", outline="")
        self.canvas.create_rectangle(490, 45, 630, 70, fill="#F44336", outline="")

        # Labels
        self.canvas.create_text(95, 82, text="Underweight", font=("Arial", 10))
        self.canvas.create_text(255, 82, text="Normal", font=("Arial", 10))
        self.canvas.create_text(415, 82, text="Overweight", font=("Arial", 10))
        self.canvas.create_text(560, 82, text="Obese", font=("Arial", 10))

        # Arrow
        self.pointer = self.canvas.create_text(
            20,
            20,
            text="▼",
            fill="red",
            font=("Arial", 20, "bold")
        )

        # BMI Value
        self.pointer_text = self.canvas.create_text(
            20,
            5,
            text="",
            fill="black",
            font=("Arial", 12, "bold")
        )

    def calculate(self):

        try:
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())

            if height <= 0 or weight <= 0:
                raise ValueError

            bmi, category, advice = calculate_bmi(height, weight)

            self.bmi_label.configure(text=str(bmi))
            self.canvas.itemconfig(
                self.pointer_text,
                text=f"BMI : {bmi}"
            )            
            self.category_label.configure(text=category)
            # Move the arrow based on BMI

            if bmi < 18.5:
                position = 95

            elif bmi < 25:
                position = 225

            elif bmi < 30:
                position = 415

            else:
                position = 560

            self.canvas.coords(
                self.pointer,
                position,
                20
            )

            self.canvas.coords(
                self.pointer_text,
                position,
                5
            )

            
            self.advice_label.configure(text=advice)

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter valid height and weight."
            )

    def clear(self):

        # Clear input fields
        self.height_entry.delete(0, "end")
        self.weight_entry.delete(0, "end")
        self.age_entry.delete(0, "end")

        # Reset gender
        self.gender_menu.set("Male")

        # Reset BMI
        self.bmi_label.configure(
            text="--",
            text_color="#4CAF50"
        )

        # Reset category
        self.category_label.configure(
            text="Not Calculated",
            text_color="#1976D2"
        )

        # Reset advice
        self.advice_label.configure(
            text="Enter your height and weight\nthen click Calculate BMI."
        )

        # Reset BMI meter
        self.canvas.coords(self.pointer, 20, 20)
        self.canvas.coords(self.pointer_text, 20, 5)
        self.canvas.itemconfig(self.pointer_text, text="")

    def go_back(self):
        self.destroy()
        self.parent.deiconify()

    