# Serviço para capturar as posições de cliques no dashboard.
# Você pode iniciar o processo clicando no "run" ou usando o terminal com o seguinte comando:
# cd services -> python positions.py
#
# Obs: Você terá 30 segundos para posicionar o cursor no local desejado.

import time
import pyautogui as py


class Positions:

    @staticmethod
    def capture_positions():

        time.sleep(30)
        response = py.position()

        if response:
            x = response[0]
            y = response[1]
            response = (x, y)

            return response

if __name__ == '__main__':
    return_positions = Positions.capture_positions()

    print(return_positions)
