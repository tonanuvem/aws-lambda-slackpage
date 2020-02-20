import json
from botocore.vendored import requests

print('Loading function')

url = "https://hooks.slack.com/services/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"
canal = "#lab-testes"

def lambda_handler(event, context):
    try:
        print(event)
        if not 'msg' in event:
            return 'Campo vazio : msg'
        texto=event['msg']
        print("Texto = "+ texto)
        return postMSG_criada_para_o_slack(texto)
        
    except Exception as e:
        erro = "Erro na function: " + repr(e);
        print(erro)
        return erro
    
def postMSG_criada_para_o_slack(msg):
    # format payload for slack
    sdata = formatForSlack(msg)
    r = requests.post(url, sdata, headers={'Content-Type': 'application/json'})
    if r.status_code == 200:
      return 'SUCCEDED: Sent slack webhook.  Msg = ' + msg
    else:
      return 'FAILED: Send slack webhook'

def formatForSlack(msg):
  payload = {
    "channel":canal,
    "username":'ALUNO_Serverless',
    "text": msg,
    "icon_emoji":':cyclone'
  }
  return json.dumps(payload)
