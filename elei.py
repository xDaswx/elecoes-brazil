import requests,json,time
headers = {
    'authority': 'resultados.tse.jus.br',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.5',
    'referer': 'https://resultados.tse.jus.br/oficial/app/index.html',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}

r = requests.get('https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json', headers=headers).json()


def check():
		print("Horario de atualização:", r['hg'])
		print("Apuração:", r['pst'])
		print("------------------")
		for candi in r['cand']:
			print(f"{candi['nm']} '{candi['n']}' - Votos: {candi['vap']}")
		print("------------------")
	
while True:
	check()
	time.sleep(60)
	