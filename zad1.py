import datetime
class Company:
    def __init__(self,code,datestart,risk_percent):
        self.code = code
        self.datestart = datestart
        self.risk_percent = risk_percent

class ApiLondon:
    def __init__(self):
        self.companies = []
    def add_company(self,company):
        self.companies.append(company)
    def getRisk(self,code,days):
        isCompany = False
        for el in self.companies:
            if code in el.code:
                isCompany = True
                print("Ryzyko wynosi " +  str(el.risk_percent))
        if isCompany == False:
            return -1

    
class ApiSingapur:
    def __init__(self):
        self.companies = []
    def add_company(self,company):
        self.companies.append(company)
    def checkCompany(self,code):
        isCompany = False
        for i in self.companies:
            if i.code == code:
                isCompany = True
                print(i.code + "Jest na giełdzie w Singapurze")
        if isCompany == False:
            return -1
    def getCompanyRisk(self,code,months):
        for el in self.companies:
            print("Ryzyko wynosi " + str(el.risk_percent))
class ApiNewYork:
    def __init__(self):
        self.companies = []
    def add_company(self,company):
        self.companies.append(company)
    def companyTrustworthy(self,code,days):
        isCompany = False
        for el in self.companies:
            if code in el.code:
                isCompany = True
                print("Ryzyko wynosi " +  str(el.risk_percent))
        if isCompany == False:
            return -1

class Facade:
    def __init__(self):
        self.newyork = ApiNewYork()
        self.singapur = ApiSingapur()
        self.london = ApiLondon()
        company1 = Company('ORLACL',datetime.datetime(2021, 2, 10),0)
        company1b = Company('ORLACL',datetime.datetime(2021, 2, 10),100)
        company2 = Company('ORLBOK',datetime.datetime(2021, 2, 10),100)
        company3 = Company('ORLDRU',datetime.datetime(2021, 2, 10),100)
        self.newyork.add_company(company1)
        self.singapur.add_company(company1b)
        self.singapur.add_company(company2)
        self.london.add_company(company3)
    def interface(self):
        self.singapur.checkCompany("ORLACL")
        self.singapur.checkCompany("ORLBOK")
    def analytics(self,code):
        srednia = []
        sred = 0 
        for el in self.newyork.companies:
            if code in el.code:
                print("dodaje do nowego yorku")
                self.newyork.companyTrustworthy(code,"30")
                srednia.append(el)
        for el in self.singapur.companies:
            if code in el.code:
                print("dodaje do singapuru")
                self.singapur.getCompanyRisk(code,"14")
                srednia.append(el)
        for el in self.london.companies:
            if code in el.code:
                print("dodaje do londynu")
                self.london.getRisk(code,"11")
                srednia.append(el)
        for el in srednia:
            sred = sred + el.risk_percent
        wynik = sred / len(srednia)
        print(wynik)

if __name__ == "__main__":
    facade = Facade()
    facade.interface()
    facade.analytics("ORLACL")


     
