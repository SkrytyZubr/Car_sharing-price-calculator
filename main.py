from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class calculator(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.dict_result = {}
        self.gui()

    def gui(self):

        label1 = QLabel('Kilometry:', self)
        label2 = QLabel('Minuty:', self)
        label3 = QLabel('Najniższa cena:', self)

        position = QGridLayout()
        position.addWidget(label1, 0, 0)
        position.addWidget(label2, 0, 1)
        position.addWidget(label3, 0, 2)

        self.value_lab_1 = QLineEdit()
        self.value_lab_2 = QLineEdit()
        self.result = QLineEdit()

        self.result.readonly = True
        self.result.setToolTip('Wpisz <b>liczby</b>')

        position.addWidget(self.value_lab_1, 1, 0)
        position.addWidget(self.value_lab_2, 1, 1)
        position.addWidget(self.result, 1, 2)

        calculateBtn = QPushButton('Oblicz', self)

        position.addWidget(calculateBtn, 2, 1)

        self.setLayout(position)

        self.setGeometry(20, 20, 500, 50)
        self.setWindowIcon(QIcon('images/car.png'))
        self.setWindowTitle("Car-sharing price calculator")
        self.show()

        calculateBtn.clicked.connect(self.call)

    def call(self):

        signal = self.sender()

        number_1 = float(self.value_lab_1.text())
        number_2 = float(self.value_lab_2.text())
        result_over = ''

        if signal.text() == 'Oblicz':

            company = ('Traficar clio', 'MiiMove Astra', 'MiiMove Ampera', 'Panek economt sta', 
                'Panek economt kil', 'Panek economt min', 'Panek comfort sta', 'Panek comfort kil', 
                'Panek comfort min', '4mobility economy', '4mobility premium')
            price_star = (2.99, 0, 0, 0, 2.89, 2.89, 0, 2.89, 2.89, 0, 0)
            price_km = (1.5, 0.8, 0, 0.8, 0, 0.99, 0.82, 0, 1.29, 0.8, 0.8)
            price_min = (0, 0.67, 1.19, 0.55, 1.49, 0, 0.8, 1.99, 0, 0.5, 0.8)

            for a in range(0,11):
                self.algorithm(number_1, number_2, company[a], price_star[a], price_km[a], price_min[a])
            
            result_over = min(self.dict_result, key=self.dict_result.get), + min(self.dict_result.values())

            self.result.setText(str(result_over))
    
    def algorithm(self, time, distance, company, start, km, min):
        alg_result = round(time*min + distance*km + start, 2)
        self.dict_result[company] = alg_result

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = calculator()
    sys.exit(app.exec_())