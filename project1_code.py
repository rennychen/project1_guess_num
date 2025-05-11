from project1 import Ui_Dialog
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QShortcut
import sys
import random #產生亂數

app = QApplication(sys.argv)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)

ans = start_num = 0
end_num = 100


def page_change():
    ui.stackedWidget.setCurrentIndex(1)
    global ans
    ans = random.randint(1,100)  # 產生 1 到 100 之間的整數
    ui.lineEdit.setFocus()


def guess_num():
    global start_num,end_num
    try:
        num = int(ui.lineEdit.text())
        if num <=0 or num >100:
            ui.label_3.setText("輸入錯誤,請輸入1~100的數字")
            ui.lineEdit.setText("")
        elif num != ans:
            if num > ans:
                end_num = num
                ui.label_3.setText(f"猜錯了!範圍縮小到{start_num}~{end_num}")
                ui.lineEdit.setText("")
            else:
                start_num = num
                ui.label_3.setText(f"猜錯了!範圍縮小到{start_num}~{end_num}")
                ui.lineEdit.setText("")
        else:
            ui.label_3.setText("答對囉!!!!!!")
    except ValueError:
        ui.label_3.setText("輸入錯誤,請輸入數字")
        ui.lineEdit.setText("")

ui.pushButton_4.clicked.connect(page_change)
ui.pushButton_3.clicked.connect(guess_num)
quit_enter1 = QShortcut(QKeySequence("Return"), widget) #return = 主鍵盤的enter 47,48行 按下enter鍵等同於按確認鍵
quit_enter1.activated.connect(guess_num)
quit_enter2 = QShortcut(QKeySequence("Enter"), widget) #enter = 數字鍵盤的enter 47,48行 按下enter鍵等同於按確認鍵
quit_enter2.activated.connect(guess_num)
widget.show()
app.exec_()
