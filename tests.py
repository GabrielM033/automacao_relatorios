import os
import time
import pyautogui as py
import unittest
import shutil
import keyboard
import webbrowser

from settings_citys.citys import citys_list
from settings.settings import URL_FINANCIAL_10, URL_FINANCIAL_20


#Get in position
class TestPosition(unittest.TestCase):

    def test_position(self):

        time.sleep(10)
        posi = py.position()
        print(posi)


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


class TestDict(unittest.TestCase):

    def test_dict(self):
        mmyy = "Mai-25"
        open_browser = 826, 1058

        variables_operational = {
            #"MMYY": mmyy,
            "OPEN_BROWSER": open_browser
        }

        for teste in variables_operational:
            posi = variables_operational[teste]

            time.sleep(5)
            py.click(posi)


class TestOpenBrowser(unittest.TestCase):

    def teste_browser(self):

        if URL_FINANCIAL_20:

            try:
                # Vamos usar o webbrowser pelo fato de abrir direto no navegador default
                # e pelo fato de não precisar fazer login no powerbi cada vez que abrir um link

                webbrowser.open(URL_FINANCIAL_10)
                time.sleep(12)
                webbrowser.open(URL_FINANCIAL_20)
                time.sleep(12)
                py.hotkey('ctrl', 'w')


            except Exception as e:
                print(e)


class TestRenameFolder(unittest.TestCase):

    def test_rename(self):

        for city_current in citys_list:

            validation = os.listdir(f'C:\\Users\\gabri\\OneDrive - ladydriver.com.br\\Backup_Lady\\Cidades\\{city_current}')

            if 'Relatorio_Financeiro' in validation:
                continue

            before_name_folder = f'C:\\Users\\gabri\\OneDrive - ladydriver.com.br\\Backup_Lady\\Cidades\\{city_current}\\Relatório Financeiro'

            new_name_folder = f'C:\\Users\\gabri\\OneDrive - ladydriver.com.br\\Backup_Lady\\Cidades\\{city_current}\\Relatorio_Financeiro'

            os.replace(before_name_folder, new_name_folder)

            validation = os.listdir(f'C:\\Users\\gabri\\OneDrive - ladydriver.com.br\\Backup_Lady\\Cidades\\{city_current}')

            print(f'City_{city_current}: {validation}')












