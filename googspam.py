import sys
import mechanize
import random
import string

def fill_control(control):
    total = len(control.get_items())
    set_vals = str(control.get_items()[random.randint(1,total-1)])
    control.value = [set_vals]


def text_rand(control,length):
    control.value = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(length))   



def  fill_form(form):
    for control in form.controls:
        if control.type=="text":
            text_rand(control,'15')
        elif control.type=="textarea":
            text_rand(control,'100')
        elif control.type=="radio":
            fill_control(control)
        elif control.type=="checkbox":
            fill_control(control)
        elif control.type=="select":
            fill_control(control)
    


def new_browser():
    bs = mechanize.Browser()
    bs.set_handle_robots(False)
    bs.set_handle_refresh(False)
    return bs



def googspam(url,ntimes = 1):
    browser = new_browser()
    total = ntimes
    while times:
        browser.open(url)
        browser.form = list(browser.forms())[0]
        fill_form(browser.form)
        browser.submit()
        times -=1
        print("Times" , total-times)


if __name__ == '__main__':
    if len(sys.argv)<3:
        print("Run script as \n 'python googspam.py 'url' times ")
        exit()
    url = sys.argv[1]
    ntimes = sys.argv[2]
    googspam(url,ntimes)
