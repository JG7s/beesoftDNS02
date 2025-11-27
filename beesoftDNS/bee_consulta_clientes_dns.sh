#!/bin/bash

# Desenvolvido por: Bee Solutions
# Autor: Fernando Almondes
# Data: 08/11/2024 - 18:52

cat /usr/lib/zabbix/externalscripts/beedns/saida-captura-clientes-dns.txt | sort -u | wc -l
