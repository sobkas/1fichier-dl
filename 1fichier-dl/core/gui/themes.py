from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor

'''
Dark Theme
'''

dark_theme = QPalette()

dark_theme.setColor(QPalette.Window, QColor(35, 39, 48))
dark_theme.setColor(QPalette.WindowText, Qt.white)
dark_theme.setColor(QPalette.Base, QColor(24, 27, 33))
dark_theme.setColor(QPalette.AlternateBase, QColor(35, 39, 48))
dark_theme.setColor(QPalette.ToolTipBase, Qt.white)
dark_theme.setColor(QPalette.ToolTipText, Qt.white)
dark_theme.setColor(QPalette.Text, Qt.white)
dark_theme.setColor(QPalette.Button, QColor(35, 39, 48))
dark_theme.setColor(QPalette.ButtonText, Qt.white)
dark_theme.setColor(QPalette.BrightText, Qt.red)
dark_theme.setColor(QPalette.Highlight, QColor(42, 130, 218))
dark_theme.setColor(QPalette.HighlightedText, Qt.black)