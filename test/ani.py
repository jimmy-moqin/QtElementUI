from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPalette
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class CustomWidget(QWidget):
    def paintEvent(self, event):
        # Retrieve the final style information
        style = self.style()
        # print style in readable format
        
        palette = self.palette()

        # Capture the desired style properties
        background_color = palette.color(QPalette.Background)
        text_color = palette.color(QPalette.Text)

        # Perform custom painting using the captured style properties
        painter = QPainter(self)
        painter.fillRect(self.rect(), background_color)
        painter.setPen(text_color)
        painter.drawText(self.rect(), Qt.AlignCenter, "Custom Widget")

        # Call the base class paintEvent to ensure standard painting is performed
        super().paintEvent(event)

# Create the application and main window
app = QApplication([])
window = QWidget()

# Set a style sheet for the main window
window.setStyleSheet("QWidget { background-color: lightblue; color: white; }")

# Create a custom widget
custom_widget = CustomWidget()

# Add the custom widget to the main window layout
layout = QVBoxLayout()
layout.addWidget(custom_widget)
window.setLayout(layout)

# Show the main window
window.show()

# Run the application event loop
app.exec()
