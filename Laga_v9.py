# ph wert problem "zwischen" noch loesen
# Saeureneutralisationskapazitaet bisher nicht mit drin in DepV, muss? nachlesen
# Cyanide richtig? (Cyanide gesamt = Cynanid?)
# Weitere Anmerkungen BBSchG hinzufuegen
# Grenzwere etc. fuer gefaehrlichen Abfall hinzufuegen
# OptionMenu hinzufuegen ->mg/L ug/L etc.

from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog, ttk
import os
import csv
import datetime
import fpdf

#Button.place(x=0,y=0)

#LAGA Einbauklassen, BBSchG und DepV Blanko-Listen (Feststoffe=TS | Eluat=El)/ Bodenart/ Datum
#LAGA
Z0_TS = []
Z0_Stern_TS = []
Z1_TS = []
Z2_TS = []
Higher_Z2_TS = []
Z0_EL = []
Z11_EL = []
Z12_EL = []
Z2_EL = []
Higher_Z2_EL = []
#BBSchG
BBSchG_Eingehalten = []
BBSchG_Ueberschritten = []
BBSchG_Vorsorgewerte_ueberschritten = []
BBSchG_Anmerkungen = []
#DepV (Rekultivierungsschicht -> REK / Geologische Barriere -> GEO)
DK0_TS = []
DK1_TS = []
DK2_TS = []
DK3_TS = []
Higher_DK3_TS = []
REK_TS_Eingehalten = []
GEO_TS_Eingehalten = []
REK_TS_Ueberschritten = []
GEO_TS_Ueberschritten = []
DK0_EL = []
DK1_EL = []
DK2_EL = []
DK3_EL = []
Higher_DK3_EL = []
REK_EL_Eingehalten = []
GEO_EL_Eingehalten = []
REK_EL_Ueberschritten = []
GEO_EL_Ueberschritten = []
REK_TS_Vorsorgewerte_ueberschritten = []
REK_EL_Vorsorgewerte_ueberschritten = []
GEO_TS_Vorsorgewerte_ueberschritten = []
GEO_EL_Vorsorgewerte_ueberschritten = []
#Bodenart/Datum
Bodenart = []
datelist = []

#Datum	
today = datetime.date.today()
datelist.append(today)

#Option Menue
Options_Feststoff = ["mg/kg TM", "ug/kg TM"]
Options_Eluat = ["mg/L", "ug/L"]


