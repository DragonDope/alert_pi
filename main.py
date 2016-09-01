#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
import email_alarm
from ConfigParser import SafeConfigParser

def main():
	init()
	Loop()

def init():

	# Einstellungen abrufenund setzen
	#--------------------------------

        config = SafeConfigParser()
        config.read('alert.conf')

	email = config.getboolean('alert', 'email')			# Soll eine Alarm- E-Mail versendet werden?
	telefon = config.getboolean('alert', 'telefon')			# Soll ein Alarmanruf ausgeführt werden

	IN_01 = config.getint('hardware', 'pin_IN_01')
	IN_02 = config.getint('hardware', 'pin_IN_02')
	IN_03 = config.getint('hardware', 'pin_IN_03')
	IN_04 = config.getint('hardware', 'pin_IN_04')

	#Schlagwort Dictionary

	name_IN_01 = config.get('name', 'name_IN_01')
	name_IN_02 = config.get('name', 'name_IN_02')
	name_IN_03 = config.get('name', 'name_IN_03')
	name_IN_04 = config.get('name', 'name_IN_04')

	OUT_01 = config.getint('hardware', 'pin_OUT_01')
	OUT_02 = config.getint('hardware', 'pin_OUT_02')
	OUT_03 = config.getint('hardware', 'pin_OUT_03')


        # GPIO initialisieren
        #---------------------
        GPIO.setmode(GPIO.BOARD)       					# PIN Nummerierung per P1 RPi Board
        GPIO.setwarnings(False)         				# Warnung mehrfach Initialisierung deaktivieren

	GPIO.setup(IN_01, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)		# GPIO PIN einstellen
	GPIO.setup(IN_02, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)		# GPIO PIN einstellen
	GPIO.setup(IN_03, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)          # GPIO PIN einstellen
	GPIO.setup(IN_04, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)          # GPIO PIN einstellen
	GPIO.setup(OUT_01, GPIO.OUT)					# GPIO PIN einstellen
	GPIO.setup(OUT_02, GPIO.OUT)                                    # GPIO PIN einstellen
	GPIO.setup(OUT_03, GPIO.OUT)                                    # GPIO PIN einstellen


def Loop():

	while(true):
		# Zusänder der Eingänge abrufen
		#------------------------------
		zeit = time.strftime("%Y-%m-%d;%X")				# Aktuelle Systemzeit einlesen
		state_01 = GPIO.input(IN_01)					# GPIO Status einlesen
		state_02 = GPIO.input(IN_02)					# GPIO Status einlesen
		state_03 = GPIO.input(IN_03)					# GPIO Status einlesen
		state_04 = GPIO.input(IN_04)                                    # GPIO Status einlesen

		time.sleep(0.5)							#Wartezeit bis die Schleifen ein weiters mal durchlaufen wird


def Result():

	# Bildschirmausgabe
	#-------------------
	print(str(zeit)  + " ; " + name_IN_01 + " ; " + str(state_01) + " (Pull-DOWN)")		# Bildschirmausgabe
	print(str(zeit)  + " ; " + name_IN_02 + " ; " + str(state_02) + " (Pull-DOWN)")		# Bildschirmausgabe
	print(str(zeit)  + " ; " + name_IN_03 + " ; " + str(state_03) + " (Pull-DOWN)")            # Bildschirmausgabe
	print(str(zeit)  + " ; " + name_IN_04 + " ; " + str(state_04) + " (Pull-DOWN)")            # Bildschirmausgabe


	# Daten in Datei speichern
	#--------------------------
	file = open("alert.csv","a")							# Datei öffnen
	file.write(str(zeit) + " ; " + name_IN_01 + " ; " + str(state_01) + " (Pull-DOWN)\n")	# Daten in Datei speichern
	file.write(str(zeit) + " ; " + name_IN_02 + " ; " + str(state_02) + " (Pull-DOWN)\n")	# Daten in Datei speichern
	file.write(str(zeit) + " ; " + name_IN_03 + " ; " + str(state_03) + " (Pull-DOWN)\n")      # Daten in Datei speichern
	file.write(str(zeit) + " ; " + name_IN_04 + " ; " + str(state_04) + " (Pull-DOWN)\n")      # Daten in Datei speichern
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


def close():

	# Abschlussprozedur
	#------------------
	GPIO.cleanup()							# GPIO Einstellungen zurücksetzen


#Codeblock zum Testen bei direktem aufrufen der Datei
#----------------------------------------------------
if __name__ == "__main__":
	main()
