import subprocess
import sys
from PyQt5.QtWidgets import (QApplication, QWidget,QPushButton, QToolTip,
                              QLabel, QLineEdit, QPlainTextEdit, QComboBox)
from PyQt5.QtGui import QFont



# --------  CLASSES DEFINITION      --------#

class Root_mainWindow(QWidget):  # ereditarietà
	
	list_function_toTest = []
	list_input_variable = []
	list_calibration_variable = []
	list_expected_output_variable = []
	
	
	# costruttore
	def __init__(self):
		super().__init__()
	
	
	
	#class members:
	
	def init_root_windows(self,title):
		
		#set the size and the window title 
		self.setGeometry(200,200,600,750) #positionx,positiony,sizex,sizey
		self.setWindowTitle(title)
		
		#setting Tooltip
		QToolTip.setFont(QFont('Helvetica', 10))
	
		
		#--- INPUT  ----#
		
		#labels
		enter_function_label = QLabel(self)
		input_label = QLabel(self)
		#setting labels:
		enter_function_label.setText("Enter The Function To Test:")
		enter_function_label.move(10,40)
		input_label.setText("Enter The Input Variables:")
		input_label.move(10,97)
		
		#textArea
		self.enter_function_text = QLineEdit(self)
		self.input_text = QPlainTextEdit(self)
		#setting QPlainTextEdit:
		self.enter_function_text.resize(400,30)
		self.input_text.resize(400,160)
		self.enter_function_text.move(6,60)
		self.input_text.move(6,120)
		
		
		#--- CALIBRATION   ---#
		self.calibration_label = QLabel(self)
		#setting labels:
		self.calibration_label.setText("Enter The Calibrations Variables:")
		self.calibration_label.move(10,290)
		
		#textArea
		self.calibration_text = QPlainTextEdit(self)
		#setting QPlainTextEdit:
		self.calibration_text.resize(400,160)
		self.calibration_text.move(6,310)
		
		#--- OUTPUT  ---#
		self.output_label = QLabel(self)
		#setting labels:
		self.output_label.setText("Enter The Expected Values:")
		self.output_label.move(10,490)
		
		#textArea
		self.output_text = QPlainTextEdit(self)
		#setting QPlainTextEdit:
		self.output_text.resize(400,160)
		self.output_text.move(6,510)
		
		
		#Buttons:
		self.btn_commit_input = QPushButton('Commit', self)
		self.btn_run_script = QPushButton('RUN', self)
		
		#seting Buttons
		self.btn_commit_input.setToolTip("commit all the input entered")
		self.btn_commit_input.move(450,550)
		
		self.btn_run_script.setToolTip("run the script")
		self.btn_run_script.move(450,600)
		
		#Signal & slots Buttons:
		self.btn_commit_input.clicked.connect(self.commit_input) # use the button signal "clicked"
		
		
		
		self.show()
		return
		
	#this function store the QTextEdit contents in lists and will run some fuction
	# to save the content of text area in a file: 
	def commit_input(self):
		
		function_to_test = self.enter_function_text.text()
		input_variable =  self.input_text.toPlainText()
		calibration_variable = self.calibration_text.toPlainText()
		expected_output_variable = self.output_text.toPlainText()
		
		#store the text in list:
		self.list_function_toTest = list(function_to_test.split("\n"))
		self.list_input_variable = list(input_variable.split('\n'))
		self.list_calibration_variable = list(calibration_variable.split('\n'))
		self.list_expected_output_variable = list(expected_output_variable.split('\n'))
		
		self.print_variable_list()
		self.add_items_tolist()
		self.scrivi_su_file()
		
		return
		
	def print_variable_list(self):
		print(self.list_function_toTest)
		print(self.list_input_variable)
		print(self.list_calibration_variable)
		print(self.list_expected_output_variable)
		
		return 
	
	def add_items_tolist(self):
		
		self.list_function_toTest.insert(0,"//start")
		self.list_function_toTest[1] = ( "void " + self.list_function_toTest[1] + "(void);")
		self.list_input_variable.insert(0,"input:")
		#da aggiustare questo trucco:
		self.list_input_variable.append("//variabili da dichiarare")
		self.list_input_variable.append("TbBOOLEAN VeTHMC_b_AWP_AftrRunExhTmCptrd;")
		
		self.list_calibration_variable.insert(0,"//calibrazioni")
		self.list_expected_output_variable.insert(0,"output:")
		self.list_expected_output_variable.append("//fine")
		self.print_variable_list()
		
		return
	
	def scrivi_su_file(self):
		print ("scritto su file")
		temp_join_list = (self.list_function_toTest + self.list_input_variable + self.list_calibration_variable + self.list_expected_output_variable)
		
		f = open("testo.txt",'w')
		for item in temp_join_list:
			f.write(item+"\n")
	
		f.close()
		
		return