# Klasse Tkinter
class GUI:
	def __init__(self, master, name, wert_TS, wert_EL, 
		Limit_Z0_T_TS,
		Limit_Z0_SL_TS,
		Limit_Z0_Sa_TS, 
		Limit_Z0_Stern_TS,
		Limit_Z1_TS,
		Limit_Z2_TS, 
		Limit_Z0_EL, 
		Limit_Z11_EL, 
		Limit_Z12_EL, 
		Limit_Z2_EL,
		Limit_BBSchG_T,
		Limit_BBSchG_SL,
		Limit_BBSchG_Sa,
		Limit_BBSchG_HumusU8,
		Limit_BBSchG_HumusUE8,
		Limit_DK0_TS,
		Limit_DK1_TS,
		Limit_DK2_TS,
		Limit_DK3_TS,
		Limit_REK_TS,
		Limit_GEO_TS,
		Limit_DK0_EL,
		Limit_DK1_EL,
		Limit_DK2_EL,
		Limit_DK3_EL,
		Limit_REK_EL,
		Limit_GEO_EL):

		mainframe = Frame(master).grid(column=0,row=0, sticky=(N,W,E,S) )

		Label(master, text = "").grid(row=0, sticky=E)
		Label(master, text = "Projektname").grid(row=1, sticky=E)
		Label(master, text = "").grid(row=2, sticky=E)

		Label(master, text = "Bodenart").grid(row=3, sticky=E)
		Label(master, text = "Anteil Humus (TOC)").grid(row=4, sticky=E)
		Label(master, text = "").grid(row=5, sticky=E)

		Label(master, text = "Werte Feststoff", width = 17, fg='black').grid(row=6, column=1, padx=10)
		Label(master, text = "Werte Eluat", width = 17, fg='black').grid(row=6, column=3)
		
		Label(master, text = "Arsen (mg/kg TM)").grid(row=7, sticky=E)
		Label(master, text = "Blei (mg/kg TM)").grid(row=8, sticky=E)
		Label(master, text = "Cadmium (mg/kg TM)").grid(row=9, sticky=E)
		Label(master, text = "Chrom gesamt (mg/kg TM)").grid(row=10, sticky=E)
		Label(master, text = "Kupfer (mg/kg TM)").grid(row=11, sticky=E)
		Label(master, text = "Nickel (mg/kg TM)").grid(row=12, sticky=E)
		Label(master, text = "Quecksilber (mg/kg TM)").grid(row=13, sticky=E)
		Label(master, text = "Thallium (mg/kg TM)").grid(row=14, sticky=E)
		Label(master, text = "Zink (mg/kg TM)").grid(row=15, sticky=E)
		Label(master, text = "EOX (mg/kg TM)").grid(row=16, sticky=E)
		Label(master, text = "Kohlenwasserstoffe C10-C40 (mg/kg TM)").grid(row=17, sticky=E)		
		Label(master, text = "Kohlenwasserstoffe C10-C22 (mg/kg TM)").grid(row=18, sticky=E)
		Label(master, text = "Cyanid gesamt (mg/kg TM)").grid(row=19, sticky=E)
		Label(master, text = "BTX (BTEX) (mg/kg TM)").grid(row=20, sticky=E)
		Label(master, text = "LHKW (mg/kg TM)").grid(row=21, sticky=E)
		Label(master, text = "PAK 16 (PAK(EPA)) (mg/kg TM)").grid(row=22, sticky=E)
		Label(master, text = "Benzo(a)pyren (mg/kg TM)").grid(row=23, sticky=E)
		Label(master, text = "PCB 6 (mg/kg TM)").grid(row=24, sticky=E)
		Label(master, text = "PCB 7 (mg/kg TM)").grid(row=25, sticky=E)		
		Label(master, text = "TOC (Masse-%)").grid(row=26, sticky=E)
		Label(master, text = "Gluehverlust (Masse-%)").grid(row=27, sticky=E)
		Label(master, text = "Saeureneutralisationskapazitaet (mmol/kg)").grid(row=28, sticky=E)	
		Label(master, text = "Extr. lipohile Stoffe (Masse-%)").grid(row=29, sticky=E)
		Label(master, text = "Dioxine / Furane (ng/kg TM)").grid(row=30, sticky=E)	

		Label(master, text = "Arsen (ug/L)").grid(row=7, column=2, sticky=E)
		Label(master, text = "Blei (ug/L)").grid(row=8, column=2, sticky=E)
		Label(master, text = "Cadmium (ug/L)").grid(row=9, column=2, sticky=E)
		Label(master, text = "Chrom gesamt (ug/L)").grid(row=10, column=2, sticky=E)		
		Label(master, text = "Kupfer (ug/L)").grid(row=11, column=2, sticky=E)
		Label(master, text = "Nickel (ug/L)").grid(row=12, column=2, sticky=E)
		Label(master, text = "Quecksilber (ug/L)").grid(row=13, column=2, sticky=E)
		Label(master, text = "Zink (ug/L)").grid(row=14, column=2, sticky=E)
		Label(master, text = "Cyanid (ug/L)").grid(row=15, column=2, sticky=E)	
		Label(master, text = "Cyanid, leicht freisetzbar (ug/L)").grid(row=16, column=2, sticky=E)
		Label(master, text = "Phenolindex (ug/L)").grid(row=17, column=2, sticky=E)
		Label(master, text = "Chlorid (mg/L)").grid(row=18, column=2, sticky=E)	
		Label(master, text = "Sulfat (mg/L)").grid(row=19, column=2, sticky=E)
		Label(master, text = "pH-Wert").grid(row=20, column=2, sticky=E)
		Label(master, text = "Leitfaehigkeit (uS/cm)").grid(row=21, column=2, sticky=E)
		Label(master, text = "DOC (mg/L)").grid(row=22, column=2, sticky=E)
		Label(master, text = "Fluorid (mg/L)").grid(row=23, column=2, sticky=E)
		Label(master, text = "Barium (mg/L)").grid(row=24, column=2, sticky=E)
		Label(master, text = "Molybdaen (ug/L)").grid(row=25, column=2, sticky=E)
		Label(master, text = "Antimon (ug/L)").grid(row=26, column=2, sticky=E)
		Label(master, text = "Selen (ug/L)").grid(row=27, column=2, sticky=E)
		Label(master, text = " Gesamtgehalt an gel. Stoffen (mg/L)").grid(row=28, column=2, sticky=E)

		Label(master, text = "   Hinweise zur Dateneingabe:").grid(row=33, column=0, sticky=W+E)
		Label(master, text = "   1. Bei Wert unter Bestimmungs- ").grid(row=34, column=0, sticky=W+E)
		Label(master, text = '      "grenze < benutzen (z.B. <0.5)').grid(row=35, column=0, sticky=W+E)
		Label(master, text = "   2. Dezimalstellen mit Punkt (.) angeben").grid(row=36, column=0, sticky=W+E)

		global resultLabel
		resultLabel = Label(root, text = "")
		resultLabel.grid(row=32, column=2)

		global entry0
		global entry1
		global entry2
		global entry3
		global entry4
		global entry5
		global entry6
		global entry7
		global entry8
		global entry9
		global entry10
		global entry11
		global entry12
		global entry13
		global entry14
		global entry15
		global entry16
		global entry17
		global entry18
		global entry19
		global entry20
		global entry21
		global entry22
		global entry23
		global entry24
		global entry25
		global entry26
		global entry27
		global entry28
		global entry29
		global entry30
		global entry31
		global entry32
		global entry33
		global entry34
		global entry35
		global entry36
		global entry37
		global entry38
		global entry39
		global entry40
		global entry41
		global entry42
		global entry43
		global entry44
		global entry45
		global entry46

		entry0 = Entry(master) # Projektname
		# Feststoff 24x
		entry1 = Entry(master) # Stoff1
		entry2 = Entry(master) # Stoff2
		entry3 = Entry(master) # Stoff3
		entry4 = Entry(master) # Stoff4
		entry5 = Entry(master) # Stoff5
		entry6 = Entry(master) # Stoff6
		entry7 = Entry(master) # Stoff7
		entry8 = Entry(master) # Stoff8
		entry9 = Entry(master) # Stoff9
		entry10 = Entry(master) # Stoff10
		entry11 = Entry(master) # Stoff11
		entry12 = Entry(master) # Stoff12
		entry13 = Entry(master) # Stoff13
		entry14 = Entry(master) # Stoff14
		entry15 = Entry(master) # Stoff15
		entry16 = Entry(master) # Stoff16
		entry17 = Entry(master) # Stoff17
		entry18 = Entry(master) # Stoff18
		entry19 = Entry(master) # Stoff19
		entry20 = Entry(master) # Stoff20
		entry21 = Entry(master) # Stoff21
		entry22 = Entry(master) # Stoff22
		entry23 = Entry(master) # Stoff23
		entry24 = Entry(master) # Stoff24

		# Eluat 22x
		entry25 = Entry(master) # Stoff25
		entry26 = Entry(master) # Stoff26
		entry27 = Entry(master) # Stoff27
		entry28 = Entry(master) # Stoff28
		entry29 = Entry(master) # Stoff29
		entry30 = Entry(master) # Stoff30
		entry31 = Entry(master) # Stoff31
		entry32 = Entry(master) # Stoff32
		entry33 = Entry(master) # Stoff33
		entry34 = Entry(master) # Stoff34
		entry35 = Entry(master) # Stoff35
		entry36 = Entry(master) # Stoff36
		entry37 = Entry(master) # Stoff37
		entry38 = Entry(master) # Stoff38
		entry39 = Entry(master) # Stoff39
		entry40 = Entry(master) # Stoff40
		entry41 = Entry(master) # Stoff41
		entry42 = Entry(master) # Stoff42
		entry43 = Entry(master) # Stoff43
		entry44 = Entry(master) # Stoff44
		entry45 = Entry(master) # Stoff45
		entry46 = Entry(master) # Stoff46

		entry0.grid(row=1, column=1, sticky=N)
		# Feststoff 24x
		entry1.grid(row=7, column=1)
		entry2.grid(row=8, column=1)
		entry3.grid(row=9, column=1)
		entry4.grid(row=10, column=1)
		entry5.grid(row=11, column=1)
		entry6.grid(row=12, column=1)
		entry7.grid(row=13, column=1)
		entry8.grid(row=14, column=1)
		entry9.grid(row=15, column=1)
		entry10.grid(row=16, column=1)
		entry11.grid(row=17, column=1)
		entry12.grid(row=18, column=1)
		entry13.grid(row=19, column=1)
		entry14.grid(row=20, column=1)
		entry15.grid(row=21, column=1)
		entry16.grid(row=22, column=1)
		entry17.grid(row=23, column=1)
		entry18.grid(row=24, column=1)
		entry19.grid(row=25, column=1)
		entry20.grid(row=26, column=1)
		entry21.grid(row=27, column=1)
		entry22.grid(row=28, column=1)
		entry23.grid(row=29, column=1)
		entry24.grid(row=30, column=1)
		
		entry25.grid(row=7, column=3)
		entry26.grid(row=8, column=3)
		entry27.grid(row=9, column=3)
		entry28.grid(row=10, column=3)
		entry29.grid(row=11, column=3)
		entry30.grid(row=12, column=3)
		entry31.grid(row=13, column=3)
		entry32.grid(row=14, column=3)
		entry33.grid(row=15, column=3)
		entry34.grid(row=16, column=3)
		entry35.grid(row=17, column=3)
		entry36.grid(row=18, column=3)
		entry37.grid(row=19, column=3)
		entry38.grid(row=20, column=3)
		entry39.grid(row=21, column=3)
		entry40.grid(row=22, column=3)
		entry41.grid(row=23, column=3)
		entry42.grid(row=24, column=3)
		entry43.grid(row=25, column=3)
		entry44.grid(row=26, column=3)
		entry45.grid(row=27, column=3)
		entry46.grid(row=28, column=3)

		Button(master, text="Bewertung", fg="black", bg="white", padx = 2, pady = 2, command=self.Stoff).grid(row=32, column=3, sticky=W+E)
		Button(master, text="Beenden", command=root.destroy, bg="white", padx = 2, pady = 2).grid(row=34, column=3, sticky=W+E)
		Radiobutton(master, text="Ton", variable=var1, command=self.Bodenart, value=1).grid(row=3, column=2, sticky=W)
		Radiobutton(master, text="Schluff/L.", variable=var1, command=self.Bodenart, value=2).grid(row=3, column=1, sticky=E)
		Radiobutton(master, text="Sand", variable=var1, command=self.Bodenart, value=3).grid(row=3, column=1, sticky=W)
		radiobutton_Humus1 = Radiobutton(master, text=">8% (>4%)", variable=var2, command=self.Humus, value=1).grid(row=4, column=1, sticky=W)
		Radiobutton(master, text="<=8% (<=4%)", variable=var2, command=self.Humus, value=2).grid(row=4, column=2, sticky=W)

		# https://pythonguides.com/python-tkinter-optionmenu/
		# setting variable for Integers
		clicked = StringVar()
		clicked.set(Options_Feststoff[0])
		# creating widget
		OptionArsen_TS = OptionMenu(master, clicked, *Options_Feststoff, command = self.Concentrations).grid(row=7, column=2, sticky=W)







		# Instance Variables
		self.name = name
		self.wert_TS = wert_TS
		self.wert_EL = wert_EL
		self.Limit_Z0_Sa_TS = Limit_Z0_Sa_TS
		self.Limit_Z1_TS = Limit_Z1_TS
		self.Limit_Z2_TS = Limit_Z2_TS
		self.Limit_Z0_SL_TS = Limit_Z0_SL_TS
		self.Limit_Z0_Stern_TS = Limit_Z0_Stern_TS
		self.Limit_Z0_T_TS = Limit_Z0_T_TS
		self.Limit_Z0_EL = Limit_Z0_EL
		self.Limit_Z11_EL = Limit_Z11_EL
		self.Limit_Z12_EL = Limit_Z12_EL
		self.Limit_Z2_EL = Limit_Z2_EL
		self.Limit_BBSchG_T = Limit_BBSchG_T
		self.Limit_BBSchG_SL = Limit_BBSchG_SL
		self.Limit_BBSchG_Sa = Limit_BBSchG_Sa
		self.Limit_BBSchG_HumusU8 = Limit_BBSchG_HumusU8
		self.Limit_BBSchG_HumusUE8 = Limit_BBSchG_HumusUE8
		self.Limit_DK0_TS = Limit_DK0_TS
		self.Limit_DK1_TS = Limit_DK1_TS
		self.Limit_DK2_TS = Limit_DK2_TS
		self.Limit_DK3_TS = Limit_DK3_TS
		self.Limit_REK_TS = Limit_REK_TS
		self.Limit_GEO_TS = Limit_GEO_TS
		self.Limit_DK0_EL = Limit_DK0_EL
		self.Limit_DK1_EL = Limit_DK1_EL
		self.Limit_DK2_EL = Limit_DK2_EL
		self.Limit_DK3_EL = Limit_DK3_EL
		self.Limit_REK_EL = Limit_REK_EL
		self.Limit_GEO_EL = Limit_GEO_EL

	def Bodenart(self):
		global Bodenart_auswahl # Die globale Variable kann ausserhalb der Funktion genutzt werden
		Bodenart_auswahl = var1.get()
		if Bodenart_auswahl == 1:
			Bodenart_auswahl = "Bodenart: Ton"
			print (Bodenart_auswahl)
		elif Bodenart_auswahl == 2:
			Bodenart_auswahl = "Bodenart: Schluff"
			print (Bodenart_auswahl)
		elif Bodenart_auswahl == 3:
			Bodenart_auswahl = "Bodenart: Sand"
			print (Bodenart_auswahl)

	def Humus(self):
		global Humus
		Humus = var2.get()
		if Humus == 1:
			Humus = "Anteil Humus (TOC): >8% (>4%)"
			print(Humus)
		elif Humus == 2:
			Humus = "Anteil Humus (TOC): <=8% (<=4%)"
			print(Humus)

	def Concentrations(self):
		Concentrations = variable.get()
		print(Concentrations)

	def Stoff(self):
		Liste_Stoffe = [EOX, KW_C10_C40, KW_mobiler_Anteil_C10_C22, Cyanid_gesamt, BTX_BTEX, LHKW,
		PAK_16, Benzopyren, PCB6, PCB7, Arsen, Blei, Cadmium, Chrom_gesamt, Kupfer, Nickel, Quecksilber, Thallium,
		Zink, TOC, Gluehverlust, Lipohile_Stoffe, pH_Wert, Leitfaehigkeit, Cyanid, Cyanid_lf, Phenolindex,
		Chlorid, Sulfat, DOC, Fluorid, Barium, Molybdaen, Antimon, Selen, Gesamtgehalt_geloeste_Feststoffe, Dioxine,
		Saeureneutralisationskapazitaet] # Liste mit allen Stoffen, benutzt fuer die unten stehenden Pruefungen (richtgie Dateneingabe etc.)

		Liste_Stoffe_LAGA = [Arsen, Blei, Cadmium, Chrom_gesamt, Kupfer, Nickel, Quecksilber,
		Zink, EOX, KW_C10_C40, KW_mobiler_Anteil_C10_C22, Cyanid_gesamt, BTX_BTEX, LHKW,
		PAK_16, Benzopyren, PCB6, Thallium, TOC, Leitfaehigkeit, pH_Wert, Cyanid, Phenolindex,
		Chlorid, Sulfat] # Liste benutzt fuer LAGA-Pruefung

		Liste_Stoffe_BBSchG_Schwermetalle = [Blei, Cadmium, Chrom_gesamt, Kupfer, Nickel, Quecksilber, Zink] #Extra Liste fuer Pruefung BBSchG abhaengig von der Bodenart
		Liste_Stoffe_BBSchG_Kohlenwasserstoffe = [PAK_16, Benzopyren, PCB6] # Extra Liste fuer Pruefung BBSchG abhaengig vom Humusgehalt

		Liste_Stoffe_DepV = [KW_C10_C40, BTX_BTEX, PAK_16, PCB7, TOC, Gluehverlust,
		Lipohile_Stoffe, pH_Wert, Leitfaehigkeit, Cyanid_lf, Phenolindex, Arsen,
		Blei, Cadmium, Chrom_gesamt, Kupfer, Nickel, Quecksilber, Zink, Chlorid, Sulfat,
		DOC, Fluorid, Barium, Molybdaen, Antimon, Selen, Gesamtgehalt_geloeste_Feststoffe] # Liste benutzt fuer DepV-Pruefung

		# Feststoff
		Arsen.wert_TS = entry1.get()
		Blei.wert_TS = entry2.get()
		Cadmium.wert_TS = entry3.get()
		Chrom_gesamt.wert_TS = entry4.get()
		Kupfer.wert_TS = entry5.get()
		Nickel.wert_TS = entry6.get()
		Quecksilber.wert_TS = entry7.get()
		Thallium.wert_TS = entry8.get()
		Zink.wert_TS = entry9.get()
		EOX.wert_TS = entry10.get()
		KW_C10_C40.wert_TS = entry11.get()
		KW_mobiler_Anteil_C10_C22.wert_TS = entry12.get()
		Cyanid_gesamt.wert_TS = entry13.get()
		BTX_BTEX.wert_TS = entry14.get()
		LHKW.wert_TS = entry15.get()
		PAK_16.wert_TS = entry16.get()
		Benzopyren.wert_TS = entry17.get()
		PCB6.wert_TS = entry18.get()
		PCB7.wert_TS = entry19.get()
		TOC.wert_TS = entry20.get()
		Gluehverlust.wert_TS = entry21.get()
		Saeureneutralisationskapazitaet.wert_TS = entry22.get()
		Lipohile_Stoffe.wert_TS = entry23.get()
		Dioxine.wert_TS = entry24.get()

		# Eluat
		Arsen.wert_EL = entry25.get()
		Blei.wert_EL = entry26.get()
		Cadmium.wert_EL = entry27.get()
		Chrom_gesamt.wert_EL = entry28.get()
		Kupfer.wert_EL = entry29.get()
		Nickel.wert_EL = entry30.get()
		Quecksilber.wert_EL = entry31.get()
		Zink.wert_EL = entry32.get()
		Cyanid.wert_EL = entry33.get()
		Cyanid_lf.wert_EL = entry34.get()
		Phenolindex.wert_EL = entry35.get()
		Chlorid.wert_EL = entry36.get()
		Sulfat.wert_EL = entry37.get()
		pH_Wert.wert_EL = entry38.get()
		Leitfaehigkeit.wert_EL = entry39.get()
		DOC.wert_EL = entry40.get()
		Fluorid.wert_EL = entry41.get()
		Barium.wert_EL = entry42.get()
		Molybdaen.wert_EL = entry43.get()
		Antimon.wert_EL = entry44.get()
		Selen.wert_EL = entry45.get()
		Gesamtgehalt_geloeste_Feststoffe.wert_EL = entry46.get()

		# Ueberpruefen, ob eine Zahl eingegeben wurde. Bei keiner Angabe x Wert annehmen.
		for i in Liste_Stoffe:
			if i.wert_TS == "":
				i.wert_TS = 10000000
			else:
				pass
			if i.wert_EL == "":
				i.wert_EL = 10000000
			else:
				pass

		if pH_Wert.wert_EL == "":
			pH_Wert.wert_EL = 10000000
		else:
			pass

		# Kontrolle ob positive Zahl (float) eingegeben wurde, dann weiter, sonst Ausnahme (except)
		try:
			for i in Liste_Stoffe:
				# Wenn < vor der Zahl eingegeben wird, wird die Zahl als float angenommen
				if i.wert_TS == str(i.wert_TS) and i.wert_TS[0:1] == "<":
						i.wert_TS = float(i.wert_TS[1:])
				elif i.wert_TS == str(i.wert_TS):
					i.wert_TS = float(i.wert_TS)
				elif i.wert_TS == float(i.wert_TS):
					pass
				if i.wert_EL == str(i.wert_EL) and i.wert_EL[0:1] == "<":
						i.wert_EL = float(i.wert_EL[1:])
				elif i.wert_EL == float(i.wert_EL):
					pass
				#elif i.wert_TS == str(i.wert_TS): (scheint nicht notwendig zu sein dieses "extra" Statement)
					#raise ValueError

				# Ueberpruefen ob eine Zahl als float eingegeben wurde und nicht negativ ist, sonst "except"
				i.wert_TS = float(i.wert_TS)
				i.wert_EL = float(i.wert_EL)
				if i.wert_TS < 0:
					raise ValueError
				if i.wert_EL < 0:
					raise ValueError

			resultLabel.config(text="Eingabe erfolgreich", bg = "green")

			# LAGA Feststoff Einordnung
			for i in Liste_Stoffe_LAGA:

				if i.name in Z0_TS: # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
					Z0_TS.remove(i.name)
				else:
					pass
				if i.name in Z0_Stern_TS:
					Z0_Stern_TS.remove(i.name)
				else:
					pass
				if i.name in Z1_TS:
					Z1_TS.remove(i.name)
				else:
					pass
				if i.name in Z2_TS:
					Z2_TS.remove(i.name)
				else:
					pass
				if i.name in Higher_Z2_TS:
					Higher_Z2_TS.remove(i.name)
				else:
					pass

				if Bodenart_auswahl == "Bodenart: Sand":
					if i.wert_TS < i.Limit_Z0_Sa_TS:
						Z0_TS.extend({i.name})
					else:
						if i.wert_TS < i.Limit_Z0_Stern_TS:
							Z0_Stern_TS.extend({i.name})
						else:
							if i.wert_TS < i.Limit_Z1_TS:
								Z1_TS.extend({i.name})
							else:
								if i.wert_TS < i.Limit_Z2_TS:
									Z2_TS.extend({i.name})
								else: 
									if i.wert_TS > i.Limit_Z2_TS and i.wert_TS < 10000000:
										Higher_Z2_TS.extend({i.name})
				elif Bodenart_auswahl == "Bodenart: Schluff":
					if i.wert_TS < i.Limit_Z0_SL_TS:
						Z0_TS.extend({i.name})
					else:
						if i.wert_TS < i.Limit_Z0_Stern_TS:
							Z0_Stern_TS.extend({i.name})
						else:
							if i.wert_TS < i.Limit_Z1_TS:
								Z1_TS.extend({i.name})
							else:
								if i.wert_TS < i.Limit_Z2_TS:
									Z2_TS.extend({i.name})
								else: 
									if i.wert_TS > i.Limit_Z2_TS and i.wert_TS < 10000000:
										Higher_Z2_TS.extend({i.name})
				elif Bodenart_auswahl == "Bodenart: Ton":
					if i.wert_TS < i.Limit_Z0_T_TS:
						Z0_TS.extend({i.name})
					else:
						if i.wert_TS < i.Limit_Z0_Stern_TS:
							Z0_Stern_TS.extend({i.name})
						else:
							if i.wert_TS < i.Limit_Z1_TS:
								Z1_TS.extend({i.name})
							else:
								if i.wert_TS < i.Limit_Z2_TS:
									Z2_TS.extend({i.name})
								else: 
									if i.wert_TS > i.Limit_Z2_TS and i.wert_TS < 10000000:
										Higher_Z2_TS.extend({i.name})

			# LAGA Eluat Einordnung
			for i in Liste_Stoffe_LAGA:

				if i.name in Z0_EL: # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
					Z0_EL.remove(i.name)
				else:
					pass
				if i.name in Z11_EL:
					Z11_EL.remove(i.name)
				else:
					pass	
				if i.name in Z12_EL:
					Z12_EL.remove(i.name)
				else:
					pass
				if i.name in Z2_EL:
					Z2_EL.remove(i.name)
				else:
					pass
				if i.name in Higher_Z2_EL:
					Higher_Z2_EL.remove(i.name)
				else:
					pass					

				if i.wert_EL < i.Limit_Z0_EL:
					Z0_EL.extend({i.name})
				else:
					if i.wert_EL < i.Limit_Z11_EL:
						Z11_EL.extend({i.name})
					else:
						if i.wert_EL < i.Limit_Z12_EL:
							Z12_EL.extend({i.name})
						else:
							if i.wert_EL < i.Limit_Z2_EL:
								Z2_EL.extend({i.name})
							else:
								if i.wert_EL > i.Limit_Z2_EL and i.wert_EL < 10000000:
									Higher_Z2_EL.extend({i.name})

			# LAGA pH Wert Einordnung
			if pH_Wert.name in Z2_EL: # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
				Z2_EL.remove(i.name)
			else:
				pass
			if pH_Wert.name in Z12_EL: # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
				Z12_EL.remove(i.name)
			else:
				pass

			if pH_Wert.wert_EL == 10000000:
				print ("pH nicht eingegeben")
				#pass
			elif pH_Wert.wert_EL >= 6.5 and pH_Wert.wert_EL <= 9.5:
				print ("pH groesser gleich 6.5 und kleiner gleich 9.5")
				pass
			elif 5.5 <= pH_Wert.wert_EL < 6.0:
				print ("pH groesser gleich 5.5 und kleiner 6.0")
				Z2_EL.extend({pH_Wert.name})
			elif 6.0 <= pH_Wert.wert_EL < 6.5:
				print ("pH groesser gleich 6.0 und kleiner 6.5")
				Z12_EL.extend({pH_Wert.name})
			elif 9.5 < pH_Wert.wert_EL <= 12.0:
				print ("pH groesser 9.5 und kleiner gleich 12.0")
				Z12_EL.extend({pH_Wert.name})
			elif 5.5 > pH_Wert.wert_EL or pH_Wert.wert_EL > 12.0: 
				print ("pH kleiner 5.5 oder groesser 12.0") 
			else:
				pass

			# BBSchG Einordnung Kohlenwasserstoffe (abhaengig vom Humusgehalt)
			for i in Liste_Stoffe_BBSchG_Kohlenwasserstoffe:
				
				if i.name in BBSchG_Ueberschritten: # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
					BBSchG_Ueberschritten.remove(i.name)
				else:
					pass

				if Humus == "Anteil Humus (TOC): >8% (>4%)":
					if i.wert_TS > i.Limit_BBSchG_HumusUE8 and i.wert_TS != 10000000:
						BBSchG_Ueberschritten.extend({i.name})
					else:
						pass
				elif Humus == "Anteil Humus (TOC): <=8% (<=4%)":
					if i.wert_TS > i.Limit_BBSchG_HumusU8 and i.wert_TS != 10000000:
						BBSchG_Ueberschritten.extend({i.name})
					else:
						pass
				else:
					pass

			# BBSchG Einordnung Schwermetalle (abhaengig von Bodenart)
			for i in Liste_Stoffe_BBSchG_Schwermetalle:

				if i.name in BBSchG_Ueberschritten: # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
					BBSchG_Ueberschritten.remove(i.name)
				else:
					pass

				if Bodenart_auswahl == "Bodenart: Sand":
					if i.wert_TS > i.Limit_BBSchG_Sa and i.wert_TS != 10000000:
						BBSchG_Ueberschritten.extend({i.name})
					else:
						pass
				elif Bodenart_auswahl == "Bodenart: Schluff":
					if i.wert_TS > i.Limit_BBSchG_SL and i.wert_TS != 10000000:
						BBSchG_Ueberschritten.extend({i.name})
					else:
						pass
				elif Bodenart_auswahl == "Bodenart: Ton":
					if i.wert_TS > i.Limit_BBSchG_T and i.wert_TS != 10000000:
						BBSchG_Ueberschritten.extend({i.name})
					else:
						pass
				else:
					pass

			# BBSchG -> Falls Humus >8% Info, dass Schwermetalle nicht beruecksichtigt werden
			if "Schwermetalle werden aufgrund Humusgehalt >8% nicht beruecksichtigt" in BBSchG_Anmerkungen: # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
				BBSchG_Anmerkungen.remove("Schwermetalle werden aufgrund Humusgehalt >8% nicht beruecksichtigt")
			else:
				pass

			if Humus == "Anteil Humus (TOC): >8% (>4%)":
				BBSchG_Anmerkungen.extend(["Schwermetalle werden aufgrund Humusgehalt >8% nicht beruecksichtigt"])
			else:
				pass

			# DepV Einordnung (DK, REK, GEO)
			for i in Liste_Stoffe_DepV:

				if i.name in DK0_TS: # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
					DK0_TS.remove(i.name)
				else:
					pass
				if i.name in DK1_TS:
					DK1_TS.remove(i.name)
				else:
					pass	
				if i.name in DK2_TS:
					DK2_TS.remove(i.name)
				else:
					pass
				if i.name in DK3_TS:
					DK3_TS.remove(i.name)
				else:
					pass
				if i.name in Higher_DK3_TS:
					Higher_DK3_TS.remove(i.name)
				else:
					pass	
				if i.name in GEO_TS_Eingehalten:
					GEO_TS_Eingehalten.remove(i.name)
				else:
					pass
				if i.name in GEO_TS_Ueberschritten:
					GEO_TS_Ueberschritten.remove(i.name)
				else:
					pass
				if i.name in REK_TS_Eingehalten:
					REK_TS_Eingehalten.remove(i.name)
				else:
					pass
				if i.name in REK_TS_Ueberschritten:
					REK_TS_Ueberschritten.remove(i.name)
				else:
					pass
				if i.name in DK0_EL:
					DK0_EL.remove(i.name)
				else:
					pass
				if i.name in DK1_EL:
					DK1_EL.remove(i.name)
				else:
					pass
				if i.name in DK2_EL:
					DK2_EL.remove(i.name)
				else:
					pass
				if i.name in DK3_EL:
					DK3_EL.remove(i.name)
				else:
					pass
				if i.name in Higher_DK3_EL:
					Higher_DK3_EL.remove(i.name)
				else:
					pass
				if i.name in GEO_EL_Eingehalten:
					GEO_EL_Eingehalten.remove(i.name)
				else:
					pass
				if i.name in GEO_EL_Ueberschritten:
					GEO_EL_Ueberschritten.remove(i.name)
				else:
					pass
				if i.name in REK_EL_Eingehalten:
					REK_EL_Eingehalten.remove(i.name)
				else:
					pass
				if i.name in REK_EL_Ueberschritten:
					REK_EL_Ueberschritten.remove(i.name)
				else:
					pass							

				# DK Feststoff
				if i.wert_TS <= i.Limit_DK0_TS:
					DK0_TS.extend({i.name})
				elif i.wert_TS <= i.Limit_DK1_TS:
					DK1_TS.extend({i.name})
				elif i.wert_TS <= i.Limit_DK2_TS:
					DK2_TS.extend({i.name})
				elif i.wert_TS <= i.Limit_DK3_TS:
					DK3_TS.extend({i.name})
				elif i.wert_TS > i.Limit_DK3_TS and i.wert_TS < 10000000:
					Higher_DK3_TS.extend({i.name})
				else:
					pass

				#GEO Feststoff
				if i.wert_TS <= i.Limit_GEO_TS:
					GEO_TS_Eingehalten.extend({i.name})
				elif i.wert_TS > i.Limit_GEO_TS and i.wert_TS < 10000000:
					GEO_TS_Ueberschritten.extend({i.name})
				else:
					pass
					
				#REK Feststoff
				if i.wert_TS <= i.Limit_REK_TS:
					REK_TS_Eingehalten.extend({i.name})
				elif i.wert_TS > i.Limit_REK_TS and i.wert_TS < 10000000:
					REK_TS_Ueberschritten.extend({i.name})
				else:
					pass

				# DK Eluat
				if i.wert_EL <= i.Limit_DK0_EL:
					DK0_EL.extend({i.name})
				elif i.wert_EL <= i.Limit_DK1_EL:
					DK1_EL.extend({i.name})
				elif i.wert_EL <= i.Limit_DK2_EL:
					DK2_EL.extend({i.name})
				elif i.wert_EL <= i.Limit_DK3_EL:
					DK3_EL.extend({i.name})
				elif i.wert_EL > i.Limit_DK3_EL and i.wert_EL < 10000000:
					Higher_DK3_EL.extend({i.name})
				else:
					pass

				#GEO Eluat
				if i.wert_EL <= i.Limit_GEO_EL:
					GEO_EL_Eingehalten.extend({i.name})
				elif i.wert_EL > i.Limit_GEO_EL and i.wert_EL < 10000000:
					GEO_EL_Ueberschritten.extend({i.name})
				else:
					pass
					
				#REK Eluat
				if i.wert_EL <= i.Limit_REK_EL:
					REK_EL_Eingehalten.extend({i.name})
				elif i.wert_EL > i.Limit_REK_EL and i.wert_EL < 10000000:
					REK_EL_Ueberschritten.extend({i.name})
				else:
					pass

			# Data Output
			strZ0_TS = ', '.join(Z0_TS) # Liste in string konvertieren
			strZ0_Stern_TS = ', '.join(Z0_Stern_TS)
			strZ1_TS = ', '.join(Z1_TS)
			strZ2_TS = ', '.join(Z2_TS)
			strHigher_Z2_TS = ', '.join(Higher_Z2_TS)
			strZ0_EL = ', '.join(Z0_EL)
			strZ11_EL = ', '.join(Z11_EL)
			strZ12_EL = ', '.join(Z12_EL)
			strZ2_EL = ', '.join(Z2_EL)
			strHigher_Z2_EL = ', '.join(Higher_Z2_EL)
			strBBSchG_Eingehalten = ', '.join(BBSchG_Eingehalten)
			strBBSchG_Ueberschritten = ', '.join(BBSchG_Ueberschritten)
			strDK0_TS = ', '.join(DK0_TS)
			strDK1_TS = ', '.join(DK1_TS)
			strDK2_TS = ', '.join(DK2_TS)
			strDK3_TS = ', '.join(DK3_TS)
			strHigher_DK3_TS = ', '.join(Higher_DK3_TS)
			strREK_TS_Ueberschritten = ', '.join(REK_TS_Ueberschritten)
			strGEO_TS_Ueberschritten = ', '.join(GEO_TS_Ueberschritten)
			strDK0_EL = ', '.join(DK0_EL)
			strDK1_EL = ', '.join(DK1_EL)
			strDK2_EL = ', '.join(DK2_EL)
			strDK3_EL = ', '.join(DK3_EL)
			strHigher_DK3_EL = ', '.join(Higher_DK3_EL)
			strREK_EL_Ueberschritten = ', '.join(REK_EL_Ueberschritten)
			strGEO_EL_Ueberschritten = ', '.join(GEO_EL_Ueberschritten)
			strBBSchG_Anmerkungen =', '.join(BBSchG_Anmerkungen)

			# BBSchG -> Falls in Liste mehr als 0 items, dann Notiz: Vorsorgewerte ueberschritten
			del BBSchG_Vorsorgewerte_ueberschritten[:] # Deletes contenct of the list
			if len(strBBSchG_Ueberschritten) > 0:
				BBSchG_Vorsorgewerte_ueberschritten.extend(["Ja"])
			elif len(strBBSchG_Ueberschritten) == 0:
				BBSchG_Vorsorgewerte_ueberschritten.extend(["Nein"])
			else:
				pass
			strBBSchG_Vorsorgewerte_ueberschritten = ', '.join(BBSchG_Vorsorgewerte_ueberschritten)

			# Create PDF
			pdf = fpdf.FPDF(format='letter')
			pdf.add_page()
			
			pdf.set_fill_color(180)

			pdf.set_font('Arial', 'B', size = 14)
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = 'Bundes-Bodenschutzgesetz', ln = 1, fill=True)
			pdf.set_font('Arial', size = 11)
			pdf.cell(w = 55, h = 8, border  = 1, align = "L", txt = 'Vorsorgewerte ueberschritten:')
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = strBBSchG_Vorsorgewerte_ueberschritten, ln = 1)
			pdf.cell(w = 55, h = 8, border  = 1, align = "L", txt = 'Ueberschreitung fuer:')
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = strBBSchG_Ueberschritten, ln = 1)
			pdf.cell(w = 55, h = 8, border  = 1, align = "L", txt = 'Anmerkungen:')
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = strBBSchG_Anmerkungen, ln = 1)
			pdf.cell(w = 0, h = 8, border  = 0, align = "L", ln = 1)

			pdf.set_font('Arial', 'B', size = 14)
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = 'LAGA', ln = 1, fill=True)
			pdf.set_font('Arial', size = 11)
			pdf.cell(w = 19, h = 8, border  = 1, align = "L", txt = 'Feststoff')
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = '>Z2: ' + strHigher_Z2_TS, ln = 1)
			pdf.cell(w = 19, h = 8, border  = 1, align = "L")
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = 'Z2: ' + strZ2_TS, ln = 1)
			pdf.cell(w = 19, h = 8, border  = 1, align = "L")
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = 'Z1: ' + strZ1_TS, ln = 1)
			pdf.cell(w = 19, h = 8, border  = 1, align = "L", txt = 'Eluat')
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = '>Z2: ' + strHigher_Z2_EL, ln = 1)
			pdf.cell(w = 19, h = 8, border  = 1, align = "L")
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = 'Z2: ' + strZ2_EL, ln = 1)
			pdf.cell(w = 19, h = 8, border  = 1, align = "L")
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = 'Z1.2: ' + strZ12_EL, ln = 1)
			pdf.cell(w = 19, h = 8, border  = 1, align = "L")
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = 'Z1.1: ' + strZ11_EL, ln = 1)
			pdf.cell(w = 0, h = 8, border  = 0, align = "L", ln = 1)

			pdf.set_font('Arial', 'B', size = 14)
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = 'Deponieverordnung', ln = 1, fill=True)
			pdf.set_font('Arial', size = 11)
			pdf.cell(w = 19, h = 8, border  = 1, align = "L", txt = 'Feststoff')
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = '>DK3: ' + strHigher_DK3_TS, ln = 1)
			pdf.cell(w = 19, h = 8, border  = 1, align = "L")
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = 'DK3: ' + strDK3_TS, ln = 1)
			pdf.cell(w = 19, h = 8, border  = 1, align = "L")
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = 'DK2: ' + strDK2_TS, ln = 1)
			pdf.cell(w = 19, h = 8, border  = 1, align = "L")
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = 'DK1: ' + strDK1_TS, ln = 1)
			pdf.cell(w = 19, h = 8, border  = 1, align = "L", txt = 'Eluat')
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = '>DK3: ' + strHigher_DK3_EL, ln = 1)
			pdf.cell(w = 19, h = 8, border  = 1, align = "L")
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = 'DK3: ' + strDK3_EL, ln = 1)
			pdf.cell(w = 19, h = 8, border  = 1, align = "L")
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = 'DK2: ' + strDK2_EL, ln = 1)
			pdf.cell(w = 19, h = 8, border  = 1, align = "L")
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = 'DK1: ' + strDK1_EL, ln = 1)
			
			pdf.set_font('Arial', 'B', size = 11)			
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = 'Grenzwertueberschreitung Rekultivierungsschicht', ln = 1)
			pdf.set_font('Arial', size = 11)
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = 'Feststoff: ' + strREK_TS_Ueberschritten, ln = 1)
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = 'Eluat: ' + strREK_EL_Ueberschritten, ln = 1)

			pdf.set_font('Arial', 'B', size = 11)
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = 'Grenzwertueberschreitung Geologische Barriere', ln = 1)
			pdf.set_font('Arial', size = 11)
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = 'Feststoff: ' + strGEO_TS_Ueberschritten, ln = 1)
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = 'Eluat: ' + strGEO_EL_Ueberschritten, ln = 1)
			pdf.cell(w = 0, h = 8, border  = 0, align = "L", ln = 1)

			pdf.set_font('Arial', 'B', size = 14)
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = 'Gefaehrlicher Abfall', ln = 1, fill=True)
			pdf.set_font('Arial', size = 11)
			pdf.cell(w = 90, h = 8, border  = 1, align = "L", txt = 'Vorsorgewerte fuer S-H / Hamburg eingehalten:')
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = 'Nein', ln = 1)
			pdf.cell(w = 90, h = 8, border  = 1, align = "L", txt = 'Ueberschreitung fuer:')
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = 'Arsen, Kupfer, Blei', ln = 1)
			pdf.cell(w = 90, h = 8, border  = 1, align = "L", txt = 'Vorsorgewerte fuer Niedersachsen eingehalten:')
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = 'Nein', ln = 1)
			pdf.cell(w = 90, h = 8, border  = 1, align = "L", txt = 'Ueberschreitung fuer:')
			pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = 'Arsen, Kupfer, Blei', ln = 1)



			#pdf.write(pdf.cell(w = 0, h = 8, border  = 1, align = "L", txt = 'Hello World!'), 5, "Projekt:" + " " + entry0.get() + '\n' + '\n' +  "Datum (J-M-T): " + str(datelist[0]) 
				#+ '\n' "__________________________________________________________________________________" + '\n' + '\n'
				#+ Bodenart_auswahl + '\n' + '\n' + Humus
				#+ '\n' "__________________________________________________________________________________"
				#+ '\n' + '\n' + "Pruefung Vorsorgewerte Bundes-Bodenschutzgesetz" + '\n' + '\n' + "Ueberschritten:" + " " + strBBSchG_Ueberschritten
				#+ '\n' "__________________________________________________________________________________" 
				#+ '\n' + '\n' + "Pruefung LAGA M20" + '\n' + '\n' 
				#+ "LAGA Einbauklasse Feststoff:" + '\n' + "  Z0:" + " " + strZ0_TS + '\n' + "  Z0*:" + " " + strZ0_Stern_TS 
				#+ '\n' + "  Z1:" + " " + strZ1_TS + '\n' + "  Z2:" + " " + strZ2_TS + '\n' + " >Z2:" + " " + strHigher_Z2_TS + '\n' + '\n' 
				#+ "LAGA Einbauklasse Eluat:" + '\n' + "  Z0:" + " " + strZ0_EL + '\n' + "  Z1.1:" + " " + strZ11_EL 
				#+ '\n' + "  Z1.2:" + " " + strZ12_EL + '\n' + "  Z2:" + " " + strZ2_EL + '\n' + " >Z2:" + " " + strHigher_Z2_EL + '\n' 
				#+ "__________________________________________________________________________________"  
				#+ '\n' + '\n' + "Pruefung Deponieverordnung" + '\n' + '\n' 
				#+ "Deponieklasse Feststoff:" + '\n' + "  DK1:" + " " + strDK1_TS + '\n' + "  DK2:" + " " + strDK2_TS 
				#+ '\n' + "  DK3:" + " " + strDK3_TS + '\n' + "  >DK3:" + " " + strHigher_DK3_TS 
				#+ '\n' + "  Rekultivierungsschicht ueberschritten:" + " " + strREK_TS_Ueberschritten
				#+ '\n' + "  Geologische Barriere ueberschritten:" + " " + strGEO_TS_Ueberschritten
				#+ '\n' + '\n'
				#+ "Deponieklasse Eluat:" + '\n' + "  DK1:" + " " + strDK1_EL + '\n' + "  DK2:" + " " + strDK2_EL 
				#+ '\n' + "  DK3:" + " " + strDK3_EL + '\n' + "  >DK3:" + " " + strHigher_DK3_EL 
				#+ '\n' + "  Rekultivierungsschicht ueberschritten:" + " " + strREK_EL_Ueberschritten
				#+ '\n' + "  Geologische Barriere ueberschritten:" + " " + strGEO_EL_Ueberschritten
				#+ '\n'
				#+ "__________________________________________________________________________________"  
				#+ '\n' + '\n' 
				#+ "Werte Feststoff:" + '\n' 
				#+ "  Arsen (mg/kg TM) = " + entry1.get() + '\n' 
				#+ "  Blei (mg/kg TM) = " + entry2.get() + '\n'
				#+ "  Cadmium (mg/kg TM) = " + entry3.get() + '\n'
				#+ "  Chrom gesamt (mg/kg TM) = " + entry4.get() + '\n'
				#+ "  Kupfer (mg/kg TM) = " + entry5.get() + '\n'
				#+ "  Nickel (mg/kg TM) = " + entry6.get() + '\n'
				#+ "  Quecksilber (mg/kg TM) = " + entry7.get() + '\n'
				#+ "  Thallium (mg/kg TM) = " + entry8.get() + '\n'
				#+ "  Zink (mg/kg TM) = " + entry9.get() + '\n'
				#+ "  EOX C10-C40 (mg/kg TM) = " + entry10.get() + '\n'
				#+ "  Kohlenwasserstoffe C10-C40 (mg/kg TM) = " + entry11.get() + '\n'
				#+ "  Kohlenwasserstoffe C10-C22 (mg/kg TM) = " + entry12.get() + '\n'
				#+ "  Cyanid gesamt (mg/kg TM) = " + entry13.get() + '\n'
				#+ "  BTX (BTEX) (mg/kg TM) = " + entry14.get() + '\n'
				#+ "  LHKW (mg/kg TM) = " + entry15.get() + '\n'
				#+ "  PAK 16 (mg/kg TM) = " + entry16.get() + '\n'
				#+ "  Benzo(a)pyren (mg/kg TM) = " + entry17.get() + '\n'
				#+ "  PCB6 (mg/kg TM) = " + entry18.get() + '\n'
				#+ "  PCB7 (mg/kg TM) = " + entry19.get() + '\n'
				#+ "  TOC (Masse-%) = " + entry20.get() + '\n'
				#+ "  Gluehverlust (Masse-%) = " + entry21.get() + '\n'
				#+ "  Saeureneutralisationskapazitaet (mmol/kg) = " + entry22.get() + '\n'
				#+ "  Extrahierbare lipophile Stoffe (Masse-%) = " + entry23.get() + '\n'
				#+ "  Dioxine / Furane (ng/kg TM) = " + entry24.get() + '\n' + '\n'
				#+ "Werte Eluat:" + '\n'
				#+ "  Arsen (ug/L) = " + entry25.get() + '\n'
				#+ "  Blei (ug/L) = " + entry26.get() + '\n'
				#+ "  Cadmium (ug/L) = " + entry27.get() + '\n'
				#+ "  Chrom gesamt (ug/L) = " + entry28.get() + '\n'
				#+ "  Kupfer (ug/L) = " + entry29.get() + '\n'
				#+ "  Nickel (ug/L) = " + entry30.get() + '\n'
				#+ "  Quecksilber (ug/L) = " + entry31.get() + '\n'
				#+ "  Zink (ug/L) = " + entry32.get() + '\n'
				#+ "  Cyanid (ug/L) = " + entry33.get() + '\n'
				#+ "  Cyanid, leicht freisetzbar (ug/L) = " + entry34.get() + '\n'
				#+ "  Phenolindex (ug/L) = " + entry35.get() + '\n'
				#+ "  Chlorid (mg/L) = " + entry36.get() + '\n'
				#+ "  Sulfat (mg/L) = " + entry37.get() + '\n'
				#+ "  pH-Wert = " + entry38.get() + '\n'
				#+ "  Leitfaehigkeit (uS/cm) = " + entry39.get()
				#+ "  DOC (mg/L) = " + entry40.get() + '\n'
				#+ "  Fluorid (mg/L) = " + entry41.get() + '\n'
				#+ "  Barium (mg/L) = " + entry42.get() + '\n'
				#+ "  Molybdaen (ug/L) = " + entry43.get() + '\n'
				#+ "  Antimon (ug/L) = " + entry44.get() + '\n'
				#+ "  Selen (ug/L) = " + entry45.get() + '\n'
				#+ "  Gesamtgehalt an geloesten Feststoffen (mg/L) = " + entry46.get() + '\n')

			safe_file = tkFileDialog.asksaveasfilename(initialdir = "/",title = "Speichern unter",
				filetypes = (("PDF","*.pdf"),("all files","*.*")))
			pdf.output(safe_file +".pdf")
			
		except ValueError:
			resultLabel.config(text="Werte pruefen", bg = "red")

		except NameError:
			resultLabel.config(text="Bodenart / Anteil Humus waehlen", bg = "red")

