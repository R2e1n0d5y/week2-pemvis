import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QComboBox,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
    QFrame,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class FormBiodataMahasiswa(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Biodata Mahasiswa")
        self.resize(620, 760)
        self.setup_ui()
        self.set_styles()

    def setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(18)

        # Judul
        title = QLabel("Form Biodata Mahasiswa")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # Input Nama
        self.label_nama = QLabel("Nama Lengkap:")
        self.input_nama = QLineEdit()
        self.input_nama.setPlaceholderText("Masukkan nama lengkap")
        self.input_nama.setText("Muhammad Rendi Maulana")

        # Input NIM
        self.label_nim = QLabel("NIM:")
        self.input_nim = QLineEdit()
        self.input_nim.setPlaceholderText("Masukkan NIM")
        self.input_nim.setText("F1D02310081")

        # Input Kelas
        self.label_kelas = QLabel("Kelas:")
        self.input_kelas = QLineEdit()
        self.input_kelas.setPlaceholderText("Contoh: Informatika-D")
        self.input_kelas.setText("D201")

        # ComboBox Jenis Kelamin
        self.label_jk = QLabel("Jenis Kelamin:")
        self.combo_jk = QComboBox()
        self.combo_jk.addItems(["Laki-laki", "Perempuan"])
        self.combo_jk.setPlaceholderText("Pilih jenis kelamin")
        self.combo_jk.setCurrentIndex(0)

        # Tambahkan ke layout
        main_layout.addWidget(self.label_nama)
        main_layout.addWidget(self.input_nama)

        main_layout.addWidget(self.label_nim)
        main_layout.addWidget(self.input_nim)

        main_layout.addWidget(self.label_kelas)
        main_layout.addWidget(self.input_kelas)

        main_layout.addWidget(self.label_jk)
        main_layout.addWidget(self.combo_jk)

        # Tombol
        button_layout = QHBoxLayout()
        button_layout.setSpacing(14)

        self.btn_tampilkan = QPushButton("Tampilkan")
        self.btn_reset = QPushButton("Reset")

        self.btn_tampilkan.clicked.connect(self.tampilkan_data)
        self.btn_reset.clicked.connect(self.reset_form)

        button_layout.addWidget(self.btn_tampilkan)
        button_layout.addWidget(self.btn_reset)
        button_layout.addStretch()

        main_layout.addLayout(button_layout)

        # Area hasil
        self.hasil_frame = QFrame()
        self.hasil_frame.setObjectName("hasilFrame")
        hasil_layout = QVBoxLayout()
        hasil_layout.setContentsMargins(20, 20, 20, 20)
        hasil_layout.setSpacing(12)

        self.label_hasil_judul = QLabel("DATA BIODATA")
        judul_font = QFont()
        judul_font.setPointSize(12)
        judul_font.setBold(True)
        self.label_hasil_judul.setFont(judul_font)

        self.label_hasil = QLabel("Data belum ditampilkan.")
        self.label_hasil.setWordWrap(True)
        self.label_hasil.setAlignment(Qt.AlignTop | Qt.AlignLeft)

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

            QLineEdit, QComboBox {
                background-color: #dfeadf;
                border: 1px solid #65c46a;
                border-radius: 10px;
                padding: 12px 14px;
                min-height: 28px;
                font-size: 16px;
            }

            QLineEdit:focus, QComboBox:focus {
                border: 2px solid #48b85a;
            }

            QPushButton {
                border: none;
                border-radius: 8px;
                padding: 12px 24px;
                color: white;
                font-weight: bold;
                min-width: 110px;
            }

            QPushButton#btnTampilkan {
                background-color: #3498db;
            }

            QPushButton#btnReset {
                background-color: #95a5a6;
            }

            QFrame#hasilFrame {
                background-color: #d9ead9;
                border-left: 5px solid #2fad53;
                border-radius: 10px;
            }
            """
        )

        self.btn_tampilkan.setObjectName("btnTampilkan")
        self.btn_reset.setObjectName("btnReset")

    def tampilkan_data(self):
        nama = self.input_nama.text().strip()
        nim = self.input_nim.text().strip()
        kelas = self.input_kelas.text().strip()
        jenis_kelamin = self.combo_jk.currentText().strip()

        if not nama or not nim or not kelas or not jenis_kelamin:
            QMessageBox.warning(
                self,
                "Validasi",
                "Semua field harus diisi terlebih dahulu.",
            )
            return

        hasil = (
            f"Nama: {nama}\n"
            f"NIM: {nim}\n"
            f"Kelas: {kelas}\n"
            f"Jenis Kelamin: {jenis_kelamin}"
        )
        self.label_hasil.setText(hasil)

    def reset_form(self):
        self.input_nama.clear()
        self.input_nim.clear()
        self.input_kelas.clear()
        self.combo_jk.setCurrentIndex(-1)
        self.label_hasil.setText("Data belum ditampilkan.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormBiodataMahasiswa()
    window.show()
    sys.exit(app.exec())