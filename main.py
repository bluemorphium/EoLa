from eola import *
import matplotlib.pyplot as plt

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.close.clicked.connect(QApplication.instance().quit)
		self.open_file.clicked.connect(self.open_file_dialog)
		self.analyze.clicked.connect(self.start_analyzing)
		self.plot.clicked.connect(self.start_plotting)

	def quit(self):
		pass

	def open_file_dialog(self):
		fileName = QFileDialog.getOpenFileName(self, "Open Logfile")
		self.logfile_path.setText(QApplication.translate("MainWindow", fileName[0], None))

	def start_analyzing(self):
		error_message = "FILE NOT FOUND OR DOES NOT EXIST!\n\n(or other bad things happened, send help!)"

		data = load_file(self.logfile_path.text())

		if data == error_message:
			self.output.setMarkdown(QApplication.translate("MainWindow", error_message, None))

		else:
			dates = get_start_and_end(data)
			time_in_combat = (datetime.strptime(dates[1], "%Y.%m.%d %H:%M:%S") - datetime.strptime(dates[0], "%Y.%m.%d %H:%M:%S")).seconds

			output = f"Name: \t \t {data[0][0]} \n\n Date: \t \t {data[0][1]} \n\n  Time in combat: \t {time_in_combat} seconds \n\n Damage done: \t {sum_a_stat(0, data)} \n\n Damage received: \t {sum_a_stat(1, data)} \n\n Remote Repair done: \t {sum_a_stat(2, data)} \n\n Remote Repair received: \t {sum_a_stat(3, data)} \n\n Remote Shield done: \t {sum_a_stat(4, data)}\n\nRemote Shield received: \t {sum_a_stat(5, data)} \n\n Remote Energy done: \t {sum_a_stat(6, data)} \n\n Remote Energy received: \t {sum_a_stat(7, data)} \n\n Energy gained to Nosferatu: \t {sum_a_stat(8, data)} \n\n Energy lost to Nosferatu: \t {sum_a_stat(9, data)} \n\n Energy Neutralyzed: \t {sum_a_stat(10, data)} \n\n Energy lost to Neutralyzed: \t {sum_a_stat(11, data)}"

			self.output.setMarkdown(QApplication.translate("MainWindow", output, None))

	def start_plotting(self):
		data = load_file(self.logfile_path.text())

		plt.plot(get_plot_data(0, data)[0], get_plot_data(0, data)[1], label = "Damage done", color='green')
		plt.plot(get_plot_data(1, data)[0], get_plot_data(1, data)[1], label = "Damage received", color='red')
		plt.plot(get_plot_data(2, data)[0], np.add(get_plot_data(2, data)[1], get_plot_data(4, data)[1]), label = "Remote repair/shield done", color='blue', linestyle='dashed')
		plt.plot(get_plot_data(2, data)[0], np.add(get_plot_data(3, data)[1], get_plot_data(5, data)[1]), label = "Remote repair/shield receivced", color='orange', linestyle='dashed')
		plt.xlabel("Seconds")
		plt.ylabel("Damage")
		plt.legend()
		plt.grid(axis = 'y')
		plt.get_current_fig_manager().set_window_title('EoLa graph')
		plt.show()


app = QApplication()
mainwindow = MainWindow()
mainwindow.show()
app.exec()
