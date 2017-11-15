import pyshark
 
cap = pyshark.FileCapture('test.pcap')
filtered_cap = pyshark.FileCapture(path_to_file, display_filter='http')


cap = pyshark.FileCapture('test.pcap', display_filter="http")
 for pkt in cap:
     print pkt.highest_layer
#Still in two minds about which tool to use to properly parse .pcap file to show source IP and hostnames. For now:
import subprocess

#bashCommand
ngrep_cmd = "ngrep -I test.pcap -W byline | grep Host | sort | uniq > test.csv"


subprocess.call([ngrep_cmd], shell=True)


