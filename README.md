# EncourageExpress

This Python code is a program that sends a motivational quote via email to a specific recipient if the day of the week is Sunday (i.e., if the today variable equals 6).

The program first imports the necessary modules - datetime and smtplib for date and time calculations and email sending, respectively, and random for generating a random quote. It then defines a function fetchQuote() that reads a text file quotes.txt and returns a random quote from that file.

Next, the program uses the datetime.now() function to get the current date and time, and the weekday() method to get the day of the week, where Monday is 0 and Sunday is 6. It then generates a random quote using the fetchQuote() function and assigns it to the variable q.

If the day of the week is Sunday (i.e., today equals 6), the program uses the smtplib module to connect to an email server (in this case, smtp.gmail.com) on port 587, and logs in to the sender's Gmail account using the login() method. It then sends an email to the recipient's email address with a subject line "Motivation Dose!" and the quote as the body of the email.
