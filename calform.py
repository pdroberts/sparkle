# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\calibration_window.ui'
#
# Created: Tue May 21 11:55:28 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CalibrationWindow(object):
    def setupUi(self, CalibrationWindow):
        CalibrationWindow.setObjectName(_fromUtf8("CalibrationWindow"))
        CalibrationWindow.resize(685, 368)
        self.centralwidget = QtGui.QWidget(CalibrationWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_4.addWidget(self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tabs = QtGui.QTabWidget(self.centralwidget)
        self.tabs.setObjectName(_fromUtf8("tabs"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.freq_spnbx = QtGui.QSpinBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.freq_spnbx.setFont(font)
        self.freq_spnbx.setMaximum(200)
        self.freq_spnbx.setSingleStep(5)
        self.freq_spnbx.setProperty("value", 5)
        self.freq_spnbx.setObjectName(_fromUtf8("freq_spnbx"))
        self.gridLayout.addWidget(self.freq_spnbx, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_32 = QtGui.QLabel(self.tab)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.gridLayout.addWidget(self.label_32, 6, 0, 1, 1)
        self.aisr_spnbx = QtGui.QSpinBox(self.tab)
        self.aisr_spnbx.setMinimum(10)
        self.aisr_spnbx.setMaximum(400)
        self.aisr_spnbx.setObjectName(_fromUtf8("aisr_spnbx"))
        self.gridLayout.addWidget(self.aisr_spnbx, 6, 1, 1, 1)
        self.label_33 = QtGui.QLabel(self.tab)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.gridLayout.addWidget(self.label_33, 6, 2, 1, 1)
        self.dur_spnbx = QtGui.QSpinBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dur_spnbx.setFont(font)
        self.dur_spnbx.setMinimum(100)
        self.dur_spnbx.setMaximum(50000)
        self.dur_spnbx.setSingleStep(100)
        self.dur_spnbx.setProperty("value", 1000)
        self.dur_spnbx.setObjectName(_fromUtf8("dur_spnbx"))
        self.gridLayout.addWidget(self.dur_spnbx, 2, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 2, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)
        self.sr_spnbx = QtGui.QSpinBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sr_spnbx.setFont(font)
        self.sr_spnbx.setMinimum(10)
        self.sr_spnbx.setMaximum(400)
        self.sr_spnbx.setSingleStep(10)
        self.sr_spnbx.setProperty("value", 10)
        self.sr_spnbx.setObjectName(_fromUtf8("sr_spnbx"))
        self.gridLayout.addWidget(self.sr_spnbx, 1, 1, 1, 1)
        self.risefall_spnbx = QtGui.QSpinBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.risefall_spnbx.setFont(font)
        self.risefall_spnbx.setMaximum(100)
        self.risefall_spnbx.setObjectName(_fromUtf8("risefall_spnbx"))
        self.gridLayout.addWidget(self.risefall_spnbx, 5, 1, 1, 1)
        self.db_spnbx = QtGui.QSpinBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.db_spnbx.setFont(font)
        self.db_spnbx.setMaximum(150)
        self.db_spnbx.setSingleStep(5)
        self.db_spnbx.setProperty("value", 20)
        self.db_spnbx.setObjectName(_fromUtf8("db_spnbx"))
        self.gridLayout.addWidget(self.db_spnbx, 4, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 5, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 4, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.tab)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 3, 2, 1, 1)
        self.pause_spnbx = QtGui.QSpinBox(self.tab)
        self.pause_spnbx.setMinimum(0)
        self.pause_spnbx.setMaximum(6000)
        self.pause_spnbx.setSingleStep(100)
        self.pause_spnbx.setObjectName(_fromUtf8("pause_spnbx"))
        self.gridLayout.addWidget(self.pause_spnbx, 3, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.tabs.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.db_stop_spnbx = QtGui.QSpinBox(self.tab_2)
        self.db_stop_spnbx.setObjectName(_fromUtf8("db_stop_spnbx"))
        self.gridLayout_2.addWidget(self.db_stop_spnbx, 2, 2, 1, 1)
        self.freq_step_spnbx = QtGui.QSpinBox(self.tab_2)
        self.freq_step_spnbx.setObjectName(_fromUtf8("freq_step_spnbx"))
        self.gridLayout_2.addWidget(self.freq_step_spnbx, 1, 3, 1, 1)
        self.freq_stop_spnbx = QtGui.QSpinBox(self.tab_2)
        self.freq_stop_spnbx.setObjectName(_fromUtf8("freq_stop_spnbx"))
        self.gridLayout_2.addWidget(self.freq_stop_spnbx, 1, 2, 1, 1)
        self.label_21 = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_2.addWidget(self.label_21, 2, 4, 1, 1)
        self.label_19 = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_2.addWidget(self.label_19, 1, 4, 1, 1)
        self.freq_start_spnbx = QtGui.QSpinBox(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.freq_start_spnbx.setFont(font)
        self.freq_start_spnbx.setMaximum(200)
        self.freq_start_spnbx.setSingleStep(5)
        self.freq_start_spnbx.setProperty("value", 5)
        self.freq_start_spnbx.setObjectName(_fromUtf8("freq_start_spnbx"))
        self.gridLayout_2.addWidget(self.freq_start_spnbx, 1, 1, 1, 1)
        self.db_step_spnbx = QtGui.QSpinBox(self.tab_2)
        self.db_step_spnbx.setObjectName(_fromUtf8("db_step_spnbx"))
        self.gridLayout_2.addWidget(self.db_step_spnbx, 2, 3, 1, 1)
        self.db_start_spnbx = QtGui.QSpinBox(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.db_start_spnbx.setFont(font)
        self.db_start_spnbx.setMaximum(150)
        self.db_start_spnbx.setSingleStep(5)
        self.db_start_spnbx.setProperty("value", 20)
        self.db_start_spnbx.setObjectName(_fromUtf8("db_start_spnbx"))
        self.gridLayout_2.addWidget(self.db_start_spnbx, 2, 1, 1, 1)
        self.label_25 = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_2.addWidget(self.label_25, 1, 0, 1, 1)
        self.label_26 = QtGui.QLabel(self.tab_2)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_2.addWidget(self.label_26, 0, 1, 1, 1)
        self.label_18 = QtGui.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_2.addWidget(self.label_18, 2, 0, 1, 1)
        self.label_27 = QtGui.QLabel(self.tab_2)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_2.addWidget(self.label_27, 0, 2, 1, 1)
        self.label_28 = QtGui.QLabel(self.tab_2)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_2.addWidget(self.label_28, 0, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_22 = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_3.addWidget(self.label_22, 0, 0, 1, 1)
        self.dur_spnbx_2 = QtGui.QSpinBox(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dur_spnbx_2.setFont(font)
        self.dur_spnbx_2.setMinimum(100)
        self.dur_spnbx_2.setMaximum(50000)
        self.dur_spnbx_2.setSingleStep(100)
        self.dur_spnbx_2.setProperty("value", 1000)
        self.dur_spnbx_2.setObjectName(_fromUtf8("dur_spnbx_2"))
        self.gridLayout_3.addWidget(self.dur_spnbx_2, 0, 1, 1, 1)
        self.label_24 = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_3.addWidget(self.label_24, 0, 2, 1, 1)
        self.label_14 = QtGui.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_3.addWidget(self.label_14, 0, 3, 1, 1)
        self.risefall_spnbx_2 = QtGui.QSpinBox(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.risefall_spnbx_2.setFont(font)
        self.risefall_spnbx_2.setMaximum(100)
        self.risefall_spnbx_2.setObjectName(_fromUtf8("risefall_spnbx_2"))
        self.gridLayout_3.addWidget(self.risefall_spnbx_2, 0, 4, 1, 1)
        self.label_20 = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_3.addWidget(self.label_20, 0, 5, 1, 1)
        self.label_23 = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_3.addWidget(self.label_23, 1, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_3.addWidget(self.label_15, 1, 2, 1, 1)
        self.label_17 = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_3.addWidget(self.label_17, 1, 3, 1, 1)
        self.sr_spnbx_2 = QtGui.QSpinBox(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sr_spnbx_2.setFont(font)
        self.sr_spnbx_2.setMinimum(10)
        self.sr_spnbx_2.setMaximum(400)
        self.sr_spnbx_2.setSingleStep(10)
        self.sr_spnbx_2.setProperty("value", 100)
        self.sr_spnbx_2.setObjectName(_fromUtf8("sr_spnbx_2"))
        self.gridLayout_3.addWidget(self.sr_spnbx_2, 1, 4, 1, 1)
        self.label_16 = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_3.addWidget(self.label_16, 1, 5, 1, 1)
        self.reprate_spnbx = QtGui.QDoubleSpinBox(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reprate_spnbx.setFont(font)
        self.reprate_spnbx.setMinimum(0.1)
        self.reprate_spnbx.setMaximum(10.0)
        self.reprate_spnbx.setProperty("value", 0.5)
        self.reprate_spnbx.setObjectName(_fromUtf8("reprate_spnbx"))
        self.gridLayout_3.addWidget(self.reprate_spnbx, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.tabs.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.tabs)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.verticalLayout_3.addItem(spacerItem1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_29 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_4.addWidget(self.label_29, 0, 0, 1, 1)
        self.aochan_box = QtGui.QComboBox(self.centralwidget)
        self.aochan_box.setObjectName(_fromUtf8("aochan_box"))
        self.gridLayout_4.addWidget(self.aochan_box, 0, 1, 1, 1)
        self.label_30 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.gridLayout_4.addWidget(self.label_30, 1, 0, 1, 1)
        self.aichan_box = QtGui.QComboBox(self.centralwidget)
        self.aichan_box.setObjectName(_fromUtf8("aichan_box"))
        self.gridLayout_4.addWidget(self.aichan_box, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_4)
        self.label_31 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_31.setFont(font)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.verticalLayout_3.addWidget(self.label_31)
        self.freq_label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.freq_label.sizePolicy().hasHeightForWidth())
        self.freq_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.freq_label.setFont(font)
        self.freq_label.setObjectName(_fromUtf8("freq_label"))
        self.verticalLayout_3.addWidget(self.freq_label)
        self.db_label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.db_label.setFont(font)
        self.db_label.setObjectName(_fromUtf8("db_label"))
        self.verticalLayout_3.addWidget(self.db_label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.start_button = QtGui.QPushButton(self.centralwidget)
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.horizontalLayout.addWidget(self.start_button)
        self.stop_button = QtGui.QPushButton(self.centralwidget)
        self.stop_button.setObjectName(_fromUtf8("stop_button"))
        self.horizontalLayout.addWidget(self.stop_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        CalibrationWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(CalibrationWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 685, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAdvanced = QtGui.QMenu(self.menubar)
        self.menuAdvanced.setObjectName(_fromUtf8("menuAdvanced"))
        CalibrationWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(CalibrationWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        CalibrationWindow.setStatusBar(self.statusbar)
        self.actionDisplay_Options = QtGui.QAction(CalibrationWindow)
        self.actionDisplay_Options.setObjectName(_fromUtf8("actionDisplay_Options"))
        self.menuAdvanced.addAction(self.actionDisplay_Options)
        self.menubar.addAction(self.menuAdvanced.menuAction())

        self.retranslateUi(CalibrationWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QObject.connect(self.dur_spnbx, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), CalibrationWindow.set_interval_min)
        QtCore.QObject.connect(self.sr_spnbx_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), CalibrationWindow.set_dur_max)
        QtCore.QObject.connect(self.actionDisplay_Options, QtCore.SIGNAL(_fromUtf8("triggered()")), CalibrationWindow.launch_display_dlg)
        QtCore.QMetaObject.connectSlotsByName(CalibrationWindow)

    def retranslateUi(self, CalibrationWindow):
        CalibrationWindow.setWindowTitle(_translate("CalibrationWindow", "MainWindow", None))
        self.label.setText(_translate("CalibrationWindow", "Speaker Calibration", None))
        self.label_6.setText(_translate("CalibrationWindow", "Rise fall time", None))
        self.label_32.setText(_translate("CalibrationWindow", "Acq rate", None))
        self.label_33.setText(_translate("CalibrationWindow", "kHz", None))
        self.label_9.setText(_translate("CalibrationWindow", "ms", None))
        self.label_8.setText(_translate("CalibrationWindow", "kHz", None))
        self.label_3.setText(_translate("CalibrationWindow", "Sample rate", None))
        self.label_5.setText(_translate("CalibrationWindow", "Intensity", None))
        self.label_7.setText(_translate("CalibrationWindow", "kHz", None))
        self.label_11.setText(_translate("CalibrationWindow", "ms", None))
        self.label_10.setText(_translate("CalibrationWindow", "dB SPL", None))
        self.label_2.setText(_translate("CalibrationWindow", "Interval", None))
        self.label_4.setText(_translate("CalibrationWindow", "Duration", None))
        self.label_12.setText(_translate("CalibrationWindow", "ms", None))
        self.label_13.setText(_translate("CalibrationWindow", "Frequency", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab), _translate("CalibrationWindow", "Tab 1", None))
        self.label_21.setText(_translate("CalibrationWindow", "dB SPL", None))
        self.label_19.setText(_translate("CalibrationWindow", "kHz", None))
        self.label_25.setText(_translate("CalibrationWindow", "Frequency", None))
        self.label_26.setText(_translate("CalibrationWindow", "Start", None))
        self.label_18.setText(_translate("CalibrationWindow", "Intensity", None))
        self.label_27.setText(_translate("CalibrationWindow", "Stop", None))
        self.label_28.setText(_translate("CalibrationWindow", "Step", None))
        self.label_22.setText(_translate("CalibrationWindow", "Duration", None))
        self.label_24.setText(_translate("CalibrationWindow", "ms", None))
        self.label_14.setText(_translate("CalibrationWindow", "Rise fall time", None))
        self.label_20.setText(_translate("CalibrationWindow", "ms", None))
        self.label_23.setText(_translate("CalibrationWindow", "Rep rate", None))
        self.label_15.setText(_translate("CalibrationWindow", "reps/s", None))
        self.label_17.setText(_translate("CalibrationWindow", "Sample rate", None))
        self.label_16.setText(_translate("CalibrationWindow", "kHz", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_2), _translate("CalibrationWindow", "Tab 2", None))
        self.label_29.setText(_translate("CalibrationWindow", "Stim channel", None))
        self.label_30.setText(_translate("CalibrationWindow", "AI channel", None))
        self.label_31.setText(_translate("CalibrationWindow", "Now Playing:", None))
        self.freq_label.setText(_translate("CalibrationWindow", "Frquency : 15kHz", None))
        self.db_label.setText(_translate("CalibrationWindow", "Intensity : 100 dB", None))
        self.start_button.setText(_translate("CalibrationWindow", "Start", None))
        self.stop_button.setText(_translate("CalibrationWindow", "Stop", None))
        self.menuAdvanced.setTitle(_translate("CalibrationWindow", "Advanced", None))
        self.actionDisplay_Options.setText(_translate("CalibrationWindow", "Display Options", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    CalibrationWindow = QtGui.QMainWindow()
    ui = Ui_CalibrationWindow()
    ui.setupUi(CalibrationWindow)
    CalibrationWindow.show()
    sys.exit(app.exec_())

