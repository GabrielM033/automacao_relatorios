import os
import shutil

class CreateRoute(object):

    def __init__(self, city, month, report, details=None):

        self.city = city
        self.month = month
        self.report = report
        self.details = details


    def rename_file(self):

        type_report = None
        name_file = None

        if self.report == 'financial':
            type_report = 'Relatorio_Financeiro'
            name_file = f'Relatórios Financeiros {self.details}.pdf'

        else:
            type_report = 'Relatorio_Operacional'
            name_file = 'Relatórios Operacionais.pdf'


        #Rename_file
        new_name_file = f'{type_report}-{self.city}-{self.month}.pdf'

        before_name_file = f'C:\\Users\\gabri\\OneDrive - ladydriver.com.br\\Downloads_relatorios\\{name_file}'

        file_renamed = f'C:\\Users\\gabri\\OneDrive - ladydriver.com.br\\Downloads_relatorios\\{new_name_file}'

        os.rename(before_name_file, file_renamed)


        #Create_folder_backup
        name_folder_report = type_report
        folder_month = (f'C:\\Users\\gabri\\OneDrive - ladydriver.com.br\\Backup_Lady\\Cidades\\{self.city}\\'
                  f'{name_folder_report}\\{self.month}')

        try:

            #Se não tiver a pasta vai dar o Type error FileNotError.
            #Caso tenha a pasta, vai excluir por segurança e criar uma nova.
            os.listdir(folder_month)

            shutil.rmtree(folder_month)
            os.mkdir(folder_month)

            folder_download = file_renamed
            folder_backup = folder_month

            shutil.copy(folder_download, folder_backup)

        except FileNotFoundError:
            os.mkdir(folder_month)

            file_folder_download = file_renamed
            file_folder_backup = folder_month

            shutil.copy(file_folder_download, file_folder_backup)

        except Exception as e:
            print(f'Error in create folder backup, {self.month}, for city: {self.city}')


        #Completed
        folder_month_created = os.listdir(folder_month)

        name_file = f'{name_folder_report}-{self.city}-{self.month}.pdf'
        response = name_file if name_file in folder_month_created else (f'Error created folder {self.month} or copy '
                                                                        f'file {self.city} to folder backup')

        return response


class ConsultationFile(object):

    def __init__(self, city, report, month):
        self.city = city
        self.report = report
        self.month = month


    def consultation(self):

        if self.report == 'operational':

            files_created = os.listdir('C:\\Users\\gabri\\OneDrive - ladydriver.com.br\\Downloads_relatorios')
            city_name_file = f"Relatorio_Operacional-{self.city}-{self.month}.pdf"

            if city_name_file in files_created:
                return True
            else:
                return False

        if self.report == 'financial':

            files_created = os.listdir('C:\\Users\\gabri\\OneDrive - ladydriver.com.br\\Downloads_relatorios')
            city_name_file = f"Relatorio_Financeiro-{self.city}-{self.month}.pdf"

            if city_name_file in files_created:
                return True
            else:
                return False