# Run GUI-Programm
root = Tk()

#Frame title
root.title("  Boden- und abfallrechtlichen Bewertung (Copyright: Johannes Krohn)")

#Icon
root.iconbitmap("C:/Users/Johannes/Documents/Programmieren/Python/Deklarationsanalyse/icon2.ico")

#Frame geometry 
root.geometry("850x850")
root.resizable(0, 0) #Don't allow resizing in the x or y direction

#Frame icon
#root.iconbitmap

#input picture
#img = ImageTk.PhotoImage(Image.open(path))

# Variablen fuer Bodenart- und Humusfunktion
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()


# Objekte ("Instance") herstellen, welche das "self" in der Klasse GUI ersetzen
# Parameter Feststoff + Eluat
# 0 = Platzhalterwert

Arsen = GUI(root, "Arsen", 0, 0,
	20, 15, 10, 15, 45, 150, # LAGA Feststoff Grenzwerte
	14, 14, 20, 60, # LAGA Eluat Grenzwerte
	0, 0, 0, 0, 0, # BBSchG Grenzwerte (Limit_BBSchG_T, Limit_BBSchG_SL, Limit_BBSchG_Sa, Limit_BBSchG_HumusU8, Limit_BBSchG_HumusUE8)
	0, 0, 0, 0, # DepV Feststoff Deponieklasse Grenzwerte
	0, # DepV Feststoff Rekultivierungsschicht (REK) Grenzwert
	0, # DepV Feststoff Geologische Barriere (GEO) Grenzwert
	50, 200, 200, 2500, # DepV Eluat Deponieklasse Grenzwerte
	10, # DepV Eluat Rekultivierungsschicht (REK) Grenzwert
	10) # DepV Eluat Geologische Barriere (GEO) Grenzwert
