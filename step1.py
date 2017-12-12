import subprocess

command = "tshark -r test1.pcapng -2 -R http.request -Tfields -e ip.src -e http.host | sort | uniq>step1.csv"

subprocess.call([command], shell= True)

command2="tshark -r test1.pcapng -2 -R http.request -Tfields -e ip.dst | sort | uniq>step1dns.csv"

subprocess.call([command2], shell= True)


