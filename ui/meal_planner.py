import customtkinter as ctk
from PIL import Image


class MealPlannerWindow(ctk.CTkToplevel):

    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.title("Meal Planner")
        self.geometry("1280x720")
        self.configure(fg_color="#F4F6F9")

        self.protocol("WM_DELETE_WINDOW", self.go_back)

        self.create_ui()

    def create_ui(self):

        # ===========================
        # Header
        # ===========================

        header = ctk.CTkFrame(
            self,
            height=70,
            fg_color="#4CAF50",
            corner_radius=0
        )

        header.pack(fill="x")

        title = ctk.CTkLabel(
            header,
            text="🍽️ Meal Planner",
            font=("Segoe UI", 30, "bold"),
            text_color="white"
        )

        title.pack(side="left", padx=30, pady=15)

        app = ctk.CTkLabel(
            header,
            text="👤 DiaCare AI",
            font=("Segoe UI", 18, "bold"),
            text_color="white"
        )

        app.pack(side="right", padx=30)

        # ===========================
        # Main Frame
        # ===========================

        main = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        main.pack(fill="both", expand=True, padx=20, pady=20)

        # ===========================
        # Left Panel
        # ===========================

        left = ctk.CTkFrame(
            main,
            width=310,
            fg_color="white",
            corner_radius=15,
            border_width=1,
            border_color="#D6DBDF"
        )

        left.pack(side="left", fill="y", padx=(0,20))
        left.pack_propagate(False)

        heading = ctk.CTkLabel(
            left,
            text="Meal Details",
            font=("Segoe UI",24,"bold"),
            text_color="black"
        )

        heading.pack(pady=(25,25))

        # ---------------- Age ----------------

        ctk.CTkLabel(
            left,
            text="Age",
            anchor="w",
            font=("Segoe UI",16,"bold"),
            text_color="black"
        ).pack(fill="x", padx=30)

        self.age_entry = ctk.CTkEntry(
            left,
            width=240,
            height=40,
            placeholder_text="Enter Age"
        )

        self.age_entry.pack(pady=(5,20))

        # ---------------- Gender ----------------

        ctk.CTkLabel(
            left,
            text="Gender",
            anchor="w",
            font=("Segoe UI",16,"bold"),
            text_color="black"
        ).pack(fill="x", padx=30)

        self.gender = ctk.CTkOptionMenu(
            left,
            width=240,
            values=[
                "Male",
                "Female"
            ]
        )

        self.gender.pack(pady=(5,20))

        # ---------------- Diabetes ----------------

        ctk.CTkLabel(
            left,
            text="Diabetes Type",
            anchor="w",
            font=("Segoe UI",16,"bold"),
            text_color="black"
        ).pack(fill="x", padx=30)

        self.diabetes = ctk.CTkOptionMenu(
            left,
            width=240,
            values=[
                "Prediabetes",
                "Type 1",
                "Type 2"
            ]
        )

        self.diabetes.pack(pady=(5,20))

        # ---------------- Preference ----------------

        ctk.CTkLabel(
            left,
            text="Meal Preference",
            anchor="w",
            font=("Segoe UI",16,"bold"),
            text_color="black"
        ).pack(fill="x", padx=30)

        self.preference = ctk.CTkOptionMenu(
            left,
            width=240,
            values=[
                "Vegetarian",
                "Non Vegetarian"
            ]
        )

        self.preference.pack(pady=(5,30))

        # ---------------- Buttons ----------------

        self.generate_btn = ctk.CTkButton(
            left,
            text="Generate Plan",
            width=240,
            height=45,
            fg_color="#4CAF50",
            hover_color="#43A047",
            command=self.generate_plan
        )

        self.generate_btn.pack(pady=8)

        self.clear_btn = ctk.CTkButton(
            left,
            text="Clear",
            width=240,
            height=45,
            fg_color="#FF9800",
            hover_color="#F57C00",
            command=self.clear_data
        )

        self.clear_btn.pack(pady=8)

        self.back_btn = ctk.CTkButton(
            left,
            text="Back",
            width=240,
            height=45,
            fg_color="#607D8B",
            hover_color="#546E7A",
            command=self.go_back
        )

        self.back_btn.pack(pady=8)

        # ===========================
        # Right Panel
        # ===========================

        right = ctk.CTkScrollableFrame(
            main,
            fg_color="white",
            corner_radius=15,
            border_width=1,
            border_color="#D6DBDF"
        )

        right.pack(side="right", fill="both", expand=True)
                # ===========================
        # Banner Image
        # ===========================

        try:

            image = Image.open("assets/meal_banner.jpg")

            self.banner = ctk.CTkImage(
                light_image=image,
                dark_image=image,
                size=(760, 180)
            )

            banner = ctk.CTkLabel(
                right,
                image=self.banner,
                text=""
            )

            banner.pack(pady=(20,10))

        except:

            banner = ctk.CTkLabel(
                right,
                text="🥗 Healthy Meal Planner",
                font=("Segoe UI",30,"bold"),
                text_color="#4CAF50"
            )

            banner.pack(pady=30)

        # ===========================
        # Title
        # ===========================

        title = ctk.CTkLabel(
            right,
            text="Today's Healthy Meal Plan",
            font=("Segoe UI",24,"bold"),
            text_color="black"
        )

        title.pack(pady=(5,20))

        # ===========================
        # Breakfast Card
        # ===========================

        self.breakfast = ctk.CTkFrame(
            right,
            fg_color="#E3F2FD",
            corner_radius=12,
            height=70
        )

        self.breakfast.pack(fill="x", padx=25, pady=6)

        self.breakfast_label = ctk.CTkLabel(
            self.breakfast,
            text="🥣 Breakfast : --",
            font=("Segoe UI",16,"bold"),
            text_color="black",
            anchor="w"
        )

        self.breakfast_label.pack(anchor="w", padx=15, pady=18)

        # ===========================
        # Lunch Card
        # ===========================

        self.lunch = ctk.CTkFrame(
            right,
            fg_color="#FFF3E0",
            corner_radius=12,
            height=70
        )

        self.lunch.pack(fill="x", padx=25, pady=6)

        self.lunch_label = ctk.CTkLabel(
            self.lunch,
            text="🍛 Lunch : --",
            font=("Segoe UI",16,"bold"),
            text_color="black",
            anchor="w"
        )

        self.lunch_label.pack(anchor="w", padx=15, pady=18)

        # ===========================
        # Evening Snack Card
        # ===========================

        self.snack = ctk.CTkFrame(
            right,
            fg_color="#F3E5F5",
            corner_radius=12,
            height=70
        )

        self.snack.pack(fill="x", padx=25, pady=6)

        self.snack_label = ctk.CTkLabel(
            self.snack,
            text="☕ Evening Snack : --",
            font=("Segoe UI",16,"bold"),
            text_color="black",
            anchor="w"
        )

        self.snack_label.pack(anchor="w", padx=15, pady=18)
                # ===========================
        # Dinner Card
        # ===========================

        self.dinner = ctk.CTkFrame(
            right,
            fg_color="#E8F5E9",
            corner_radius=12,
            height=70
        )

        self.dinner.pack(fill="x", padx=25, pady=6)

        self.dinner_label = ctk.CTkLabel(
            self.dinner,
            text="🍽️ Dinner : --",
            font=("Segoe UI",16,"bold"),
            text_color="black",
            anchor="w"
        )

        self.dinner_label.pack(anchor="w", padx=15, pady=18)

        # ===========================
        # Water Intake Card
        # ===========================

        self.water = ctk.CTkFrame(
            right,
            fg_color="#E1F5FE",
            corner_radius=12,
            height=60
        )

        self.water.pack(fill="x", padx=25, pady=(12,6))

        self.water_label = ctk.CTkLabel(
            self.water,
            text="💧 Water Intake : --",
            font=("Segoe UI",16,"bold"),
            text_color="black",
            anchor="w"
        )

        self.water_label.pack(anchor="w", padx=15, pady=15)

        # ===========================
        # Health Tip Card
        # ===========================

        self.tip = ctk.CTkFrame(
            right,
            fg_color="#FFFDE7",
            corner_radius=12,
            height=80
        )

        self.tip.pack(fill="x", padx=25, pady=(6,20))

        self.tip_label = ctk.CTkLabel(
            self.tip,
            text="❤️ Health Tip : Generate a meal plan to receive a health tip.",
            font=("Segoe UI",16,"bold"),
            text_color="black",
            justify="left",
            wraplength=700,
            anchor="w"
        )

        self.tip_label.pack(anchor="w", padx=15, pady=18)

    # ==========================================
    # Generate Meal Plan
    # ==========================================
    def generate_plan(self):

        from services.meal_services import generate_meal_plan

        diabetes = self.diabetes.get()
        preference = self.preference.get()

        plan = generate_meal_plan(diabetes, preference)

        self.breakfast_label.configure(
            text=f"🥣 Breakfast : {plan['Breakfast']}"
        )

        self.lunch_label.configure(
            text=f"🍛 Lunch : {plan['Lunch']}"
        )

        self.snack_label.configure(
            text=f"☕ Evening Snack : {plan['Snack']}"
        )

        self.dinner_label.configure(
            text=f"🍽️ Dinner : {plan['Dinner']}"
        )

        self.water_label.configure(
            text=f"💧 Water Intake : {plan['Water']}"
        )

        self.tip_label.configure(
            text=f"❤️ Health Tip : {plan['Tip']}"
        )
        

    # ==========================================
    # Clear Data
    # ==========================================

    def clear_data(self):

        self.age_entry.delete(0, "end")

        self.gender.set("Male")

        self.diabetes.set("Prediabetes")

        self.preference.set("Vegetarian")

        self.breakfast_label.configure(
            text="🥣 Breakfast : --"
        )

        self.lunch_label.configure(
            text="🍛 Lunch : --"
        )

        self.snack_label.configure(
            text="☕ Evening Snack : --"
        )

        self.dinner_label.configure(
            text="🍽️ Dinner : --"
        )

        self.water_label.configure(
            text="💧 Water Intake : --"
        )

        self.tip_label.configure(
            text="❤️ Health Tip : Generate a meal plan to receive a health tip."
        )

    # ==========================================
    # Back
    # ==========================================

    def go_back(self):

        self.destroy()

        self.parent.deiconify()