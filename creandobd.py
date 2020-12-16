# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 17:55:23 2020

@author: Federico
"""


import sqlite3

conexion = sqlite3.connect("database.db")

conexion.close()