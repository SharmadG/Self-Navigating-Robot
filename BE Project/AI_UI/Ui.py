import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import QTimer, QTime, Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Set the display dimensions
        display_width = 480
        display_height = 320

        # Set the window size and title
        self.resize(display_width, display_height)
        self.setWindowTitle('Self Navigating AI Robot')

        # Frame 1
        self.frame1 = QLabel(self)
        self.frame1.setGeometry(0, 0, display_width, display_height)
        self.frame1.setStyleSheet('''background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(37, 41, 52, 255), stop:1 rgba(18, 20, 26, 255));''')

        # Group 1
        self.bandyaBut = QPushButton('Use BANDYA', self)
        self.bandyaBut.setGeometry(121, 250, 237, 45)  # Adjusted position for your display
        self.bandyaBut.setFixedSize(237, 45)

        font = QFont()
        font.setFamily('Oswald')
        font.setWeight(400)
        font.setPointSize(20)
        self.bandyaBut.setFont(font)

        self.bandyaBut.setStyleSheet('''
                    QPushButton {
                        color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(144, 247, 236, 255), stop:1 rgba(50, 204, 188, 255));
                        background: transparent;
                        border: none;
                    }
                    QPushButton:hover {
                        color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(50, 204, 188, 255), stop:1 rgba(144, 247, 236, 255));
                    }
                ''')

        # Load and display the image
        self.image_label = QLabel(self)
        image_path = '/AI_UI/pngs/Minion2.png'
        pixmap = QPixmap(image_path)
        # Calculate scaling factor
        scaling_factor = min(display_width / pixmap.width(), display_height / pixmap.height())
        # Scale the pixmap
        scaled_pixmap = pixmap.scaled(int(pixmap.width() * scaling_factor), int(pixmap.height() * scaling_factor), Qt.KeepAspectRatio)
        # Set the scaled pixmap to the image label
        self.image_label.setPixmap(scaled_pixmap)
        # Center the image label
        self.image_label.setGeometry(int((display_width - scaled_pixmap.width()) / 2), int((display_height - scaled_pixmap.height()) / 2), scaled_pixmap.width(), scaled_pixmap.height())

        # Time label
        self.time_label = QLabel(self)
        self.time_label.setGeometry(0, 30, display_width, 71)  # Adjusted position for your display
        font.setPointSize(28)
        self.time_label.setFont(font)
        self.time_label.setAlignment(Qt.AlignCenter)  # Center align the text horizontally
        self.time_label.setStyleSheet('''
                    font-family: 'Oswald';
                    font-style: normal;
                    font-weight: 400;
                    line-height: 71px;
                    color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(144, 247, 236, 255), stop:1 rgba(50, 204, 188, 255));
                ''')

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)  # Update every 1000 milliseconds (1 second)

        # Show the initial time
        self.updateTime()

        self.show()

    def updateTime(self):
        current_time = QTime.currentTime()
        time_str = current_time.toString('h:mm:ss AP')
        self.time_label.setText(time_str)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
