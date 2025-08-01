# Criar um objeto "SettingsOperational" e "SettingsFiancial" novo para os desktop novos: 'desktop_2', 'desktop_3' e etc...

URL_FINANCIAL_10 = ('https://app.powerbi.com/groups/me/reports/8ffa1918-9b78-4f42-ac28-6b540553df4f/'
                    'ReportSectionf74734c5a6ad30731242?ctid=ad905b11-40ec-4e81-be7c-8c604b7f00a3&experience=power-bi&clientSideAuth=0')
URL_FINANCIAL_125 = ('https://app.powerbi.com/groups/me/reports/4503ab71-45cf-4096-a35d-434ef6e5b56b/'
                     'ReportSectionf74734c5a6ad30731242?ctid=ad905b11-40ec-4e81-be7c-8c604b7f00a3&experience=power-bi&clientSideAuth=0')
URL_FINANCIAL_15 = ('https://app.powerbi.com/groups/me/reports/b5e2efb6-c167-4b9e-be81-12519f6e3429/'
                    'ReportSectionf74734c5a6ad30731242?ctid=ad905b11-40ec-4e81-be7c-8c604b7f00a3&experience=power-bi&clientSideAuth=0')
URL_FINANCIAL_20 = ('https://app.powerbi.com/groups/me/reports/cbd44925-ddbe-4761-b63e-a0d1615e2895/'
                    'ReportSectionf74734c5a6ad30731242?ctid=ad905b11-40ec-4e81-be7c-8c604b7f00a3&experience=power-bi&clientSideAuth=0')

URL_OPERATIONAL = ('https://app.powerbi.com/groups/me/reports/8b282a72-2ea6-4c6f-9198-4634f9b2c056/'
                   'ReportSection?ctid=ad905b11-40ec-4e81-be7c-8c604b7f00a3&experience=power-bi&clientSideAuth=0')


MONTH = "Jul-25"
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

            positions_desktop2 = {
                "MMYY": self.month
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