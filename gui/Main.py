import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QToolBar, QFileDialog, QMessageBox, QMainWindow

from PBDD import BDD
from prog.Alphabet import decryptVigenere, encryptVigenere, decryptCaesar, encryptCaesar
from prog.lfsr import LFSR


class Window(QMainWindow):
    # class MainWindow(object):
    def __init__(self):
        # def setupUi(self, Window):
        super(Window, self).__init__()
        self.setFixedSize(800, 600)
        self.setWindowTitle('BDD (Бинарные решающие диаграммы) в Логическом Криптоанализе')
        self.setWindowIcon(QIcon('icons/public.png'))

        self.init_Action()
        self.init_Content()
        self.init_StatusBar()
        self.init_Menu()
        self.init_ToolBar()
        self.set_Actions2Menu()
        self.set_Actions2StatusBar()
        self.set_Actions2ToolBar()
        self.set_Triggers2Actions()
        self.show()

    def init_Content(self):
        self.centralwidget = QtWidgets.QWidget(self)

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 765, 565))
        self.tabWidget.setStyleSheet("")

        ########____ПЕРВАЯ ВКЛАДКА____
        self.tab1 = QtWidgets.QWidget()
        self.horizontalLayoutWidget1 = QtWidgets.QWidget(self.tab1)
        self.horizontalLayoutWidget1.setGeometry(QtCore.QRect(8, 8, 740, 528))
        self.MainLayout1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget1)
        self.MainLayout1.setContentsMargins(0, 0, 0, 0)

        self.LeftVlLayout1 = QtWidgets.QVBoxLayout()

        self.option1HLayout1 = QtWidgets.QHBoxLayout()
        self.labelKey1 = QtWidgets.QLabel(self.horizontalLayoutWidget1)
        self.labelKey1.setText("<h3>Число тактов: </h3>")
        self.keyLine1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget1)
        self.option1HLayout1.addWidget(self.labelKey1)
        self.option1HLayout1.addWidget(self.keyLine1)
        self.LeftVlLayout1.addLayout(self.option1HLayout1)

        self.option2HLayout1 = QtWidgets.QHBoxLayout()
        self.labelTaps = QtWidgets.QLabel(self.horizontalLayoutWidget1)
        self.labelTaps.setText("<h3>Регистры сдвига: </h3>")
        self.tapsLine = QtWidgets.QLineEdit(self.horizontalLayoutWidget1)
        self.option2HLayout1.addWidget(self.labelTaps)
        self.option2HLayout1.addWidget(self.tapsLine)
        self.LeftVlLayout1.addLayout(self.option2HLayout1)

        self.labelInput1 = QtWidgets.QLabel(self.horizontalLayoutWidget1)
        self.labelInput1.setText("<h3>Ввод последовательности:</h3>")
        self.labelInput1.setText("<h3>Ввод последовательности:</h3>")
        self.textInput1 = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget1)
        self.LeftVlLayout1.addWidget(self.labelInput1)
        self.LeftVlLayout1.addWidget(self.textInput1)

        self.buttonHLayout1 = QtWidgets.QHBoxLayout()
        self.encryptButton1 = QtWidgets.QPushButton(self.horizontalLayoutWidget1)
        self.encryptButton1.setText("Зашифровать")
        self.encryptButton1.setStatusTip("Зашифровать")
        self.buttonHLayout1.addWidget(self.encryptButton1)
        self.encryptButton1.clicked.connect(self.LFSR)
        self.LeftVlLayout1.addLayout(self.buttonHLayout1)

        self.labelOutput1 = QtWidgets.QLabel(self.horizontalLayoutWidget1)
        self.labelOutput1.setText("<h3>Вывод результата:</h4>")
        self.textOutput1 = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget1)
        self.LeftVlLayout1.addWidget(self.labelOutput1)
        self.LeftVlLayout1.addWidget(self.textOutput1)
        self.MainLayout1.addLayout(self.LeftVlLayout1)

        self.RightVLayout1 = QtWidgets.QVBoxLayout()

        self.labelFormula1 = QtWidgets.QLabel(self.horizontalLayoutWidget1)
        self.labelFormula1.setText("<h3>Формулы:</h4>")
        self.textFormula1 = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget1)
        self.labelResult1 = QtWidgets.QLabel(self.horizontalLayoutWidget1)
        self.textResult1 = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget1)
        self.RightVLayout1.addWidget(self.labelFormula1)
        self.RightVLayout1.addWidget(self.textFormula1)
        self.RightVLayout1.addWidget(self.textResult1)

        self.MainLayout1.addLayout(self.RightVLayout1)
        self.tabWidget.addTab(self.tab1, "РСЛОС")
        self.tabWidget.setCurrentIndex(0)

        ########____ВТОРАЯ ВКЛАДКА____
        self.tab2 = QtWidgets.QWidget()
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(8, 8, 740, 528))

        self.MainLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.MainLayout.setContentsMargins(0, 0, 0, 0)

        self.LeftVlLayout = QtWidgets.QVBoxLayout()

        self.option1HLayout = QtWidgets.QHBoxLayout()
        self.labelKey = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelKey.setText("<h3>Ключ: </h3>")
        self.keyLine = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.option1HLayout.addWidget(self.labelKey)
        self.option1HLayout.addWidget(self.keyLine)
        self.LeftVlLayout.addLayout(self.option1HLayout)

        self.labelInput = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelInput.setText("<h3>Входной текст:</h3>")
        self.textInput = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.LeftVlLayout.addWidget(self.labelInput)
        self.LeftVlLayout.addWidget(self.textInput)

        self.buttonHLayout = QtWidgets.QHBoxLayout()
        self.encryptButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.encryptButton.setText("Зашифровать")
        self.encryptButton.setStatusTip("Зашифровать")
        self.decryptButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.decryptButton.setText("Расшифровать")
        self.decryptButton.setStatusTip("Расшифровать")
        self.buttonHLayout.addWidget(self.decryptButton)
        self.buttonHLayout.addWidget(self.encryptButton)
        self.decryptButton.clicked.connect(self.Decrypt)
        self.encryptButton.clicked.connect(self.Encrypt)

        self.LeftVlLayout.addLayout(self.buttonHLayout)
        self.labelOutput = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelOutput.setText("<h3>Вывод результата:</h4>")
        self.textOutput = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.LeftVlLayout.addWidget(self.labelOutput)
        self.LeftVlLayout.addWidget(self.textOutput)

        self.MainLayout.addLayout(self.LeftVlLayout)

        self.RightVLayout = QtWidgets.QVBoxLayout()

        self.labelFormula = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelFormula.setText("<h3>Формулы:</h4>")
        self.textFormula = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.labelResult = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.textResult = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)

        self.RightVLayout.addWidget(self.labelFormula)
        self.RightVLayout.addWidget(self.textFormula)
        self.RightVLayout.addWidget(self.textResult)
        self.MainLayout.addLayout(self.RightVLayout)

        self.tabWidget.addTab(self.tab2, "Шифр Виженера и Шифр Цезаря")

        self.setCentralWidget(self.centralwidget)
        self.tabWidget.setCurrentIndex(0)

    def init_StatusBar(self):
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setSizeGripEnabled(True)
        self.setStatusBar(self.statusbar)

    def init_Action(self):
        self.SaveAction = QtWidgets.QAction(QIcon('icons/save.png'), "Сохранить", self)
        self.ExitAction = QtWidgets.QAction(QIcon('icons/exit.png'), "Выход", self)
        self.HelpAction = QtWidgets.QAction(QIcon('icons/question.png'), "Помощь", self)
        self.AboutAction = QtWidgets.QAction(QIcon('icons/about.png'), "О программе", self)
        self.buildBddAction = QtWidgets.QAction(QIcon('icons/bdd1.png'), 'Построить  BDD', self)
        self.buildRobddAction = QtWidgets.QAction(QIcon('icons/robdd1.png'), 'Построить  ROBDD', self)

        self.SaveAction.setShortcut(('Ctrl+S'))
        self.ExitAction.setShortcut('Ctrl+Q')
        self.HelpAction.setShortcut('Ctrl+H')
        self.AboutAction.setShortcut('Ctrl+I')

    def set_Actions2StatusBar(self):

        self.SaveAction.setStatusTip('Сохранить')
        self.ExitAction.setStatusTip('Выход')
        self.HelpAction.setStatusTip('Помощь')
        self.AboutAction.setStatusTip('О программе')
        self.buildBddAction.setStatusTip('Построить BDD')
        self.buildRobddAction.setStatusTip('Построить ROBDD')

    def set_Triggers2Actions(self):
        self.SaveAction.triggered.connect(self.save1)
        self.ExitAction.triggered.connect(self.close)
        self.HelpAction.triggered.connect(self.help)
        self.AboutAction.triggered.connect(self.about)
        self.buildBddAction.triggered.connect(self.buildBdd)
        self.buildRobddAction.triggered.connect(self.buildRobdd)

    def init_Menu(self):
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.fileMenu = QtWidgets.QMenu(self.menubar)
        self.helpMenu = QtWidgets.QMenu(self.menubar)
        self.fileMenu.setTitle("Файл ")
        self.helpMenu.setTitle("Справка")
        self.menubar.addAction(self.fileMenu.menuAction())
        self.menubar.addAction(self.helpMenu.menuAction())
        self.setMenuBar(self.menubar)

    def set_Actions2Menu(self):
        self.fileMenu.addAction(self.SaveAction)
        self.fileMenu.addAction(self.ExitAction)
        self.helpMenu.addAction(self.HelpAction)
        self.helpMenu.addAction(self.AboutAction)

    def init_ToolBar(self):
        self.toolbar = QToolBar()
        self.addToolBar(Qt.LeftToolBarArea, self.toolbar)

    def set_Actions2ToolBar(self):
        self.toolbar.addAction(self.buildBddAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.buildRobddAction)
        self.toolbar.addSeparator()
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.SaveAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.HelpAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.ExitAction)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Выход', "Вы действительно хотите нас покинуть?",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:

            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def save1(self):
        name = QFileDialog.getSaveFileName(self, "Сохранить файл", filter="Text Files (*.txt)")[0]
        file = open(name, 'w')
        text = self.textResult1.toPlainText()
        file.write(text)
        file.close()

    #def save(self):




    def about(self):
        QMessageBox.about(self, 'О программе',
                          "Исследование библиотеки BDD и ее применение в решении задач логического криптоанализа")

    def help(self):
        QMessageBox.information(self, 'Помощь', "БИБЛИОТЕКА PBDD (PBL)\n"
                                                "\n"
                                                "3.1.1	Операторы\n"
                                                "В библиотеке используются следующие операторы:\n"
                                                "•	И               -	обозначение: &\n"
                                                "•	ИЛИ             -	обозначение: |\n"
                                                "•	Эквиваленция    - 	обозначение: <=>\n"
                                                "•	Импликация	    -	обозначение: =>\n"
                                                "•	Отрицание	    -	обозначение: ~\n"
                                                "•	Исключающее ИЛИ	-   обозначение: XOR\n"
                                                "•	Скобки          -	обозначение: ( )\n"
                                                "\n"
                                                "\n"
                                                "3.1.2	Ключевые слова\n"
                                                "Ниже перечислены ключевые слова, которые не могут использоваться как имена переменных вместе с кратким описанием\n"
                                                "Var_Order	-	Используется при объявлении порядка переменных\n"
                                                "Main_Exp	-	Используется для определения логического выражения\n"
                                                "XOR		    -	Оператор «Исключающее ИЛИ»\n"
                                                "\n"
                                                "\n"
                                                "3.1.3	Объявление переменных и формул.\n"
                                                "Порядок переменных объявляется следующим способом:\n"
                                                "Var_Order : x1 x2 x3\n"
                                                "\n"
                                                "Нет ограничения единственного объявления переменных. Есть возможность объявлять переменные несколько раз, только не следует их повторять. Например:\n"
                                                "Var_Order : x1 x2 x3\n"
                                                "Var_Order : x4 y1 y2\n"
                                                "\n"
                                                "Чтобы объявить формулу достаточно использовать оператор «=». Например X представляет собой x1 & x2 & ~x3. Для этого достаточно написать:\n"
                                                "X = x1 & x2 & ~x3.\n"
                                                "Теперь Х можно использовать вместо x1 & x2 & ~x3 в других формулах.\n"
                                                "После того, как произведены объявление всех переменных и формул, с помощью Main_Exp можно задать выражение, которое нужно действительно решить. Например, есть две формулы, хранящиеся в X1 и X2, и нужно решить конъюнкцию формул, то имеем запись:\n"
                                                "Main_Exp : X1 & X2.\n"
                                                "\n"
                                                "3.1.4	Дополнительное\n"
                                                "Есть возможность оставлять комментарии, для этого достаточно перед строкой комментария поставить символ #.\n")

    def buildBdd(self):

        file = QFileDialog.getOpenFileName(self, 'Открыть файл',"","Text Files (*.txt)")[0]
        filele = open(file)
        data = filele.read()
        self.textFormula1.setPlainText(data)
        bdd = BDD.bdd_init(file)
        BDD.ite_build(bdd)

        stats = BDD.stat_string(bdd)
        sat_count = BDD.sat_count(bdd)
        sat_assigns = BDD.all_sat(bdd)
        sat_assigns_string = ""
        for x in sat_assigns:
            sat_assigns_string += str(x) + "\n"

        STAT_str = "Number of satisfying assignments: " + str(sat_count) + "\n" \
                   + stats + "\n\nAll satisfying assignts:\n" + "------------------------------\n" \
                   + sat_assigns_string

        self.textResult1.setPlainText(STAT_str)

    def buildRobdd(self):
        file = QFileDialog.getOpenFileName(self, 'Открыть файл',"","Text Files (*.txt)")[0]
        filele = open(file)
        data = filele.read()
        self.textFormula1.setPlainText(data)

        bdd = BDD.bdd_init(file)
        BDD.ite_build(bdd)
        BDD.reorder_ite_build(bdd)

        stats = BDD.stat_string(bdd)
        sat_count = BDD.sat_count(bdd)
        sat_assigns = BDD.all_sat(bdd)
        sat_assigns_string = ""
        for x in sat_assigns:
            sat_assigns_string += str(x) + "\n"
            print(x)

        BDD.dot_bdd(bdd)
        STAT_str = "Number of satisfying assignments: " + str(sat_count) + "\n" \
                   + stats + "\n\nAll satisfying assignts:\n" + "------------------------------\n" \
                   + sat_assigns_string

        self.textResult1.setPlainText(STAT_str)

    def LFSR(self):
        key = int(self.keyLine1.text())
        text = list(self.textInput1.toPlainText())
        seed = []
        for i in range(len(text)):
            seed.append(int(text[i]))
        tapsstr = self.tapsLine.text()
        tapslist = tapsstr.split(",")
        taps = []
        for i in range(len(tapslist)):
            taps.append(int(tapslist[i]))
        print(taps, type(taps))
        code = LFSR(seed, taps, key)
        print(code, type(code))
        self.textOutput1.setPlainText(code)

    def Encrypt(self):
        key = self.keyLine.text()
        key = key.upper()
        word = str(self.textInput.toPlainText())
        word = word.upper().replace('', '')
        if key.isalpha():
            text = encryptVigenere(key, word)
        elif key.isdigit():
            text = encryptCaesar(key, word)
        self.textOutput.setPlainText(text)

    def Decrypt(self):
        key = self.keyLine.text()
        key = key.upper()
        word = str(self.textInput.toPlainText())
        word = word.upper().replace(' ', '')
        if key.isalpha():
            text = decryptVigenere(key, word)
        elif key.isdigit():
            text = decryptCaesar(key, word)
        self.textOutput.setPlainText(text)


def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())