import os
import time
import pyautogui as py
import unittest
import keyboard


class TestPosition(unittest.TestCase):

    def test_position(self):
        '''time.sleep(10)
        position = py.position()
        print(position)'''

        files_created = os.listdir('C:\\Users\\gabri\\OneDrive - ladydriver.com.br\\Downloads_relatorios')

        if 'Relatórios Operacionais.pdf' in files_created:
            
            print("Tem arquivo aqui dentro!") 

        else:
            print("Não caiu no if")


posi = TestPosition()
posi.test_position()
