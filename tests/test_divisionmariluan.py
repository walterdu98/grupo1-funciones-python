# tests/test_divisionmariluan.py
from funciones.divisionmariluan import divisionmariluan

def test_divisionmariluan():
 # división normal
 assert divisionmariluan(10, 2) == 5

 # division número impar
 assert divisionmariluan(5, 2) == 2.5

 # división por cero 
 assert divisionmariluan(5, 0) is None