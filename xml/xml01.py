# Programa para importar o XML do podcast 99vidas e gravar no banco SQLite
# Futuramente irei fazer uma tela de consulta aos episódios do podcast que forem baixados

import urllib.request as request
import xml.etree.ElementTree as ET
from pathlib import Path
import time
import sys
from Banco import Banco

# Importar esse XML para a leitura, caso o XML ainda não exista
# http://99vidas.com.br/99vidas.xml

sArqXml = 'arquivo.xml'
sURL = 'http://99vidas.com.br/99vidas.xml'

pArquivo = Path(sArqXml)
if (not pArquivo.is_file()):
    print('XML ainda não baixado. Baixando...')
    request.urlretrieve(sURL, sArqXml)
    time.sleep(5)
else:
    print('XML já baixado. Prosseguindo...')

print('Ler o arquivo XML baixado')

# Usar esse site para aprender a ler XML
# https://www.datacamp.com/community/tutorials/python-xml-elementtree

fXml = ET.parse(sArqXml)
xRoot = fXml.getroot()

if (len(xRoot) == 0):
    print('XML vazio...')
    sys.exit()

channel = xRoot[0]

# Abrir uma conexão com o banco
banco = Banco()
conn = banco.conexao.cursor()

for xItem in channel.iter('item'):
    xTitle = xItem.find('title')
    xEnclosure = xItem.find('enclosure')
    xData = xItem.find('pubDate')

    banco.insertEpisodio(conn, xTitle.text, xEnclosure.text, xData.text)

    #print(xEnclosure.attrib['url'])
    #print (xTitle.text)

banco.conexao.commit()
conn.close()