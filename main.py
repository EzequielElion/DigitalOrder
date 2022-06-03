from PyQt5 import uic,QtWidgets


def IniciarCaixa():
    WorkArea.show()
   













app=QtWidgets.QApplication([])
MainPage=uic.loadUi("main page.ui")
WorkArea=uic.loadUi("pagina de caixa.ui")
MainPage.pushButton.clicked.connect(IniciarCaixa)
MainPage.show()
app.exec()