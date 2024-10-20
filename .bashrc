# Iniciar sistema

clear

# Iniciar tor

echo -n "Iniciando Tor..."
TOR_BINARY=/data/data/com.termux/files/usr/bin/tor
 --quiet &>/dev/null &
echo "Listo."

# Banner

cd

clear

cd Stellar

python banner.py

cd


# Comandos principales

menu() {
 cd Stellar
 python menu.py
 cd
}


reload() {
  clear
  cd Stellar
  python banner.py
  cd
}


# Comandos para funciones y scripts

ipinfo() {
  cd Stellar/osint
  python ipinfo.py
  cd
}

phoneinfo() {
  cd Stellar/osint
  python phoneinfo.py
  cd
}

urlinfo() {
  cd Stellar/osint
  python urlinfo.py
  cd
}

# Comandos para historial y utilidades

ipinfohistory() {
  cd Stellar/database
  python ips_info_db_consult.py
  cd
}

phoneinfohistory() {
  cd Stellar/database
  python phone_info_db_consult.py
  cd
}

ia() {
  cd Stellar/ia
  python iahttp.py
  cd
}

}
