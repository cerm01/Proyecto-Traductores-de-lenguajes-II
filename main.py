from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
import sys


class Lexico(object):
    #Constructor de la clase
    def __init__(self, cadena, id, tipo):
        self.cadena = cadena
        self.token = id
        self.tipo = tipo
    #Retorna la cadena y el token
    def __str__(self):
        return "%s  %s" % (self.cadena, self.token)
    #Retorna la cadena
    def obtenercadena(self):
       return self.cadena
    #Retorna el token
    def obtenertoken(self):
        return self.token
    #Retorna la descripcion
    def obtenerdescripcion(self):
        return self.tipo

    
class MainWindow(QMainWindow):
    #
    def __init__(self):
        super(MainWindow, self).__init__() #Constructor de la clase padre
        self.setFixedSize(980,650) #Tamaño de la ventana
        self.setWindowTitle("Analizador lexico")

        self.tablaResultados = QTableWidget(self) #Tabla
        
        if (self.tablaResultados.columnCount()<3): #Si la tabla tiene menos de 3 columnas
            self.tablaResultados.setColumnCount(3)
        
        __qtablewidgetitem = QTableWidgetItem("TOKEN") #Crea un item
        self.tablaResultados.setHorizontalHeaderItem(1, __qtablewidgetitem) #Agrega el item a la tabla
        __qtablewidgetitem = QTableWidgetItem("CADENA") #Crea un item
        self.tablaResultados.setHorizontalHeaderItem(0, __qtablewidgetitem) #Agrega el item a la tabla
        __qtablewidgetitem = QTableWidgetItem("DESCRIPCIÓN") #Crea un item 
        self.tablaResultados.setHorizontalHeaderItem(2, __qtablewidgetitem) #Agrega el item a la tabla
       
        self.tablaResultados.setColumnWidth(0,451) #Tamaño de las columnas
        self.tablaResultados.setColumnWidth(1,89) #Tamaño de las columnas
        self.tablaResultados.setColumnWidth(2,360) #Tamaño de las columnas
        self.tablaResultados.setGeometry(QRect(20,300,940,340)) #Posicion y tamaño de la tabla

        self.inputTexto = QTextEdit(self) #Input de la cadena
        self.inputTexto.setGeometry(QRect(40,20,380,250)) #Posicion y tamaño del input
        
        font = QFont()  #Fuente
        font.setPointSize(15) #Tamaño de la fuente
        self.inputTexto.setFont(font) #Agrega la fuente al input

        self.boton = QPushButton("VALIDAR",self) #Boton
        self.boton.setGeometry(QRect(440,125,100,50)) #Posicion y tamaño del boton

        self.inputTexto_2 = QTextEdit(self) #Input de la tabla
        self.inputTexto_2.setGeometry(QRect(560,20,380,250)) #Posicion y tamaño del input
        font = QFont() #Fuente
        font.setPointSize(15) #Tamaño de la fuente
        self.inputTexto_2.setFont(font) #Agrega la fuente al input
        self.boton.clicked.connect(self.Analizador) #Conecta el boton con el metodo analizador


    def Analizador(self):
        cadena = str(self.inputTexto.toPlainText()) #Obtiene el texto del input
        listaLexico = list() #Lista de tipo Lexico
        i = 0 #Contador
        size = len(cadena) #Tamaño de la cadena
        cadena = cadena + " " #Agrega un espacio al final de la cadena
        cadenaTemp = "" #Cadena temporal
        # Ciclo que recorre la cadena
        while i < size:
            cadenaTemp = ""
            # Si es una letra
            if cadena[i].isalpha() == True:
                # Ciclo que recorre la cadena
                while cadena[i].isalpha() == True or cadena[i].isdigit() == True: # Si es una letra o un digito
                    # Si es una letra
                    if cadena[i] == " ":
                        break
                    cadenaTemp = cadenaTemp + cadena[i]
                    i = i+1
                    if i==size:
                        break
                # Si la cadena es una palabra reservada
                if cadenaTemp == "if": # Si es if
                    tiposDeDato = Lexico(cadenaTemp, 9, "IF")
                    listaLexico.append(tiposDeDato)
                elif cadenaTemp == "while": # Si es while
                    tiposDeDato = Lexico(cadenaTemp, 10, "WHILE")
                    listaLexico.append(tiposDeDato)
                elif cadenaTemp == "return": # Si es return
                    tiposDeDato = Lexico(cadenaTemp, 11, "RETURN")
                    listaLexico.append(tiposDeDato)
                elif cadenaTemp == "else": # Si es else
                    tiposDeDato = Lexico(cadenaTemp, 12, "ELSE")
                    listaLexico.append(tiposDeDato)
                elif cadenaTemp == "int":  # Si es int
                    tiposDeDato = Lexico(cadenaTemp, 0, "Tipo de dato")
                    listaLexico.append(tiposDeDato)
                elif cadenaTemp == "float": # Si es float
                    tiposDeDato = Lexico(cadenaTemp, 0, "Tipo de dato")
                    listaLexico.append(tiposDeDato)
                elif cadenaTemp == "char": # Si es char
                    tiposDeDato = Lexico(cadenaTemp, 0, "Tipo de dato")
                    listaLexico.append(tiposDeDato)
                elif cadenaTemp == "void": # Si es void
                    tiposDeDato = Lexico(cadenaTemp, 0, "Tipo de dato")
                    listaLexico.append(tiposDeDato)
                else:
                    tiposDeDato = Lexico(cadenaTemp, 1, "ID")
                    listaLexico.append(tiposDeDato)
            # Si es un digito
            elif cadena[i].isdigit() == True:
                while cadena[i].isdigit() == True:
                    cadenaTemp = cadenaTemp + cadena[i]
                    i = i+1
                    if i==size:
                        break
                tiposDeDato = Lexico(cadenaTemp, 13, "Constante")
                listaLexico.append(tiposDeDato)
            # Si es un caracter de tipo operarador logico    
            elif (cadena[i] == "|" and cadena[i+1] == "|") or (cadena[i] == "&" and cadena[i+1] == "&"):
               cadenaTemp = cadena[i] + cadena[i+1]
               tiposDeDato = Lexico(cadenaTemp, 15, "Operador logico")
               listaLexico.append(tiposDeDato)
               i = i +2
            # Si es un caracter de tipo operador suma
            elif cadena[i] == "+" or cadena[i] == "-":
                cadenaTemp = cadena[i]
                tiposDeDato = Lexico(cadenaTemp, 14, "Operador suma")
                listaLexico.append(tiposDeDato)
                i = i +1
            
            # Si es un caracter de tipo operador multiplicacion
            elif cadena[i] == "*" or cadena[i] == "/":
                cadenaTemp = cadena[i]
                tiposDeDato = Lexico(cadenaTemp,16, "Operador multiplicación ")
                listaLexico.append(tiposDeDato)
                i = i +1
            # Si es un caracter de tipo operador relacional
            elif (cadena[i] == "=" and cadena[i+1] == "=") or (cadena[i] == "<" and cadena[i+1] == "=") or (cadena[i] == ">" and cadena[i+1] == "=") or (cadena[i] == "!" and cadena[i+1] == "="):
                cadenaTemp = cadena[i] + cadena[i+1]
                tiposDeDato = Lexico(cadenaTemp, 17, "Operador relacional")
                listaLexico.append(tiposDeDato)
                i = i +2
            # Si es un caracter de tipo operador relacional
            elif cadena[i] == "<" or cadena[i] == ">":
                cadenaTemp = cadena[i]
                tiposDeDato = Lexico(cadenaTemp, 17, "Operador relacional ")
                listaLexico.append(tiposDeDato)
                i = i + 1
            # Sie es un $
            elif cadena[i] == "$":
                cadenaTemp = "$"
                tiposDeDato = Lexico(cadenaTemp, 18, "$")
                listaLexico.append(tiposDeDato)
                i = i + 1
            # Si es un ;
            elif cadena[i] == ";":
                cadenaTemp = ";"
                tiposDeDato = Lexico(cadenaTemp, 2, "Punto y coma")
                listaLexico.append(tiposDeDato)
                i = i + 1
            # Si es una ,
            elif cadena[i] == ",":
                cadenaTemp = ","
                tiposDeDato = Lexico(cadenaTemp, 3, "Coma")
                listaLexico.append(tiposDeDato)
                i = i + 1
            # Si es un (
            elif cadena[i] == "(":
                cadenaTemp = "("
                tiposDeDato = Lexico(cadenaTemp, 4, "Parentesis izquierdo")
                listaLexico.append(tiposDeDato)
                i = i + 1
            # Si es un )
            elif cadena[i] == ")":
                cadenaTemp = ")"
                tiposDeDato = Lexico(cadenaTemp, 5, "Parentesis derecho")
                listaLexico.append(tiposDeDato)
                i = i + 1
            # Si es un {
            elif cadena[i] == "{":
                cadenaTemp = "{"
                tiposDeDato = Lexico(cadenaTemp, 6, "Llave izquierda")
                listaLexico.append(tiposDeDato)
                i = i + 1
            # Si es un }
            elif cadena[i] == "}":
                cadenaTemp = "}"
                tiposDeDato = Lexico(cadenaTemp, 7, "Llave derecha")
                listaLexico.append(tiposDeDato)
                i = i + 1
            # Si es un =
            elif cadena[i] == "=":
                cadenaTemp = "="
                tiposDeDato = Lexico(cadenaTemp, 8, "Igual")
                listaLexico.append(tiposDeDato)
                i = i + 1
            # Si es un espacio
            elif cadena[i] == " ":
                i = i + 1
            # Si es un caracter invalido
            else:
                i = i+1

    
        row=0 #Fila
        self.tablaResultados.setRowCount(len(listaLexico)) #Numero de filas
        for tiposDeDato in listaLexico: #Ciclo que recorre la lista
            aux = tiposDeDato.obtenercadena() #Obtiene la cadena
            aux2 = tiposDeDato.obtenertoken() #Obtiene el token
            aux3 = tiposDeDato.obtenerdescripcion() #Obtiene la descripcion
            self.tablaResultados.setItem(row,0, QtWidgets.QTableWidgetItem(str(aux))) #Agrega la cadena a la tabla
            self.tablaResultados.setItem(row,1, QtWidgets.QTableWidgetItem(str(aux2))) #Agrega el token a la tabla
            self.tablaResultados.setItem(row,2, QtWidgets.QTableWidgetItem(str(aux3))) #Agrega la descripcion a la tabla
            row = row+1 #Aumenta la fila



app = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
app.exec()