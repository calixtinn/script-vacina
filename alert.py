# coding=utf-8
import re
import requests
import os
from dotenv import load_dotenv


def run():
    os.system("curl -sL https://smart24.com.br/vacina/formiga -o /tmp/vacina.html")
    html = open('/tmp/vacina.html', 'r', encoding="utf-8")
    content = html.read()
    content = content.lower()
    html.close()
    age = re.search('prioridade:.*[0-9]+ anos', content).group()
    age = re.search('[0-9]+', age).group()
    if age == TARGET_AGE:
        if not os.path.isfile('/tmp/enviou'):
            send_message('IDADE DE {} ANOS CHEGOU!!! REGISTRE-SE PARA A VACINA CONTRA A COVID-19!!! https://smart24.com.br/vacina/formiga'.format(TARGET_AGE))
            return


def send_message(text):
        os.system("touch /tmp/enviou")
        send_text = 'https://api.telegram.org/bot' + API_KEY + '/sendMessage?chat_id=' + CHAT_ID + '&parse_mode=Markdown&text=' + text
        response = requests.get(send_text)
        print("Idade Alcançada! Mensagem enviada")
        return response.json()


if __name__ == '__main__':
    load_dotenv()
    TARGET_AGE = os.environ.get('TARGET_AGE')
    API_KEY = os.environ.get('API_KEY')
    CHAT_ID = os.environ.get('CHAT_ID')
    run()