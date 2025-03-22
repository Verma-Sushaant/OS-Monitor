from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout
from cpu_details import CPUMonitorWidget
from memory_details import MemoryMonitorWidget
from disk_details import DiskMonitorWidget
from network_details import NetworkMonitorWidget
from gpu_details import GPUMonitorWidget
import pyqtgraph as pg

pg.setConfigOption('background', '#121212')
pg.setConfigOption('foreground', 'white')
pg.setConfigOptions(antialias=True)

class SystemMonitorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("System Monitor")
        self.resize(1280, 768)
        
        dark_stylesheet = """
        QWidget {
            background-color: #121212;
            color: #E0E0E0;
            font-family: 'Segoe UI', sans-serif;
        }
        QTabWidget::pane {
            border: 1px solid #333;
            top: -1px;
            background: #1E1E1E;
        }
        QTabBar::tab {
            background: #1E1E1E;
            color: #CCCCCC;
            padding: 8px;
            border: 1px solid #333;
            border-bottom-color: #1E1E1E;
        }
        QTabBar::tab:selected {
            background: #333333;
            color: #FFFFFF;
        }
        QLabel {
            color: #E0E0E0;
        }
        QPushButton {
            background-color: #333333;
            color: #FFFFFF;
            border-radius: 6px;
            padding: 5px;
        }
        QPushButton:hover {
            background-color: #444444;
        }
        QLineEdit, QTextEdit {
            background-color: #222222;
            color: #DDDDDD;
            border: 1px solid #555555;
        } """
        self.setStyleSheet(dark_stylesheet)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.add_monitor_tab(CPUMonitorWidget, "CPU Monitor")
        self.add_monitor_tab(MemoryMonitorWidget, "Memory")
        self.add_monitor_tab(DiskMonitorWidget, "Disk")
        self.add_monitor_tab(NetworkMonitorWidget, "Network")
        self.add_monitor_tab(GPUMonitorWidget, "GPU Monitor")

    def add_monitor_tab(self, widget_class, title):
        tab = QWidget()
        layout = QVBoxLayout()
        widget = widget_class()
        layout.addWidget(widget)
        tab.setLayout(layout)
        self.tabs.addTab(tab, title)

if __name__ == "__main__":
    app = QApplication([])
    window = SystemMonitorApp()
    window.show()
    app.exec_()
