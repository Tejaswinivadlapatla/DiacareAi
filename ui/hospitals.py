import customtkinter as ctk
import threading
import webbrowser
from PIL import Image

from services.hospital_service import search_hospitals


class HospitalWindow(ctk.CTk):

    def __init__(self, home_page):
        super().__init__()

        self.home_page = home_page

        self.title("DiaCare AI - Nearby Hospitals")
        self.state("zoomed")
        self.configure(fg_color="#EEF3F8")

        self.protocol("WM_DELETE_WINDOW", self.go_back)

        self.create_header()

        self.create_top_section()

        self.create_result_section()

    # =====================================================
    # HEADER
    # =====================================================

    def create_header(self):

        header = ctk.CTkFrame(
            self,
            height=90,
            fg_color="#2563EB",
            corner_radius=0
        )

        header.pack(fill="x")

        back_btn = ctk.CTkButton(
            header,
            text="← Back",
            width=110,
            height=42,
            fg_color="white",
            text_color="#2563EB",
            hover_color="#E5E7EB",
            command=self.go_back
        )

        back_btn.place(x=20, y=23)

        title = ctk.CTkLabel(
            header,
            text="Nearby Diabetes Hospitals",
            font=("Arial", 30, "bold"),
            text_color="white"
        )

        title.pack(pady=22)

    # =====================================================
    # TOP SECTION
    # =====================================================

    def create_top_section(self):

        container = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        container.pack(fill="x", padx=25, pady=15)

        # ---------------- LEFT PANEL ----------------

        left = ctk.CTkFrame(
            container,
            width=430,
            height=420,
            fg_color="transparent"
        )

        left.pack(side="left", padx=20)
        left.pack_propagate(False)

        ctk.CTkLabel(
            left,
            text="Enter City",
            font=("Arial", 20, "bold")
        ).pack(anchor="w", pady=(15, 10))

        self.city_entry = ctk.CTkEntry(
            left,
            width=380,
            height=45,
            placeholder_text="Enter city..."
        )

        self.city_entry.pack(anchor="w")

        self.search_button = ctk.CTkButton(
            left,
            text="Search",
            width=180,
            height=45,
            fg_color="#22C55E",
            hover_color="#16A34A",
            command=self.search
        )

        self.search_button.pack(
            pady=25
        )

        self.status = ctk.CTkLabel(
            left,
            text="",
            font=("Arial", 16),
            text_color="#15803D"
        )

        self.status.pack()

        # ---------------- RIGHT PANEL ----------------

        right = ctk.CTkFrame(
            container,
            fg_color="white",
            corner_radius=15
        )

        right.pack(
            side="right",
            padx=10,
            fill="both",
            expand=True
        )

        # If you have hospital_banner.png keep this.
        # Otherwise we'll replace it with an emoji later.

        try:

            image = ctk.CTkImage(
                light_image=Image.open("assets/hospital_banner.png"),
                size=(900, 470)
            )

            label = ctk.CTkLabel(
                right,
                image=image,
                text=""
            )

            label.image = image
            label.pack(
                fill="both",
                expand=True
            )

        except Exception:

            ctk.CTkLabel(
                right,
                text="🏥",
                font=("Arial", 120)
            ).pack(expand=True)

    # =====================================================
    # RESULT SECTION
    # =====================================================

    def create_result_section(self):

        self.result_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="#EEF3F8"
        )

        self.result_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

    # =====================================================
    # SEARCH BUTTON
    # =====================================================

    def search(self):

        city = self.city_entry.get().strip()

        if city == "":

            self.status.configure(
                text="Please enter a city.",
                text_color="red"
            )

            return

        self.search_button.configure(
            state="disabled"
        )

        self.status.configure(
            text="Searching hospitals...",
            text_color="green"
        )

        threading.Thread(
            target=self.search_thread,
            args=(city,),
            daemon=True
        ).start()
        # =====================================================
    # SEARCH THREAD
    # =====================================================

    def search_thread(self, city):

        hospitals = search_hospitals(city)

        # Update UI only from the main Tkinter thread
        self.after(0, lambda: self.display_results(hospitals))

    # =====================================================
    # DISPLAY RESULTS
    # =====================================================

    def display_results(self, hospitals):

        self.search_button.configure(state="normal")

        for widget in self.result_frame.winfo_children():
            widget.destroy()

        if len(hospitals) == 0:

            self.status.configure(
                text="No hospitals found.",
                text_color="red"
            )

            empty = ctk.CTkLabel(
                self.result_frame,
                text="No hospitals found near this city.",
                font=("Arial", 20, "bold")
            )

            empty.pack(pady=40)

            return

        self.status.configure(
            text=f"{len(hospitals)} Hospitals Found",
            text_color="#15803D"
        )

        for hospital in hospitals:

            card = ctk.CTkFrame(
                self.result_frame,
                fg_color="white",
                corner_radius=15,
                border_width=1,
                border_color="#D1D5DB"
            )

            card.pack(
                fill="x",
                padx=10,
                pady=12
            )

            # ---------------- Hospital Name ----------------

            title = ctk.CTkLabel(
                card,
                text="🏥  " + hospital["name"],
                font=("Arial", 22, "bold"),
                anchor="w"
            )

            title.pack(
                anchor="w",
                padx=20,
                pady=(15, 8)
            )

            # ---------------- Hospital Type ----------------

            if hospital["type"] == "Diabetes Care":
                badge_color = "#16A34A"
            else:
                badge_color = "#2563EB"

            badge = ctk.CTkLabel(
                card,
                text=hospital["type"],
                width=160,
                height=30,
                fg_color=badge_color,
                text_color="white",
                corner_radius=15,
                font=("Arial", 13, "bold")
            )

            badge.pack(
                anchor="w",
                padx=20
            )

            # ---------------- Address ----------------

            address = ctk.CTkLabel(
                card,
                text="📍 " + hospital["address"],
                wraplength=900,
                justify="left",
                font=("Arial", 15)
            )

            address.pack(
                anchor="w",
                padx=20,
                pady=(12, 6)
            )

            # ---------------- Distance ----------------

            distance = ctk.CTkLabel(
                card,
                text=f"🚗 Distance : {hospital['distance']} km",
                font=("Arial", 15, "bold"),
                text_color="#0F766E"
            )

            distance.pack(
                anchor="w",
                padx=20,
                pady=(0, 10)
            )

            # ---------------- Buttons ----------------

            button_frame = ctk.CTkFrame(
                card,
                fg_color="transparent"
            )

            button_frame.pack(
                fill="x",
                padx=20,
                pady=(0, 15)
            )

            maps_btn = ctk.CTkButton(
                button_frame,
                text="📍 Open in Google Maps",
                width=220,
                height=38,
                fg_color="#2563EB",
                hover_color="#1D4ED8",
                command=lambda url=hospital["maps_url"]: webbrowser.open(url)
            )

            maps_btn.pack(side="right")

        # =====================================================
    # BACK BUTTON
    # =====================================================

    def go_back(self):

        try:
            self.destroy()

            if self.home_page is not None:
                self.home_page.deiconify()
                self.home_page.state("zoomed")

        except Exception as e:
            print("Back Error :", e)

    # =====================================================
    # WINDOW CLOSE
    # =====================================================

    def on_close(self):

        try:
            self.destroy()

        except:
            pass

    # =====================================================
    # CLEAR RESULTS
    # =====================================================

    def clear_results(self):

        for widget in self.result_frame.winfo_children():
            widget.destroy()

    # =====================================================
    # SHOW ERROR MESSAGE
    # =====================================================

    def show_error(self, message):

        self.clear_results()

        self.status.configure(
            text=message,
            text_color="red"
        )

        error_frame = ctk.CTkFrame(
            self.result_frame,
            fg_color="white",
            corner_radius=15
        )

        error_frame.pack(
            fill="x",
            padx=10,
            pady=25
        )

        ctk.CTkLabel(
            error_frame,
            text="❌",
            font=("Arial", 50)
        ).pack(pady=(20, 10))

        ctk.CTkLabel(
            error_frame,
            text=message,
            font=("Arial", 20, "bold")
        ).pack(pady=(0, 20))

    # =====================================================
    # SHOW LOADING
    # =====================================================

    def show_loading(self):

        self.clear_results()

        loading = ctk.CTkFrame(
            self.result_frame,
            fg_color="white",
            corner_radius=15
        )

        loading.pack(
            fill="x",
            padx=10,
            pady=30
        )

        ctk.CTkLabel(
            loading,
            text="🔍 Searching Nearby Hospitals...",
            font=("Arial", 22, "bold"),
            text_color="#2563EB"
        ).pack(pady=40)

    # =====================================================
    # END OF CLASS
    # =====================================================