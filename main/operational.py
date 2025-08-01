import pyautogui as py
import webbrowser
import unittest
import keyboard
import time
import os

# from settings_citys.citys_test import citys_list

from settings_citys.citys import citys_list
from environment_variables.environment import Positions
from services.services_route import CreateRoute, ConsultationFile



class StartOperational(unittest.TestCase):

    def test_relatorio_operational(self):

        REPORT = 'operational'

        positionsoperational = Positions()
        response_positions = positionsoperational.positions_click(REPORT)

        webbrowser.open(response_positions['OPEN_BROWSER'])
        time.sleep(15)

        include_city_in_array = None
        list_citys_created = []

        for city_name in citys_list:

            city_select = citys_list[city_name]

            if isinstance(citys_list, dict) and city_select['active'] == 1:

                #Valida se o arquivo já está criado, para não criar duplicado.
                consultationpdf = ConsultationFile(city_name, REPORT, response_positions['MMYY'])

                if consultationpdf.consultation():
                    continue

                time.sleep(4)
                py.click(response_positions['VIEW_CADASTROS'])

                time.sleep(8)
                py.click(response_positions['BOX_NAME_CITY_1'])

                py.sleep(10)
                py.hotkey('ctrl', 'a'), time.sleep(4)
                py.press('backspace')

                time.sleep(5)
                keyboard.write(city_name)

                time.sleep(12)
                py.click(response_positions['SELECT_CITY_CHECKBOX_1'])

                time.sleep(5)
                py.click(response_positions['VIEW_CADASTROS'])

                time.sleep(5)
                py.click(response_positions['VIEW_GMV'])

                time.sleep(5)
                py.click(response_positions['VIEW_ONDEMAND'])

                time.sleep(5)
                py.click(response_positions['VIEW_AGENDAMENTOS'])

                time.sleep(5)
                py.click(response_positions['VIEW_AOPAX'])

                time.sleep(5)
                py.click(response_positions['BOX_NAME_CITY_2'])

                time.sleep(10)
                py.hotkey('ctrl', 'a'), time.sleep(4)
                py.press('backspace')

                time.sleep(5)
                keyboard.write(city_name)

                time.sleep(12)
                py.click(response_positions['SELECT_CITY_CHECKBOX_2'])

                time.sleep(5)
                py.click(response_positions['VIEW_AOMOTO'])

                time.sleep(5)
                py.click(response_positions['VIEW_AOSCH'])

                time.sleep(5)
                py.click(response_positions['VIEW_AOGMV'])

                time.sleep(5)
                py.click(response_positions['VIEW_ANALYSIS'])


                time.sleep(5)
                py.click(response_positions['SELECT_EXPORTAR']), time.sleep(4)
                py.click(response_positions['SELECT_PDF']), time.sleep(4)
                py.click(response_positions['CONFIRM_EXPORTAR']), time.sleep(4)

                py.click(response_positions['VIEW_CADASTROS'])
                time.sleep(120)

                # Validar se o download foi conluído
                try:

                    name_file = 'Relatórios Operacionais.pdf'
                    city_in_list = os.listdir('C:\\Users\\gabri\\OneDrive - ladydriver.com.br\\Downloads_relatorios')

                    if name_file in city_in_list:

                        cr = CreateRoute(city_name, response_positions['MMYY'], REPORT)

                        result = cr.rename_file()
                        include_city_in_array = result
                        list_citys_created.append(include_city_in_array)

                    if name_file not in city_in_list:

                        time.sleep(60)

                        if name_file in city_in_list:

                            cr = CreateRoute(city_name, response_positions['MMYY'], REPORT)

                            result = cr.rename_file()
                            include_city_in_array = result
                            list_citys_created.append(include_city_in_array)

                    if name_file not in city_in_list:

                        result = f'Download da city {city_name} falhou!'
                        include_city_in_array = result
                        list_citys_created.append(include_city_in_array)

                except Exception as e:
                    print(e)
                    continue

        print(list_citys_created)


            