import re
import json
import sys

#Desenvolvido por: Bee Solutions
#Autor: Fernando Almondes
#Data: 05/11/2024 - 23:55

# Capturando os pacotes DNS: tcpdump -ni ens18 udp port 53 -c 1000 -w dns.pcap
# Criando o arquivo com as estatisticas do dnstop: dnstop dump.pcap -l4 > dnstop.txt

#1 - Sources (Top origens)
#2 - Destinations (Top destinos)
#3 - Query Type (Tipo das requisicoes)
#4 - Opcode (Codigo das requisicoes)
#5 - Rcode (Resultados das requisicoes)
#6 - Query Name (root)
#7 - Query Name (n1)
#8 - Query Name (n2)
#9 - Query Name (n3)
#10 - Source para root
#11 - Source para n1
#12 - Source para n2
#13 - Source para n3

try:
    op = int(sys.argv[1])
except:
    print()
    print('--> Desenvolvido por: Bee Solutions')
    print('--> Autor: Fernando Almondes')
    print('--> Use: python beedns.py 1-3 ou 5-13')
    print()
    exit(1)

if op == 4:
    print()
    print('--> Desenvolvido por: Bee Solutions')
    print('--> Autor: Fernando Almondes')
    print('--> Use: python beedns.py 1-3 ou 5-13')
    print()
    exit(1)

# Abrir o arquivo e ler o conteudo
with open("/opt/bee/beesoftDNS/tmp/dnstop.txt", "r") as f:
    conteudo = f.read()

# Dividir o conteudo com base no delimitador
partes = conteudo.split("------\n")

# Remover linhas em branco e imprimir cada parte
partes = [parte.strip() for parte in partes if parte.strip()]

# Removendo strings indesejadas
rp = re.sub(r'Source.*|---.*', '', partes[op]).strip()
rp = re.sub(r'Destination.*', '', rp).strip()
rp = re.sub(r'Query.*', '', rp).strip()
rp = re.sub(r'Opcode.*', '', rp).strip()
rp = re.sub(r'Rcode.*', '', rp).strip()
rp = re.sub(r'Count.*', '', rp).strip()
rp = re.sub(r'\?', '', rp).strip()
#print(rp)

# Transformando a saida da regex em uma lista, cada linha um item
teste = re.split('\n', rp)
#print(teste)

lista = []

# Adicionando os itens em uma nova lista, removendo espacos em branco e seprandos os elementos por ponto e virgula
for i in teste:
    lista.append(re.sub(r'\s+',';', i))

# Criando novas listas baseadas na separadao anterior
var = [t.split(';') for t in lista]

lista_final = []

# Criando dicionario final para transformar em um json (limitando a consulta a 10 resultados)
for i in var[:10]:
    if len(i[0]):
        dicionario = {
            "dominio": i[0],
            "qut": i[1]
            #"pct": i[2]
        }

        lista_final.append(dicionario)

saida_final = json.dumps(lista_final, indent=4)
print(saida_final)