from PySide.QtWidgets import QApplication,QMainWindow,QPushButton,QPlainTextEdit,QMessageBox,QLineEdit,QLabel
import socket

def handleCalc():
    info_IP=edit.text()
    info_route=edit2.text()
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    mysocket.connect((info_IP, infp_route))

    cmd = 'GET http://IP/romeo.txt HTTP/1.0\r\n\r\n'.encode()

    mysocket.send(cmd)

    while True:
        data = mysocket.recv(512)
        if (len(data) < 1):
            break
        str = data.decode()

    mysocket.close()
    connct.setPlainText(str)


app=QApplication([])
window=QMainWindow()
window.setWindowTitle('获取网址内的文件信息')
window.resize(500,500)
window.move(50,50)

connect=QPlainTextEdit(window)
connect.resize(400,300)
connect.move(10,200)
connect.setPlaceholderText('内容显示')

label1=QLabel(window)
label1.move(40,60)
label1.resize(130,20)
label1.setText('IP：')

label2=QLabel(window)
label2.move(120,60)
label2.resize(130,20)
label2.setText('route：')

edit=QLineEdit(window)
edit.move(60,60)
edit.setPlaceholderText('Please input IpAddress:')

edit2=QLineEdit(window)
edit2.move(140,60)
edit2.setPlaceholderText("Please input route:")



button=QPushButton(window)
button.resize(40,40)
button.move(150,150)
button.setText('OK')
button.clicked.connect(handleCalc)

window.show()
ap.exec_()