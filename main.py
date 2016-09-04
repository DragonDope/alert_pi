#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
import email_alarm
from ConfigParser import SafeConfigParser


# Einstellungen abrufen und setzen
#---------------------------------
config = SafeConfigParser()
config.read('./alert.conf')

email = config.getboolean('alert', 'email')			# Soll eine Alarm- E-Mail versendet werden?
telefon = config.getboolean('alert', 'telefon')			# Soll ein Alarmanruf ausgeführt werden

IN_01 = config.getint('hardware', 'pin_IN_01')
IN_02 = config.getint('hardware', 'pin_IN_02')
IN_03 = config.getint('hardware', 'pin_IN_03')
IN_04 = config.getint('hardware', 'pin_IN_04')
IN_05 = config.getint('hardware', 'pin_IN_05')
IN_06 = config.getint('hardware', 'pin_IN_06')
IN_07 = config.getint('hardware', 'pin_IN_07')
IN_08 = config.getint('hardware', 'pin_IN_08')

#Schlagwort Dictionary

name_IN_01 = config.get('name', 'name_IN_01')
name_IN_02 = config.get('name', 'name_IN_02')
name_IN_03 = config.get('name', 'name_IN_03')
name_IN_04 = config.get('name', 'name_IN_04')
name_IN_05 = config.get('name', 'name_IN_05')
name_IN_06 = config.get('name', 'name_IN_06')
name_IN_07 = config.get('name', 'name_IN_07')
name_IN_08 = config.get('name', 'name_IN_08')


OUT_01 = config.getint('hardware', 'pin_OUT_01')
OUT_02 = config.getint('hardware', 'pin_OUT_02')
OUT_03 = config.getint('hardware', 'pin_OUT_03')
OUT_04 = config.getint('hardware', 'pin_OUT_04')
OUT_05 = config.getint('hardware', 'pin_OUT_05')
OUT_06 = config.getint('hardware', 'pin_OUT_06')

logfile = config.get('alert', 'logfile')


# GPIO initialisieren
#---------------------
GPIO.setmode(GPIO.BOARD)       					# PIN Nummerierung per P1 RPi Board
GPIO.setwarnings(False)         				# Warnung mehrfach Initialisierung deaktivieren

GPIO.setup(IN_01, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)		# GPIO PIN einstellen
GPIO.setup(IN_02, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)		# GPIO PIN einstellen
GPIO.setup(IN_03, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)          # GPIO PIN einstellen
GPIO.setup(IN_04, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)          # GPIO PIN einstellen
GPIO.setup(IN_05, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)          # GPIO PIN einstellen
GPIO.setup(IN_06, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)          # GPIO PIN einstellen
GPIO.setup(IN_07, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)          # GPIO PIN einstellen
GPIO.setup(IN_08, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)          # GPIO PIN einstellen
GPIO.setup(OUT_01, GPIO.OUT)					# GPIO PIN einstellen
GPIO.setup(OUT_02, GPIO.OUT)                                    # GPIO PIN einstellen
GPIO.setup(OUT_03, GPIO.OUT)                                    # GPIO PIN einstellen
GPIO.setup(OUT_04, GPIO.OUT)                                    # GPIO PIN einstellen
GPIO.setup(OUT_05, GPIO.OUT)                                    # GPIO PIN einstellen
GPIO.setup(OUT_06, GPIO.OUT)                                    # GPIO PIN einstellen


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
		# Zusänder der Eingänge abrufen
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

                if GPIO.input(IN_01):	                                  	# Auslöser
                        save_log(zeit, name_IN_01)                              # Log eintragen
                if GPIO.input(IN_02):   	                               	# Auslöser
                        save_log(zeit, name_IN_02)                              # Log eintragen
                if GPIO.input(IN_03):           	                       	# Auslöser
                        save_log(zeit, name_IN_03)                              # Log eintragen
                if GPIO.input(IN_04):                   	               	# Auslöser
                        save_log(zeit, name_IN_04)                              # Log eintragen
                if GPIO.input(IN_05):                           	       	# Auslöser
                        save_log(zeit, name_IN_05)                              # Log eintragen
                if GPIO.input(IN_06):                                  		# Auslöser
                        save_log(zeit, name_IN_06)                              # Log eintragen
                if GPIO.input(IN_07):                                 	 	# Auslöser
                        save_log(zeit, name_IN_07)                              # Log eintragen
                if GPIO.input(IN_08):                                 		# Auslöser
                        save_log(zeit, name_IN_08)                              # Log eintragen

		time.sleep(0.5)							#Wartezeit bis die Schleifen ein weiters mal durchlaufen wird


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
