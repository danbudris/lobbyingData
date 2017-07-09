import csv

Badguys = ["Oil & Gas","Mining","Electric Utilities","Automotive","Chemical & Related Manufacturing","Forestry & Forest Products"]


class Person(object):
    "Person parent class"
    def __init__ (self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        
    def get_name(self):
        return "%s %s, %s" %(self.firstname, self.lastname)
        
class Legislator(Person):
    "Legislator sub class of person"
    def __init__(self,firstname,lastname,politicalbranch):
        Person.__init__(self,firstname,lastname)
        self.politicalbranch = politicalbranch
        self.donors = {}
        self.relevent_influencers = {}
        self.relevent_influencers_environmental = {}
        self.lcv_score_by_year = {}
        
    def get_influencers(self):
        data = '/Users/Dan/Documents/projects/lobbyingData/datastore/2016_%s_%s_industry_contributions.csv'%(self.lastname, self.firstname)
        with open(data, 'rb') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.relevent_influencers[(row['indus'])] = int(row['totals'])
                if row['indus'] in Badguys:
                    self.relevent_influencers_environmental[(row['indus'])] = int(row['totals'])
    
    def get_contributors(self):
        data = '/Users/Dan/Documents/projects/lobbyingData/datastore/mitchm.csv'
        with open(data, 'rb') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Orgname'] not in self.donors:
                    self.donors[(row['Orgname'])] = 0
                if row['Orgname'] in self.donors:
                    self.donors[(row['Orgname'])] += int(row['Amount'])

    def get_lcv_score(self):
        data = '/Users/Dan/Documents/projects/lobbyingData/datastore/%s_%s_lcv.csv' % (self.lastname, self.firstname)
        with open(data, 'rb') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.lcv_score_by_year[(row['Year'])]=[(row['Score']),(row['Pro-environment Votes']),(row['Anti-environment Votes'])]
                
    def lcv_score_in_year(self, year):
        print self.lcv_score_by_year[year]
        
    def lcv_score_in_cycle(self, year):
        year1 = self.lcv_score_by_year[year][0]
        year2 = self.lcv_score_by_year["%s" % str((int(year)-1))][0]
        yearone = year1.replace("%","")
        yeartwo = year2.replace("%","")
        print ((int(yearone) + int(yeartwo))/2)
        self.score_to_contribs = ((int(yearone) + int(yeartwo))/2)