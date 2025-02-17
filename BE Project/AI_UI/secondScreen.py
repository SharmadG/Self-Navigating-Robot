import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QFont, QIcon, QPixmap
from thirdScreen import ThirdScreen  # Import the ThirdScreen class

class SecondScreen(QWidget):
    def __init__(self, first_screen):
        super().__init__()
        self.first_screen = first_screen
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
        self.LButton1 = QPushButton('AI Chatbot', self)
        self.LButton1.setGeometry(51, 99, 0, 0)  # Adjusted position for your display
        self.LButton1.setFixedSize(162, 121)

        self.RButton2 = QPushButton('ML Detection', self)
        self.RButton2.setGeometry(270, 99, 0, 0)  # Adjusted position for your display
        self.RButton2.setFixedSize(162, 121)
        self.RButton2.clicked.connect(self.openThirdScreen)  # Connect ML Detection button click event

        self.backBut = QPushButton(self)
        self.backBut.setGeometry(20, 20, 0, 0)  # Adjusted position for your display
        self.backBut.setFixedSize(30, 30)
        self.backBut.clicked.connect(self.goBackToFirstScreen)  # Connect to the method

        # Set the back button icon
        back_icon_path = 'C:/Users/Admin/Desktop/BE Project/AI_UI/icons/back.png'  # Ensure this file is in the same directory or provide the correct path
        back_icon = QIcon(QPixmap(back_icon_path))
        if not QPixmap(back_icon_path).isNull():
            self.backBut.setIcon(back_icon)
            self.backBut.setIconSize(self.backBut.size())
        else:
            print(f"Error: Image at path {back_icon_path} not found or failed to load.")

        # Apply the stylesheet to LButton1 and RButton2
        self.LButton1.setStyleSheet("""
            QPushButton {
                color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(144, 247, 236, 255), stop:1 rgba(50, 204, 188, 255));
                background: transparent;
                border: 2px solid rgba(144, 247, 236, 255);  /* Border color same as font color */
                border-radius: 10px;  /* Optional: add rounded corners */
            }
            QPushButton:hover {
                color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(50, 204, 188, 255), stop:1 rgba(144, 247, 236, 255));
            }
        """)

        self.RButton2.setStyleSheet("""
            QPushButton {
                color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(144, 247, 236, 255), stop:1 rgba(50, 204, 188, 255));
                background: transparent;
                border: 2px solid rgba(144, 247, 236, 255);  /* Border color same as font color */
                border-radius: 10px;  /* Optional: add rounded corners */
            }
            QPushButton:hover {
                color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(50, 204, 188, 255), stop:1 rgba(144, 247, 236, 255));
            }
        """)

        self.backBut.setStyleSheet("""
            QPushButton {
                background-color: rgba(144, 247, 236, 255);  /* Set background color same as border color */
                border: 2px solid rgba(144, 247, 236, 255);  /* Border color same as font color */
                border-radius: 15px;  /* Adjust border-radius to create rounded corners */
            }
        """)

        font = QFont()
        font.setFamily('Oswald')
        font.setWeight(400)
        font.setPointSize(15)
        self.LButton1.setFont(font)
        self.RButton2.setFont(font)
        self.backBut.setFont(font)


        self.show()

    def goBackToFirstScreen(self):
        self.first_screen.show()
        self.close()

    def openThirdScreen(self):
        if hasattr(self, 'third_screen') and isinstance(self.third_screen, ThirdScreen):
            self.third_screen.show()
        else:
            self.third_screen = ThirdScreen(self)
            self.third_screen.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SecondScreen(None)  # Pass None since this is standalone testing
    sys.exit(app.exec_())
