# Inserir a URL referente ao acesso do dashboard, pois cada usuário possui uma URL diferente.
# Atualizar a variável "DESKTOP", de acordo com o computador que será utilizado. Ex: desktop_1, desktop_2, etc.
# Atualizar a variável "MONTH", de acordo com o mês dos relatórios.
#
# Obs: Cada máquina possui uma posição de interação com o dashboard, devido à diferença no tamanho da tela.
# Sendo assim, é necessário coletar as posições para cada máquina que for executar o projeto. O "desktop_1" já possui essas posições.


URL_FINANCIAL_10 = ()
URL_FINANCIAL_125 = ()
URL_FINANCIAL_15 = ()
URL_FINANCIAL_20 = ()

URL_OPERATIONAL = ()


MONTH = "Set-25"
DESKTOP = 'desktop_1'


class SettingsOperational(object):

    def __init__(self, desktop, month, url):
        self.desktop = desktop
        self.month = month
        self.url = url


    def settings_position(self):

        if self.desktop == 'desktop_1':

            positions_desktop1 = {
                "MMYY": self.month,
                "OPEN_BROWSER": self.url,
                "BOX_NAME_CITY_1": (596, 442),
                "SELECT_CITY_CHECKBOX_1": (464, 501),
                "VIEW_CADASTROS": (135, 301),
                "VIEW_GMV": (137, 337),
                "VIEW_ONDEMAND": (142, 383),
                "VIEW_AGENDAMENTOS": (184, 435),
                "VIEW_AOPAX": (131, 487),
                "BOX_NAME_CITY_2": (618, 556),
                "SELECT_CITY_CHECKBOX_2": (464, 606),
                "VIEW_AOMOTO": (157, 533),
                "VIEW_AOSCH": (115, 583),
                "VIEW_AOGMV": (141, 638),
                "VIEW_ANALYSIS": (143, 686),
                "SELECT_EXPORTAR": (503, 212),
                "SELECT_PDF": (508, 354),
                "CONFIRM_EXPORTAR": (1110, 731)
            }
            return positions_desktop1

        if self.desktop == 'desktop_2':

            # Coletar os valores das chaves, em: services/positions.py...
            positions_desktop2 = {
                "MMYY": self.month,
                "OPEN_BROWSER": self.url,
                "BOX_NAME_CITY_1": (),
                "SELECT_CITY_CHECKBOX_1": (),
                "VIEW_CADASTROS": (),
                "VIEW_GMV": (),
                "VIEW_ONDEMAND": (),
                "VIEW_AGENDAMENTOS": (),
                "VIEW_AOPAX": (),
                "BOX_NAME_CITY_2": (),
                "SELECT_CITY_CHECKBOX_2": (),
                "VIEW_AOMOTO": (),
                "VIEW_AOSCH": (),
                "VIEW_AOGMV": (),
                "VIEW_ANALYSIS": (),
                "SELECT_EXPORTAR": (),
                "SELECT_PDF": (),
                "CONFIRM_EXPORTAR": ()
            }
            return positions_desktop2


class SettingsFinancial(object):

    def __init__(self, desktop, month):
        self.desktop = desktop
        self.month = month


    def settings_position(self):

        if self.desktop == 'desktop_1':
            positions_desktop1 = {
                "MMYY": self.month,
                "VIEW_GMV": (154, 296),
                "BOX_NAME_CITY": (601, 463),
                "SELECT_CITY_CHECKBOX": (467, 514),
                "VIEW_RESUMO_DIARIO": (143, 351),
                "VIEW_RESUMO_GERAL": (144, 398),
                "SELECT_EXPORTAR": (510, 230),
                "SELECT_PDF": (507, 370),
                "CONFIRM_EXPORTAR": (1114, 735)
            }
            return positions_desktop1

        if self.desktop == 'desktop_2':

            # Coletar os valores das chaves, em: services/positions.py...
            positions_desktop2 = {
                "MMYY": self.month,
                "VIEW_GMV": (),
                "BOX_NAME_CITY": (),
                "SELECT_CITY_CHECKBOX": (),
                "VIEW_RESUMO_DIARIO": (),
                "VIEW_RESUMO_GERAL": (),
                "SELECT_EXPORTAR": (),
                "SELECT_PDF": (),
                "CONFIRM_EXPORTAR": ()
            }
            return positions_desktop2