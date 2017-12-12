import csv
import json

class Node(object):
    def __init__(self, name, size=None):
        self.name = name
        self.children = []
        self.size = size

    def child(self, cname, size=None):
        child_found = [c for c in self.children if c.name == cname]
        if not child_found:
            _child = Node(cname, size)
            self.children.append(_child)
        else:
            _child = child_found[0]
        return _child

    def as_dict(self):
        res = {'name': self.name}
        if self.size is None:
            res['children'] = [c.as_dict() for c in self.children]
        else:
            res['size'] = self.size
        return res


root = Node('Hosts')

with open('step2.csv', 'r') as f:
    reader = csv.reader(f)
    reader.next()
    for row in reader:
        grp1, grp2, size = row
        root.child(grp1).child(grp2).child(size)
    		
#print json.dumps(root.as_dict(), indent=4)
jsonfile = open('step3.json', 'w')
out = json.dumps(root.as_dict(), indent=4)
jsonfile.write(out)
