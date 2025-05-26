import pyautogui as py
import keyboard
import time
import os

from list_city import citys
from environment_variables.environment import  (OPEN_BROWSER, BOX_NAME_CITY_1, SELECT_CITY_CHECKBOX_1, VIEW_CADASTROS, VIEW_GMV,
                                                VIEW_ONDEMAND, VIEW_AGENDAMENTOS, VIEW_AOPAX, BOX_NAME_CITY_2,
                                                SELECT_CITY_CHECKBOX_2, VIEW_AOMOTO, VIEW_AOSCH, VIEW_AOGMV, VIEW_ANALYSIS,
                                                SELECT_EXPORTAR, SELECT_PDF, CONFIRM_EXPORTAR, FILES_CREATED, MMYY)
from services.services_route import CreateRoute
import unittest



class StartOperational(unittest.TestCase):

    def test_relatorio_operational(self):

        time.sleep(5)
        py.doubleClick(OPEN_BROWSER)

        include_city_in_array = None
        list_citys_created = []

        for city_name in citys.citys_list:

            if isinstance(citys.citys_list, dict) and citys.citys_list[city_name] == 1:

                #Valida se o arquivo já está criado, para não criar duplicado.
                if self.list_files_created(city_name):
                    continue

                time.sleep(10)
                py.click(BOX_NAME_CITY_1)

                py.sleep(10)
                py.hotkey('ctrl', 'a'), time.sleep(4)
                py.press('backspace')

                time.sleep(5)
                keyboard.write(city_name)

                time.sleep(12)
                py.click(SELECT_CITY_CHECKBOX_1)

                time.sleep(5)
                py.click(VIEW_CADASTROS)

                time.sleep(5)
                py.click(VIEW_GMV)

                time.sleep(5)
                py.click(VIEW_ONDEMAND)

                time.sleep(5)
                py.click(VIEW_AGENDAMENTOS)

                time.sleep(5)
                py.click(VIEW_AOPAX)

                time.sleep(5)
                py.click(BOX_NAME_CITY_2)

                time.sleep(10)
                py.hotkey('ctrl', 'a'), time.sleep(4)
                py.press('backspace')

                time.sleep(5)
                keyboard.write(city_name)

                time.sleep(12)
                py.click(SELECT_CITY_CHECKBOX_2)

                time.sleep(5)
                py.click(VIEW_AOMOTO)

                time.sleep(5)
                py.click(VIEW_AOSCH)

                time.sleep(5)
                py.click(VIEW_AOGMV)

                time.sleep(5)
                py.click(VIEW_ANALYSIS)


                time.sleep(5)
                py.click(SELECT_EXPORTAR), time.sleep(4)
                py.click(SELECT_PDF), time.sleep(4)
                py.click(CONFIRM_EXPORTAR)
                time.sleep(120)

                py.click(VIEW_CADASTROS)

                # Validar se o download foi conluído
                try:

                    name_file = 'Relatórios Operacionais.pdf'
                    city_in_list = os.listdir('C:\\Users\\gabri\\OneDrive - ladydriver.com.br\\Downloads_relatorios')

                    if name_file in city_in_list:

                        cr = CreateRoute(city_name, MMYY)

                        result = cr.rename_file()
                        include_city_in_array = result

                    if name_file not in city_in_list:

                        time.sleep(60)

                        if name_file in city_in_list:

                            cr = CreateRoute(city_name, MMYY)

                            result = cr.rename_file()
                            include_city_in_array = result

                    if name_file not in city_in_list:

                        result = f'Download da city {city_name} falhou!'
                        include_city_in_array = result

                except Exception as e:
                    print(e)
                    continue

                list_citys_created.append(include_city_in_array)

        print(include_city_in_array)


    def list_files_created(self, city):

        files_created = os.listdir('C:\\Users\\gabri\\OneDrive - ladydriver.com.br\\Downloads_relatorios')
        city_name_file = f"Relatorios_Operacionais-{city}-{MMYY}.pdf"

        if city_name_file in files_created:
            return True
        else:
            return False


            