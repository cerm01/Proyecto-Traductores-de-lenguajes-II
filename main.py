from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
import sys


class Lexico(object):
    def __init__(self, cadena, id, tipo):
        self.cadena = cadena
        self.token = id
        self.tipo = tipo

    def __str__(self):
        return "%s  %s" % (self.cadena, self.token)
        
    def obtenercadena(self):
       return self.cadena

    def obtenertoken(self):
        return self.token

    def obtenerdescripcion(self):
        return self.tipo

    
class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(980,650)
        self.setWindowTitle("Analizador lexico")
        
        self.tablaResultados = QTableWidget(self)
        
        if (self.tablaResultados.columnCount()<3):
            self.tablaResultados.setColumnCount(3)
        
        __qtablewidgetitem = QTableWidgetItem("TOKEN")
        self.tablaResultados.setHorizontalHeaderItem(1, __qtablewidgetitem)
        __qtablewidgetitem = QTableWidgetItem("CADENA")
        self.tablaResultados.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem = QTableWidgetItem("DESCRIPCIÓN")
        self.tablaResultados.setHorizontalHeaderItem(2, __qtablewidgetitem)
       
        self.tablaResultados.setColumnWidth(0,451)
        self.tablaResultados.setColumnWidth(1,89)
        self.tablaResultados.setColumnWidth(2,360)
        self.tablaResultados.setGeometry(QRect(20,300,940,340))

        self.inputTexto = QTextEdit(self)
        self.inputTexto.setGeometry(QRect(40,20,380,250))
        
        font = QFont()
        font.setPointSize(15)
        self.inputTexto.setFont(font)

        self.boton = QPushButton("VALIDAR",self)
        self.boton.setGeometry(QRect(440,125,100,50))

        self.inputTexto_2 = QTextEdit(self)
        self.inputTexto_2.setGeometry(QRect(560,20,380,250))
        font = QFont()
        font.setPointSize(15)
        self.inputTexto_2.setFont(font)
        
        self.boton.clicked.connect(self.Analizador)


    def Analizador(self):
        cadena = str(self.inputTexto.toPlainText())
        listaLexico = list()
        i = 0
        size = len(cadena)
        cadena = cadena + " "
        cadenaTemp = ""

        while i < size:
            cadenaTemp = ""
            if cadena[i].isalpha() == True:
                while cadena[i].isalpha() == True or cadena[i].isdigit() == True:
                    if cadena[i] == " ":
                        break
                    cadenaTemp = cadenaTemp + cadena[i]
                    i = i+1
                    if i==size:
                        break
                if cadenaTemp == "if":
                    tiposDeDato = Lexico(cadenaTemp, 9, "IF")
                    listaLexico.append(tiposDeDato)
                elif cadenaTemp == "while":
                    tiposDeDato = Lexico(cadenaTemp, 10, "WHILE")
                    listaLexico.append(tiposDeDato)
                elif cadenaTemp == "return":
                    tiposDeDato = Lexico(cadenaTemp, 11, "RETURN")
                    listaLexico.append(tiposDeDato)
                elif cadenaTemp == "else":
                    tiposDeDato = Lexico(cadenaTemp, 12, "ELSE")
                    listaLexico.append(tiposDeDato)
                elif cadenaTemp == "int":
                    tiposDeDato = Lexico(cadenaTemp, 0, "Tipo de dato")
                    listaLexico.append(tiposDeDato)
                elif cadenaTemp == "float":
                    tiposDeDato = Lexico(cadenaTemp, 0, "Tipo de dato")
                    listaLexico.append(tiposDeDato)
                elif cadenaTemp == "char":
                    tiposDeDato = Lexico(cadenaTemp, 0, "Tipo de dato")
                    listaLexico.append(tiposDeDato)
                elif cadenaTemp == "void":
                    tiposDeDato = Lexico(cadenaTemp, 0, "Tipo de dato")
                    listaLexico.append(tiposDeDato)
                else:
                    tiposDeDato = Lexico(cadenaTemp, 1, "ID")
                    listaLexico.append(tiposDeDato)

            elif cadena[i].isdigit() == True:
                while cadena[i].isdigit() == True:
                    cadenaTemp = cadenaTemp + cadena[i]
                    i = i+1
                    if i==size:
                        break
                tiposDeDato = Lexico(cadenaTemp, 13, "Constante")
                listaLexico.append(tiposDeDato)
                
            elif (cadena[i] == "|" and cadena[i+1] == "|") or (cadena[i] == "&" and cadena[i+1] == "&"):
               cadenaTemp = cadena[i] + cadena[i+1]
               tiposDeDato = Lexico(cadenaTemp, 17, "Operador logico")
               listaLexico.append(tiposDeDato)
               i = i +2
            
            elif cadena[i] == "+" or cadena[i] == "-":
                cadenaTemp = cadena[i]
                tiposDeDato = Lexico(cadenaTemp, 14, "Operador suma")
                listaLexico.append(tiposDeDato)
                i = i +1
            
            
            elif cadena[i] == "*" or cadena[i] == "/":
                cadenaTemp = cadena[i]
                tiposDeDato = Lexico(cadenaTemp,16, "Operador multiplicación ")
                listaLexico.append(tiposDeDato)
                i = i +1

            elif (cadena[i] == "=" and cadena[i+1] == "=") or (cadena[i] == "<" and cadena[i+1] == "=") or (cadena[i] == ">" and cadena[i+1] == "=") or (cadena[i] == "!" and cadena[i+1] == "="):
                cadenaTemp = cadena[i] + cadena[i+1]
                tiposDeDato = Lexico(cadenaTemp, 17, "Operador relacional")
                listaLexico.append(tiposDeDato)
                i = i +2

            elif cadena[i] == "<" or cadena[i] == ">":
                cadenaTemp = cadena[i]
                tiposDeDato = Lexico(cadenaTemp, 17, "Operador relacional ")
                listaLexico.append(tiposDeDato)
                i = i + 1

            elif cadena[i] == "$":
                cadenaTemp = "$"
                tiposDeDato = Lexico(cadenaTemp, 18, "$")
                listaLexico.append(tiposDeDato)
                i = i + 1
            
            elif cadena[i] == ";":
                cadenaTemp = ";"
                tiposDeDato = Lexico(cadenaTemp, 2, "Punto y coma")
                listaLexico.append(tiposDeDato)
                i = i + 1
            
            elif cadena[i] == ",":
                cadenaTemp = ","
                tiposDeDato = Lexico(cadenaTemp, 3, "Coma")
                listaLexico.append(tiposDeDato)
                i = i + 1
            
            elif cadena[i] == "(":
                cadenaTemp = "("
                tiposDeDato = Lexico(cadenaTemp, 4, "Parentesis izquierdo")
                listaLexico.append(tiposDeDato)
                i = i + 1
            
            elif cadena[i] == ")":
                cadenaTemp = ")"
                tiposDeDato = Lexico(cadenaTemp, 5, "Parentesis derecho")
                listaLexico.append(tiposDeDato)
                i = i + 1
            
            elif cadena[i] == "{":
                cadenaTemp = "{"
                tiposDeDato = Lexico(cadenaTemp, 6, "Llave izquierda")
                listaLexico.append(tiposDeDato)
                i = i + 1

            elif cadena[i] == "}":
                cadenaTemp = "}"
                tiposDeDato = Lexico(cadenaTemp, 7, "Llave derecha")
                listaLexico.append(tiposDeDato)
                i = i + 1
            
            elif cadena[i] == "=":
                cadenaTemp = "="
                tiposDeDato = Lexico(cadenaTemp, 8, "Igual")
                listaLexico.append(tiposDeDato)
                i = i + 1

            elif cadena[i] == " ":
                i = i + 1

            else:
                i = i+1

    
        row=0
        self.tablaResultados.setRowCount(len(listaLexico))
        for tiposDeDato in listaLexico:
            aux = tiposDeDato.obtenercadena()
            aux2 = tiposDeDato.obtenertoken()
            aux3 = tiposDeDato.obtenerdescripcion()
            self.tablaResultados.setItem(row,0, QtWidgets.QTableWidgetItem(str(aux)))
            self.tablaResultados.setItem(row,1, QtWidgets.QTableWidgetItem(str(aux2)))
            self.tablaResultados.setItem(row,2, QtWidgets.QTableWidgetItem(str(aux3)))
            row = row+1



app = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
app.exec()