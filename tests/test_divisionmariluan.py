# tests/test_dividir_mariluan.py
from funciones.dividir_marilluan import dividir_mariluan

def test_dividir_mariluan():
 # división normal
 assert dividir_mariluan(10, 2) == 5

 # division número impar
 assert dividir_mariluan(5, 2) == 2.5

 # división por cero 
 assert dividir_mariluan(5, 0) is None