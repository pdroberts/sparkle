from PyQt4 import QtGui
from caldialog_form import Ui_CalibrationDialog

class CalibrationDialog(QtGui.QDialog):
    def __init__(self, parent=None, default_vals=None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_CalibrationDialog()
        self.ui.setupUi(self)
        print default_vals
        if default_vals is not None:
            self.ui.calfile_lnedt.setText(default_vals['calfile'])
            self.ui.caldb_spnbx.setValue(default_vals['caldb'])
            self.ui.calv_spnbx.setValue(default_vals['calv'])
            self.ui.calf_spnbx.setValue(default_vals['calf'])
            self.ui.calfile_radio.setChecked(default_vals['use_calfile'])

    def browseFiles(self):
        calfile = QtGui.QFileDialog.getOpenFileName(self, u"Select calibration file", 
                                    self.ui.calfile_lnedt.text(), "Calibration data files(*.hdf5 *.h5)")
        if calfile is not None:
            self.ui.calfile_lnedt.setText(calfile)

    def values(self):
        results = {}
        results['use_calfile'] = self.ui.calfile_radio.isChecked()
        results['calfile'] = self.ui.calfile_lnedt.text()
        results['caldb'] = self.ui.caldb_spnbx.value()
        results['calv'] = self.ui.calv_spnbx.value()
        results['calf'] = self.ui.calf_spnbx.value()

        return results