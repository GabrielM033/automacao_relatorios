import os
import shutil

class CreateRoute(object):

    def __init__(self, city, month):

        self.city = city
        self.month = month


    def rename_file(self):

        #Renomear_o_arquivo
        new_name_city = f'Relatorios_Operacionais-{self.city}-{self.month}.pdf'

        before_name = 'C:\\Users\\gabri\\OneDrive - ladydriver.com.br\\Downloads_relatorios\\Relatórios Operacionais.pdf'

        new_name = f'C:\\Users\\gabri\\OneDrive - ladydriver.com.br\\Downloads_relatorios\\{new_name_city}'

        os.rename(before_name, new_name)


        #Create_folder
        folder_month = (f'C:\\Users\\gabri\\OneDrive - ladydriver.com.br\\Backup_Lady\\Cidades\\{self.city}\\'
                  f'Relatório Operacional\\{self.month}')

        try:

            #Se não tiver a pasta vai dar o erro FileNotError
            os.listdir(folder_month)

            shutil.rmtree(folder_month)
            os.mkdir(folder_month)

            folder_download = new_name
            folder_backup = folder_month

            shutil.copy(folder_download, folder_backup)

        except FileNotFoundError:
            os.mkdir(folder_month)

            file_folder_download = new_name
            file_folder_backup = folder_month

            shutil.copy(file_folder_download, file_folder_backup)

        except Exception as e:
            print(f'Error in create folder {self.month} for city: {self.city}')


        #Completed
        folder_month_created = os.listdir(folder_month)

        name_file = f'Relatorios_Operacionais-{self.city}-{self.month}.pdf'
        response = name_file if name_file in folder_month_created else (f'Error created folder {self.month} and copy '
                                                                        f'file {self.city} to folder backup')

        return response
