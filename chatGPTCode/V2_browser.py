import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QWebEngineView widget and set its url
        self.view = QWebEngineView(self)
        self.view.setUrl(QUrl('https://www.google.com'))
        self.setCentralWidget(self.view)

        # Create a QLineEdit widget for entering URLs
        self.url_bar = QLineEdit(self)
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.setCentralWidget(self.url_bar)

        # Add the URL bar and the QWebEngineView to the window
        self.setGeometry(50, 50, 800, 600)
        self.setWindowTitle('Qt Web Browser')
        self.show()

    def navigate_to_url(self):
        # Get the URL from the URL bar and navigate to it
        url = self.url_bar.text()
        print(self.view.url())
        if not url.startswith('http'):
            url = 'http://' + url
        self.view.setUrl(QUrl(url))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = Browser()
    sys.exit(app.exec_())
