from Disease import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys
from skimage import io, color
from matplotlib import pyplot as plt
import numpy as np
import json

#lightredregion = io.imread('region1.json')
imgky = io.imread('croppednewmap.png')
image = color.rgba2rgb(imgky)

plt.figure(figsize=(8, 8))

class DrawingApp(QMainWindow):
    def __init__(self):
        super().__init__()

        #Initializing widget stuff
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.canvas = CanvasWidget(central_widget)
        layout.addWidget(self.canvas)

        button_layout = QHBoxLayout()

        #Create buttons with their functions
        self.runButton = QPushButton("Run", central_widget)
        self.runButton.clicked.connect(self.run)

        self.diseaseType1Button = QPushButton("DiseaseType1", central_widget)
        #self.rotate_button.clicked.connect(self.rotation)

        self.diseaseType2Button = QPushButton("DiseaseType3", central_widget)
        #self.shear_button.clicked.connect(self.shear)

        self.diseaseType3Button = QPushButton("DiseaseType4", central_widget)
        #self.scale_button.clicked.connect(self.scale)

        #button_layout.addWidget(self.diseaseType0Button)
        button_layout.addWidget(self.diseaseType1Button)
        button_layout.addWidget(self.diseaseType2Button)
        button_layout.addWidget(self.diseaseType3Button)

        #Create text box for input param
        label = QLabel("Enter Disease parameters:", central_widget)

        self.text_box = QLineEdit(central_widget)
        layout.addLayout(button_layout)

        layout.addWidget(label)
        layout.addWidget(self.text_box)

        central_widget.setLayout(layout)
        self.setGeometry(100, 100, 600, 600)


    #Define what you want buttons to do
    def run(self):
        text = self.text_box.text()
        if text:
            param = int(text)
        else:
            param = 0
        self.canvas.turnRed(self, region2, param)

class CanvasWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.rect_drawn = False
        self.points = []

    def turnRed(self, region, param):
        self.region = region
        for i in param:
            for row in region:
                for pixel in row:
                    if np.allclose(pixel, [1,1,1]):
                        pixel[1] = 0
                        pixel[2] = 0
                        pixel[0] = pixel[0] + 0.1
                        plt.imshow(region)
                        plt.show()
                        self.update()

    def paintEvent(self, event):
        if self.rect_drawn:
            #After a button is clicked
            painter = QPainter(self)
            pixmap = QPixmap("region_2.png")
            painter.drawPixmap(self.rect(), pixmap)

        else:
            #Before a button is clicked
            painter = QPainter(self)
            pixmap = QPixmap("out_put_regions\\region_2.png")
            painter.drawPixmap(self.rect(), pixmap)
            

def main():
    app = QApplication(sys.argv)
    window = DrawingApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()