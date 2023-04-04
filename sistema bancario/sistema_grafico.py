import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QInputDialog

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.extrato = []
        self.dict_extarto = {}
        self.saldo = 0

        self.initUI()

    def initUI(self):

        # Criação dos widgets
        label1 = QLabel('Escolha a operação:')
        button1 = QPushButton('Depositar')
        button2 = QPushButton('Sacar')
        button3 = QPushButton('Mostrar extrato')
        button4 = QPushButton('Sair')

        # Adiciona os widgets no layout vertical
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addWidget(button3)
        vbox.addWidget(button4)

        # Criação da janela principal e adiciona o layout vertical
        self.setLayout(vbox)
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('Banco')

        # Conecta os botões às funções correspondentes
        button1.clicked.connect(self.depositar)
        button2.clicked.connect(self.sacar)
        button3.clicked.connect(self.mostrar_extrato)
        button4.clicked.connect(self.close)

        self.show()

    def depositar(self):
        deposito, ok = QInputDialog.getDouble(self, 'Depósito', 'Valor depósito:')
        if ok:
            if deposito < 0:
                QMessageBox.warning(self, 'Erro', 'Não é possível depositar valores menores do que 0')
            else:
                self.saldo += deposito
                self.extrato.append(deposito)
                self.dict_extrato = {
                    'Depositos': self.extrato
                }
                continuar, ok = QInputDialog.getText(self, 'Continuar?', 'Deseja continuar? (sim ou não)')
                if ok and continuar.lower() == 'sim':
                    self.depositar()

    def sacar(self):
        saque, ok = QInputDialog.getDouble(self, 'Saque', f'Saldo atual: R${self.saldo:.2f}\nValor a sacar:')
        if ok:
            if saque > self.saldo:
                QMessageBox.warning(self, 'Erro', 'Saldo insuficiente')
            else:
                self.saldo -= saque
                self.extrato.append(-saque)
                self.dict_extrato = {
                    'Depositos': [d for d in self.extrato if d > 0],
                    'Saques': [d for d in self.extrato if d < 0]
                }
                QMessageBox.information(self, 'Saque', f'Saque realizado com sucesso!\nNovo saldo: R${self.saldo:.2f}')

    def mostrar_extrato(self):
        extrato_str = f"{'Operação':<10} {'Valor':>10}\n"
        for op, val in self.dict_extrato.items():
            for v in val:
                extrato_str += f"{op:<10} R${v:.2f}\n"
        extrato_str += f"\n{'Saldo':<10} R${self.saldo:.2f}"
        QMessageBox.information(self, 'Extrato', extrato_str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())