#!/bin/bash

# Desenvolvido por: Bee Solutions
# Autor: Fernando Almondes
# Data: 05/11/2024 - 23:11

interface='ens18'

# Verifique o caminho completo para os executaveis e ajuste se necessario
# which timeout 
# which dnstop

# Capturando informacoes sobre as consultas DNS - Padrao 10s
/usr/bin/timeout 10 /usr/sbin/tcpdump -ni $interface udp port 53 -w /opt/bee/beesoftDNS/tmp/dns.pcap
/usr/bin/dnstop /opt/bee/beesoftDNS/tmp/dns.pcap -l4 > /opt/bee/beesoftDNS/tmp/dnstop.txt

check=$(cat /opt/bee/beesoftDNS/tmp/dnstop.txt | grep 'A?')

if [[ -z "$check" ]]; then

echo ""
echo "--> Desenvolvido por: Bee Solutions"
echo "--> Autor: Fernando Almondes"
echo "--> Erro! (Verifique se o arquivo pcap foi gerado corretamente..."
echo ""

exit 1

fi

for i in $(seq $i 13);
do
#echo $i

/opt/bee/beesoftDNS/venv/bin/python3 /opt/bee/beesoftDNS/dnstop.py $i > /opt/bee/beesoftDNS/tmp/$i.json

done