Blei = GUI(root, "Blei", 0, 0,
	100, 70, 40, 140, 210, 700,
	40, 40, 80, 200,
	100, 70, 40, 0, 0,
	0, 0, 0, 0,
	140,
	0,
	50, 200, 1000, 5000,
	40,
	20)
Cadmium = GUI(root,"Cadmium",0, 0,
	1.5, 1, 0.4, 1, 3, 10,
	1.5, 1.5, 3, 6,
	1.5, 1, 0.4, 0, 0,
	0, 0, 0, 0,
	1,
	0,
	4, 50, 100, 500,
	2,
	2)
Chrom_gesamt = GUI(root, "Chrom gesamt", 0, 0,
	100, 60, 30, 120, 180, 600,
	12.5, 12.5, 25, 60,
	100, 60, 30, 0, 0,
	0, 0, 0, 0,
	120,
	0,
	50, 300, 1000, 7000,
	30,
	0)
Kupfer = GUI(root, "Kupfer", 0, 0,
	60, 40, 20, 80, 120, 400,
	20, 20, 60, 100,
	60, 40, 20, 0, 0,
	0, 0, 0, 0,
	80,
	0,
	200, 1000, 5000, 10000,
	50,
	50)
Nickel = GUI(root, "Nickel", 0, 0,
	70, 50, 15, 100, 150, 500,
	15, 15, 20, 70,
	70, 50, 15, 0, 0,
	0, 0, 0, 0,
	100,
	0,
	40, 200, 1000, 4000,
	50,
	40)
