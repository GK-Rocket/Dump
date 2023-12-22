import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QWidget


class Browser(QWebEngineView):
    def __init__(self):
        # Create a QWebEngineView widget and set its url
        QWebEngineView.__init__(self)
        self.setWindowTitle('Web Browser')
        self.setUrl(QUrl('https://duckduckgo.com/'))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create a browser instance and show it
    browser = Browser()
    browser.show()

    # Run the application's event loop
    sys.exit(app.exec_())

