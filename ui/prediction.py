import customtkinter as ctk
from services.prediction_service import predict_diabetes


class PredictionWindow(ctk.CTk):

    def __init__(self, home_page):
        super().__init__()

        self.home_page = home_page

        self.title("DiaCare AI - Diabetes Prediction")
        self.state("zoomed")
        self.configure(fg_color="#EEF3F8")

        self.protocol("WM_DELETE_WINDOW", self.go_back)

        self.create_header()
        self.create_body()

    # --------------------------------------------------

    def create_header(self):

        header = ctk.CTkFrame(
            self,
            height=90,
            fg_color="#2563EB",
            corner_radius=0
        )
        header.pack(fill="x")

        back = ctk.CTkButton(
            header,
            text="← Back",
            width=110,
            command=self.go_back
        )
        back.place(x=20, y=25)

        ctk.CTkLabel(
            header,
            text="Diabetes Prediction",
            font=("Arial", 30, "bold"),
            text_color="white"
        ).pack(pady=22)

    # --------------------------------------------------

    def create_body(self):

        container = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        container.pack(fill="both", expand=True, padx=20, pady=20)

        # LEFT PANEL (Scrollable)
        left = ctk.CTkScrollableFrame(
            container,
            width=420,
            fg_color="white",
            corner_radius=15
        )
        left.pack(side="left", fill="both", padx=(0, 20), pady=5)

        # RIGHT PANEL
        self.result_frame = ctk.CTkFrame(
            container,
            fg_color="white",
            corner_radius=15
        )
        self.result_frame.pack(
            side="right",
            fill="both",
            expand=True
        )

        ctk.CTkLabel(
            left,
            text="Patient Information",
            font=("Arial", 24, "bold")
        ).pack(pady=(15, 25))

        self.entries = {}

        fields = [
            ("Pregnancies", "preg"),
            ("Glucose", "glu"),
            ("Blood Pressure", "bp"),
            ("Skin Thickness", "skin"),
            ("Insulin", "ins"),
            ("BMI", "bmi"),
            ("Diabetes Pedigree Function", "dpf"),
            ("Age", "age")
        ]

        for text, key in fields:

            ctk.CTkLabel(
                left,
                text=text,
                font=("Arial", 16, "bold")
            ).pack(anchor="w", padx=20, pady=(8, 3))

            entry = ctk.CTkEntry(
                left,
                width=350,
                height=42,
                placeholder_text=f"Enter {text}"
            )

            entry.pack(padx=20, pady=(0, 10))

            self.entries[key] = entry

        ctk.CTkButton(
            left,
            text="Predict",
            width=320,
            height=45,
            fg_color="#16A34A",
            hover_color="#15803D",
            command=self.predict
        ).pack(pady=(15, 10))

        ctk.CTkButton(
            left,
            text="Clear",
            width=320,
            height=45,
            fg_color="#2563EB",
            hover_color="#1D4ED8",
            command=self.clear_inputs
        ).pack(pady=(0, 20))

        self.show_default_result()

        # --------------------------------------------------
    # PREDICT
    # --------------------------------------------------

    def predict(self):

        try:

            pregnancies = float(self.entries["preg"].get())
            glucose = float(self.entries["glu"].get())
            blood_pressure = float(self.entries["bp"].get())
            skin_thickness = float(self.entries["skin"].get())
            insulin = float(self.entries["ins"].get())
            bmi = float(self.entries["bmi"].get())
            dpf = float(self.entries["dpf"].get())
            age = float(self.entries["age"].get())

        except ValueError:

            self.show_result(
                "❌ Invalid Input",
                "Please enter valid numeric values in all fields.",
                "#DC2626"
            )
            return

        result, confidence = predict_diabetes(
            pregnancies,
            glucose,
            blood_pressure,
            skin_thickness,
            insulin,
            bmi,
            dpf,
            age
        )

        if result == "Diabetic":
            title = "⚠ Diabetes Detected"
            color = "#DC2626"
        else:
            title = "✅ Non-Diabetic"
            color = "#16A34A"

        message = (
            f"Prediction : {result}\n\n"
            f"Confidence : {confidence}%"
        )

        self.show_result(title, message, color)

    # --------------------------------------------------
    # RESULT
    # --------------------------------------------------

    def show_result(self, title, message, color):

        for widget in self.result_frame.winfo_children():
            widget.destroy()

        card = ctk.CTkFrame(
            self.result_frame,
            fg_color="white",
            corner_radius=20
        )
        card.pack(fill="both", expand=True, padx=30, pady=30)

        ctk.CTkLabel(
            card,
            text=title,
            font=("Arial", 30, "bold"),
            text_color=color
        ).pack(pady=(70, 20))

        ctk.CTkLabel(
            card,
            text=message,
            font=("Arial", 22),
            justify="center"
        ).pack()

        ctk.CTkLabel(
            card,
            text="DiaCare AI",
            font=("Arial", 16),
            text_color="gray"
        ).pack(side="bottom", pady=25)

    # --------------------------------------------------
    # DEFAULT RESULT
    # --------------------------------------------------

    def show_default_result(self):

        for widget in self.result_frame.winfo_children():
            widget.destroy()

        card = ctk.CTkFrame(
            self.result_frame,
            fg_color="white",
            corner_radius=20
        )

        card.pack(fill="both", expand=True, padx=30, pady=30)

        ctk.CTkLabel(
            card,
            text="🩺 Diabetes Prediction",
            font=("Arial", 30, "bold"),
            text_color="#2563EB"
        ).pack(pady=(70, 20))

        ctk.CTkLabel(
            card,
            text="Fill all patient details\nand click Predict.",
            font=("Arial", 22),
            justify="center"
        ).pack()

        ctk.CTkLabel(
            card,
            text="Powered by Machine Learning",
            font=("Arial", 16),
            text_color="gray"
        ).pack(side="bottom", pady=25)

    # --------------------------------------------------
    # CLEAR
    # --------------------------------------------------

    def clear_inputs(self):

        for entry in self.entries.values():
            entry.delete(0, "end")

        self.show_default_result()

    # --------------------------------------------------
    # BACK
    # --------------------------------------------------

    def go_back(self):

        self.destroy()

        if self.home_page is not None:
            self.home_page.deiconify()
            self.home_page.state("zoomed")