# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'L:\__current work__\04_Python\OptiSim\OptiSim\ui\extractbandgap.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1091, 533)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.minFitSlider = QtWidgets.QSlider(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minFitSlider.sizePolicy().hasHeightForWidth())
        self.minFitSlider.setSizePolicy(sizePolicy)
        self.minFitSlider.setSingleStep(500)
        self.minFitSlider.setPageStep(500)
        self.minFitSlider.setOrientation(QtCore.Qt.Horizontal)
        self.minFitSlider.setObjectName("minFitSlider")
        self.horizontalLayout_2.addWidget(self.minFitSlider)
        self.minFitSB = QtWidgets.QDoubleSpinBox(Dialog)
        self.minFitSB.setObjectName("minFitSB")
        self.horizontalLayout_2.addWidget(self.minFitSB)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.maxFitSlider = QtWidgets.QSlider(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxFitSlider.sizePolicy().hasHeightForWidth())
        self.maxFitSlider.setSizePolicy(sizePolicy)
        self.maxFitSlider.setSingleStep(500)
        self.maxFitSlider.setPageStep(500)
        self.maxFitSlider.setOrientation(QtCore.Qt.Horizontal)
        self.maxFitSlider.setObjectName("maxFitSlider")
        self.horizontalLayout_3.addWidget(self.maxFitSlider)
        self.maxFitSB = QtWidgets.QDoubleSpinBox(Dialog)
        self.maxFitSB.setObjectName("maxFitSB")
        self.horizontalLayout_3.addWidget(self.maxFitSB)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fitModeDirect = QtWidgets.QRadioButton(self.groupBox)
        self.fitModeDirect.setChecked(True)
        self.fitModeDirect.setObjectName("fitModeDirect")
        self.verticalLayout.addWidget(self.fitModeDirect)
        self.fitModeIndirect = QtWidgets.QRadioButton(self.groupBox)
        self.fitModeIndirect.setObjectName("fitModeIndirect")
        self.verticalLayout.addWidget(self.fitModeIndirect)
        self.fitModeForbiddenDirect = QtWidgets.QRadioButton(self.groupBox)
        self.fitModeForbiddenDirect.setObjectName("fitModeForbiddenDirect")
        self.verticalLayout.addWidget(self.fitModeForbiddenDirect)
        self.fitModeForbiddenIndirect = QtWidgets.QRadioButton(self.groupBox)
        self.fitModeForbiddenIndirect.setObjectName("fitModeForbiddenIndirect")
        self.verticalLayout.addWidget(self.fitModeForbiddenIndirect)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fitModeCostum = QtWidgets.QRadioButton(self.groupBox)
        self.fitModeCostum.setObjectName("fitModeCostum")
        self.horizontalLayout.addWidget(self.fitModeCostum)
        self.fitModeCostumSB = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.fitModeCostumSB.setMinimum(-20.0)
        self.fitModeCostumSB.setMaximum(20.0)
        self.fitModeCostumSB.setProperty("value", 0.66)
        self.fitModeCostumSB.setObjectName("fitModeCostumSB")
        self.horizontalLayout.addWidget(self.fitModeCostumSB)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.startFit = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startFit.sizePolicy().hasHeightForWidth())
        self.startFit.setSizePolicy(sizePolicy)
        self.startFit.setObjectName("startFit")
        self.verticalLayout_2.addWidget(self.startFit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QtCore.QSize(400, 200))
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.alphaPlot = MplWidgetEgExtraction(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alphaPlot.sizePolicy().hasHeightForWidth())
        self.alphaPlot.setSizePolicy(sizePolicy)
        self.alphaPlot.setObjectName("alphaPlot")
        self.horizontalLayout_4.addWidget(self.alphaPlot)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Bandgap extraction from optical constants"))
        self.label_3.setText(_translate("Dialog", "min fit limit"))
        self.label_4.setText(_translate("Dialog", "max fit limit"))
        self.groupBox.setTitle(_translate("Dialog", "fit mode (alpha = A/hv * (hv-Eg)^m"))
        self.fitModeDirect.setText(_translate("Dialog", "allowed direct (m = 0.5)"))
        self.fitModeIndirect.setText(_translate("Dialog", "allowed indirect (m = 2)"))
        self.fitModeForbiddenDirect.setText(_translate("Dialog", "forbidden direct (m = 1.5)"))
        self.fitModeForbiddenIndirect.setText(_translate("Dialog", "forbidden indirect (m = 3)"))
        self.fitModeCostum.setText(_translate("Dialog", "custom"))
        self.startFit.setText(_translate("Dialog", "fit"))
        self.label_2.setText(_translate("Dialog", "fit results"))

from ui.mplwidget_EgExtraction import MplWidgetEgExtraction

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

