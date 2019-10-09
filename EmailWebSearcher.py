
import re
import requests

url = input("Type in the URL You wanna search for e-mail Adresses: ")

f = requests.get(url)

emails = re.findall(r'[\w.-]+@[\w.-]+', f.text)
phones= re.findall(r'\d{4}\s\d{4}' ,f.text)

print('\n\nLista de emails econtrados no site: \n')
for email in emails:
    print(email)

print('\n\nLista de telefones encontrados no site: \n')
for phone in phones:
    print(phone)