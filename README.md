# httpaw-CSEC462-2171-Makhija--Menezes

Tool that inputs .pcap files and parses through them, picking up any websites that have been visited. It will then sort out websites that have been visited frequently along with which hosts visited them. This can help figure out which websites should be tested/looked into as hosts visit it often.



Steps that will be taken for project completion: 

Step 1: We will be coding in python and call tshark to parse in .pcap files. Tshark display filters will be used to find websites that have been visited by hosts which will be redirected to another file.

Step 2: The file will be sorted so that they are all unique and all websites will have a count value. This will show how many hosts visit a particular website.

Step 3: The sorted websites will be used to visualize. We are considering using d3js. This graph in particular where a website will be a higher node with host names as the lower node. http://mbostock.github.io/d3/talk/20111018/cluster.html

