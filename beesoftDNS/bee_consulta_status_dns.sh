#!/bin/bash

# Desenvolvido por: Bee Solutions
# Autor: Fernando Almondes
# Data: 08/11/2024 - 18:52

OP=$1

check=$(cat /opt/bee/beesoftDNS/tmp/5.json)

if [[ -z "$check" ]]; then

echo ""
echo "--> Erro ao verificar arquivo json..."
echo ""

exit 1

fi

if [[ -z "$OP" ]]; then

echo ""
echo "--> Use: ./bee_consulta_status_dns.sh Noerror|Refused|Servfail "
echo""

exit 1

fi

resultado=$(cat /opt/bee/beesoftDNS/tmp/5.json | jq -r '.[] | select(.dominio == "'"$OP"'") | .qut')

re='^[0-9]+$'

if [[ $resultado =~ $re ]]; then

echo "$resultado"

else

echo "0"

fi
