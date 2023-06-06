import requests 

def verificarSiteOnline(msg):
  '''
  -> checar conexão de intenet com site
  '''
  url = msg
  try:
    requests.get(url)
  except:
    print("site off")
  else:
    print("Site online")

verificarSiteOnline("http://pudim.com.br/") 
 