Quecksilber = GUI(root, "Quecksilber", 0, 0,
	1, 0.5, 0.1, 1, 1.5, 5,
	0.5, 0.5, 1, 2,
	1, 0.5, 0.1, 0, 0,
	0, 0, 0, 0,
	1,
	0,
	1, 5, 20, 200,
	0.2,
	0.2)
Zink = GUI(root, "Zink", 0, 0,
	200, 150, 60, 300, 450, 1500,
	150, 150, 200, 600,
	200, 150, 60, 0, 0,
	0, 0, 0, 0,
	300,
	0,
	400, 2000, 5000, 20000,
	100,
	100)

# Parameter Feststoff
EOX = GUI(root, "EOX", 0, 0,
	1, 1, 1, 1, 3, 10,
	0, 0, 0, 0,
	0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0,
	0,
	0, 0, 0, 0,
	0,
	0)
KW_C10_C40 = GUI(root, "Kohlenwasserstoffe (C10-C40)", 0, 0,
	100, 100, 100, 400, 600, 2000,
	0, 0, 0, 0,
	0, 0, 0, 0, 0,
	500, 0, 0, 0,
	0,
	100,
	0, 0, 0, 0,
	0,
	0)
KW_mobiler_Anteil_C10_C22 = GUI(root, "Kohlenwasserstoffe (C10-C22)", 0, 0,
	100, 100, 100, 200, 300, 1000,
	0, 0, 0, 0,
	0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0,
	0,
	0, 0, 0, 0,
	0,
	0)
