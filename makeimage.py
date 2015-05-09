#!/usr/bin/env python
#-*- coding:utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

class browser(QWebView):
    def __init__(self, parent=None):
        super(browser, self).__init__(parent)
	self.setFixedSize(1920, 1080)
        self.timerScreen = QTimer()
        self.timerScreen.setInterval(17000)
        self.timerScreen.setSingleShot(True)
        self.timerScreen.timeout.connect(self.takeScreenshot)

        self.loadFinished.connect(self.timerScreen.start)
        self.load(QUrl("file:///home/pi/index1.html"))    

    def takeScreenshot(self):    
        image   = QImage(self.page().mainFrame().contentsSize(), QImage.Format_ARGB32)
        painter = QPainter(image)

        self.page().mainFrame().render(painter)

        painter.end()
       # image.save(self.title() + ".png")
	image.save("webimage.png")

        sys.exit()

if __name__ == "__main__":
    import  sys        
    app  = QApplication(sys.argv)
    main = browser()
    app.exec_()
