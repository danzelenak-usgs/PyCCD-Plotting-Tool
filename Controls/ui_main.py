# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_MAIN.UI'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PyCCDPlottingTool(object):
    def setupUi(self, PyCCDPlottingTool):
        PyCCDPlottingTool.setObjectName("PyCCDPlottingTool")
        PyCCDPlottingTool.resize(659, 566)
        PyCCDPlottingTool.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(PyCCDPlottingTool)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_main = QtWidgets.QGridLayout()
        self.gridLayout_main.setObjectName("gridLayout_main")
        self.horizontalLayout_json = QtWidgets.QHBoxLayout()
        self.horizontalLayout_json.setObjectName("horizontalLayout_json")
        self.browsejsonline = QtWidgets.QLineEdit(self.centralwidget)
        self.browsejsonline.setObjectName("browsejsonline")
        self.horizontalLayout_json.addWidget(self.browsejsonline)
        self.browsejsonbutton = QtWidgets.QPushButton(self.centralwidget)
        self.browsejsonbutton.setObjectName("browsejsonbutton")
        self.horizontalLayout_json.addWidget(self.browsejsonbutton)
        self.gridLayout_main.addLayout(self.horizontalLayout_json, 8, 0, 1, 1)
        self.plotbutton = QtWidgets.QPushButton(self.centralwidget)
        self.plotbutton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotbutton.sizePolicy().hasHeightForWidth())
        self.plotbutton.setSizePolicy(sizePolicy)
        self.plotbutton.setMinimumSize(QtCore.QSize(100, 0))
        self.plotbutton.setMaximumSize(QtCore.QSize(100, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 132, 132))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(198, 198, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 165, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 66, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(88, 88, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 132, 132))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(193, 193, 193))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 132, 132))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(198, 198, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 165, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 66, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(88, 88, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 132, 132))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(193, 193, 193))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 66, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 132, 132))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(198, 198, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(165, 165, 165))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 66, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(88, 88, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 66, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(66, 66, 66))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 132, 132))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 132, 132))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 132, 132))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.plotbutton.setPalette(palette)
        self.plotbutton.setObjectName("plotbutton")
        self.gridLayout_main.addWidget(self.plotbutton, 17, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_main.addItem(spacerItem, 20, 0, 1, 1)
        self.horizontalLayout_hvinput = QtWidgets.QHBoxLayout()
        self.horizontalLayout_hvinput.setObjectName("horizontalLayout_hvinput")
        self.hline = QtWidgets.QLineEdit(self.centralwidget)
        self.hline.setMaximumSize(QtCore.QSize(50, 16777215))
        self.hline.setMaxLength(2)
        self.hline.setObjectName("hline")
        self.horizontalLayout_hvinput.addWidget(self.hline)
        self.vline = QtWidgets.QLineEdit(self.centralwidget)
        self.vline.setMaximumSize(QtCore.QSize(50, 16777215))
        self.vline.setMaxLength(2)
        self.vline.setObjectName("vline")
        self.horizontalLayout_hvinput.addWidget(self.vline)
        self.gridLayout_main.addLayout(self.horizontalLayout_hvinput, 4, 0, 1, 1)
        self.cache_label = QtWidgets.QLabel(self.centralwidget)
        self.cache_label.setObjectName("cache_label")
        self.gridLayout_main.addWidget(self.cache_label, 5, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_main.addItem(spacerItem1, 2, 0, 1, 1)
        self.arccoordsline = QtWidgets.QLineEdit(self.centralwidget)
        self.arccoordsline.setClearButtonEnabled(True)
        self.arccoordsline.setObjectName("arccoordsline")
        self.gridLayout_main.addWidget(self.arccoordsline, 1, 0, 1, 1)
        self.horizontalLayout_cache = QtWidgets.QHBoxLayout()
        self.horizontalLayout_cache.setObjectName("horizontalLayout_cache")
        self.browsecacheline = QtWidgets.QLineEdit(self.centralwidget)
        self.browsecacheline.setObjectName("browsecacheline")
        self.horizontalLayout_cache.addWidget(self.browsecacheline)
        self.browsecachebutton = QtWidgets.QPushButton(self.centralwidget)
        self.browsecachebutton.setObjectName("browsecachebutton")
        self.horizontalLayout_cache.addWidget(self.browsecachebutton)
        self.gridLayout_main.addLayout(self.horizontalLayout_cache, 6, 0, 1, 1)
        self.horizontalLayout_hvLabels = QtWidgets.QHBoxLayout()
        self.horizontalLayout_hvLabels.setObjectName("horizontalLayout_hvLabels")
        self.label_h = QtWidgets.QLabel(self.centralwidget)
        self.label_h.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_h.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_h.setAlignment(QtCore.Qt.AlignCenter)
        self.label_h.setObjectName("label_h")
        self.horizontalLayout_hvLabels.addWidget(self.label_h)
        self.label_v = QtWidgets.QLabel(self.centralwidget)
        self.label_v.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_v.setAlignment(QtCore.Qt.AlignCenter)
        self.label_v.setObjectName("label_v")
        self.horizontalLayout_hvLabels.addWidget(self.label_v)
        self.gridLayout_main.addLayout(self.horizontalLayout_hvLabels, 3, 0, 1, 1)
        self.exitbutton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitbutton.sizePolicy().hasHeightForWidth())
        self.exitbutton.setSizePolicy(sizePolicy)
        self.exitbutton.setMinimumSize(QtCore.QSize(100, 0))
        self.exitbutton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.exitbutton.setObjectName("exitbutton")
        self.gridLayout_main.addWidget(self.exitbutton, 21, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.radioshp = QtWidgets.QRadioButton(self.centralwidget)
        self.radioshp.setChecked(True)
        self.radioshp.setAutoExclusive(False)
        self.radioshp.setObjectName("radioshp")
        self.gridLayout_main.addWidget(self.radioshp, 12, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_main.addItem(spacerItem2, 11, 0, 1, 1)
        self.json_label = QtWidgets.QLabel(self.centralwidget)
        self.json_label.setObjectName("json_label")
        self.gridLayout_main.addWidget(self.json_label, 7, 0, 1, 1)
        self.coords_label = QtWidgets.QLabel(self.centralwidget)
        self.coords_label.setObjectName("coords_label")
        self.gridLayout_main.addWidget(self.coords_label, 0, 0, 1, 1)
        self.horizontalLayout_plotsave = QtWidgets.QHBoxLayout()
        self.horizontalLayout_plotsave.setObjectName("horizontalLayout_plotsave")
        self.browseoutputline = QtWidgets.QLineEdit(self.centralwidget)
        self.browseoutputline.setObjectName("browseoutputline")
        self.horizontalLayout_plotsave.addWidget(self.browseoutputline)
        self.browseoutputbutton = QtWidgets.QPushButton(self.centralwidget)
        self.browseoutputbutton.setObjectName("browseoutputbutton")
        self.horizontalLayout_plotsave.addWidget(self.browseoutputbutton)
        self.gridLayout_main.addLayout(self.horizontalLayout_plotsave, 10, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_main.addItem(spacerItem3, 14, 0, 1, 1)
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setObjectName("output_label")
        self.gridLayout_main.addWidget(self.output_label, 9, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_main.addItem(spacerItem4, 16, 0, 1, 1)
        self.listitems = QtWidgets.QListWidget(self.centralwidget)
        self.listitems.setAlternatingRowColors(False)
        self.listitems.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listitems.setObjectName("listitems")
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listitems.addItem(item)
        self.gridLayout_main.addWidget(self.listitems, 15, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_main, 0, 0, 1, 1)
        self.outputverticalLayout = QtWidgets.QVBoxLayout()
        self.outputverticalLayout.setObjectName("outputverticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.outputverticalLayout.addWidget(self.label)
        self.plainTextEdit_results = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_results.setReadOnly(True)
        self.plainTextEdit_results.setObjectName("plainTextEdit_results")
        self.outputverticalLayout.addWidget(self.plainTextEdit_results)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.outputverticalLayout.addWidget(self.label_2)
        self.plainTextEdit_click = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_click.setReadOnly(True)
        self.plainTextEdit_click.setObjectName("plainTextEdit_click")
        self.outputverticalLayout.addWidget(self.plainTextEdit_click)
        self.clearpushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearpushButton.sizePolicy().hasHeightForWidth())
        self.clearpushButton.setSizePolicy(sizePolicy)
        self.clearpushButton.setObjectName("clearpushButton")
        self.outputverticalLayout.addWidget(self.clearpushButton, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addLayout(self.outputverticalLayout, 0, 1, 1, 1)
        PyCCDPlottingTool.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PyCCDPlottingTool)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 659, 21))
        self.menubar.setObjectName("menubar")
        PyCCDPlottingTool.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PyCCDPlottingTool)
        self.statusbar.setObjectName("statusbar")
        PyCCDPlottingTool.setStatusBar(self.statusbar)

        self.retranslateUi(PyCCDPlottingTool)
        QtCore.QMetaObject.connectSlotsByName(PyCCDPlottingTool)
        PyCCDPlottingTool.setTabOrder(self.arccoordsline, self.hline)
        PyCCDPlottingTool.setTabOrder(self.hline, self.vline)
        PyCCDPlottingTool.setTabOrder(self.vline, self.browsecacheline)
        PyCCDPlottingTool.setTabOrder(self.browsecacheline, self.browsecachebutton)
        PyCCDPlottingTool.setTabOrder(self.browsecachebutton, self.browsejsonline)
        PyCCDPlottingTool.setTabOrder(self.browsejsonline, self.browsejsonbutton)
        PyCCDPlottingTool.setTabOrder(self.browsejsonbutton, self.browseoutputline)
        PyCCDPlottingTool.setTabOrder(self.browseoutputline, self.browseoutputbutton)
        PyCCDPlottingTool.setTabOrder(self.browseoutputbutton, self.radioshp)
        PyCCDPlottingTool.setTabOrder(self.radioshp, self.listitems)
        PyCCDPlottingTool.setTabOrder(self.listitems, self.plotbutton)

    def retranslateUi(self, PyCCDPlottingTool):
        _translate = QtCore.QCoreApplication.translate
        PyCCDPlottingTool.setWindowTitle(_translate("PyCCDPlottingTool", "PyCCD Plotting Tool"))
        self.browsejsonbutton.setText(_translate("PyCCDPlottingTool", "..."))
        self.plotbutton.setText(_translate("PyCCDPlottingTool", "Plot"))
        self.cache_label.setText(_translate("PyCCDPlottingTool", "Full path to cache folder:"))
        self.browsecachebutton.setText(_translate("PyCCDPlottingTool", "..."))
        self.label_h.setText(_translate("PyCCDPlottingTool", "h"))
        self.label_v.setText(_translate("PyCCDPlottingTool", "v"))
        self.exitbutton.setText(_translate("PyCCDPlottingTool", "Close"))
        self.radioshp.setText(_translate("PyCCDPlottingTool", "Create Point Shapefile on Plot"))
        self.json_label.setText(_translate("PyCCDPlottingTool", "Full path to JSON folder:"))
        self.coords_label.setText(_translate("PyCCDPlottingTool", "Paste coordinates directly from ArcMap:"))
        self.browseoutputbutton.setText(_translate("PyCCDPlottingTool", "..."))
        self.output_label.setText(_translate("PyCCDPlottingTool", "Output directory to save plots:"))
        __sortingEnabled = self.listitems.isSortingEnabled()
        self.listitems.setSortingEnabled(False)
        item = self.listitems.item(0)
        item.setText(_translate("PyCCDPlottingTool", "All Bands and Indices"))
        item = self.listitems.item(1)
        item.setText(_translate("PyCCDPlottingTool", "All Bands"))
        item = self.listitems.item(2)
        item.setText(_translate("PyCCDPlottingTool", "All Indices"))
        item = self.listitems.item(3)
        item.setText(_translate("PyCCDPlottingTool", "Blue"))
        item = self.listitems.item(4)
        item.setText(_translate("PyCCDPlottingTool", "Green"))
        item = self.listitems.item(5)
        item.setText(_translate("PyCCDPlottingTool", "Red"))
        item = self.listitems.item(6)
        item.setText(_translate("PyCCDPlottingTool", "NIR"))
        item = self.listitems.item(7)
        item.setText(_translate("PyCCDPlottingTool", "SWIR-1"))
        item = self.listitems.item(8)
        item.setText(_translate("PyCCDPlottingTool", "SWIR-2"))
        item = self.listitems.item(9)
        item.setText(_translate("PyCCDPlottingTool", "Thermal"))
        item = self.listitems.item(10)
        item.setText(_translate("PyCCDPlottingTool", "NDVI"))
        item = self.listitems.item(11)
        item.setText(_translate("PyCCDPlottingTool", "MSAVI"))
        item = self.listitems.item(12)
        item.setText(_translate("PyCCDPlottingTool", "EVI"))
        item = self.listitems.item(13)
        item.setText(_translate("PyCCDPlottingTool", "SAVI"))
        item = self.listitems.item(14)
        item.setText(_translate("PyCCDPlottingTool", "NDMI"))
        item = self.listitems.item(15)
        item.setText(_translate("PyCCDPlottingTool", "NBR"))
        item = self.listitems.item(16)
        item.setText(_translate("PyCCDPlottingTool", "NBR-2"))
        self.listitems.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("PyCCDPlottingTool", "Model Results:"))
        self.label_2.setText(_translate("PyCCDPlottingTool", "Selected Observations:"))
        self.clearpushButton.setText(_translate("PyCCDPlottingTool", "Clear"))

