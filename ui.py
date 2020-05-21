import sys
from PyQt5.QtWidgets import QApplication,QWidget,QComboBox,QHBoxLayout,QVBoxLayout,QLabel,QFormLayout,QPushButton,QTextEdit

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("KSI")
        self.init_ui()

    def init_ui(self):
        f_box1=QFormLayout()
        f_box2=QFormLayout()
        v_box=QVBoxLayout()
        h_box=QHBoxLayout()

        self.start_point=QLabel("Kalkış İskelesi seçin")
        self.scaffoldings=QComboBox()
        self.scaffoldings.addItem("İzmit")
        self.scaffoldings.addItem("Gölcük")
        self.scaffoldings.addItem("Değirmendere")
        self.scaffoldings.addItem("Karamürsel")
        self.scaffoldings.addItem("Yarımca")
        self.scaffoldings.addItem("Tütün Çiftlik") #Yazım doğru mu ?
        self.scaffoldings.addItem("Derince")


        self.take_button=QPushButton("Götür")
        self.take_button.clicked.connect(self.take)
        self.text_area=QTextEdit()

        self.finish_point=QLabel("Varış İskelesi seçin")



        self.scaffoldings2=QComboBox()
        self.scaffoldings2.addItem("İzmit")
        self.scaffoldings2.addItem("Gölcük")
        self.scaffoldings2.addItem("Değirmendere")
        self.scaffoldings2.addItem("Karamürsel")
        self.scaffoldings2.addItem("Yarımca")
        self.scaffoldings2.addItem("Tütün Çiftlik") #Yazım doğru mu ?
        self.scaffoldings2.addItem("Derince")

        f_box1.addWidget(self.start_point)
        f_box1.addWidget(self.scaffoldings)


        v_box.addStretch()
        v_box.addWidget(self.text_area)
        v_box.addWidget(self.take_button)


        f_box2.addWidget(self.finish_point)
        f_box2.addWidget(self.scaffoldings2)


        h_box.addLayout(f_box1)
        h_box.addLayout(v_box)
        h_box.addLayout(f_box2)
        self.setLayout(h_box)


        self.show()





    def take(self):
        self.text_area.setText("Güzergah yazımı")
        

app=QApplication(sys.argv)
window=window()
sys.exit(app.exec_())
