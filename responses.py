from random import choice, randint
import requests
from unidecode import unidecode
dotaAPI = 'https://api.opendota.com/api/'


def get_response(user_input):
    user_input =  str = unidecode(user_input).lower()
#Respostas do bot, lembrar adicionar lógicas de resposta de chat bot depois
    if  user_input == 'oi':
        return 'Eai!'
    elif user_input == 'help':
        return 'Favor ler a documentação %link%'
    elif user_input == 'ta rolando?':
        endpoint = ('live')
        try:
            response = requests.get(dotaAPI + endpoint)
            if response.status_code == 200:
                jsonResponse = response.json()
                return 'Tá rolando'
            else:
                print('Error:', response.status_code)
                return 'Não tá rolando'
        except requests.exceptions.RequestException as e:
            return 'Complicou'
    elif 'know player' in user_input:
        user_input = user_input[12:]
        dets = {'q' : user_input}
        endpoint = ('search/')
        print(dotaAPI + endpoint)
        try:
            response = requests.get(dotaAPI + endpoint,params=dets)
            if response.status_code == 200:
                jsonResponse = response.json()
                accId = jsonResponse[0]["account_id"]
                #avatarMedium = jsonResponse[0]["avatarmedium"]
                accId =  "{}".format(accId)
                endpoint = dotaAPI + '/players/'
                response = requests.get(endpoint + accId)
                if response.status_code == 200:
                    jsonResponse = response.json()
                    accId = jsonResponse.get("account_id")
                    return jsonResponse
                else:
                    print('Error:', response.status_code)
                    return 'Sei quem é não'
                    print(jsonResponse)
            else:
                print('Error:', response.status_code)
                return 'Sei quem é não'
        except requests.exceptions.RequestException as e:
            return 'Gabe tá ocupado'

    else: 
        return choice(["Não estou conseguindo entender.", 
                       "Não consegui pegar o que você quis dizer.", 
                       "Eu não peguei a ideia."])