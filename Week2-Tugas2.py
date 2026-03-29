import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
    QFrame,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class KonversiSuhu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Konversi Suhu")
        self.resize(620, 580)
        self.setup_ui()
        self.set_styles()

    def setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(22)

        # Header
        self.title_label = QLabel("KONVERSI SUHU")
        self.title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        self.title_label.setFont(title_font)
        self.title_label.setFixedHeight(68)
        main_layout.addWidget(self.title_label)

        # Input suhu
        self.label_input = QLabel("Masukkan Suhu (Celsius):")
        self.input_suhu = QLineEdit()
        self.input_suhu.setPlaceholderText("Masukkan angka suhu")
        self.input_suhu.setText("100")

        main_layout.addWidget(self.label_input)
        main_layout.addWidget(self.input_suhu)

        # Tombol konversi
        button_layout = QHBoxLayout()
        button_layout.setSpacing(18)

        self.btn_fahrenheit = QPushButton("Fahrenheit")
        self.btn_kelvin = QPushButton("Kelvin")
        self.btn_reamur = QPushButton("Reamur")

        self.btn_fahrenheit.clicked.connect(self.konversi_fahrenheit)
        self.btn_kelvin.clicked.connect(self.konversi_kelvin)
        self.btn_reamur.clicked.connect(self.konversi_reamur)

        button_layout.addWidget(self.btn_fahrenheit)
        button_layout.addWidget(self.btn_kelvin)
        button_layout.addWidget(self.btn_reamur)

        main_layout.addLayout(button_layout)

        # Hasil
        self.hasil_frame = QFrame()
        self.hasil_frame.setObjectName("hasilFrame")
        hasil_layout = QVBoxLayout()
        hasil_layout.setContentsMargins(24, 24, 24, 24)
        hasil_layout.setSpacing(16)

        self.label_hasil_judul = QLabel("Hasil Konversi:")
        hasil_font = QFont()
        hasil_font.setPointSize(12)
        hasil_font.setBold(True)
        self.label_hasil_judul.setFont(hasil_font)

        self.label_hasil = QLabel("100 Celsius = 212.00 Fahrenheit")
        self.label_hasil.setWordWrap(True)
        self.label_hasil.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        hasil_layout.addWidget(self.label_hasil_judul)
        hasil_layout.addWidget(self.label_hasil)
        self.hasil_frame.setLayout(hasil_layout)

        main_layout.addWidget(self.hasil_frame)
        main_layout.addStretch()

        self.setLayout(main_layout)

    def set_styles(self):
        self.setStyleSheet(
            """
            QWidget {
                background-color: #f3f3f3;
                font-family: Arial;
                font-size: 16px;
                color: #1f2d3d;
            }

            QLabel {
                background: transparent;
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

            QPushButton {
                background-color: #3498db;
                border: none;
                border-radius: 8px;
                padding: 14px 18px;
                color: white;
                font-size: 16px;
                min-height: 34px;
            }

            QPushButton:hover {
                background-color: #2f89c5;
            }

            QPushButton:pressed {
                background-color: #2777ad;
            }

            QLabel#titleHeader {
                background-color: #3498db;
                color: white;
                border-radius: 8px;
                padding: 10px;
            }

            QFrame#hasilFrame {
                background-color: #d8e9f7;
                border-left: 5px solid #0b4f9a;
                border-radius: 8px;
            }
            """
        )
        self.title_label.setObjectName("titleHeader")

    def ambil_input(self):
        teks = self.input_suhu.text().strip()

        if not teks:
            QMessageBox.warning(self, "Validasi", "Input suhu harus diisi.")
            return None

        try:
            return float(teks)
        except ValueError:
            QMessageBox.warning(self, "Validasi", "Input harus berupa angka.")
            return None

    def format_celsius(self, nilai):
        if nilai.is_integer():
            return str(int(nilai))
        return f"{nilai:.2f}"

    def tampilkan_hasil(self, celsius, hasil, satuan_tujuan):
        teks_celsius = self.format_celsius(celsius)
        self.label_hasil.setText(
            f"{teks_celsius} Celsius = {hasil:.2f} {satuan_tujuan}"
        )

    def konversi_fahrenheit(self):
        celsius = self.ambil_input()
        if celsius is None:
            return
        hasil = (celsius * 9 / 5) + 32
        self.tampilkan_hasil(celsius, hasil, "Fahrenheit")

    def konversi_kelvin(self):
        celsius = self.ambil_input()
        if celsius is None:
            return
        hasil = celsius + 273.15
        self.tampilkan_hasil(celsius, hasil, "Kelvin")

    def konversi_reamur(self):
        celsius = self.ambil_input()
        if celsius is None:
            return
        hasil = celsius * 4 / 5
        self.tampilkan_hasil(celsius, hasil, "Reamur")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KonversiSuhu()
    window.show()
    sys.exit(app.exec())
