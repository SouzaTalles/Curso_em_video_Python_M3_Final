def siteativo(url):
    from requests import get
    try:
        resp = get(url)
        if resp.status_code == 200:
            print('\033[32mConsegui acessar o site pudim com sucesso!\033[m')
        else:
            print(f'Site respondeu com status {resp.status_code}')
    except:
        print('\033[31mSite pudim não está acessível no momento.\033[m')


siteativo('https://www.pudim.com.br/')
