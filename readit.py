from PyPDF2 import PdfReader

flag = True 

def iso(x,y,z):
    global flag
    try:
        part = y.index(x)
    except:
        flag = False
    else:
        if z == 'l':
            return y[:part]
        if z == 'r':
            part += len(x)
            return y[part:]

class Solution():
    def __init__(self, filename):
        reader = PdfReader(filename)
        page = reader.pages[0]
        self.text = page.extract_text(0)
        self.dict = {}
        self.lister = self.text.split('\n')
        
    def holt(self):
        self.name = self.lister[-1]
        self.date = self.lister[8]
        lista = self.name.split(', ')
        self.dict['name'] = ' '.join(lista)
        self.dict['type'] = 'holter'
        first = iso('Number: ', self.date, 'r')
        self.dict['date'] = iso(' ', first, 'l').split('/')
        return self.dict

    def ett(self):
        self.name = self.lister[-1]
        self.date = self.lister[6]

        self.dict['type'] = 'ett'
        self.dict['name'] = iso('Name: ', self.name, 'r')
        first = iso('DOB: ', self.date, 'r')
        self.dict['date'] = iso(' ', first, 'l').split('.')
        return self.dict

    def ecg(self):
        self.name = self.lister[-6]
        self.date = self.lister[-4]
        
        self.dict['type'] = 'ecg'
        self.dict['name'] = iso('Name: ', self.name, 'r')
        self.dict['date'] = iso('Birthdate: ', self.date, 'r').split('/')
        return self.dict

def operation(op):
    solution = Solution(op)
    while True:
        if 'EXERCISE STRESS TEST REPORT' in solution.lister:
            return solution.ett()
        elif '2-D\xa0and\xa0Doppler\xa0Echocardiography\xa0Report' in solution.lister:
            return solution.ecg()
        elif 'HOLTER MONITOR REPORT' in solution.lister:
            return solution.holt()
        else:
            print('No result')
            break

print(operation())