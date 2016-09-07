#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
import email_alarm
from ConfigParser import SafeConfigParser
import re
import os


# Einstellungen abrufen und setzen
#---------------------------------
config_file = "alert.conf"

path = os.path.dirname(os.path.abspath(__file__)) 		# Pfad der aktuellen Datei
path_config_file = "%s/%s" %(path, config_file) 		# Pfad und Dateiname für die Konfigurationsdatei

config = SafeConfigParser()
config.read(path_config_file)

email = config.getboolean('alert', 'email')			# Soll eine Alarm- E-Mail versendet werden?
telefon = config.getboolean('alert', 'telefon')			# Soll ein Alarmanruf ausgeführt werden


# Liste mit allen Inputs
inputs = []
for section in config.sections():
        if re.search('^input-\d\d$', section):
                inputs.append(section)

# Liste mit allen Outputs
outputs = []
for section in config.sections():
        if re.search('^output-\d\d$', section):
                outputs.append(section)


logfile = config.get('alert', 'logfile')


# GPIO initialisieren
#---------------------
GPIO.setmode(GPIO.BOARD)       					# PIN Nummerierung per P1 RPi Board
GPIO.setwarnings(False)         				# Warnung mehrfach Initialisierung deaktivieren


# Inputs
for section in inputs:
	GPIO.setup(int(config._sections[section]["pin"]), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)		# GPIO PIN als Eingang einstellen
	GPIO.add_event_detect(int(config._sections[section]["pin"]), GPIO.RISING, bouncetime=500)	# Flankenerkennung für Eingang aktivieren

# Outputs
for section in outputs:
	GPIO.setup(int(config._sections[section]["pin"]), GPIO.OUT)					# GPIO PIN einstellen



def main():

	try:	
		print (time.strftime("%Y-%m-%d %H:%M ") + "Alert_pi gestartet") # Textausgabe

		while(True):							#Loop
			# Zusände der Eingänge abrufen
			#------------------------------
			zeit = time.strftime("%Y-%m-%d;%X")				# Aktuelle Systemzeit einlesen
			
			# Flankenerkennung
			for section in inputs:		
				if GPIO.event_detected(int(config._sections[section]["pin"])):		# Auslöser
					save_log(zeit, config._sections[section]["name"])		# Log eintragen

			# Zusandserkennung
#			for section in inputs:
#				if GPIO.input(int(config._sections[section]["pin"])):		# Auslöser
#					save_log(zeit, config._sections[section]["name"])	# Log eintragen

			time.sleep(config.getfloat('alert', 'time_interval'))			#Wartezeit bis die Schleifen ein weiters mal durchlaufen wird

        except KeyboardInterrupt:                                                       	# Ausnahme, wenn Abbruch durch Strg + C
                close()                                                            		# GPIOs zurücksetzen
                print ("\n" + time.strftime("%Y-%m-%d %H:%M ") + "Abbruch durch den Benutzer")  # Textausgabe



def save_log(time, name):
	file = open(logfile,"a")						# Datei öffnen
	file.write(str(time) + ";" + name + "\r\n")				# Daten in Datei speichern
	file.close()								# Datei schließen
	print str(time) + " " + name + " wurde ausgelöst"


def Result():

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


def close():

	# Abschlussprozedur
	#------------------
	GPIO.cleanup()							# GPIO Einstellungen zurücksetzen




#Codeblock zum Testen bei direktem aufrufen der Datei
#----------------------------------------------------
if __name__ == "__main__":
	main()
