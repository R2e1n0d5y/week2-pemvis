import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QCheckBox, QFrame
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class FormLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.resize(500, 620)
        self.setup_ui()
        self.set_styles()

    def setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(20)

        # Header
        self.title_label = QLabel("LOGIN")
        self.title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        self.title_label.setFont(title_font)
        self.title_label.setFixedHeight(70)

        # Username
        self.label_username = QLabel("Username:")
        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText("Masukkan username")

        # Password
        self.label_password = QLabel("Password:")
        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Masukkan password")
        self.input_password.setEchoMode(QLineEdit.Password)

        # Checkbox tampilkan password
        self.checkbox_show = QCheckBox("Tampilkan Password")
        self.checkbox_show.toggled.connect(self.toggle_password)

        # Tombol
        button_layout = QHBoxLayout()
        button_layout.setSpacing(15)

        self.btn_login = QPushButton("Login")
        self.btn_reset = QPushButton("Reset")

        self.btn_login.clicked.connect(self.proses_login)
        self.btn_reset.clicked.connect(self.reset_form)

        button_layout.addWidget(self.btn_login)
        button_layout.addWidget(self.btn_reset)

        # Area pesan
        self.message_frame = QFrame()
        self.message_frame.setObjectName("messageFrame")
        message_layout = QVBoxLayout()
        message_layout.setContentsMargins(18, 18, 18, 18)

        self.label_message = QLabel("Silakan masukkan username dan password.")
        self.label_message.setWordWrap(True)
        self.label_message.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        message_layout.addWidget(self.label_message)
        self.message_frame.setLayout(message_layout)

        # Susun layout
        main_layout.addWidget(self.title_label)
        main_layout.addWidget(self.label_username)
        main_layout.addWidget(self.input_username)
        main_layout.addWidget(self.label_password)
        main_layout.addWidget(self.input_password)
        main_layout.addWidget(self.checkbox_show)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.message_frame)
        main_layout.addStretch()

        self.setLayout(main_layout)

    def set_styles(self):
        self.title_label.setObjectName("titleHeader")
        self.btn_login.setObjectName("btnLogin")
        self.btn_reset.setObjectName("btnReset")

        self.setStyleSheet("""
            QWidget {
                background-color: #f3f3f3;
                font-family: Arial;
                font-size: 16px;
                color: #1f2d3d;
            }

            QLabel {
                background: transparent;
            }

            QLabel#titleHeader {
                background-color: #9b59b6;
                color: white;
                border-radius: 8px;
                padding: 10px;
            }

            QLineEdit {
                background-color: #dfeadf;
                border: 1px solid #65c46a;
                border-radius: 8px;
                padding: 12px 14px;
                min-height: 28px;
                font-size: 16px;
            }

            QLineEdit:focus {
                border: 2px solid #48b85a;
            }

            QCheckBox {
                spacing: 8px;
            }

            QPushButton {
                border: none;
                border-radius: 8px;
                padding: 12px 20px;
                color: white;
                min-width: 120px;
                min-height: 36px;
                font-size: 16px;
            }

            QPushButton#btnLogin {
                background-color: #2eaf5d;
            }

            QPushButton#btnLogin:hover {
                background-color: #27964f;
            }

            QPushButton#btnReset {
                background-color: #95a5a6;
            }

            QPushButton#btnReset:hover {
                background-color: #7f8c8d;
            }

            QFrame#messageFrame {
                background-color: #e8e8e8;
                border-left: 5px solid #bdbdbd;
                border-radius: 8px;
            }
        """)

    def toggle_password(self, checked):
        if checked:
            self.input_password.setEchoMode(QLineEdit.Normal)
        else:
            self.input_password.setEchoMode(QLineEdit.Password)

    def proses_login(self):
        username = self.input_username.text().strip()
        password = self.input_password.text().strip()

        if username == "" or password == "":
            self.tampilkan_pesan(
                "Username dan password harus diisi.",
                "#f8d7da",  # background
                "#dc3545",  # border
                "#842029"   # text
            )
            return

        if username == "admin" and password == "12345":
            self.tampilkan_pesan(
                f"Login berhasil! Selamat datang, {username}.",
                "#d4edda",
                "#28a745",
                "#155724"
            )
            self.input_username.setStyleSheet("")
            self.input_password.setStyleSheet("")
        else:
            self.tampilkan_pesan(
                "Login gagal! Username atau password salah.",
                "#f8d7da",
                "#dc3545",
                "#842029"
            )
            self.input_username.setStyleSheet("""
                background-color: white;
                border: 1px solid #ff5c5c;
                border-radius: 8px;
                padding: 12px 14px;
                min-height: 28px;
                font-size: 16px;
            """)
            self.input_password.setStyleSheet("""
                background-color: white;
                border: 1px solid #ff5c5c;
                border-radius: 8px;
                padding: 12px 14px;
                min-height: 28px;
                font-size: 16px;
            """)

    def tampilkan_pesan(self, pesan, bg_color, border_color, text_color):
        self.label_message.setText(pesan)
        self.label_message.setStyleSheet(f"color: {text_color}; font-size: 16px;")
        self.message_frame.setStyleSheet(f"""
            QFrame#messageFrame {{
                background-color: {bg_color};
                border-left: 5px solid {border_color};
                border-radius: 8px;
            }}
        """)

    def reset_form(self):
        self.input_username.clear()
        self.input_password.clear()
        self.input_password.setEchoMode(QLineEdit.Password)
        self.checkbox_show.setChecked(False)

        self.input_username.setStyleSheet("")
        self.input_password.setStyleSheet("")

        self.label_message.setText("Silakan masukkan username dan password.")
        self.label_message.setStyleSheet("color: #1f2d3d; font-size: 16px;")
        self.message_frame.setStyleSheet("""
            QFrame#messageFrame {
                background-color: #e8e8e8;
                border-left: 5px solid #bdbdbd;
                border-radius: 8px;
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormLogin()
    window.show()
    sys.exit(app.exec())