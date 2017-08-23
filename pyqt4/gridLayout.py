import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
	def __init__(self):
		super(Example,self).__init__()
		self.initUI()

	def initUI(self):
		grid = QtGui.QGridLayout()
		grid.setSpacing(0)
		self.setLayout(grid)

		names = ['Cls', 'Bck', '', 'Close',
		    '7', '8', '9', '/',
		'4', '5', '6', '*',
		    '1', '2', '3', '-',
		'0', '.', '=', '+']
		positions = [(i,j) for i in range(5) for j in range(4)]
		print(positions)
		for pos, name in zip(positions, names):
			if name=='':
				continue
			button = QtGui.QPushButton(name)
			grid.addWidget(button,*pos)
		self.move(300, 150)
		self.setWindowTitle('Calculator')
		self.show()			

app = QtGui.QApplication(sys.argv)
ex=Example()
sys.exit(app.exec_())
	