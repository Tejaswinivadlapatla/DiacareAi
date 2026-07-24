from pathlib import Path
import tkinter.messagebox as messagebox

import customtkinter as ctk
from PIL import Image


ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("green")

PROJECT_FOLDER = Path(__file__).resolve().parent.parent
IMAGE_PATH = PROJECT_FOLDER / "assets"/"logo.png"

class HomePage(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("DiaCare AI")
        self.geometry("1400x850")
        self.minsize(1100, 700)
        self.configure(fg_color="#F7FBFB")

        self.hero_image = None

        self.scroll = ctk.CTkScrollableFrame(
            self,
            fg_color="#F7FBFB"
        )
        self.scroll.pack(fill="both", expand=True)

        self.create_hero_section()
        self.create_diabetes_section()
        self.create_features_section()
        self.create_about_features_section()

        self.create_app_use_section()
        self.create_footer()

    def create_hero_section(self):

        hero_frame = ctk.CTkFrame(
            self.scroll,
            fg_color="white",
            corner_radius=0
        )
        hero_frame.pack(fill="x", padx=25, pady=(25, 45))

        left_frame = ctk.CTkFrame(
            hero_frame,
            fg_color="transparent",
            width=570
        )
        left_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(60, 25),
            pady=55
        )

        right_frame = ctk.CTkFrame(
            hero_frame,
            fg_color="transparent",
            width=650
        )
        right_frame.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(20, 30),
            pady=30
        )

        ctk.CTkLabel(
            left_frame,
            text="ABOUT DIABETES",
            font=("Segoe UI", 16, "bold"),
            text_color="#008D87"
        ).pack(anchor="w", pady=(20, 12))

        ctk.CTkLabel(
            left_frame,
            text="DiaCare AI",
            font=("Segoe UI", 46, "bold"),
            text_color="#101820"
        ).pack(anchor="w")

        ctk.CTkLabel(
            left_frame,
            text="Your Intelligent Diabetes\nHealthcare Companion",
            font=("Segoe UI", 29),
            justify="left",
            text_color="#101820"
        ).pack(anchor="w", pady=(10, 22))

        ctk.CTkLabel(
            left_frame,
            text=(
                "DiaCare AI helps you understand diabetes risk, analyze "
                "food nutrition, receive healthy meal ideas, and explore "
                "healthcare guidance in one simple application."
            ),
            font=("Segoe UI", 18),
            justify="left",
            wraplength=500,
            text_color="#3E5155"
        ).pack(anchor="w", pady=(0, 28))

        ctk.CTkButton(
            left_frame,
            text="Explore DiaCare AI",
            width=220,
            height=48,
            corner_radius=12,
            font=("Segoe UI", 16, "bold"),
            fg_color="#008D87",
            hover_color="#006F6B",
            command=self.scroll_to_features
        ).pack(anchor="w")

        if IMAGE_PATH.exists():
            image = Image.open(IMAGE_PATH)

            self.hero_image = ctk.CTkImage(
                light_image=image,
                dark_image=image,
                size=(620, 470)
            )

            ctk.CTkLabel(
                right_frame,
                text="",
                image=self.hero_image
            ).pack(fill="both", expand=True)

        else:
            ctk.CTkLabel(
                right_frame,
                text=(
                    "Image not found.\n\n"
                    "Add your image here:\n"
                    "assets/images/diabetes_about.jpg"
                ),
                font=("Segoe UI", 18),
                text_color="#647A7D"
            ).pack(fill="both", expand=True)

    def create_diabetes_section(self):

        section = ctk.CTkFrame(
            self.scroll,
            fg_color="#EAF8F6",
            corner_radius=0
        )
        section.pack(fill="x", padx=25, pady=(0, 40))

        ctk.CTkLabel(
            section,
            text="What is Diabetes?",
            font=("Segoe UI", 38, "bold"),
            text_color="#101820"
        ).pack(pady=(45, 15))

        ctk.CTkLabel(
            section,
            text=(
                "Diabetes is a long-term health condition in which the body "
                "has difficulty managing glucose, also called blood sugar. "
                "High blood sugar over time can affect the heart, kidneys, "
                "eyes, nerves and blood vessels."
            ),
            font=("Segoe UI", 18),
            justify="center",
            wraplength=1050,
            text_color="#3E5155"
        ).pack(padx=60, pady=(0, 20))

        info_frame = ctk.CTkFrame(
            section,
            fg_color="transparent"
        )
        info_frame.pack(pady=(10, 45))

        information = [
            (
                "Type 1 Diabetes",
                "The body produces little or no insulin. It requires regular medical care and insulin treatment."
            ),
            (
                "Type 2 Diabetes",
                "The body does not use insulin effectively. Lifestyle, family history and weight can contribute."
            ),
            (
                "Gestational Diabetes",
                "Diabetes that can develop during pregnancy and needs regular medical monitoring."
            )
        ]

        for title, description in information:
            card = ctk.CTkFrame(
                info_frame,
                width=315,
                height=190,
                fg_color="white",
                corner_radius=18
            )
            card.pack(side="left", padx=15)
            card.pack_propagate(False)

            ctk.CTkLabel(
                card,
                text=title,
                font=("Segoe UI", 19, "bold"),
                text_color="#008D87"
            ).pack(pady=(25, 12))

            ctk.CTkLabel(
                card,
                text=description,
                font=("Segoe UI", 14),
                justify="center",
                wraplength=255,
                text_color="#4B6063"
            ).pack()

    def create_about_features_section(self):

        section = ctk.CTkFrame(
            self.scroll,
            fg_color="white",
            corner_radius=15
        )
        section.pack(fill="x", padx=25, pady=(0,40))

        ctk.CTkLabel(
            section,
            text="Why Choose DiaCare AI?",
            font=("Segoe UI",34,"bold"),
            text_color="#101820"
        ).pack(pady=(30,10))

        ctk.CTkLabel(
            section,
            text=(
                "DiaCare AI is an intelligent healthcare application designed to "
                "support diabetes awareness and promote healthier lifestyles. "
                "It combines Artificial Intelligence with easy-to-use health tools "
                "to help users monitor their well-being and make informed decisions."
            ),
            font=("Segoe UI",17),
            wraplength=1000,
            justify="center",
            text_color="#4B6063"
        ).pack(padx=40, pady=(0,25))

        features = (
            "• Diabetes Prediction – Predict diabetes risk using Machine Learning.\n\n"
            "• Nutrition Analysis – Analyze calories, carbohydrates, protein, sugar, GI and GL.\n\n"
            "• AI Assistant – Get instant answers to health and diabetes-related questions.\n\n"
            "• Meal Planner – Receive balanced meal suggestions for a healthier lifestyle.\n\n"
            "• BMI Calculator – Calculate Body Mass Index and understand your weight category."
        )

        ctk.CTkLabel(
            section,
            text=features,
            font=("Segoe UI",16),
            justify="left",
            wraplength=950,
            text_color="#37474F"
        ).pack(anchor="w", padx=60, pady=(0,35))

    def create_features_section(self):

        self.features_heading = ctk.CTkLabel(
            self.scroll,
            text="Explore DiaCare AI Features",
            font=("Segoe UI", 36, "bold"),
            text_color="#101820"
        )
        self.features_heading.pack(pady=(20, 5))

        ctk.CTkLabel(
            self.scroll,
            text="Everything you need for diabetes awareness and everyday health support.",
            font=("Segoe UI", 17),
            text_color="#647A7D"
        ).pack(pady=(0, 25))

        cards_frame = ctk.CTkFrame(
            self.scroll,
            fg_color="transparent"
        )
        cards_frame.pack(pady=(0, 40))

        features = [
            ("🩺", "Diabetes Prediction", "Enter health values to receive a diabetes-risk screening result."),
            ("🍎", "Nutrition Analysis", "View calories, protein, carbohydrates, sugar, GI and GL."),
            ("🤖", "AI Assistant", "Ask questions about healthy food, exercise and diabetes care."),
            ("🍽", "Meal Planner", "Explore balanced meal suggestions for breakfast, lunch and dinner."),
            ("⚖️", "BMI Calculator", "Calculate your Body Mass Index and receive healthy weight guidance.")
        ]

        for index, feature in enumerate(features):
            icon, title, description = feature

            row = 0
            column = index 

            card = ctk.CTkFrame(
                cards_frame,
                width=250,
                height=250,
                fg_color="white",
                corner_radius=18,
                border_width=1,
                border_color="#B2F3EC"
            )
            card.grid(row=row, column=column, padx=17, pady=17)
            card.grid_propagate(False)

            ctk.CTkLabel(
                card,
                text=icon,
                font=("Segoe UI Emoji", 38)
            ).pack(pady=(22, 7))

            ctk.CTkLabel(
                card,
                text=title,
                font=("Segoe UI", 18, "bold"),
                text_color="#008D87"
            ).pack()

            desc = ctk.CTkLabel(
                card,
                text=description,
                font=("Segoe UI", 13),
                justify="center",
                wraplength=220,
                text_color="#52686B"
            )
            desc.pack(pady=(8, 10))