class Second_window(QWidget):
	
	list_harness=[]
	list_Calibration_set =[]
	list_UTest = []
	contenuto = [] # will contatin
	
	# costruttore
	def __init__(self):
		super().__init__()
		
		
		
	def read_file_test(self):
		print("sono in read_file_test\n")
		f = open("file_test_scritto_perl2.txt", "r")
		self.contenuto = f.readlines()
		f.close()
		
		#print("contenuto prima",self.contento)
		self.read_contenuto()
		#print("contenuto dopo",self.contento)
		return 
	
	def init_second_windows(self,title):
		#set the size and the window title 
		self.setGeometry(200,180,650,800) #positionx,positiony,sizex,sizey
		self.setWindowTitle(title)
	
		#setting Tooltip
		QToolTip.setFont(QFont('Helvetica', 10))
		
		
		#---  HARNESS  ----#
		
		#labels
		harness_label = QLabel(self)
		#setting labels:
		harness_label.setText("per harness.h:")
		harness_label.move(10,30)
		
		#textArea
		self.harness_text = QPlainTextEdit(self)
		#setting QPlainTextEdit:
		self.harness_text.resize(600,200)
		self.harness_text.move(6,60)
		
		#---  CALIBRATION  ----#
		
		#labels
		calibration_label = QLabel(self)
		#setting labels:
		calibration_label.setText("per calibration.c:")
		calibration_label.move(10,280)
		
		#textArea
		self.calibration_text = QPlainTextEdit(self)
		#setting QPlainTextEdit:
		self.calibration_text.resize(600,200)
		self.calibration_text.move(6,300)
		
		#---  CppUTEST  ----#
		
		#labels
		utest_label = QLabel(self)
		#setting labels:
		utest_label.setText("per CppUTest.c:")
		utest_label.move(10,500)
		
		#textArea
		self.utest_text = QPlainTextEdit(self)
		#setting QPlainTextEdit:
		self.utest_text.resize(600,300)
		self.utest_text.move(6,520)
		
		
		for item in self.list_harness:
			self.harness_text.appendPlainText(item)
		
		
		for item in self.list_Calibration_set:
			self.calibration_text.appendPlainText(item)
		
		
		for item in self.list_UTest:
			self.utest_text.appendPlainText(item)
		
		
		self.show()
		return
	

	def load_list_harness(self,k):
		list_harness = [ ]
		exit_condition = 0
		counter = k
		while exit_condition != 1:
			item = self.contenuto[counter]
			if (item != "//PER CppUTest Calibration_set: \n"):
				list_harness.append(item)
				counter = counter+1
			else:
				exit_condition = 1
		return list_harness,counter

	def load_list_Calibration_set(self,k):
		list_Calibration_set = [ ]
		exit_condition = 0
		counter = k
		while exit_condition != 1:
			item = self.contenuto[counter]
			if (item != "//PER CppUTest Cpp_UTest: \n"):
				list_Calibration_set.append(item)
				counter = counter+1
			else:
				exit_condition = 1
				
		return list_Calibration_set,counter


	def load_list_UTest(self,k):
		list_UTest = [ ]
		counter = k
		size = len(self.contenuto) #ultimo elemento
		#caricare in lista fino all'utlimo elemento
		while counter != size:
			item = self.contenuto[counter] 
			list_UTest.append(item)
			counter = counter+1
			
		return list_UTest,counter
	
	
	def read_contenuto(self):
		k = 0
		for element in self.contenuto:
			if element == "//PER CppUTest harness: \n" :
				self.list_harness,k = self.load_list_harness(k)
		
			elif element == "//PER CppUTest Calibration_set: \n" :
				self.list_Calibration_set,k = self.load_list_Calibration_set(k)
		
			elif element == "//PER CppUTest Cpp_UTest: \n":
				self.list_UTest,k = self.load_list_UTest(k)
	
		k = k+1
		#fine for loop
		
		return
		

#fine classe

# -------  FUNCTION DEFINITION:    --------#


#eseguire perl script da python.
def launch_perl_script():
	#variable to pass as argument for the external script:
	interpreter = "perl"
	execute_script = "crea_test.pl"
	#launch the script:
	pipe = subprocess.run([interpreter, execute_script, "PTCS_G4DSLCSSE66_DE","24.24.161.40"])
	#avvia seconda windows
	sec_win.read_file_test() #crea il file o lo legge per la prima volra
	sec_win.init_second_windows("SHOW TEST")
	return
	




#MAIN:



#entry point for GUI
app = QApplication(sys.argv)

# create an instance of main root window
root = Root_mainWindow()
root.init_root_windows("SET INPUT")
sec_win = Second_window()


#when RUN is clicked launch the perl script.
root.btn_run_script.clicked.connect(launch_perl_script) # use the button signal "clicked"


sys.exit(app.exec_())



