Cyanid_gesamt = GUI(root, "Cyanide gesamt", 0, 0,
	1, 1, 1, 1, 3, 10,
	0, 0, 0, 0,
	0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0,
	0,
	0, 0, 0, 0,
	0,
	0)
BTX_BTEX = GUI(root, "BTX (BTEX)", 0, 0,
	1, 1, 1, 1, 1, 1,
	0, 0, 0, 0,
	0, 0, 0, 0, 0,
	6, 0, 0, 0,
	0,
	1,
	0, 0, 0, 0,
	0,
	0)
LHKW = GUI(root, "LHKW", 0, 0,
	1, 1, 1, 1, 1, 1,
	0, 0, 0, 0,
	0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0,
	0,
	0, 0, 0, 0,
	0,
	0)
PAK_16 = GUI(root, "PAK16 (EPA)", 0, 0,
	3, 3, 3, 3, 3, 30,
	0, 0, 0, 0,
	0, 0, 0, 10, 3,
	30, 0, 0, 0,
	5,
	1,
	0, 0, 0, 0,
	0,
	0)
Benzopyren = GUI(root, "Benzo(a)pyren", 0, 0,
	0.3, 0.3, 0.3, 0.6, 0.9, 3,
	0, 0, 0, 0,
	0, 0, 0, 1, 0.3,
	0, 0, 0, 0,
	0.6,
	0,
	0, 0, 0, 0,
	0,
	0)
