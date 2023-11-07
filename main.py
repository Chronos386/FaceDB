import sys
from PyQt5.QtWidgets import QApplication
from interface.adm_db_panel import AdmDbPanel


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdmDbPanel()
    window.show()
    sys.exit(app.exec_())
