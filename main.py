import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #navBar
        navbar = QToolBar()
        self.addToolBar(navbar)

        volta_btn = QAction('Voltar', self)
        volta_btn.triggered.connect(self.browser.back)
        navbar.addAction(volta_btn)

        avancar_btn = QAction('Avancar', self)
        avancar_btn.triggered.connect(self.browser.forward)
        navbar.addAction(avancar_btn)

        atualizar_btn = QAction('Atualizar', self)
        atualizar_btn.triggered.connect(self.browser.reload)
        navbar.addAction(atualizar_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navegar_home)
        navbar.addAction(home_btn)

        self.barra_url = QLineEdit()
        self.barra_url.returnPressed.connect(self.navegar_para_url)
        navbar.addWidget(self.barra_url)

        self.browser.urlChanged.connect(self.atualizatUrl)

    def navegar_home(self):
        self.browser.setUrl(QUrl('https://www.google.com/'))

    def navegar_para_url(self):
        url = self.barra_url.text()
        self.browser.setUrl(QUrl(url))
    def atualizatUrl(self, q):
        self.barra_url.setText(q.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName('Meu navegador')
window = MainWindow()
app.exec_()


