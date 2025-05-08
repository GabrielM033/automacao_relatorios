import pyautogui as py
import keyboard
import time
import os

from list_city import citys
from environment_variables import environment
from services.services_route import CreateRoute


class StartOperational(object):

    def __init__(self):
        pass

    def relatorio_operational(self):

        time.sleep(5)
        py.click(environment.OPEN_BROWSER)

        for city_name in citys.citys_list:

            if isinstance(citys.citys_list, dict) and citys.citys_list[city_name] == 1:

                #Valida se o arquivo já está criado, para não criar duplicado.
                if self.list_files_created(city_name):
                    continue

                time.sleep(3)
                py.click(environment.BOX_NAME_CITY_1)

                py.sleep(10)
                py.hotkey('ctrl', 'a'), time.sleep(4)
                py.press('backspace')

                time.sleep(5)
                keyboard.write(city_name)

                time.sleep(10)
                py.click(environment.SELECT_CITY_CHECKBOX_1)

                time.sleep(5)
                py.click(environment.VIEW_CADASTROS)

                time.sleep(5)
                py.click(environment.VIEW_GMV)

                time.sleep(5)
                py.click(environment.VIEW_ONDEMAND)

                time.sleep(5)
                py.click(environment.VIEW_AGENDAMENTOS)

                time.sleep(5)
                py.click(environment.VIEW_AOPAX)

                time.sleep(5)
                py.click(environment.BOX_NAME_CITY_2)

                time.sleep(10)
                py.hotkey('ctrl', 'a'), time.sleep(4)
                py.press('backspace')

                time.sleep(5)
                keyboard.write(city_name)

                time.sleep(10)
                py.click(environment.SELECT_CITY_CHECKBOX_2)

                time.sleep(5)
                py.click(environment.VIEW_AOMOTO)

                time.sleep(5)
                py.click(environment.VIEW_AOSCH)

                time.sleep(5)
                py.click(environment.VIEW_AOGMV)

                time.sleep(5)
                py.click(environment.VIEW_ANALYSIS)


                time.sleep(5)
                py.click(environment.SELECT_EXPORTAR), time.sleep(4)
                py.click(environment.SELECT_PDF), time.sleep(4)
                py.click(environment.CONFIRM_EXPORTAR)
                time.sleep(120)

                # Validar se o download foi conluído
                try:

                    city_in_list = environment.FILES_CREATED

                    name_file = 'Relatórios Operacionais.pdf'

                    if name_file in city_in_list:

                        cr = CreateRoute(city_name, environment.MMYY)
                        result = cr.completed()

                        include_array = result

                    if name_file is not city_in_list:

                        time.sleep(120)

                        if name_file in city_in_list:
                            cr = CreateRoute(city_name, environment.MMYY)
                            result = cr.completed()

                            include_array = result

                    if name_file is not city_in_list:

                        result = f'Download da city {city_name} falhou!'
                        include_array = result


                #Pensar em criar um log de erro
                except Exception as e:
                    continue

    def list_files_created(self, city):

        files_created = environment.FILES_CREATED
        city_name_file = f"Relatorios_Operacionais-{city}-{environment.MMYY}.pdf"

        if city_name_file in files_created:
            return True
        else:
            return False


            