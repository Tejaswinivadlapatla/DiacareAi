import threading
import customtkinter as ctk

from services.chatbot_service import ask_diacare_ai


class ChatbotWindow(ctk.CTkToplevel):

    def __init__(self, home_page):
        super().__init__(home_page)

        self.home_page = home_page
        self.conversation_history = []

        self.title("DiaCare AI Assistant")
        self.geometry("1000x700")
        self.minsize(850, 600)
        self.configure(fg_color="#F5FAF9")

        self.protocol("WM_DELETE_WINDOW", self.go_back)

        self.create_header()
        self.create_chat_area()
        self.create_input_area()

    def create_header(self):

        header = ctk.CTkFrame(
            self,
            fg_color="#07856F",
            corner_radius=0,
            height=95
        )
        header.pack(fill="x")
        back_btn = ctk.CTkButton(
            header,
            text="← Back",
            width=100,
            height=38,
            fg_color="white",
            text_color="#07856F",
            hover_color="#DDF7F2",
            command=self.go_back
        )

        back_btn.place(x=20, y=20)

        ctk.CTkLabel(
            header,
            text=" <-Back 🤖  DiaCare AI Assistant",
            font=("Segoe UI", 26, "bold"),
            text_color="white"
        ).pack(anchor="w", padx=30, pady=(18, 2))

        ctk.CTkLabel(
            header,
            text="Ask general questions about diabetes, food, exercise and healthy habits.",
            font=("Segoe UI", 14),
            text_color="#DDF7F2"
        ).pack(anchor="w", padx=32)

    def create_chat_area(self):

        chat_frame = ctk.CTkFrame(
            self,
            fg_color="white",
            corner_radius=18
        )
        chat_frame.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=25
        )

        self.chat_box = ctk.CTkTextbox(
            chat_frame,
            font=("Segoe UI", 16),
            wrap="word",
            fg_color="white",
            text_color="#213B3F"
        )
        self.chat_box.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        self.chat_box.insert(
            "end",
            "DiaCare AI:\n"
            "Hello! I can provide general information about diabetes, food, "
            "exercise and healthy habits.\n\n"
            "This assistant does not provide a medical diagnosis.\n\n"
        )

        self.chat_box.configure(state="disabled")

    def create_input_area(self):

        input_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        input_frame.pack(fill="x", padx=25, pady=(0, 20))

        self.question_entry = ctk.CTkEntry(
            input_frame,
            height=48,
            font=("Segoe UI", 16),
            placeholder_text="answer your queries here"
        )
        self.question_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 12)
        )

        self.question_entry.bind("<Return>", lambda event: self.send_message())

        self.send_button = ctk.CTkButton(
            input_frame,
            text="Send",
            width=120,
            height=48,
            font=("Segoe UI", 16, "bold"),
            fg_color="#07856F",
            hover_color="#056A59",
            command=self.send_message
        )
        self.send_button.pack(side="right")

        self.status_label = ctk.CTkLabel(
            self,
            text="",
            font=("Segoe UI", 13),
            text_color="#647A7D"
        )
        self.status_label.pack(pady=(0, 12))

    def send_message(self):

        question = self.question_entry.get().strip()

        if not question:
            return

        self.add_message("👤 : You", question)

        self.question_entry.delete(0, "end")
        self.question_entry.configure(state="disabled")
        self.send_button.configure(state="disabled")
        self.status_label.configure(text="DiaCare AI is thinking...")

        worker = threading.Thread(
            target=self.get_ai_response,
            args=(question,),
            daemon=True
        )
        worker.start()

    def get_ai_response(self, question):

        answer = ask_diacare_ai(
            question,
            self.conversation_history
        )

        self.conversation_history.append((question, answer))

        self.after(
            0,
            lambda: self.show_ai_response(answer)
        )

    def show_ai_response(self, answer):

        self.add_message("🤖 DiaCare AI", answer)

        self.question_entry.configure(state="normal")
        self.send_button.configure(state="normal")
        self.status_label.configure(text="")

        self.question_entry.focus()

    def add_message(self, sender, message):

        self.chat_box.configure(state="normal")

        self.chat_box.insert(
            "end",
            f"{sender}:\n{message}\n\n"
        )

        self.chat_box.see("end")
        self.chat_box.configure(state="disabled")

    def go_back(self):

        self.home_page.deiconify()
        self.destroy()