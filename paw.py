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

#new code 
import dpkt, socket, glob, pcap, os

    files = [open(f) for f in glob.glob('*.pcap')]
    abc = dpkt.pcap.Reader(file("abc.pcap", "rb")) #opening two pcap files
    def = dpkt.pcap.Reader(file("def.pcap", "rb")) #opening two pcap files

    print files
    print "\r\n"
    List = [abc, fgh] #storing the pcap files in a list to use it

    for ts, data in zip(List): #use these variables we will be able to extract the source and destination from our pcap file
       eth = dpkt.ethernet.Ethernet(data)
       ip = eth.data
       tcp = ip.data

       src = socket.inet_ntoa(ip.src) #source ip
       dst = socket.inet_ntoa(ip.dst) #destination ip

       if tcp.dport == 80 and len(tcp.data) > 0:
          http = dpkt.http.Request(tcp.data)
          print "HTTP Request /", http.version
          print "Type: ", http.method
          print "URI: ", http.uri
          print "User-Agent: ", http.headers ['user-agent']
          print "Source: ", src
          print "Destination: ", dst
          print "\r\n" #once we get the source and destination, we basically visualize that in d3.js

