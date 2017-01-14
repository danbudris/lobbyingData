import xml.etree.ElementTree as ET
import os

##START FUNCTIONS##

values = []

def returnValues(child):
    '''encapsulated the recurse function in another function, because it was not returning the correct values if the 'values' list was inside of the recurse function'''
    def recurseXML(child):
        ''' recurse through the XML, and return a list of non-empty values '''
        for subchild in child:
            if not "\n" in subchild.text:
                values.append([subchild.tag,subchild.text])
            recurseXML(subchild)
        return values
        
    values = []
    return recurseXML(child)

def buildTree(path):
    ''' create the tree from the given data '''
    tree = ET.parse(path)
    root = tree.getroot()
    return root

##END FUNCTIONS##

Datapath = '/Users/Dan/Documents/projects/lobbyingData/Datastore/2016_1stQuarter_XML'
temp = '/Users/Dan/Documents/projects/lobbyingData/Datastore/2016_1stQuarter_XML/300802522.xml'
attributes = {'lobbyistFirstName':'','lobbyistLastName':'','organizationName':'','clientName':'','issueAreaCode':'','income':'','senateID':'','houseID':'','address1':'','address2':'','city':'','state':'','zip':'','country':'','federal_agencies':''}
lobbyistlist = []

#for filename in os.listdir(Datapath):
    #path = str(Datapath)+str(filename)
tree = buildTree(temp)
data = returnValues(tree)

for line in data:
    if line[0] in attributes:
        attributes[line[0]] = line[1]


