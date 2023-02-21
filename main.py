import datetime as dt
import smtplib
import random
def fetchQuote():
    quotes_file=open("./quotes.txt","r", encoding='utf-8')
    list_of_quotes = quotes_file.readlines()

    number_of_quotes = len(list_of_quotes)
    my_quote=list_of_quotes[random.randrange(number_of_quotes)]
    return my_quote
today=dt.datetime.now().weekday()
print(today)
q = str(fetchQuote())
if(today==6):
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.login("MandeeepShergill94@gmail.com",password="ftcyowflodtsewai")
        connection.sendmail(from_addr="MandeeepShergill94@gmail.com", to_addrs="MaanoShergill@gmail.com",msg="SUbject - Motivation Dose!\n\n"+str(q.encode('utf-8')))

