# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainAppaZOJRT.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(442, 392)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(442, 392))
        MainWindow.setMaximumSize(QSize(442, 392))
        icon = QIcon()
        icon.addFile(u"bars.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.logfile_path = QLineEdit(self.centralwidget)
        self.logfile_path.setObjectName(u"logfile_path")
        self.logfile_path.setGeometry(QRect(10, 10, 421, 22))
        palette = QPalette()
        brush = QBrush(QColor(212, 212, 212, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
        self.logfile_path.setPalette(palette)
        self.close = QPushButton(self.centralwidget)
        self.close.setObjectName(u"close")
        self.close.setGeometry(QRect(360, 356, 72, 24))
        self.open_file = QPushButton(self.centralwidget)
        self.open_file.setObjectName(u"open_file")
        self.open_file.setGeometry(QRect(360, 39, 72, 24))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.open_file.sizePolicy().hasHeightForWidth())
        self.open_file.setSizePolicy(sizePolicy1)
        self.analyze = QPushButton(self.centralwidget)
        self.analyze.setObjectName(u"analyze")
        self.analyze.setGeometry(QRect(360, 69, 72, 24))
        self.output = QTextBrowser(self.centralwidget)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(10, 40, 341, 339))
        sizePolicy.setHeightForWidth(self.output.sizePolicy().hasHeightForWidth())
        self.output.setSizePolicy(sizePolicy)
        self.plot = QPushButton(self.centralwidget)
        self.plot.setObjectName(u"plot")
        self.plot.setGeometry(QRect(360, 99, 72, 24))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EoLa v1.2", None))
        self.logfile_path.setText(QCoreApplication.translate("MainWindow", u"Path to a logfile", None))
        self.close.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.open_file.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.analyze.setText(QCoreApplication.translate("MainWindow", u"Analyze", None))
        self.output.setMarkdown(QCoreApplication.translate("MainWindow", u"Load a logfile\n"
"\n"
"", None))
        self.output.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Load a logfile</p></body></html>", None))
        self.plot.setText(QCoreApplication.translate("MainWindow", u"Show graph", None))
    # retranslateUi

