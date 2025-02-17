import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from firstScreen import FirstScreen
from secondScreen import SecondScreen

if __name__ == '__main__':
    app = QApplication(sys.argv)

    stacked_widget = QStackedWidget()

    first_screen = FirstScreen(stacked_widget)
    second_screen = SecondScreen()  # Remove the argument here

    stacked_widget.addWidget(first_screen)
    stacked_widget.addWidget(second_screen)

    stacked_widget.setCurrentIndex(0)

    stacked_widget.resize(480, 320)
    stacked_widget.show()

    sys.exit(app.exec_())
