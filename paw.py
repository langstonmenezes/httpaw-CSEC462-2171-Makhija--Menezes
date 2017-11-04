import pyshark
 
cap = pyshark.FileCapture('test.pcap')
filtered_cap = pyshark.FileCapture(path_to_file, display_filter='http')


cap = pyshark.FileCapture('test.pcap', display_filter="http")
 for pkt in cap:
     print pkt.highest_layer