PCB6 = GUI(root, "PCB6", 0, 0,
	0.05, 0.05, 0.05, 0.1, 0.15, 0.5,
	0, 0, 0, 0,
	0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0,
	0,
	0, 0, 0, 0,
	0,
	0)
PCB7 = GUI(root, "PCB7", 0, 0,
	0, 0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0, 0, 0, 0, 0,
	1, 0, 0, 0,
	0.1,
	0.02,
	0, 0, 0, 0,
	0,
	0)
Thallium = GUI(root, "Thallium", 0, 0,
	1, 0.7, 0.4, 0.7, 2.1, 7,
	0, 0, 0, 0,
	0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0,
	0,
	0, 0, 0, 0,
	0,
	0)
TOC = GUI(root, "TOC", 0, 0,
	0.5, 0.5, 0.5, 0.5, 1.5, 5,
	0, 0, 0, 0,
	0, 0, 0, 0, 0,
	1, 1, 3, 6,
	0,
	1,
	0, 0, 0, 0,
	0,
	0)
Gluehverlust = GUI(root, "Gluehverlust", 0, 0,
	0, 0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0, 0, 0, 0, 0,
	3, 3, 5, 10,
	0,
	3,
	0, 0, 0, 0,
	0,
	0)
Saeureneutralisationskapazitaet = GUI(root, "Saeureneutralisationskapazitaet", 0, 0,
	0, 0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0,
	0,
	0, 0, 0, 0,
	0,
	0)
