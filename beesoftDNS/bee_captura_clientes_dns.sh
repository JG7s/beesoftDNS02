#!/bin/bash

# Desenvolvido por: Bee Solutions
# Autor: Fernando Almondes
# Data: 08/11/2024 - 18:52

interface="ens18"

# Verifique o caminho completo para os executaveis e ajuste se necessario
# which timeout 
# which tcpdump

/usr/bin/timeout 10 /usr/bin/tcpdump -ni $interface 'udp dst port 53' -l 2>/dev/null | awk '{print $3}' | sed 's/\.\([0-9]*\)$//' > /usr/lib/zabbix/externalscripts/beedns/saida-captura-clientes-dns.txt
