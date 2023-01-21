from splinter import Browser
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
import time
import requests

try:
    chromedriver_autoinstaller.install()
    options = Options()
    options.add_argument('disable-blink-features=AutomationControlled')
    browser = Browser('chrome', incognito=True, options=options)
except:
    raise Exception('Problem setting up automation.')

try:
    browser.visit('https://chong.kai-oscar.com/oscar/index')

    while True:
        if not browser.find_by_id('username'):
            browser.reload()
            time.sleep(10)
            if not browser.find_by_id('username'):
                raise Exception('Problem initializing OSCAR.')
        else:
            browser.find_by_id('username').fill('Nathan')
            break
        
    browser.find_by_id('password').fill('Nathan2003')
    browser.find_by_css('button.button.is-green.btn-primary').click()


    browser.visit('https://chong.kai-oscar.com/kaiemr/#/inbox?providerNo=400001')

    # add in switch to documents to file
    #browser.find_by_css('a.s_a_j_dropdown-toggle').first.click()
    #browser.find_by_text('Documents, to File').click()
    time.sleep(5)
    browser.find_by_css('tr.inbox-row').first.click()

except: 
    raise Exception('Problem initializing OSCAR.')

# run the 

section = browser.find_by_id('modal-container')


section.find_by_tag('input').first.fill('Hi')
section.find_by_css('input.s_a_j_color_2.keyword').fill('Chong, Nathan')


search = section.find_by_tag('app-typeahead').first
drop = search.find_by_tag('ul')


class FindDate:
    def __init__(self):
        self.element = None
    def runthrough(self, elemlist):
        if len(elemlist) == 0:
            self.element = None
        else: 
            x = 0
            while x < len(elemlist):
                iter = elemlist[x]
                text = iter.text
                if '2003-05-31' in text.lower() and 'chong, nathan' in text.lower():
                    self.element = iter
                    break
                else: 
                    x += 1

while True:
    if not drop.find_by_tag('li'):
        time.sleep(20)
        if not drop.find_by_tag('li'):
            raise Exception('No name matches found.')
    else:
        namelist = drop.find_by_tag('li')
        break

finder = FindDate()
finder.runthrough(namelist)
if finder.element == None:
    raise Exception('No DOB matches found.')
else:
    finder.element.click()

nobs = section.find_by_css('div.tags')
#nobs.find_by_text('Documents, to File').click()

section.find_by_text('Print').click()
doc = browser.url
r = requests.get(doc, allow_redirects = True)
open('testy.pdf', 'wb').write(r.content)



