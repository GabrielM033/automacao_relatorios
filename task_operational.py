import pyautogui as py
import keyboard
import time
import sys
import os

from list_city import citys
from environment_variables import environment


class StartOperational():

    def __init__(self):
        pass    


    def relatorio_operational(self):

        time.sleep(5)
        py.click(environment.open_browser)

        for city_current in citys.citys_list:

            city_name_file = (f"Relatorios_Operacionais-{city_current}-{environment.mmyy}.pdf")

            if isinstance(citys.citys_list, list):
                
                #Valida se o arquivo já está criado, para não criar duplicado.
                if city_name_file in environment.files_created:
                    
                    continue

                time.sleep(3)
                py.click(environment.box_name_city_1)
                
                py.sleep(10)
                py.hotkey('ctrl', 'a'), time.sleep(4)
                py.press('backspace')
                
                time.sleep(5)
                keyboard.write(city_current)
                
                time.sleep(10)
                py.click(environment.select_city_checkbox_1)
                
                time.sleep(5) 
                py.click(environment.view_cadastros)

                time.sleep(5)
                py.click(environment.view_gmv)

                time.sleep(5)
                py.click(environment.view_ondemand)

                time.sleep(5)
                py.click(environment.view_agendamentos)

                time.sleep(5)
                py.click(environment.view_aopax)

                time.sleep(5)
                py.click(environment.box_name_city_2)

                time.sleep(10)
                py.hotkey('ctrl', 'a'), time.sleep(4)                
                py.press('backspace')

                time.sleep(5)
                keyboard.write(city_current)

                time.sleep(10)
                py.click(environment.select_city_checkbox_2)

                time.sleep(5)
                py.click(environment.view_aomoto)

                time.sleep(5)
                py.click(environment.view_aosch)

                time.sleep(5)
                py.click(environment.view_aogmv)

                time.sleep(5)
                py.click(environment.view_analysis)


                #parte de download e exportação do arquivo
                time.sleep(5)
                py.click(environment.select_exportar), time.sleep(4)
                py.click(environment.select_pdf), time.sleep(4)
                py.click(environment.confirm_exportar)
                time.sleep(120)

                try:

                    if 'Relatórios Operacionais.pdf' in environment.files_created:

                        before_name = 'C:\\Users\\gabri\\OneDrive - ladydriver.com.br\\Downloads_relatorios\\Relatórios Operacionais.pdf' 
                        new_name = f'C:\\Users\\gabri\\OneDrive - ladydriver.com.br\\Downloads_relatorios\\{city_name_file}'
                        os.rename(before_name, new_name)

                    else:
                        time.sleep(120)

                        if 'Relatórios Operacionais.pdf' in environment.files_created:

                            before_name = 'C:\\Users\\gabri\\OneDrive - ladydriver.com.br\\Downloads_relatorios\\Relatórios Operacionais.pdf' 
                            new_name = f'C:\\Users\\gabri\\OneDrive - ladydriver.com.br\\Downloads_relatorios\\{city_name_file}'
                            os.rename(before_name, new_name)
                        

                #Cidade X não criada. Pensar em criar um log no except!
                except Exception as e:
                    continue 

            else:
                sys.exit()

        


            