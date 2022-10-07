from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QTextEdit,QMessageBox
from socket import *

def handleCalc():
    IP = '0.0.0.0'
    PORT = 50000
    BUFLEN = 512

    listenSocket = socket(AF_INET,SOCK_STREAM)
    listenSocket.bind((IP,PORT))

    listenSocket.listen(8)
    textEdit.setPlainText(f'''服务启动成功！！！\n监听在{PORT}端口\n等待客户连接......''')

    dataSocket, addr = listenSocket.accept()
    

app = QApplication([])

window = QMainWindow()
window.resize(500, 400)
window.move(300, 310)
window.setWindowTitle('Message Server')

textEdit = QTextEdit(window)

textEdit.move(10,25)
textEdit.resize(300,350)

button = QPushButton('Start', window)
button.move(380,80)

window.show()

button.clicked.connect(handleCalc)

app.exec_()