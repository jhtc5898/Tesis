print("Resultado")
from pyscopus import Scopus
import pandas as pd
import requests
key = '0387c7142db3254ed53c09c131ecf8c0'
scopus = Scopus(key)
search_df = scopus.search("ALL(medicina)", count=100)
print(search_df.keys())

listalinks = list()
listatitulos = list()
listabstract = list()

for i in range(len(search_df['scopus_id'])):
	try:
	
		pub_abs = scopus.retrieve_abstract(search_df['scopus_id'][i])
		listabstract.append(pub_abs['abstract'])
		listalinks.append(search_df['scopus_id'][i])
		listatitulos.append(search_df['title'][i])
	except:
		print(" ")

dict={'link':listalinks ,'title':listatitulos,'abstract':listabstract,'fuente':"scopus"}
print(len(listalinks),",",len(listatitulos),",",len(listabstract))

df=pd.DataFrame(dict)
print(df)


# URL

url = 'https://www.doaj.org/api/v2/search/articles/all(lenguaje)?pageSize=100'


headers = {'Content-Type': 'application/json;charset=UTF-8', 'Access-Control-Allow-Origin': '*'}


# Get content

r = requests.get(url, headers=headers)


# Decode JSON response into a Python dict:

content = r.json()

json = content['results']

listalinks = list()

listatitulos = list()

listabstract = list()

listakeywords = list()


for i in range(len(json)):

    #print(i)

    try:

        nivel4=json[i]['bibjson']['keywords']

        #print(nivel4)

        listakeywords.append(nivel4)

        

        nivel1=json[i]['bibjson']['link'][0]['url']

        #print(nivel1)

        listalinks.append(nivel1)

        

        nivel2=json[i]['bibjson']['title']

        #print(nivel2)

        listatitulos.append(nivel2)

        

        nivel3=json[i]['bibjson']['abstract']

        #print(nivel3)

        listabstract.append(nivel3)

          

    except:

        print(" ")

dict = {'link': listalinks, 'title': listatitulos, 'abstract': listabstract ,'keywords':listakeywords ,'fuente':"doaj"} 

df = pd.DataFrame(dict) 
print(df)

