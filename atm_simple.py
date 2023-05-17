# -*- coding: utf-8 -*-
"""
Created on Tue May  9 16:46:29 2023
@author: LAB02 
"""
import os
class Cajero:
    def __init__(self):
        self.continuar = True
        self.monto = 5000

    def contraseña(self):
        contador = 1
        while contador <= 3:
            x = int(input("ingrese su contraseña:" ))
            if x == 5467:
                print("Contraseña Correcta")
                break
            else:
                print(f"Contraseña Incorrecta, le quedan {3 - contador} intentos")
                if contador == 3:
                    print("No puede realizar operaciones.")
                    self.continuar = False
                contador+=1

    def menu(self):
        os.system("cls")   #esto es solo para windows
        self.contraseña()
        opcion = 0
        while opcion != "4":
            #os.system("cls")
            print(""" Bienvenido al cajero automatico
            ******Menú******
            1-  Depositar
            2- Retirar
            3- Ver saldo
            4- Salir """)
            opcion = input("Su opción es: ")
            if self.continuar:
                if opcion == "1" :
                    self.depositar()
                elif opcion == "2" :
                    self.retiro()
                elif opcion == "3":
                    self.ver()
                elif opcion == "4":
                    print("Programa finalizado")
                else:
                    print("NO existe esa opción")
            else:
                if opcion in "123":
                    print("Imposible realizar esa operación")
                elif opcion == "4":
                    print("Programa finalizado")
                else:
                    print("No existe esa opción")
    
    def depositar(self):
        depo = int(input("Ingrese su monto a depositar:"))
        print("Usted a depositado", depo)
        print(f"Su nuevo saldo es {self.monto + depo}")
        self.monto += depo

    def retiro(self):
        retirar = int(input("¿Cuánto desea retirar? : "))
        print("Su monto actual es", self.monto)
        if self.monto >= retirar :
            print(f"Usted a retirado: {retirar} , su nuevo monto es {self.monto - retirar}")
            self.monto-=retirar
        else:
            print("Imposible realizar el retiro, su monto es menor")

    def ver(self):
        print("Su saldo es: " , self.monto)
        
    def depositarTEST(self, cantidad):
        if(cantidad <= 0):
            return -1
        
        self.monto += cantidad
        return self.monto
    
    def retirarTEST(self, cantidad):
        if(self.monto < cantidad):
            return -1
        if(cantidad <= 0):
            return -1
        
        self.monto -= cantidad
        return self.monto
    
    def verTEST(self):
        return self.monto
