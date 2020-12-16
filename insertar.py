# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 18:40:13 2020

@author: Federico
"""


import sqlite3

conexion = sqlite3.connect("database.db")
cursor = conexion.cursor()
cursor.execute("""INSERT INTO PERSONAS VALUES(
                'Mariano',
                'Filo',
                21
                )
               """)
conexion.commit()
conexion.close()