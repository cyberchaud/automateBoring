import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
#type(conn)
print(conn)
print(conn.ehlo())
print(conn.starttls())

#conn.login('', '') #conn.login(username, password)
#google will need an application specific password
conn.quit()