Lipohile_Stoffe = GUI(root, "Extrahierbare Lipohile Stoffe", 0, 0,
	0, 0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0, 0, 0, 0, 0,
	0.1, 0.4, 0.8, 4,
	0,
	0,
	0, 0, 0, 0,
	0,
	0)
Dioxine = GUI(root, "Dioxine / Furane", 0, 0,
	0, 0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0,
	0,
	0, 0, 0, 0,
	0,
	0)

# Parameter Eluat
pH_Wert = GUI(root, "pH-Wert", 0, 0,
	0, 0, 0, 0, 0, 0,
	6.5, 6.5, 6, 5.5,
	0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0,
	0, 
	5.5, 5.5, 5.5, 4,
	6.5,
	6.5)
# pH_Wert = GUI(root, "pH-Wert", 0, 0,
# 	0, 0, 0, 0, 0, 0,
# 	[6.5, 9.5],[6.5, 9.5],[6,12],[5.5,12])

Leitfaehigkeit = GUI(root, "Leitfaehigkeit", 0, 0,
	0, 0, 0, 0, 0, 0,
	250, 250, 1500, 2000,
	0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0,
	0, 
	0, 0, 0, 0,
	500,
	0)
Cyanid = GUI(root, "Cyanid", 0, 0,
	0, 0, 0, 0, 0, 0,
	5, 5, 10, 20,
	0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0,
	0, 
	0, 0, 0, 0,
	0,
	0)
Cyanid_lf = GUI(root, "Cyanid (leicht freisetzbar)", 0, 0,
	0, 0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0,
	0, 
	10, 100, 500, 1000,
	0,
	10)
Phenolindex = GUI(root, "Phenolindex", 0, 0,
	0, 0, 0, 0, 0, 0,
	20, 20, 40, 100,
	0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0,
	0, 
	100, 200, 5000, 10000,
	0,
	50)
Chlorid = GUI(root, "Chlorid", 0, 0,
	0, 0, 0, 0, 0, 0,
	30, 30, 50, 100,
	0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0,
	0, 
	80, 1500, 1500, 2500,
	10,
	10)
Sulfat = GUI(root, "Sulfat", 0, 0,
	0, 0, 0, 0, 0, 0,
	20, 20, 50, 200,
	0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0,
	0, 
	100, 2000, 2000, 5000,
	50,
	50)
DOC = GUI(root, "DOC", 0, 0,
	0, 0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0,
	0, 
	50, 50, 80, 100,
	0,
	0)
Fluorid = GUI(root, "Fluorid", 0, 0,
	0, 0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0,
	0, 
	1, 5, 15, 50,
	0,
	0)
Barium = GUI(root, "Barium", 0, 0,
	0, 0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0,
	0, 
	2, 5, 10, 30,
	0,
	0)
Molybdaen = GUI(root, "Molybdaen", 0, 0,
	0, 0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0,
	0, 
	50, 300, 1000, 3000,
	0,
	0)
Antimon = GUI(root, "Antimon", 0, 0,
	0, 0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0,
	0, 
	6, 30, 70, 500,
	0,
	0)
Selen = GUI(root, "Selen", 0, 0,
	0, 0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0,
	0, 
	10, 30, 50, 700,
	0,
	0)
Gesamtgehalt_geloeste_Feststoffe = GUI(root, "Gesamtgehalt an geloesten Feststoffen", 0, 0,
	0, 0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0, 0, 0, 0, 0,
	0, 0, 0, 0,
	0,
	0, 
	400, 3000, 6000, 10000,
	0,
	400)

print("Erfolgreich gestartet!")
# Laesst das GUI-Programm in einer loop laufen

root.mainloop()
