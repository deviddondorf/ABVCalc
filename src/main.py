from PySide6.QtWidgets import QApplication, QPlainTextEdit, QPushButton, QLCDNumber, QGroupBox, QLabel
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtGui import QDoubleValidator
import os
import sys


BASE_DIR = os.environ.get("ABV_DATA", os.path.dirname(os.path.abspath(__file__)))
UI_PATH = os.path.join(BASE_DIR, "ui", "ABVCalculator.ui")

app = QApplication([])
vali = QDoubleValidator()

uiFile = QFile("ABVCalculator.ui")
uiFile.open(QFile.ReadOnly)
loader = QUiLoader()
window = loader.load(uiFile)

ogInput = window.findChild(QPlainTextEdit, "ogInputBox")
fgInput = window.findChild(QPlainTextEdit, "fgInputBox")
calBtn = window.findChild(QPushButton, "pushButton")
lcd = window.findChild(QLCDNumber, "lcdNumber")
errorBox = window.findChild(QGroupBox, "ErrorBox_2")
errorText = window.findChild(QLabel, "label_7")


#ogInput.setValidator(vali)
errorBox.setVisible(False)



ogValue = 0
fgValue = 0

def on_button_click():

    errorBox.setVisible(False)
    try:
        x = ogInput.toPlainText()
        y = fgInput.toPlainText()
        try:
            ogValue = float(x)
            fgValue = float(y)
        except ValueError:
            print("ValueError")
            ogValue = 0.0
            fgValue = 0.0
    except ValueError:
        errorBox.setVisible(True)
    else:
        resultABV = (ogValue - fgValue) * 131.25
        if resultABV <= 0.0:
            print("ValueError")
            errorBox.setVisible(True)
        else:
            resultABV = (ogValue - fgValue) * 131.25
            print(resultABV)
            if 0.90 <= ogValue <= 1.16 and 0.90 <= fgValue <= 1.16:
             lcd.display(resultABV)    

calBtn.clicked.connect(on_button_click)
window.show()
app.exec()