import os
import time
import pyautogui as py
import unittest
import shutil
import keyboard

#Get in position
class TestPosition(unittest.TestCase):

    def test_position(self):

        time.sleep(8)
        posi = py.position()
        print(posi)


#Click in position
class TestRoute(unittest.TestCase):

    def test_route(self):

        files = os.listdir('C:\\Users\\gabri\\OneDrive - ladydriver.com.br\\Downloads_relatorios')
        print(files)



class TestFile(unittest.TestCase):

    def test_file(self):

        folder_month = None

        try:

            folder_month = ('C:\\Users\\gabri\\OneDrive - ladydriver.com.br\\Backup_Lady\\Cidades\\americana\\'
                            'Relatório Operacional\\Abr-25')

            return_folder = os.listdir(folder_month)

            shutil.rmtree(folder_month)
            os.mkdir(folder_month)

        except FileNotFoundError:
            os.mkdir(folder_month)

        except Exception as e:
            print(e)
