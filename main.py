#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
import email_alarm
from ConfigParser import SafeConfigParser
import re


# Einstellungen abrufen und setzen
#---------------------------------
config = SafeConfigParser()
config.read('./alert.conf')

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

#Schlagwort Dictionary

logfile = config.get('alert', 'logfile')


# GPIO initialisieren
#---------------------
GPIO.setmode(GPIO.BOARD)       					# PIN Nummerierung per P1 RPi Board
GPIO.setwarnings(False)         				# Warnung mehrfach Initialisierung deaktivieren


#Inputs
for section in inputs:
	GPIO.setup(int(config._sections[section]["pin"]), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)		# GPIO PIN einstellen


#Outputs
for section in outputs:
	GPIO.setup(int(config._sections[section]["pin"]), GPIO.OUT)					# GPIO PIN einstellen


def main():
	
#        GPIO.add_event_detect(IN_01, GPIO.RISING)                       # Flankenerkennung für Eingang aktivieren
#        GPIO.add_event_detect(IN_02, GPIO.RISING)                       # Flankenerkennung für Eingang aktivieren
#        GPIO.add_event_detect(IN_03, GPIO.RISING)                       # Flankenerkennung für Eingang aktivieren
#        GPIO.add_event_detect(IN_04, GPIO.RISING)                       # Flankenerkennung für Eingang aktivieren
#        GPIO.add_event_detect(IN_05, GPIO.RISING)                       # Flankenerkennung für Eingang aktivieren
#        GPIO.add_event_detect(IN_06, GPIO.RISING)                       # Flankenerkennung für Eingang aktivieren
#        GPIO.add_event_detect(IN_07, GPIO.RISING)                       # Flankenerkennung für Eingang aktivieren
#        GPIO.add_event_detect(IN_08, GPIO.RISING)                       # Flankenerkennung für Eingang aktivieren


	while(True):							#Loop
		# Zusände der Eingänge abrufen
		#------------------------------
		zeit = time.strftime("%Y-%m-%d;%X")				# Aktuelle Systemzeit einlesen
		
#		if GPIO.event_detected(IN_01):					# Auslöser
#			save_log(zeit, name_IN_01)				# Log eintragen
#                if GPIO.event_detected(IN_02):                                  # Auslöser
#                        save_log(zeit, name_IN_02)                              # Log eintragen
#                if GPIO.event_detected(IN_03):                                  # Auslöser
#                        save_log(zeit, name_IN_03)                              # Log eintragen
#                if GPIO.event_detected(IN_04):                                  # Auslöser
#                        save_log(zeit, name_IN_04)                              # Log eintragen
#                if GPIO.event_detected(IN_05):                                  # Auslöser
#                        save_log(zeit, name_IN_05)                              # Log eintragen
#                if GPIO.event_detected(IN_06):                                  # Auslöser
#                        save_log(zeit, name_IN_06)                              # Log eintragen
#                if GPIO.event_detected(IN_07):                                  # Auslöser
#                        save_log(zeit, name_IN_07)                              # Log eintragen
#                if GPIO.event_detected(IN_08):                                  # Auslöser
#                        save_log(zeit, name_IN_08)                              # Log eintragen

		for section in inputs:
			if GPIO.input(int(config._sections[section]["pin"])):		# Auslöser
				save_log(zeit, config._sections[section]["name"])	# Log eintragen

		time.sleep(0.5)								#Wartezeit bis die Schleifen ein weiters mal durchlaufen wird


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
	GPIO.remove_event_detect(IN_01)					# Flankenerkennung deaktivieren
	GPIO.remove_event_detect(IN_02)                                 # Flankenerkennung deaktivieren
	GPIO.remove_event_detect(IN_03)                                 # Flankenerkennung deaktivieren
	GPIO.remove_event_detect(IN_04)                                 # Flankenerkennung deaktivieren
        GPIO.remove_event_detect(IN_05)                                 # Flankenerkennung deaktivieren
        GPIO.remove_event_detect(IN_06)                                 # Flankenerkennung deaktivieren
        GPIO.remove_event_detect(IN_07)                                 # Flankenerkennung deaktivieren
        GPIO.remove_event_detect(IN_08)                                 # Flankenerkennung deaktivieren




#Codeblock zum Testen bei direktem aufrufen der Datei
#----------------------------------------------------
if __name__ == "__main__":
	main()
