# httpaw-CSEC462-2171-Makhija--Menezes

Tool that inputs .pcap files and parses through them, picking up any websites that have been visited. It will then sort out websites that have been visited frequently along with which hosts visited them. This can help figure out which websites should be tested/looked into as hosts visit it often.



Steps that will be taken for project completion: 

Step 1: We will be coding in python and call tshark to parse in .pcap files. Tshark display filters will be used to find websites that have been visited by hosts which will be redirected to another file.

Step 2: The file will be sorted so that they are all unique and all websites will have a count value. This will show how many hosts visit a particular website.

Step 3: The sorted websites will be used to visualize. We are considering using d3js. This graph in particular where a website will be a higher node with host names as the lower node. http://mbostock.github.io/d3/talk/20111018/cluster.html

How to use the tool?

Step 1: Generate a PCAP file. Make sure all the .py files are in the same directory. If you are working with Linux, you will need to start apache and change some permissions in order to open the index.html file.  

Step 2: Open step1.py, input the name of the pcap file in the tshark command. (An update to have a raw input will come soon)

Step 3: Run step1.py. After that you will see that it creates a .csv file.

Step 4: Run step2.py

Step 5: Run step3.py. Now it creates a json file. Move the json file to the directory where the index.html exists. Open the index.html file and it will visualize the data
