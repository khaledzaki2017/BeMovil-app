import requests


class HablameSMS:
    def __init__(self, number, sms):
        self.number = number.strip('\n')
        self.sms = sms.strip('\n')
        self.response = ''

    def recharge(self):
        data = {
            'api': 'iMe5BoZNCN10Mu8O7lFkmqDclLnMOP',
            'cliente': '10012586',
            'numero': '57' + self.number,
            'sms': self.sms,
            'referencia': '',
        }
        self.response = requests.post(
            'https://api.hablame.co/sms/envio', params=data)
        return self.__parse_response()

    def __parse_response(self):
        response = self.response.json()
        if response['resultado'] == 0:
            if int(response['sms']['1']['resultado']) == 0:
                return [0, response['sms']['1']['id']]
            else:
                if response['sms']['1']['resultado_t'] == 'No tiene saldo disponible':
                    return [1, 'Problemas Operacionales']
                else:
                    return [1, response['sms']['1']['resultado_t']]
        else:
            return [1, response['resultado_t']]
