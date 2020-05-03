from flask import Flask, redirect, url_for, request
from flask import flash, render_template, session, abort
from random import randint

from flask_wtf import FlaskForm
from wtforms import SelectField
from flask_bootstrap import Bootstrap


from matching_algorithm import *
import smtplib


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

Bootstrap(app)
d = {}
tellers = {}

class Form(FlaskForm):
    language = SelectField('languages', choices = ['English','Spanish','Chinese', 'Tagalog', 'Vietnamese', 'French', 'Korean', 'German', 'Arabic', 'Russian', 'Italian', 'Portugese', 'Hindi', 'Polish', 'Japanese', 'Persian', 'Greek', 'Hebrew', 'Romanian', 'Thai', 'Ukranian', 'Turkish'])
    service = SelectField('services', choices = ['Consumer Checking and Savings','Auto Loans','Credit Cards','Rewards','Retirement Planning','IRAs and 401(k)s','General Investing','College Planning','Mortgage Financing','Refinancing Home','Home Equity','Business Checking and Savings','Lending','Payroll','Merchant','Financing'])
                          #['Card', 'Deposit', 'Transfer', 'Mortgage', 'Savings', 'Pay', 'Invest', 'Account', 'Loan'])


@app.route('/success/<name>', methods = ['POST', 'GET']) 
def success(name):
    name = d['language']
    name3 = d['service']

    tellers = {}

    tellers = run_algo('Steve Smith', d['language'], d['service'], 'NY')


    the_list = ['language', 'service', 'location', 'availability']
    for key1 in tellers:

        teller1 = tellers[key1][0]
        teller2 = tellers[key1][1]
        teller3 = tellers[key1][2]
  
        teller_1 = teller1[1]
        teller_2 = teller2[1]
        teller_3 = teller3[1]


        teller_1_name = teller1[0]
        teller_1_lang = teller_1[the_list[0]]
        teller_1_serv = teller_1[the_list[1]]
        teller_1_loc = teller_1[the_list[2]]
        teller_1_avail = teller_1[the_list[3]]

        teller_2_name = teller2[0]
        teller_2_lang = teller_2[the_list[0]]
        teller_2_serv = teller_2[the_list[1]]
        teller_2_loc = teller_2[the_list[2]]
        teller_2_avail = teller_2[the_list[3]]

        teller_3_name = teller3[0]
        teller_3_lang = teller_3[the_list[0]]
        teller_3_serv = teller_3[the_list[1]]
        teller_3_loc = teller_3[the_list[2]]
        teller_3_avail = teller_3[the_list[3]]

##    if request.method == 'POST':
##        if "one" in request.form:
##            yolo = "hello my man"
##            return redirect(url_for('page', name4 = yolo))
    

    
    return render_template('test.html',**locals())


@app.route('/',methods = ['POST', 'GET'])
def login(): 
    form=Form()
    if request.method == 'POST':
        d['language'] = form.language.data
        return redirect(url_for('prefer', name2 = form.language.data))

    return render_template('login.html', form=form)


@app.route('/prefer<name2>',methods = ['POST', 'GET'])
def prefer(name2):

    form=Form()
    if request.method == 'POST':
        d['service'] = form.service.data
        d['service'] = request.form['services']
        print(d['service'])
        return redirect(url_for('success', name = request.form['services']))

    return render_template('prefer.html', form=form)


@app.route('/index', methods = ['GET'])
def index():

##    try:
##        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
##        server.echo()
##        server.login(gmail_user, gmail_password)
##        server.sendmail(sent_from, to, email_text)
##        server.close()
##    except:
##        print("ERROR")
    return render_template('index.html')

@app.route('/page<name4>')
def page(name4):
    yolo=name4
    return render_template('page.html',**locals())


if __name__ == '__main__': 
   app.run(debug = False)




   
