import customtkinter as ctk
from PIL import Image
from services.nutrition_service import get_nutrition


class NutritionWindow(ctk.CTkToplevel):

    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.title("Nutrition Analyzer")
        self.geometry("1250x720")
        self.configure(fg_color="#F4F6F9")

        self.protocol("WM_DELETE_WINDOW", self.go_back)

        self.create_ui()

    def create_ui(self):

        # ================= HEADER =================

        header = ctk.CTkFrame(
            self,
            height=70,
            fg_color="#4CAF50",
            corner_radius=0
        )
        header.pack(fill="x")

        ctk.CTkLabel(
            header,
            text="🥗 Nutrition Analyzer",
            font=("Segoe UI", 30, "bold")
        ).pack(pady=18)

        # ================= MAIN ==================

        main = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        main.pack(fill="both", expand=True, padx=20, pady=20)

        # ================= LEFT PANEL =================

        left = ctk.CTkFrame(
            main,
            width=300,
            corner_radius=18,
            fg_color="#35722C"
        )
        left.pack(side="left", fill="y", padx=(0,20))
        left.pack_propagate(False)

        ctk.CTkLabel(
            left,
            text="Enter Food Name",
            font=("Segoe UI",20,"bold")
        ).pack(pady=(35,15))

        self.food_entry = ctk.CTkEntry(
            left,
            width=220,
            height=42,
            placeholder_text="Apple"
        )
        self.food_entry.pack()

        ctk.CTkButton(
            left,
            text="🔍 Analyze",
            width=220,
            height=42,
            command=self.analyze_food
        ).pack(pady=25)

        ctk.CTkButton(
            left,
            text="🧹 Clear",
            width=220,
            height=42,
            fg_color="#22E681",
            hover_color="#CA6F1E",
            command=self.clear_data
        ).pack()

        ctk.CTkButton(
            left,
            text="⬅ Back",
            width=220,
            height=42,
            fg_color="#19B6EA",
            hover_color="#DCFAFA",
            command=self.go_back
        ).pack(pady=20)

        # ================= RIGHT PANEL =================

        self.right = ctk.CTkFrame(
            main,
            corner_radius=18,
            fg_color="#2EBA12"
        )
        self.right.pack(side="right", fill="both", expand=True)

        # ================= Banner =================

        try:

            image = Image.open("assets/food_banner.jpg")

            self.banner_img = ctk.CTkImage(
                light_image=image,
                dark_image=image,
                size=(760,180)
            )

            ctk.CTkLabel(
                self.right,
                image=self.banner_img,
                text=""
            ).pack(pady=15)

        except:

            ctk.CTkLabel(
                self.right,
                text="🥗 Healthy Nutrition",
                font=("Segoe UI",28,"bold")
            ).pack(pady=40)

        # ================= Food Name =================

        self.food_name = ctk.CTkLabel(
            self.right,
            text="Food Name : -",
            font=("Segoe UI",22,"bold")
        )

        self.food_name.pack(anchor="w", padx=30)

        # ================= Result Box =================

        self.result = ctk.CTkTextbox(
            self.right,
            width=760,
            height=270,
            font=("Consolas",18)
        )

        self.result.pack(padx=25,pady=20)

        self.result.insert(
            "0.0",
            "Search any food to view nutrition information."
        )

        # ================= Recommendation =================

        self.recommend = ctk.CTkLabel(
            self.right,
            text="🟢 Recommendation will appear here.",
            font=("Segoe UI",18,"bold"),
            text_color="#7DFF9B"
        )

        self.recommend.pack(anchor="w", padx=30)

        # ================= Score =================

        self.score = ctk.CTkLabel(
            self.right,
            text="⭐ Nutrition Score : -- / 10",
            font=("Segoe UI",20,"bold"),
            text_color="#FFD700"
        )

        self.score.pack(anchor="w", padx=30, pady=10)

            # ==========================
    # Analyze Food
    # ==========================

    def analyze_food(self):

        food = self.food_entry.get().strip()

        if food == "":
            self.result.delete("0.0", "end")
            self.result.insert("0.0", "Please enter a food name.")
            return

        data = get_nutrition(food)

        if data is None:
            self.food_name.configure(text="Food Name : Not Found")

            self.result.delete("0.0", "end")
            self.result.insert(
                "0.0",
                "❌ Food not found in the dataset.\n\nTry another food."
            )

            self.recommend.configure(
                text="🔴 Recommendation : Food not available.",
                text_color="red"
            )

            self.score.configure(
                text="⭐ Nutrition Score : -- / 10"
            )

            return

        self.food_name.configure(
            text=f"Food Name : {data['Food']}"
        )

        info = f"""
🔥 Calories          : {data['Calories']} kcal

🥩 Protein           : {data['Protein']} g

🍚 Carbohydrates     : {data['Carbohydrates']} g

🥑 Fat               : {data['Fat']} g

🍬 Sugar             : {data['Sugar']} g

🌾 Fiber             : {data['Fiber']} g

❤️ Cholesterol       : {data['Cholesterol']} mg

🧂 Sodium            : {data['Sodium']} mg
"""

        self.result.delete("0.0", "end")
        self.result.insert("0.0", info)

        # ----------------------------
        # Recommendation
        # ----------------------------

        calories = float(data["Calories"])
        fat = float(data["Fat"])
        sugar = float(data["Sugar"])

        if calories < 150 and fat < 5 and sugar < 10:

            recommendation = "🟢 Healthy choice for most people."
            color = "#00C853"
            score = "⭐ Nutrition Score : 9.5 / 10"

        elif calories < 300:

            recommendation = "🟡 Consume in moderation."
            color = "#F9A825"
            score = "⭐ Nutrition Score : 7.5 / 10"

        else:

            recommendation = "🔴 High calorie food. Consume occasionally."
            color = "#E53935"
            score = "⭐ Nutrition Score : 5.5 / 10"

        self.recommend.configure(
            text=recommendation,
            text_color=color
        )

        self.score.configure(
            text=score
        )

    # ==========================
    # Clear
    # ==========================

    def clear_data(self):

        self.food_entry.delete(0, "end")

        self.food_name.configure(
            text="Food Name : -"
        )

        self.result.delete("0.0", "end")
        self.result.insert(
            "0.0",
            "Search any food to view nutrition information."
        )

        self.recommend.configure(
            text="🟢 Recommendation will appear here.",
            text_color="#7DFF9B"
        )

        self.score.configure(
            text="⭐ Nutrition Score : -- / 10"
        )

    # ==========================
    # Back
    # ==========================

    def go_back(self):

        self.destroy()

        self.parent.deiconify()