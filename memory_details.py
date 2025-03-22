# import psutil
# from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout
# from PyQt5.QtCore import QTimer
# import pyqtgraph as pg

# class MemoryMonitorWidget(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)

#         layout = QGridLayout(self)
#         self.mem_plot = pg.PlotWidget(title="Memory Usage (%)")
#         self.mem_plot.setYRange(0, 100)
#         self.mem_plot.showGrid(x=True, y=True)
#         self.mem_curve = self.mem_plot.plot(pen='c')
#         layout.addWidget(self.mem_plot, 0, 0, 1, 2)

#         self.details_label = QLabel()
#         layout.addWidget(self.details_label, 1, 0, 1, 2)

#         self.mem_usage_data = [0] * 60

#         self.timer = QTimer()
#         self.timer.timeout.connect(self.update_stats)
#         self.timer.start(1000)

#     def update_stats(self):
#         mem = psutil.virtual_memory()
#         self.mem_usage_data = self.mem_usage_data[1:] + [mem.percent]
#         self.mem_curve.setData(self.mem_usage_data)

#         details = (
#             f"<b>Total:</b> {mem.total / (1024 ** 3):.2f} GB<br>"
#             f"<b>Available:</b> {mem.available / (1024 ** 3):.2f} GB<br>"
#             f"<b>Used:</b> {mem.used / (1024 ** 3):.2f} GB<br>"
#             f"<b>Free:</b> {mem.free / (1024 ** 3):.2f} GB<br>"
#             f"<b>Percent:</b> {mem.percent}%"
#         )
#         self.details_label.setText(details)

import psutil
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout
from PyQt5.QtCore import QThread, pyqtSignal
import pyqtgraph as pg
import time

class MemoryWorker(QThread):
    data_updated = pyqtSignal(float, dict)

    def run(self):
        while True:
            mem = psutil.virtual_memory()
            details = {
                'total': mem.total / (1024 ** 3),
                'available': mem.available / (1024 ** 3),
                'used': mem.used / (1024 ** 3),
                'free': mem.free / (1024 ** 3),
                'percent': mem.percent
            }
            self.data_updated.emit(mem.percent, details)
            time.sleep(1)


class MemoryMonitorWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QGridLayout(self)

        self.mem_plot = pg.PlotWidget(title="Memory Usage (%)")
        self.mem_plot.setYRange(0, 100)
        self.mem_plot.showGrid(x=True, y=True)
        self.mem_curve = self.mem_plot.plot(pen='c')
        layout.addWidget(self.mem_plot, 0, 0, 1, 2)

        self.details_label = QLabel()
        layout.addWidget(self.details_label, 1, 0, 1, 2)

        self.mem_usage_data = [0] * 60

        self.worker_thread = MemoryWorker()
        self.worker_thread.data_updated.connect(self.update_display)
        self.worker_thread.start()

    def update_display(self, percent, details):
        self.mem_usage_data = self.mem_usage_data[1:] + [percent]
        self.mem_curve.setData(self.mem_usage_data)

        details_str = (
            f"<b>Total:</b> {details['total']:.2f} GB<br>"
            f"<b>Available:</b> {details['available']:.2f} GB<br>"
            f"<b>Used:</b> {details['used']:.2f} GB<br>"
            f"<b>Free:</b> {details['free']:.2f} GB<br>"
            f"<b>Percent:</b> {details['percent']}%"
        )
        self.details_label.setText(details_str)

    def closeEvent(self, event):
        self.worker_thread.running = False
        self.worker_thread.stop()
        self.worker_thread.quit()
        self.worker_thread.wait()
        self.worker_thread.deleteLater()
        event.accept()
