import os
import keyboard
import unittest
import time
import pyautogui as py
import webbrowser

# from settings_citys.citys_test import citys_list

from settings_citys.citys import citys_list
from environment_variables.environment import Positions
from services.services_route import ConsultationFile, CreateRoute
from settings.settings import URL_FINANCIAL_10, URL_FINANCIAL_125, URL_FINANCIAL_15, URL_FINANCIAL_20


class TestStartFinancial(unittest.TestCase):

    def test_relatorio_financial(self):

        REPORT = 'financial'

        positions_financial = Positions()
        response_positions = positions_financial.positions_click(REPORT)

        include_city_in_array = None
        list_citys_created = []

        last_percentage_processed = None

        for city_name in citys_list:

            settings_city_select = citys_list[city_name]

            if isinstance(citys_list, dict) and settings_city_select['active'] == 1:

                # Valida se o arquivo já está criado, para não criar duplicado.
                consultationpdf = ConsultationFile(city_name, REPORT, response_positions['MMYY'])

                if consultationpdf.consultation():
                    continue

                city_percentage = settings_city_select['percentage']
                match city_percentage:

                    case '10%':

                        if last_percentage_processed != '10%':

                            py.hotkey('ctrl', 'w')
                            webbrowser.open(URL_FINANCIAL_10)
                            time.sleep(20)

                    case '12,5%':

                        if last_percentage_processed != '12,5%':

                            py.hotkey('ctrl', 'w')
                            webbrowser.open(URL_FINANCIAL_125)
                            time.sleep(20)

                    case '15%':

                        if last_percentage_processed != '15%':

                            py.hotkey('ctrl', 'w')
                            webbrowser.open(URL_FINANCIAL_15)
                            time.sleep(20)

                    case '20%':

                        if last_percentage_processed != '20%':

                            py.hotkey('ctrl', 'w')
                            webbrowser.open(URL_FINANCIAL_20)
                            time.sleep(20)

                time.sleep(10)
                py.click(response_positions['VIEW_GMV']), time.sleep(6)
                py.click(response_positions['BOX_NAME_CITY']), time.sleep(10)
                py.hotkey('ctrl', 'a'), time.sleep(8)
                py.press('backspace')
                time.sleep(6)
                keyboard.write(city_name), time.sleep(10)
                py.click(response_positions['SELECT_CITY_CHECKBOX']), time.sleep(6)

                py.click(response_positions['VIEW_GMV']), time.sleep(4)
                py.click(response_positions['VIEW_RESUMO_DIARIO']), time.sleep(4)
                py.click(response_positions['VIEW_RESUMO_GERAL']), time.sleep(8)

                py.click(response_positions['SELECT_EXPORTAR']), time.sleep(8)
                py.click(response_positions['SELECT_PDF']), time.sleep(8)
                py.click(response_positions['CONFIRM_EXPORTAR']), time.sleep(8)

                py.click(response_positions['VIEW_GMV']), time.sleep(8)
                time.sleep(120)

                # Validar se o download foi conluído, e assim realizar o rename.
                try:

                    name_file = f'Relatórios Financeiros {city_percentage}.pdf'
                    city_in_list = os.listdir('C:\\Users\\gabri\\OneDrive - ladydriver.com.br\\Downloads_relatorios')

                    if name_file in city_in_list:

                        cr = CreateRoute(city_name, response_positions['MMYY'], REPORT, city_percentage)
                        result = cr.rename_file()

                        include_city_in_array = result
                        list_citys_created.append(include_city_in_array)

                    if name_file not in city_in_list:

                        time.sleep(60)

                        if name_file in city_in_list:

                            cr = CreateRoute(city_name, response_positions['MMYY'], REPORT, city_percentage)
                            result = cr.rename_file()

                            include_city_in_array = result
                            list_citys_created.append(include_city_in_array)

                    if name_file not in city_in_list:
                        result = f'Download da city {city_name}, falhou!'
                        include_city_in_array = result

                except Exception as e:
                    print(e)
                    continue

                last_percentage_processed = settings_city_select['percentage']

        print(f'List of citys createds: {list_citys_created}')
