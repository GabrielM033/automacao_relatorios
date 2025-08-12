from settings.settings import SettingsOperational, SettingsFinancial, DESKTOP, MONTH, URL_OPERATIONAL

class Positions():

    def positions_click(self, report):

        if report == 'operational':

            positions_op = SettingsOperational(DESKTOP, MONTH, URL_OPERATIONAL)
            response = positions_op.settings_position()

            return response

        if report == 'financial':

            positions_fin = SettingsFinancial(DESKTOP, MONTH)
            response = positions_fin.settings_position()

            return response





