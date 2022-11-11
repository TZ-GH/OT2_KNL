from PyQt5 import QtWidgets, uic

def testaccess(celaapp):
    return celaapp.spinBox.value

def zmena(x):
    y = window.spinBox.value() + 1
    print(x,y)

def main():
    app = QtWidgets.QApplication([])



    window = QtWidgets.QMainWindow()

    with open('TestQT.ui') as f:
        uic.loadUi(f, window)

    window.show()

    window.spinBox.valueChanged.connect(zmena)

    return app.exec()

main()