# Reserve the same space for every description
            desc.configure(height=45)

            ctk.CTkButton(
                card,
                text="Explore",
                width=120,
                height=30,
                corner_radius=10,
                command=lambda name=title: self.open_feature(name)
            ).pack()

    def create_app_use_section(self):

        section = ctk.CTkFrame(
            self.scroll,
            fg_color="#0A827B",
            corner_radius=0
        )
        section.pack(fill="x", padx=25, pady=(0, 40))

        ctk.CTkLabel(
            section,
            text="How DiaCare AI Helps You",
            font=("Segoe UI", 36, "bold"),
            text_color="white"
        ).pack(pady=(42, 15))

        ctk.CTkLabel(
            section,
            text=(
                "This application brings diabetes awareness, nutrition information "
                "and health-management tools together in one easy desktop app."
            ),
            font=("Segoe UI", 17),
            justify="center",
            wraplength=950,
            text_color="#E1F7F4"
        ).pack(padx=50, pady=(0, 25))

        benefits = [
            "✓ Understand diabetes risk early",
            "✓ Analyze nutrition values",
            "✓ Plan healthy meals",
            "✓ Calculate BMI instantly",
            "✓ Get AI-powered health guidance"
        ]

        benefits_frame = ctk.CTkFrame(
            section,
            fg_color="transparent"
        )
        benefits_frame.pack(pady=(0, 40))

        for benefit in benefits:
            ctk.CTkLabel(
                benefits_frame,
                text=benefit,
                font=("Segoe UI", 16),
                text_color="white"
            ).pack(anchor="w", pady=5)

    def create_footer(self):

        footer = ctk.CTkFrame(
            self.scroll,
            fg_color="#101820",
            corner_radius=0
        )
        footer.pack(fill="x", padx=25, pady=(0, 15))

        ctk.CTkLabel(
            footer,
            text="DiaCare AI",
            font=("Segoe UI", 24, "bold"),
            text_color="white"
        ).pack(pady=(24, 5))

        ctk.CTkLabel(
            footer,
            text="Intelligent Diabetes Prediction & Healthcare Assistant",
            font=("Segoe UI", 15),
            text_color="#445251"
        ).pack()

        ctk.CTkLabel(
            footer,
            text=(
                "This application provides general screening and educational guidance. "
                "It is not a substitute for professional medical diagnosis."
            ),
            font=("Segoe UI", 12),
            justify="center",
            wraplength=850,
            text_color="#B6CECC"
        ).pack(pady=(10, 24))

    def scroll_to_features(self):

        self.update_idletasks()

        canvas = self.scroll._parent_canvas
        bounding_box = canvas.bbox("all")

        if bounding_box is None:
            return

        content_height = bounding_box[3]

        if content_height == 0:
            return

        target = self.features_heading.winfo_y() / content_height
        current = canvas.yview()[0]

        self.smooth_scroll(canvas, current, target, 25)

    def smooth_scroll(self, canvas, start, target, steps):

        difference = target - start

        def move(step):
            position = start + (difference * step / steps)
            canvas.yview_moveto(position)

            if step < steps:
                self.after(15, move, step + 1)

        move(1)


    def open_feature(self, feature_name):

        if feature_name == "Diabetes Prediction":
            from ui.prediction import PredictionWindow

            self.withdraw()
            PredictionWindow(self)

        elif feature_name == "AI Assistant":
            from ui.chatbot import ChatbotWindow

            self.withdraw()
            ChatbotWindow(self)

        elif feature_name == "Nutrition Analysis":
            from ui.nutrition import NutritionWindow

            self.withdraw()
            NutritionWindow(self)

        elif feature_name == "Meal Planner":
            from ui.meal_planner import MealPlannerWindow

            self.withdraw()
            MealPlannerWindow(self) 

        elif feature_name == "BMI Calculator":
            from ui.bmi_calculator import BMICalculatorWindow

            self.withdraw()
            BMICalculatorWindow(self)     

        else:
            messagebox.showinfo(
                "DiaCare AI",
                f"{feature_name} will be connected next."
            )


if __name__ == "__main__":
    app = HomePage()
    app.mainloop()