import sys
from socket import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont

class ReceiverThread(QThread):
    received_signal = pyqtSignal(str)

    def __init__(self, ip, port):
        super().__init__()
        self.ip = ip
        self.port = port
        self.is_running = True

    def run(self):
        try:
            server_socket = socket(AF_INET, SOCK_DGRAM)
            server_socket.bind((self.ip, self.port))
            server_socket.settimeout(1.0)
            
            while self.is_running:
                try:
                    data, addr = server_socket.recvfrom(1024)
                    msg = f"[{addr}] {data.decode()}"
                    self.received_signal.emit(msg)
                except timeout:
                    continue
        except Exception as e:
            self.received_signal.emit(f"Error: {e}")
        finally:
            server_socket.close()

    def stop(self):
        self.is_running = False
        self.wait()

class GroundSystemCore(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.thread = None

    def initUI(self):
        self.setWindowTitle("Ground System Core")
        self.setFixedSize(600, 400)
        self.setStyleSheet("background-color: #f0f0f0;")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(30, 20, 30, 20) # 왼쪽, 위, 오른쪽, 아래

        title_label = QLabel("Ground System Core")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Arial", 26))
        title_label.setStyleSheet("margin-bottom: 20px; color: #000;")
        main_layout.addWidget(title_label)

        grid_layout = QGridLayout()
        grid_layout.setSpacing(15)

        ip_label = QLabel("Selected IP Address")
        ip_label.setFont(QFont("Arial", 10))
        grid_layout.addWidget(ip_label, 0, 0)

        self.ip_combo = QComboBox()
        self.ip_combo.addItems(["0.0.0.0"])
        self.ip_combo.setEditable(True)
        self.ip_combo.setStyleSheet("background: white; border: 1px solid #ccc; padding: 5px;")
        grid_layout.addWidget(self.ip_combo, 0, 1)

        port_label = QLabel("Port")
        port_label.setFont(QFont("Arial", 10))
        grid_layout.addWidget(port_label, 0, 2)
        
        self.port_input = QLineEdit("9000")
        self.port_input.setFixedWidth(80)
        self.port_input.setStyleSheet("background: white; border: 1px solid #ccc; padding: 5px;")
        grid_layout.addWidget(self.port_input, 0, 3)

        main_layout.addLayout(grid_layout)
        main_layout.addSpacing(20)

        btn_layout = QHBoxLayout()
        
        self.start_btn = QPushButton("Start Telemetry System")
        self.start_btn.setFixedHeight(120)
        self.start_btn.setFont(QFont("Arial", 12))
        self.start_btn.setStyleSheet("""
            QPushButton { 
                background-color: white; 
                border: 1px solid #bbb; 
                border-radius: 5px; 
            }
            QPushButton:hover { background-color: #e8e8e8; }
        """)
        self.start_btn.clicked.connect(self.toggle_server)
        
        self.log_display = QTextEdit()
        self.log_display.setReadOnly(True)
        self.log_display.setPlaceholderText("Waiting for data...")
        self.log_display.setStyleSheet("background: white; border: 1px solid #ccc; border-radius: 5px; padding: 10px;")
        
        btn_layout.addWidget(self.start_btn, 1)
        btn_layout.addWidget(self.log_display, 1)
        
        main_layout.addLayout(btn_layout)
        main_layout.addSpacing(20)

        bottom_layout = QHBoxLayout()
        
        self.close_btn = QPushButton("Close")
        self.close_btn.setFixedWidth(100)
        self.close_btn.setStyleSheet("background-color: white; border: 1px solid #ccc; padding: 5px;")
        self.close_btn.clicked.connect(self.close)

        bottom_layout.addStretch()
        bottom_layout.addWidget(self.close_btn)
        
        main_layout.addLayout(bottom_layout)

    def toggle_server(self):
        if self.thread is None or not self.thread.isRunning():
            ip = self.ip_combo.currentText()
            port = int(self.port_input.text())
            
            self.thread = ReceiverThread(ip, port)
            self.thread.received_signal.connect(self.update_log)
            self.thread.start()
            
            self.start_btn.setText("Stop Telemetry")
            self.start_btn.setStyleSheet("background-color: #fdd; border: 1px solid #faa; border-radius: 5px;")
            self.update_log(f"Server started on {ip}:{port}")
        else:
            self.thread.stop()
            self.start_btn.setText("Start Telemetry System")
            self.start_btn.setStyleSheet("background-color: white; border: 1px solid #bbb; border-radius: 5px;")
            self.update_log("Server stopped.")

    def update_log(self, text):
        self.log_display.append(text)
        self.log_display.verticalScrollBar().setValue(
            self.log_display.verticalScrollBar().maximum()
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GroundSystemCore()
    window.show()
    sys.exit(app.exec_())
