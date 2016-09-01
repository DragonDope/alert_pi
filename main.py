#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
import email_alarm
from ConfigParser import SafeConfigParser

def main():

	# Einstellungen
	#---------------

        parser = SafeConfigParser()
        parser.read('config.conf')
        print parser.get('files', 'digitemp_config_file')


	email = True			# Soll eine Alarm- E-Mail versendet werden?
	telefon = True			# Soll ein Alarmanruf ausgeführt werden?

	# GPIO initialisieren
	#---------------------
	GPIO.setmode(GPIO.BOARD)	# PIN Nummerierung per P1 RPi Board
	GPIO.setwarnings(False)		# Warnung mehrfach Initialisierung deaktivieren


	# Ein- und Ausgänge deklarieren
	#-------------------------------
	IN_01 = 15
	IN_02 = 16

	OUT_01 = 18

	GPIO.setup(IN_01, GPIO.IN, pull_up_down=GPIO.PUD_UP)		# GPIO PIN einstellen
	GPIO.setup(IN_02, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)		# GPIO PIN einstellen
	GPIO.setup(OUT_01, GPIO.OUT)					# GPIO PIN einstellen

	zeit = time.strftime("%Y-%m-%d;%X")				# Aktuelle Systemzeit einlesen
	state_01 = GPIO.input(IN_01)					# GPIO Status einlesen
	state_02 = GPIO.input(IN_02)					# GPIO Status einlesen


	# Bildschirmausgabe
	#-------------------
	print(str(zeit)  + " ; GPIO 01 = " + str(state_01) + " (Pull-UP)")		# Bildschirmausgabe
	print(str(zeit)  + " ; GPIO 02 = " + str(state_02) + " (Pull-DOWN)")		# Bildschirmausgabe


	# Daten in Datei speichern
	#--------------------------
	file = open("alarm.csv","a")							# Datei öffnen
	file.write(str(zeit) + " ; GPIO 01 = " + str(state_01) + " (Pull-UP)\n")	# Daten in Datei speichern
	file.write(str(zeit) + " ; GPIO 02 = " + str(state_02) + " (Pull-UP)\n")	# Daten in Datei speichern
	file.close()									# Datei schließen


	# Alarmausgeben
	#--------------
	email_alarm.senden(email)					# Je nach Einstellung wird eine Alarm- E-Mail versendet
	if telefon:							# Bedingung für Telefonalarm
		GPIO.output(OUT_01, True)					# GPIO-Ausgang setzen
		print("Start TIME")
		print(time.strftime("%Y-%m-%d;%X"))                             # Aktuelle Systemzeit einlesen
		time.sleep(1.0)							# Wartezeit
		GPIO.output(OUT_01, False)					# GPIO zurücksetzen
		print("End TIME")
		print(time.strftime("%Y-%m-%d;%X"))                             # Aktuelle Systemzeit einlesen


	# Abschlussprozedur
	#------------------
	GPIO.cleanup()							# GPIO Einstellungen zurücksetzen


	#time.sleep(0.5)



#Codeblock zum Testen bei direktem aufrufen der Datei
#----------------------------------------------------
if __name__ == "__main__":
	main()
