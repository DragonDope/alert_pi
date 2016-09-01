#!/usr/bin/env python
# -*- coding: utf-8 -*-

def senden(email):
	"""	Dies ist ein kleines Programm zum verschicken einer E-Mail mit Anhang.
	Creator: DragonDope	Date: 2014-09-07

	Mit der Variablen "email" kann man die Funktion aktivieren und deaktivieren

	Info: Kein Rückgabewerte
	"""

	import smtplib
	import os
	from email.message import Message
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText
	from email.mime.application import MIMEApplication
	
	#Ein-/Ausschalter fuer E-Mailversand
	#----------------------------------
	#email = test
	
	print ("---> Programm START <---")
	
	#Einstellungen E-Mailversand
	#---------------------------
	host = "smtp.1und1.de"
	port = 25
	benutzer = "benutzerprogramm@online.de"
	passwort = "XXXxxxXXX"
	absender = "Benutzer Programm <benutzer@online.de>"
	empfaenger = "Max Mustermann <maxmustermann@gmx.de>"
	dateianhang = "/home/pi/LMF_project/alert/alarm.csv"
	
	if email:
		print("E-Mail Funktion wird ausgeführt")
		#E-Mail Erstellung (Header, Text usw.)
		msg = MIMEMultipart()
		msg["Subject"] = "Alarmstatus"
		msg["From"] = absender
		msg["To"] = empfaenger
	
		mailtext = MIMEText("Hier kommt noch ein geeigneter Text dazu")
		msg.attach(mailtext)
	
	
		if os.path.exists(dateianhang):
			file = open(dateianhang)
			anhang = MIMEApplication(file.read())
			#anhang.add_header("Content-ID", "<csv>")  Noch noch verbessert werden
			anhang.add_header("Content-Disposition", "attachment", filename=os.path.basename(dateianhang))
			anhang.add_header("Content-Disposition", "inline", filename=os.path.basename(dateianhang))
			file.close()
			msg.attach(anhang)
		else:
			print("Datei existiert nicht!\nE-Mail ohne Dateianhang wird ohne Anhang verschickt")
	
		body = msg.as_string()
		
		#E-Mail Sendevorgang (per smtp mit starttls)
		print("Starte Sendevorgang ...")
		smtp = smtplib.SMTP(host,port)
		smtp.starttls()
		smtp.login(benutzer,passwort)
		smtp.sendmail(absender,empfaenger,body)
		smtp.quit()
		print("Die E-Mail wurde erfolgreich versendet")
	else:
		print ("Die E-Mail Funktion ist nicht aktiv")

	print ("---> Programm ENDE <---")


#Codeblock zum Testen bei direktem aufrufen der Datei
if __name__ == "__main__":
	print("\nProgramm testen mit -True-\n----------")
	senden(True)
	
	print("\nProgramm test mit -False-\n----------")
	senden(False)

