class Person(object):
    "Person parent class"
    def __init__ (self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        
    def get_name(self):
        return "%s %s, %s" %(self.firstname, self.lastname)
        
class Lobbyist(Person):
    "Lobbyist subclass of person"
    def __init__(self,firstname):
        self.firstname = firstname
class Legislator(Person):
    "Legislator sub class of person"
    def __init__(self,firstname,lastname,politicalbranch):
        Person.__init__(self,firstname,lastname)
        self.politicalbranch = politicalbranch
        
class Organization(object):
    "An organization parent class"
    def __init__(self,name,address,city,state,zipcode,country):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.country = country

    def get_details(self):
        return self.name
        
    def get_members(self):
        "Returns a list of person objects associated with this organization"
        return self.members

class Firm(Organization):
    "lobbying firm sub class"
    def __init__(self,name,address):
        self.name = name
           
class Corporation(Organization):
    "corporation sub class"
    def __init__(self,name,address):
        self.name = name
        
class Government(Organization):
    "government sub class"
    def __init__(self,name,address):
        self.name = name
    
    
    