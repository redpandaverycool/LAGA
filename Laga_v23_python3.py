# ph wert problem "zwischen" noch loesen
# Saeureneutralisationskapazitaet bisher nicht mit drin in DepV, muss? nachlesen
# Weitere Anmerkungen BBSch, LAGA und DepV hinzufuegen
# Grenzwere etc. fuer gefaehrlichen Abfall hinzufuegen
# Button "Info: Hinweise zur Dateneingabe"
# Button "Info: Bewertungsgrundlagen", -> Gesetze und Grenzwerte etc. hinterlegen
# Button "Info": Herkunft Stoffe
# Butto "Text generieren"
# Werte und Einheten BSchV und DepV und Gef. Abfall noch prüfen
# If else code block prüfen, ob dieser korrekt klassifiziert

##### Prüfung Werte LAGA
# FERTIG LAGA EINSTUFUNG PRÜFEN!!!!!
# FERTIG TS Z0* -> Für Bodenart TON gelten andere Grenzwerte für Arsen, Cadmium, Thallium, siehe PDF M20_II
# FERTIG TS Z0Stern -> Bei Überschreitung ist die Ursache zu prüfen
# FERTIG TS Z1 EOX -> Bei Überschreitung ist die Ursache zu prüfen
# FERTIG TS Z1 PAK16 -> Tabelle II.1.2-4: Fußnote 3) Bodenmaterial mit Zuordnungswerten > 3 mg/kg und ≤ 9 mg/kg darf nur in Gebieten mit hydrogeologisch günstigen Deckschichten eingebaut werden.
# FERTIG, Nein auch für Z0-Werte ....TS KW10-40 auch für Z0 Werte? Oder nur Z0Stern? Falls nur für Z0Stern muss das noch angepasst werden.
# FERTIG TS Z0 und Z0 Stern TOC -> Bei einem C:N-Verhältnis > 25 beträgt der Zuordnungswert 1 Masse-%
# FERTIG Eluat Z0/Z0* -> Quecksilber < 0,5, nicht wie der anderen <= -> prüfen, ob dies so im if else code steht
# FERTIG Eluat Z1 -> Quecksilber < 0,5 (s.o.), auch hier prüfen
# FERTIG Eluat pH-Wert -> Extra prüfen, ob korrekt da ein Spezialfall (Spanne)
# FERTIG Eluat Chlorid Z2 -> Ausnahme: Bei natürlichen Böden in Ausnahmefällen bis 300 mg/l
# FERTIG Eluat Arsen Z2 -> Ausnahme: Bei natürlichen Böden in Ausnahmefällen bis 120 Ug/l
# TOC Einheit in Masse-% oder Masse-% TM?



######BBSchV
# FERTIG Hinweis Schwermetalle: Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten: unbedenklich, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen

# Anmerkungen nur zeigen, wenn auch Werte eingegeben wurden!
# FERTIG Fussnoten
# FERTIG Extra Button -> b) Stark schluffige Sande sind entsprechend der Bodenart Lehm/Schluff zu bewerten. (Bei Sand, stark schluffig?)
# FERTIG c) Bei Böden der Bodenart Ton mit einem pH-Wert von < 6,0 gelten für Cadmium, Nickel und Zink die Vorsorgewerte der Bodenart Lehm/Schluff.
# FERTIG c) Bei Böden der Bodenart Lehm/Schluff mit einem pH-Wert von < 6,0 gelten für Cadmium, Nickel und Zink die Vorsorgewerte der Bodenart Sand.
# c) FERTIG Bei Böden mit einem pH-Wert von < 5,0 sind die Vorsorgewerte für Blei entsprechend den ersten beiden Anstrichen herabzusetzen.
# d) FERTIG Die Vorsorgewerte der Tabelle 4.1 finden für Böden und Bodenhorizonte mit einem Humusgehalt von mehr als 8 Prozent keine Anwendung. Für diese Böden können die zuständigen Behörden ggf. gebietsbezogene Festsetzungen treffen.
# e) FERTIG Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten: unbedenklich, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen

##### DepV
# FERTIG siehe DepV-Dokument
# FERTIG Gucken, ob noch mit den richtigen Einheiten die Klassifikation gemacht wird
# FERTIG Wird Chlorid richtig eingestuft? Gleich Grenzwerte bei DK2 und DK3
# Pheolindex ist bei DepV "Phenole" in mg/L, das muss so entsprechend auch in das PDF geschrieben werden und nicht "Phenolindex"
# Antimon C0-Wert noch hinzufügen
# FERTIG Ph Werte einstufung prüfen (ähnlich wie bei LAGA). ggf- copy paste von da
# FERTIG Fußnoten noch einpflegen
# Extr. lip. Stoffe in Masse%-TM?? anstatt nur Masse%?

# Noch to do
##### Gefährlicher Abfall
# PDF ausgabe anpassen
# Werte auch pdf ausdrucken
# Auswertungsgrundlagen im Programm darstellen (Tabellen und Grundlage welche Gesetze)
# Hinweise zur Dateneingabe hinzufügen (Zeile 228)

from tkinter import *
import tkinter, tkinter.constants, tkinter.filedialog, tkinter.ttk
from tkinter.filedialog import askopenfilename
import os
import csv
import datetime
import fpdf
import pandas as pd
from docx import Document
from docx.shared import Cm, Pt

# Button.place(x=0,y=0)

# LAGA Einbauklassen, BBSchG und DepV Blanko-Listen (Feststoffe=TS | Eluat=El)/ Bodenart/ Datum
# LAGA
Z0_TS = []
Z0_Stern_TS = []
Z1_TS = []
Z2_TS = []
Higher_Z2_TS = []
LAGA_TS_Anmerkungen = []
Z0_EL = []
Z11_EL = []
Z12_EL = []
Z2_EL = []
Higher_Z2_EL = []
#Z0_Stern_EL -> Gleiche Grenzwerte wie Z0_EL
LAGA_EL_Anmerkungen = []
# BBSchG
BBSchG_Eingehalten = []
BBSchG_Ueberschritten = []
BBSchG_Vorsorgewerte_ueberschritten = []
BBSchG_Anmerkungen = []
# DepV (Rekultivierungsschicht -> REK / Geologische Barriere -> GEO)
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
DepV_Anmerkungen = []
# Gefährlicher Abfall
GefAbf_HH_SH_Eingehalten = []
GefAbf_HH_SH_Ueberschritten = []
GefAbf_HH_SH_Ueberschritten_Stoffe = []
GefAbf_NDS_Eingehalten = []
GefAbf_NDS_Ueberschritten = []
GefAbf_NDS_Ueberschritten_Stoffe = []
GefAbf_Anmerkungen = []
# Bodenart/Datum
Bodenart = []
datelist = []
# Datum
today = datetime.date.today()
datelist.append(today)
# Probenbezeichnung/Probenahmedatum
Probenbezeichnung = []
Probenahmedatum = []
# List entry


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
                 Limit_GEO_EL,
                 Limit_GefAbf_HH_SH,
                 Limit_GefAbf_HH_NDS):

        mainframe = Frame(master).grid(column=0, row=0, sticky=(N, W, E, S))

        Label(master, text="").grid(row=0, sticky=E)
        Label(master, text="Probenbezeichnung:").grid(column= 0, row=2, sticky=N, padx=(100, 0))
        Label(master, text="Probenahmedatum:").grid(row=3, sticky=N, padx=(100, 0))
        #Label(master, text="").grid(row=2, sticky=E)

        Label(master, text="Hauptbodenart (HB):").grid(row=4, sticky=E)
        Label(master, text="Schluffgehalt wenn HB Sand:").grid(row=7, sticky=E)
        Label(master, text="Anteil Humus (TOC):").grid(row=9, sticky=E)
        #Label(master, text="").grid(row=5, sticky=E)

        Label(master, text="Werte Feststoff", width=17, fg='black').grid(row=1, column=4, padx=10)
        Label(master, text="Werte Eluat", width=17, fg='black').grid(row=1, column=7)

        Label(master, text="Arsen").grid(row=2,column=3, sticky=E)
        Label(master, text="Blei").grid(row=3, column=3, sticky=E)
        Label(master, text="Cadmium").grid(row=4,column=3, sticky=E)
        Label(master, text="Chrom gesamt").grid(row=5,column=3, sticky=E)
        Label(master, text="Kupfer").grid(row=6,column=3, sticky=E)
        Label(master, text="Nickel").grid(row=7,column=3, sticky=E)
        Label(master, text="Quecksilber").grid(row=8,column=3, sticky=E)
        Label(master, text="Thallium").grid(row=9,column=3, sticky=E)
        Label(master, text="Zink").grid(row=10,column=3, sticky=E)
        Label(master, text="EOX").grid(row=11,column=3, sticky=E)
        Label(master, text="Kohlenwasserstoffe C10-C40").grid(row=12,column=3, sticky=E)
        Label(master, text="Kohlenwasserstoffe C10-C22").grid(row=13,column=3, sticky=E)
        Label(master, text="Cyanid gesamt").grid(row=14,column=3, sticky=E)
        Label(master, text="BTX (BTEX)").grid(row=15,column=3, sticky=E)
        Label(master, text="LHKW").grid(row=16,column=3, sticky=E)
        Label(master, text="PAK 16 (EPA)").grid(row=17,column=3, sticky=E)
        Label(master, text="Benzo(a)pyren").grid(row=18,column=3, sticky=E)
        Label(master, text="PCB 6").grid(row=19,column=3, sticky=E)
        Label(master, text="PCB 7").grid(row=20,column=3, sticky=E)
        Label(master, text="TOC").grid(row=21,column=3, sticky=E)
        Label(master, text="Glühverlust").grid(row=22,column=3, sticky=E)
        Label(master, text="Säureneutralisationskapazität").grid(row=23,column=3, sticky=E)
        Label(master, text="Extr. lipohile Stoffe").grid(row=24,column=3, sticky=E)
        Label(master, text="Dioxine / Furane").grid(row=25,column=3, sticky=E)

        Label(master, text="Arsen").grid(row=2, column=6, sticky=E)
        Label(master, text="Blei").grid(row=3, column=6, sticky=E)
        Label(master, text="Cadmium").grid(row=4, column=6, sticky=E)
        Label(master, text="Chrom gesamt").grid(row=5, column=6, sticky=E)
        Label(master, text="Kupfer").grid(row=6, column=6, sticky=E)
        Label(master, text="Nickel").grid(row=7, column=6, sticky=E)
        Label(master, text="Quecksilber").grid(row=8, column=6, sticky=E)
        Label(master, text="Zink").grid(row=9, column=6, sticky=E)
        Label(master, text="Cyanid").grid(row=10, column=6, sticky=E)
        Label(master, text="Cyanid, leicht freisetzbar").grid(row=11, column=6, sticky=E)
        Label(master, text="Phenolindex").grid(row=12, column=6, sticky=E)
        Label(master, text="Chlorid").grid(row=13, column=6, sticky=E)
        Label(master, text="Sulfat").grid(row=14, column=6, sticky=E)
        Label(master, text="pH-Wert").grid(row=15, column=6, sticky=E)
        Label(master, text="Leitfähigkeit").grid(row=16, column=6, sticky=E)
        Label(master, text="DOC").grid(row=17, column=6, sticky=E)
        Label(master, text="Fluorid").grid(row=18, column=6, sticky=E)
        Label(master, text="Barium").grid(row=19, column=6, sticky=E)
        Label(master, text="Molybdän").grid(row=20, column=6, sticky=E)
        Label(master, text="Antimon").grid(row=21, column=6, sticky=E)
        Label(master, text="Selen").grid(row=22, column=6, sticky=E)
        Label(master, text="Gesamtgehalt an gel. Stoffen").grid(row=23, column=6, sticky=E)

        #Label(master, text="   Hinweise zur Dateneingabe:").grid(row=33, column=0, sticky=W + E)
        #Label(master, text="   1. Bei Wert unter Bestimmungs- ").grid(row=34, column=0, sticky=W + E)
        #Label(master, text='      "grenze < benutzen (z.B. <0.5)').grid(row=35, column=0, sticky=W + E)
        #Label(master, text="   2. Dezimalstellen mit Punkt (.) angeben").grid(row=36, column=0, sticky=W + E)

        global resultLabel
        resultLabel = Label(root, text="")
        resultLabel.grid(row=21, column=1)

        global entry0
        global entry00
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

        entry0 = Entry(master)  # Probebezeichnung
        entry00 = Entry(master)  # Probenahmedatum
        # Feststoff 24x
        entry1 = Entry(master)  # Stoff1
        entry2 = Entry(master)  # Stoff2
        entry3 = Entry(master)  # Stoff3
        entry4 = Entry(master)  # Stoff4
        entry5 = Entry(master)  # Stoff5
        entry6 = Entry(master)  # Stoff6
        entry7 = Entry(master)  # Stoff7
        entry8 = Entry(master)  # Stoff8
        entry9 = Entry(master)  # Stoff9
        entry10 = Entry(master)  # Stoff10
        entry11 = Entry(master)  # Stoff11
        entry12 = Entry(master)  # Stoff12
        entry13 = Entry(master)  # Stoff13
        entry14 = Entry(master)  # Stoff14
        entry15 = Entry(master)  # Stoff15
        entry16 = Entry(master)  # Stoff16
        entry17 = Entry(master)  # Stoff17
        entry18 = Entry(master)  # Stoff18
        entry19 = Entry(master)  # Stoff19
        entry20 = Entry(master)  # Stoff20
        entry21 = Entry(master)  # Stoff21
        entry22 = Entry(master)  # Stoff22
        entry23 = Entry(master)  # Stoff23
        entry24 = Entry(master)  # Stoff24

        # Eluat 22x
        entry25 = Entry(master)  # Stoff25
        entry26 = Entry(master)  # Stoff26
        entry27 = Entry(master)  # Stoff27
        entry28 = Entry(master)  # Stoff28
        entry29 = Entry(master)  # Stoff29
        entry30 = Entry(master)  # Stoff30
        entry31 = Entry(master)  # Stoff31
        entry32 = Entry(master)  # Stoff32
        entry33 = Entry(master)  # Stoff33
        entry34 = Entry(master)  # Stoff34
        entry35 = Entry(master)  # Stoff35
        entry36 = Entry(master)  # Stoff36
        entry37 = Entry(master)  # Stoff37
        entry38 = Entry(master)  # Stoff38
        entry39 = Entry(master)  # Stoff39
        entry40 = Entry(master)  # Stoff40
        entry41 = Entry(master)  # Stoff41
        entry42 = Entry(master)  # Stoff42
        entry43 = Entry(master)  # Stoff43
        entry44 = Entry(master)  # Stoff44
        entry45 = Entry(master)  # Stoff45
        entry46 = Entry(master)  # Stoff46

        entry0.grid(row=2, column=1, sticky=N)
        entry00.grid(row=3, column=1, sticky=N)
        # Feststoff 24x
        entry1.grid(row=2, column=4)
        entry2.grid(row=3, column=4)
        entry3.grid(row=4, column=4)
        entry4.grid(row=5, column=4)
        entry5.grid(row=6, column=4)
        entry6.grid(row=7, column=4)
        entry7.grid(row=8, column=4)
        entry8.grid(row=9, column=4)
        entry9.grid(row=10, column=4)
        entry10.grid(row=11, column=4)
        entry11.grid(row=12, column=4)
        entry12.grid(row=13, column=4)
        entry13.grid(row=14, column=4)
        entry14.grid(row=15, column=4)
        entry15.grid(row=16, column=4)
        entry16.grid(row=17, column=4)
        entry17.grid(row=18, column=4)
        entry18.grid(row=19, column=4)
        entry19.grid(row=20, column=4)
        entry20.grid(row=21, column=4)
        entry21.grid(row=22, column=4)
        entry22.grid(row=23, column=4)
        entry23.grid(row=24, column=4)
        entry24.grid(row=25, column=4)

        entry25.grid(row=2, column=7)
        entry26.grid(row=3, column=7)
        entry27.grid(row=4, column=7)
        entry28.grid(row=5, column=7)
        entry29.grid(row=6, column=7)
        entry30.grid(row=7, column=7)
        entry31.grid(row=8, column=7)
        entry32.grid(row=9, column=7)
        entry33.grid(row=10, column=7)
        entry34.grid(row=11, column=7)
        entry35.grid(row=12, column=7)
        entry36.grid(row=13, column=7)
        entry37.grid(row=14, column=7)
        entry38.grid(row=15, column=7)
        entry39.grid(row=16, column=7)
        entry40.grid(row=17, column=7)
        entry41.grid(row=18, column=7)
        entry42.grid(row=19, column=7)
        entry43.grid(row=20, column=7)
        entry44.grid(row=21, column=7)
        entry45.grid(row=22, column=7)
        entry46.grid(row=23, column=7)

        Button(master, text="    Lade Werte aus GBA Prüfbericht    ", fg="black", bg="white", padx=2, pady=2,
               command=self.loadexcel).grid(row=16, column=1, sticky=W + E)
        Button(master, text="Zurücksetzen", command=self.Zuruecksetzen, bg="white", padx=2, pady=2).grid(row=18, column=1,
                                                                                                               sticky=W + E)
        Button(master, text="Bewertung", fg="black", bg="white", padx=2, pady=2, command=self.Stoff).grid(row=20,
                                                                                                          column=1,
                                                                                                          sticky=W + E)
        Button(master, text="Beenden", command=root.destroy, bg="white", padx=2, pady=2).grid(row=22, column=1,
                                                                                              sticky=W + E)
        Radiobutton(master, text="Ton", variable=var1, command=self.Bodenart, value=1).grid(row=6, column=1, sticky=W)
        Radiobutton(master, text="Schluff/Lehm", variable=var1, command=self.Bodenart, value=2).grid(row=5, column=1,
                                                                                                     sticky=W)
        Radiobutton(master, text="Sand", variable=var1, command=self.Bodenart, value=3).grid(row=4, column=1, sticky=W)
        Radiobutton_nichtstarkschluffhaltig = Radiobutton(master, text="Nicht stark schluffhaltig (<40%)", variable=var4, command=self.Bodenart_ergaenzung, value=1).grid(row=7, column=1, sticky=W)
        Radiobutton_starkschluffhaltig = Radiobutton(master, text="Stark schluffhaltig (40 bis <50%)", variable=var4, command=self.Bodenart_ergaenzung, value=2).grid(row=8, column=1, sticky=W)
        radiobutton_Humus1 = Radiobutton(master, text=">8% (>4%)", variable=var2, command=self.Humus, value=1).grid(
            row=9, column=1, sticky=W)
        Radiobutton(master, text="<=8% (<=4%)", variable=var2, command=self.Humus, value=2).grid(row=10, column=1,
                                                                                                 sticky=W)

        # For the OptionMenu
        global option_Feststoff_Arsen
        global option_Feststoff_Blei
        global option_Feststoff_Cadmium
        global option_Feststoff_Chromgesamt
        global option_Feststoff_Kupfer
        global option_Feststoff_Nickel
        global option_Feststoff_Quecksilber
        global option_Feststoff_Thallium
        global option_Feststoff_Zink
        global option_Feststoff_EOX
        global option_Feststoff_Kohlenwasserstoffe_C10C40
        global option_Feststoff_Kohlenwasserstoffe_C10C22
        global option_Feststoff_Cyanidegesamt
        global option_Feststoff_BTX
        global option_Feststoff_LHKW
        global option_Feststoff_PAK16
        global option_Feststoff_Benzoapyren
        global option_Feststoff_PCB6
        global option_Feststoff_PCB7
        global option_Feststoff_TOC
        global option_Feststoff_Gluehverlust
        global option_Feststoff_Saeureneutralisationskapazitaet
        global option_Feststoff_LipophileStoffe
        global option_Eluat_pH
        global option_Eluat_Leitf
        global option_Feststoff_Dioxine
        global option_Eluat_Arsen
        global option_Eluat_Blei
        global option_Eluat_Cadmium
        global option_Eluat_Chromgesamt
        global option_Eluat_Kupfer
        global option_Eluat_Nickel
        global option_Eluat_Quecksilber
        global option_Eluat_Zink
        global option_Eluat_Cyanid
        global option_Eluat_Cyanidleichtf
        global option_Eluat_Phenolindex
        global option_Eluat_Chlorid
        global option_Eluat_Sulfat
        global option_Eluat_DOC
        global option_Eluat_Fluorid
        global option_Eluat_Barium
        global option_Eluat_Molybdaen
        global option_Eluat_Antimon
        global option_Eluat_Selen
        global option_Eluat_GesGehaltGelStoffe

        option_Feststoff_Arsen = tkinter.StringVar(root)
        option_Feststoff_Blei = tkinter.StringVar(root)
        option_Feststoff_Cadmium = tkinter.StringVar(root)
        option_Feststoff_Chromgesamt = tkinter.StringVar(root)
        option_Feststoff_Kupfer = tkinter.StringVar(root)
        option_Feststoff_Nickel = tkinter.StringVar(root)
        option_Feststoff_Quecksilber = tkinter.StringVar(root)
        option_Feststoff_Thallium = tkinter.StringVar(root)
        option_Feststoff_Zink = tkinter.StringVar(root)
        option_Feststoff_EOX = tkinter.StringVar(root)
        option_Feststoff_Kohlenwasserstoffe_C10C40 = tkinter.StringVar(root)
        option_Feststoff_Kohlenwasserstoffe_C10C22 = tkinter.StringVar(root)
        option_Feststoff_Cyanidegesamt = tkinter.StringVar(root)
        option_Feststoff_BTX = tkinter.StringVar(root)
        option_Feststoff_LHKW = tkinter.StringVar(root)
        option_Feststoff_PAK16 = tkinter.StringVar(root)
        option_Feststoff_Benzoapyren = tkinter.StringVar(root)
        option_Feststoff_PCB6 = tkinter.StringVar(root)
        option_Feststoff_PCB7 = tkinter.StringVar(root)
        option_Feststoff_Gluehverlust = tkinter.StringVar(root)
        option_Feststoff_TOC = tkinter.StringVar(root)
        option_Feststoff_Saeureneutralisationskapazitaet = tkinter.StringVar(root)
        option_Feststoff_LipophileStoffe = tkinter.StringVar(root)
        option_Feststoff_Dioxine = tkinter.StringVar(root)
        option_Eluat_pH = tkinter.StringVar(root)
        option_Eluat_Leitf = tkinter.StringVar(root)
        option_Eluat_Arsen = tkinter.StringVar(root)
        option_Eluat_Blei = tkinter.StringVar(root)
        option_Eluat_Cadmium = tkinter.StringVar(root)
        option_Eluat_Chromgesamt = tkinter.StringVar(root)
        option_Eluat_Kupfer = tkinter.StringVar(root)
        option_Eluat_Nickel = tkinter.StringVar(root)
        option_Eluat_Quecksilber = tkinter.StringVar(root)
        option_Eluat_Zink = tkinter.StringVar(root)
        option_Eluat_Cyanid = tkinter.StringVar(root)
        option_Eluat_Cyanidleichtf = tkinter.StringVar(root)
        option_Eluat_Phenolindex = tkinter.StringVar(root)
        option_Eluat_Chlorid = tkinter.StringVar(root)
        option_Eluat_Sulfat = tkinter.StringVar(root)
        option_Eluat_DOC = tkinter.StringVar(root)
        option_Eluat_Fluorid = tkinter.StringVar(root)
        option_Eluat_Barium = tkinter.StringVar(root)
        option_Eluat_Molybdaen = tkinter.StringVar(root)
        option_Eluat_Antimon = tkinter.StringVar(root)
        option_Eluat_Selen = tkinter.StringVar(root)
        option_Eluat_GesGehaltGelStoffe = tkinter.StringVar(root)

        Auswahl_Einheit_Feststoff_Arsen = option_Feststoff_Arsen.get()
        Auswahl_Einheit_Feststoff_Blei = option_Feststoff_Blei.get()
        Auswahl_Einheit_Feststoff_Cadmium = option_Feststoff_Cadmium.get()
        Auswahl_Einheit_Feststoff_Chromgesamt = option_Feststoff_Chromgesamt.get()
        Auswahl_Einheit_Feststoff_Kupfer = option_Feststoff_Kupfer.get()
        Auswahl_Einheit_Feststoff_Nickel = option_Feststoff_Nickel.get()
        Auswahl_Einheit_Feststoff_Quecksilber = option_Feststoff_Quecksilber.get()
        Auswahl_Einheit_Feststoff_Thallium = option_Feststoff_Thallium.get()
        Auswahl_Einheit_Feststoff_Zink = option_Feststoff_Zink.get()
        Auswahl_Einheit_Feststoff_EOX = option_Feststoff_EOX.get()
        Auswahl_Einheit_Feststoff_Kohlenwasserstoffe_C10C40 = option_Feststoff_Kohlenwasserstoffe_C10C40.get()
        Auswahl_Einheit_Feststoff_Kohlenwasserstoffe_C10C22 = option_Feststoff_Kohlenwasserstoffe_C10C22.get()
        Auswahl_Einheit_Feststoff_Cyanidegesamt = option_Feststoff_Cyanidegesamt.get()
        Auswahl_Einheit_Feststoff_BTX = option_Feststoff_BTX.get()
        Auswahl_Einheit_Feststoff_LHKW = option_Feststoff_LHKW.get()
        Auswahl_Einheit_Feststoff_PAK16 = option_Feststoff_PAK16.get()
        Auswahl_Einheit_Feststoff_Benzoapyren = option_Feststoff_Benzoapyren.get()
        Auswahl_Einheit_Feststoff_PCB6 = option_Feststoff_PCB6.get()
        Auswahl_Einheit_Feststoff_PCB7 = option_Feststoff_PCB7.get()
        Auswahl_Einheit_Feststoff_TOC = option_Feststoff_TOC.get()
        Auswahl_Einheit_Feststoff_Gluehverlust = option_Feststoff_Gluehverlust.get()
        Auswahl_Einheit_Feststoff_Saeureneutralisationskapazitaet = option_Feststoff_Saeureneutralisationskapazitaet.get()
        Auswahl_Einheit_Feststoff_LipophileStoffe = option_Feststoff_LipophileStoffe.get()
        Auswahl_Einheit_Feststoff_Dioxine = option_Feststoff_Dioxine.get()
        Auswahl_Einheit_Eluat_pH = option_Eluat_pH.get()
        Auswahl_Einheit_Eluat_Leitf = option_Eluat_Leitf.get()
        Auswahl_Einheit_Eluat_Arsen = option_Eluat_Arsen.get()
        Auswahl_Einheit_Eluat_Blei = option_Eluat_Blei.get()
        Auswahl_Einheit_Eluat_Cadmium = option_Eluat_Cadmium.get()
        Auswahl_Einheit_Eluat_Chromgesamt = option_Eluat_Chromgesamt.get()
        Auswahl_Einheit_Eluat_Kupfer = option_Eluat_Kupfer.get()
        Auswahl_Einheit_Eluat_Nickel = option_Eluat_Nickel.get()
        Auswahl_Einheit_Eluat_Quecksilber = option_Eluat_Quecksilber.get()
        Auswahl_Einheit_Eluat_Zink = option_Eluat_Zink.get()
        Auswahl_Einheit_Eluat_Cyanid = option_Eluat_Cyanid.get()
        Auswahl_Einheit_Eluat_Cyanidleichtf = option_Eluat_Cyanidleichtf.get()
        Auswahl_Einheit_Eluat_Phenolindex = option_Eluat_Phenolindex.get()
        Auswahl_Einheit_Eluat_Chlorid = option_Eluat_Chlorid.get()
        Auswahl_Einheit_Eluat_Sulfat = option_Eluat_Sulfat.get()
        Auswahl_Einheit_Eluat_DOC = option_Eluat_DOC.get()
        Auswahl_Einheit_Eluat_Fluorid = option_Eluat_Fluorid.get()
        Auswahl_Einheit_Eluat_Barium = option_Eluat_Barium.get()
        Auswahl_Einheit_Eluat_Molybdaen = option_Eluat_Molybdaen.get()
        Auswahl_Einheit_Eluat_Antimon = option_Eluat_Antimon.get()
        Auswahl_Einheit_Eluat_Selen = option_Eluat_Selen.get()
        Auswahl_Einheit_Eluat_GesGehaltGelStoffe = option_Eluat_GesGehaltGelStoffe.get()


        option_Feststoff_Arsen.set('mg/kg TM')
        option_Feststoff_Blei.set('mg/kg TM')
        option_Feststoff_Cadmium.set('mg/kg TM')
        option_Feststoff_Chromgesamt.set('mg/kg TM')
        option_Feststoff_Kupfer.set('mg/kg TM')
        option_Feststoff_Nickel.set('mg/kg TM')
        option_Feststoff_Quecksilber.set('mg/kg TM')
        option_Feststoff_Thallium.set('mg/kg TM')
        option_Feststoff_Zink.set('mg/kg TM')
        option_Feststoff_EOX.set('mg/kg TM')
        option_Feststoff_Kohlenwasserstoffe_C10C40.set('mg/kg TM')
        option_Feststoff_Kohlenwasserstoffe_C10C22.set('mg/kg TM')
        option_Feststoff_Cyanidegesamt.set('mg/kg TM')
        option_Feststoff_BTX.set('mg/kg TM')
        option_Feststoff_LHKW.set('mg/kg TM')
        option_Feststoff_PAK16.set('mg/kg TM')
        option_Feststoff_Benzoapyren.set('mg/kg TM')
        option_Feststoff_PCB6.set('mg/kg TM')
        option_Feststoff_PCB7.set('mg/kg TM')
        option_Feststoff_TOC.set('Masse-% TM')
        option_Feststoff_Gluehverlust.set('Masse-% TM')
        option_Feststoff_Saeureneutralisationskapazitaet.set('mmol/kg TM')
        option_Feststoff_LipophileStoffe.set('Masse-%')
        option_Eluat_pH.set('')
        option_Eluat_Leitf.set('μS/cm')
        option_Feststoff_Dioxine.set('ng/kg TM')
        option_Eluat_Arsen.set('μg/L')
        option_Eluat_Blei.set('μg/L')
        option_Eluat_Cadmium.set('μg/L')
        option_Eluat_Chromgesamt.set('μg/L')
        option_Eluat_Kupfer.set('μg/L')
        option_Eluat_Nickel.set('μg/L')
        option_Eluat_Quecksilber.set('μg/L')
        option_Eluat_Zink.set('μg/L')
        option_Eluat_Cyanid.set('μg/L')
        option_Eluat_Cyanidleichtf.set('μg/L')
        option_Eluat_Phenolindex.set('μg/L')
        option_Eluat_Chlorid.set('mg/L')
        option_Eluat_Sulfat.set('mg/L')
        option_Eluat_DOC.set('mg/L')
        option_Eluat_Fluorid.set('mg/L')
        option_Eluat_Barium.set('mg/L')
        option_Eluat_Molybdaen.set('μg/L')
        option_Eluat_Antimon.set('μg/L')
        option_Eluat_Selen.set('μg/L')
        option_Eluat_GesGehaltGelStoffe.set('mg/L')

        global dict_Auswahl_Einheiten
        dict_Auswahl_Einheiten = {"Arsen": "mg/kg TM", "Blei": "mg/kg TM", "Cadmium": "mg/kg TM",
                                  "Chrom gesamt": "mg/kg TM",
                                  "Kupfer": "mg/kg TM", "Nickel": "mg/kg TM", "Quecksilber": "mg/kg TM",
                                  "Thallium": "mg/kg TM",
                                  "Zink": "mg/kg TM", "EOX": "mg/kg TM", "Kohlenwasserstoffe (C10-C40)": "mg/kg TM",
                                  "Kohlenwasserstoffe (C10-C22)": "mg/kg TM",
                                  "Cyanide gesamt": "mg/kg TM", "BTX (BTEX)": "mg/kg TM", "LHKW": "mg/kg TM",
                                  "PAK16 (EPA)": "mg/kg TM",
                                  "Benzo(a)pyren": "mg/kg TM", "PCB6": "mg/kg TM", "PCB7": "mg/kg TM", "TOC": "Masse-% TM",
                                  "Gluehverlust": "Masse-% TM",
                                  "Saeureneutralisationskapazitaet": "mmol/kg TM",
                                  "Extrahierbare Lipohile Stoffe": "Masse-%", "Dioxine / Furane": "ng/kg TM"}

        global dict_Auswahl_Einheiten_Eluat
        dict_Auswahl_Einheiten_Eluat = {"pH-Wert": "", "Leitfähigkeit": "μS/cm", "Cyanid": "μg/L",
                                    "Cyanid (leicht freisetzbar)": "μg/L", "Phenolindex": "μg/L",
                                    "Chlorid": "mg/L", "Sulfat": "mg/L", "DOC": "mg/L", "Fluorid": "mg/L",
                                    "Barium": "mg/L", "Molybdaen": "μg/L", "Antimon": "μg/L",
                                    "Selen": "μg/L", "Gesamtgehalt an geloesten Feststoffen": "mg/L", "Arsen": "μg/L",
                                    "Blei": "μg/L", "Cadmium": "μg/L",
                                    "Chrom gesamt": "μg/L", "Kupfer": "μg/L", "Nickel": "μg/L",
                                    "Quecksilber": "μg/L", "Zink": "μg/L"}

        def Auswahl_Einheit_Feststoff_Arsen_def(Auswahl_Einheit_Feststoff_Arsen):
            dict_Auswahl_Einheiten["Arsen"] = Auswahl_Einheit_Feststoff_Arsen

        def Auswahl_Einheit_Feststoff_Blei_def(Auswahl_Einheit_Feststoff_Blei):
            dict_Auswahl_Einheiten["Blei"] = Auswahl_Einheit_Feststoff_Blei

        def Auswahl_Einheit_Feststoff_Cadmium_def(Auswahl_Einheit_Feststoff_Cadmium):
            dict_Auswahl_Einheiten["Cadmium"] = Auswahl_Einheit_Feststoff_Cadmium

        def Auswahl_Einheit_Feststoff_Chromgesamt_def(Auswahl_Einheit_Feststoff_Chromgesamt):
            dict_Auswahl_Einheiten["Chrom gesamt"] = Auswahl_Einheit_Feststoff_Chromgesamt

        def Auswahl_Einheit_Feststoff_Kupfer_def(Auswahl_Einheit_Feststoff_Kupfer):
            dict_Auswahl_Einheiten["Kupfer"] = Auswahl_Einheit_Feststoff_Kupfer

        def Auswahl_Einheit_Feststoff_Nickel_def(Auswahl_Einheit_Feststoff_Nickel):
            dict_Auswahl_Einheiten["Nickel"] = Auswahl_Einheit_Feststoff_Nickel

        def Auswahl_Einheit_Feststoff_Quecksilber_def(Auswahl_Einheit_Feststoff_Quecksilber):
            dict_Auswahl_Einheiten["Quecksilber"] = Auswahl_Einheit_Feststoff_Quecksilber

        def Auswahl_Einheit_Feststoff_Thallium_def(Auswahl_Einheit_Feststoff_Thallium):
            dict_Auswahl_Einheiten["Thallium"] = Auswahl_Einheit_Feststoff_Thallium

        def Auswahl_Einheit_Feststoff_Zink_def(Auswahl_Einheit_Feststoff_Zink):
            dict_Auswahl_Einheiten["Zink"] = Auswahl_Einheit_Feststoff_Zink

        def Auswahl_Einheit_Feststoff_EOX_def(Auswahl_Einheit_Feststoff_EOX):
            dict_Auswahl_Einheiten["EOX"] = Auswahl_Einheit_Feststoff_EOX

        def Auswahl_Einheit_Feststoff_Kohlenwasserstoffe_C10C40_def(
                Auswahl_Einheit_Feststoff_Kohlenwasserstoffe_C10C40):
            dict_Auswahl_Einheiten["Kohlenwasserstoffe (C10-C40)"] = Auswahl_Einheit_Feststoff_Kohlenwasserstoffe_C10C40

        def Auswahl_Einheit_Feststoff_Kohlenwasserstoffe_C10C22_def(
                Auswahl_Einheit_Feststoff_Kohlenwasserstoffe_C10C22):
            dict_Auswahl_Einheiten["Kohlenwasserstoffe (C10-C22)"] = Auswahl_Einheit_Feststoff_Kohlenwasserstoffe_C10C22

        def Auswahl_Einheit_Feststoff_Cyanidegesamt_def(Auswahl_Einheit_Feststoff_Cyanidegesamt):
            dict_Auswahl_Einheiten["Cyanide gesamt"] = Auswahl_Einheit_Feststoff_Cyanidegesamt

        def Auswahl_Einheit_Feststoff_BTX_def(Auswahl_Einheit_Feststoff_BTX):
            dict_Auswahl_Einheiten["BTX (BTEX)"] = Auswahl_Einheit_Feststoff_BTX

        def Auswahl_Einheit_Feststoff_LHKW_def(Auswahl_Einheit_Feststoff_LHKW):
            dict_Auswahl_Einheiten["LHKW"] = Auswahl_Einheit_Feststoff_LHKW

        def Auswahl_Einheit_Feststoff_PAK16_def(Auswahl_Einheit_Feststoff_PAK16):
            dict_Auswahl_Einheiten["PAK16 (EPA)"] = Auswahl_Einheit_Feststoff_PAK16

        def Auswahl_Einheit_Feststoff_Benzoapyren_def(Auswahl_Einheit_Feststoff_Benzoapyren):
            dict_Auswahl_Einheiten["Benzo(a)pyren"] = Auswahl_Einheit_Feststoff_Benzoapyren

        def Auswahl_Einheit_Feststoff_PCB6_def(Auswahl_Einheit_Feststoff_PCB6):
            dict_Auswahl_Einheiten["PCB6"] = Auswahl_Einheit_Feststoff_PCB6

        def Auswahl_Einheit_Feststoff_PCB7_def(Auswahl_Einheit_Feststoff_PCB7):
            dict_Auswahl_Einheiten["PCB7"] = Auswahl_Einheit_Feststoff_PCB7

        def Auswahl_Einheit_Feststoff_TOC_def(Auswahl_Einheit_Feststoff_TOC):
            dict_Auswahl_Einheiten["TOC"] = Auswahl_Einheit_Feststoff_TOC

        def Auswahl_Einheit_Feststoff_Gluehverlust_def(Auswahl_Einheit_Feststoff_Gluehverlust):
            dict_Auswahl_Einheiten["Gluehverlust"] = Auswahl_Einheit_Feststoff_Gluehverlust

        def Auswahl_Einheit_Feststoff_Saeureneutralisationskapazitaet_def(
                Auswahl_Einheit_Feststoff_Saeureneutralisationskapazitaet):
            dict_Auswahl_Einheiten["Saeureneutralisationskapazitaet"] = Auswahl_Einheit_Feststoff_Saeureneutralisationskapazitaet

        def Auswahl_Einheit_Feststoff_LipophileStoffe_def(Auswahl_Einheit_Feststoff_LipophileStoffe):
            dict_Auswahl_Einheiten["Extrahierbare Lipohile Stoffe"] = Auswahl_Einheit_Feststoff_LipophileStoffe

        def Auswahl_Einheit_Feststoff_Dioxine_def(Auswahl_Einheit_Feststoff_Dioxine):
            dict_Auswahl_Einheiten["Dioxine / Furane"] = Auswahl_Einheit_Feststoff_Dioxine

        def Auswahl_Einheit_Eluat_pH_def(Auswahl_Einheit_Eluat_pH):
            dict_Auswahl_Einheiten_Eluat["pH-Wert"] = Auswahl_Einheit_Eluat_pH

        def Auswahl_Einheit_Eluat_Leitf_def(Auswahl_Einheit_Eluat_Leitf):
            dict_Auswahl_Einheiten_Eluat["Leitfähigkeit"] = Auswahl_Einheit_Eluat_Leitf

        def Auswahl_Einheit_Eluat_Arsen_def(Auswahl_Einheit_Eluat_Arsen):
            dict_Auswahl_Einheiten_Eluat["Arsen"] = Auswahl_Einheit_Eluat_Arsen

        def Auswahl_Einheit_Eluat_Blei_def(Auswahl_Einheit_Eluat_Blei):
            dict_Auswahl_Einheiten_Eluat["Blei"] = Auswahl_Einheit_Eluat_Blei

        def Auswahl_Einheit_Eluat_Cadmium_def(Auswahl_Einheit_Eluat_Cadmium):
            dict_Auswahl_Einheiten_Eluat["Cadmium"] = Auswahl_Einheit_Eluat_Cadmium

        def Auswahl_Einheit_Eluat_Chromgesamt_def(Auswahl_Einheit_Eluat_Chromgesamt):
            dict_Auswahl_Einheiten_Eluat["Chrom gesamt"] = Auswahl_Einheit_Eluat_Chromgesamt

        def Auswahl_Einheit_Eluat_Kupfer_def(Auswahl_Einheit_Eluat_Kupfer):
            dict_Auswahl_Einheiten_Eluat["Kupfer"] = Auswahl_Einheit_Eluat_Kupfer

        def Auswahl_Einheit_Eluat_Nickel_def(Auswahl_Einheit_Eluat_Nickel):
            dict_Auswahl_Einheiten_Eluat["Nickel"] = Auswahl_Einheit_Eluat_Nickel

        def Auswahl_Einheit_Eluat_Quecksilber_def(Auswahl_Einheit_Eluat_Quecksilber):
            dict_Auswahl_Einheiten_Eluat["Quecksilber"] = Auswahl_Einheit_Eluat_Quecksilber

        def Auswahl_Einheit_Eluat_Zink_def(Auswahl_Einheit_Eluat_Zink):
            dict_Auswahl_Einheiten_Eluat["Zink"] = Auswahl_Einheit_Eluat_Zink

        def Auswahl_Einheit_Eluat_Cyanid_def(Auswahl_Einheit_Eluat_Cyanid):
            dict_Auswahl_Einheiten_Eluat["Cyanid"] = Auswahl_Einheit_Eluat_Cyanid

        def Auswahl_Einheit_Eluat_Cyanidleichtf_def(Auswahl_Einheit_Eluat_Cyanidleichtf):
            dict_Auswahl_Einheiten_Eluat["Cyanid (leicht freisetzbar)"] = Auswahl_Einheit_Eluat_Cyanidleichtf

        def Auswahl_Einheit_Eluat_Phenolindex_def(Auswahl_Einheit_Eluat_Phenolindex):
            dict_Auswahl_Einheiten_Eluat["Phenolindex"] = Auswahl_Einheit_Eluat_Phenolindex

        def Auswahl_Einheit_Eluat_Chlorid_def(Auswahl_Einheit_Eluat_Chlorid):
            dict_Auswahl_Einheiten_Eluat["Chlorid"] = Auswahl_Einheit_Eluat_Chlorid

        def Auswahl_Einheit_Eluat_Sulfat_def(Auswahl_Einheit_Eluat_Sulfat):
            dict_Auswahl_Einheiten_Eluat["Sulfat"] = Auswahl_Einheit_Eluat_Sulfat

        def Auswahl_Einheit_Eluat_DOC_def(Auswahl_Einheit_Eluat_DOC):
            dict_Auswahl_Einheiten_Eluat["DOC"] = Auswahl_Einheit_Eluat_DOC

        def Auswahl_Einheit_Eluat_Fluorid_def(Auswahl_Einheit_Eluat_Fluorid):
            dict_Auswahl_Einheiten_Eluat["Fluorid"] = Auswahl_Einheit_Eluat_Fluorid

        def Auswahl_Einheit_Eluat_Barium_def(Auswahl_Einheit_Eluat_Barium):
            dict_Auswahl_Einheiten_Eluat["Barium"] = Auswahl_Einheit_Eluat_Barium

        def Auswahl_Einheit_Eluat_Molybdaen_def(Auswahl_Einheit_Eluat_Molybdaen):
            dict_Auswahl_Einheiten_Eluat["Molybdaen"] = Auswahl_Einheit_Eluat_Molybdaen

        def Auswahl_Einheit_Eluat_Antimon_def(Auswahl_Einheit_Eluat_Antimon):
            dict_Auswahl_Einheiten_Eluat["Antimon"] = Auswahl_Einheit_Eluat_Antimon

        def Auswahl_Einheit_Eluat_Selen_def(Auswahl_Einheit_Eluat_Selen):
            dict_Auswahl_Einheiten_Eluat["Selen"] = Auswahl_Einheit_Eluat_Selen

        def Auswahl_Einheit_Eluat_GesGehaltGelStoffe_def(Auswahl_Einheit_Eluat_GesGehaltGelStoffe):
            dict_Auswahl_Einheiten_Eluat["Gesamtgehalt an geloesten Feststoffen"] = Auswahl_Einheit_Eluat_GesGehaltGelStoffe

        global Options_Feststoff_Arsen
        global Options_Feststoff_Blei
        global Options_Feststoff_Cadmium
        global Options_Feststoff_Chromgesamt
        global Options_Feststoff_Kupfer
        global Options_Feststoff_Nickel
        global Options_Feststoff_Quecksilber
        global Options_Feststoff_Thallium
        global Options_Feststoff_Zink
        global Options_Feststoff_EOX
        global Options_Feststoff_KWC1040
        global Options_Feststoff_KWC1022
        global Options_Feststoff_Cyanidgesamt
        global Options_Feststoff_BTX
        global Options_Feststoff_LHKW
        global Options_Feststoff_PAK16
        global Options_Feststoff_Benzoapyren
        global Options_Feststoff_PCB6
        global Options_Feststoff_PCB7
        global Options_Feststoff_TOC
        global Options_Feststoff_Gluehverlust
        global Options_Feststoff_Saeuren
        global Options_Feststoff_LipophileStoffe
        global Options_Feststoff_Dioxine
        global Options_Eluat_Arsen
        global Options_Eluat_Blei
        global Options_Eluat_Cadmium
        global Options_Eluat_Chromgesamt
        global Options_Eluat_Kupfer
        global Options_Eluat_Nickel
        global Options_Eluat_Quecksilber
        global Options_Eluat_Zink
        global Options_Eluat_Cyanid
        global Options_Eluat_Cyanidleichtf
        global Options_Eluat_Phenolindex
        global Options_Eluat_Chlorid
        global Options_Eluat_Sulfat
        global Options_Eluat_pH
        global Options_Eluat_Leitfaehigkeit
        global Options_Eluat_DOC
        global Options_Eluat_Fluorid
        global Options_Eluat_Barium
        global Options_Eluat_Molybdaen
        global Options_Eluat_Antimon
        global Options_Eluat_Selen
        global Options_Eluat_GesGehaltGelStoffe

        Options_Feststoff_Arsen = tkinter.OptionMenu(master, option_Feststoff_Arsen, "mg/kg TM", "μg/kg TM",
                                                     command=Auswahl_Einheit_Feststoff_Arsen_def)
        Options_Feststoff_Blei = tkinter.OptionMenu(master, option_Feststoff_Blei, "mg/kg TM", "μg/kg TM",
                                                    command=Auswahl_Einheit_Feststoff_Blei_def)
        Options_Feststoff_Cadmium = tkinter.OptionMenu(master, option_Feststoff_Cadmium, "mg/kg TM", "μg/kg TM",
                                                       command=Auswahl_Einheit_Feststoff_Cadmium_def)
        Options_Feststoff_Chromgesamt = tkinter.OptionMenu(master, option_Feststoff_Chromgesamt, "mg/kg TM", "μg/kg TM",
                                                           command=Auswahl_Einheit_Feststoff_Chromgesamt_def)
        Options_Feststoff_Kupfer = tkinter.OptionMenu(master, option_Feststoff_Kupfer, "mg/kg TM", "μg/kg TM",
                                                      command=Auswahl_Einheit_Feststoff_Kupfer_def)
        Options_Feststoff_Nickel = tkinter.OptionMenu(master, option_Feststoff_Nickel, "mg/kg TM", "μg/kg TM",
                                                      command=Auswahl_Einheit_Feststoff_Nickel_def)
        Options_Feststoff_Quecksilber = tkinter.OptionMenu(master, option_Feststoff_Quecksilber, "mg/kg TM", "μg/kg TM",
                                                           command=Auswahl_Einheit_Feststoff_Quecksilber_def)
        Options_Feststoff_Thallium = tkinter.OptionMenu(master, option_Feststoff_Thallium, "mg/kg TM", "μg/kg TM",
                                                        command=Auswahl_Einheit_Feststoff_Thallium_def)
        Options_Feststoff_Zink = tkinter.OptionMenu(master, option_Feststoff_Zink, "mg/kg TM", "μg/kg TM",
                                                    command=Auswahl_Einheit_Feststoff_Zink_def)
        Options_Feststoff_EOX = tkinter.OptionMenu(master, option_Feststoff_EOX, "mg/kg TM", "μg/kg TM",
                                                   command=Auswahl_Einheit_Feststoff_EOX_def)
        Options_Feststoff_KWC1040 = tkinter.OptionMenu(master, option_Feststoff_Kohlenwasserstoffe_C10C40, "mg/kg TM", "μg/kg TM",
                                                       command=Auswahl_Einheit_Feststoff_Kohlenwasserstoffe_C10C40_def)
        Options_Feststoff_KWC1022 = tkinter.OptionMenu(master, option_Feststoff_Kohlenwasserstoffe_C10C22, "mg/kg TM", "μg/kg TM",
                                                       command=Auswahl_Einheit_Feststoff_Kohlenwasserstoffe_C10C22_def)
        Options_Feststoff_Cyanidgesamt = tkinter.OptionMenu(master, option_Feststoff_Cyanidegesamt, "mg/kg TM", "μg/kg TM",
                                                            command=Auswahl_Einheit_Feststoff_Cyanidegesamt_def)
        Options_Feststoff_BTX = tkinter.OptionMenu(master, option_Feststoff_BTX, "mg/kg TM", "μg/kg TM",
                                                   command=Auswahl_Einheit_Feststoff_BTX_def)
        Options_Feststoff_LHKW = tkinter.OptionMenu(master, option_Feststoff_LHKW, "mg/kg TM", "μg/kg TM",
                                                    command=Auswahl_Einheit_Feststoff_LHKW_def)
        Options_Feststoff_PAK16 = tkinter.OptionMenu(master, option_Feststoff_PAK16, "mg/kg TM", "μg/kg TM",
                                                     command=Auswahl_Einheit_Feststoff_PAK16_def)
        Options_Feststoff_Benzoapyren = tkinter.OptionMenu(master, option_Feststoff_Benzoapyren, "mg/kg TM", "μg/kg TM",
                                                           command=Auswahl_Einheit_Feststoff_Benzoapyren_def)
        Options_Feststoff_PCB6 = tkinter.OptionMenu(master, option_Feststoff_PCB6, "mg/kg TM", "μg/kg TM",
                                                    command=Auswahl_Einheit_Feststoff_PCB6_def)
        Options_Feststoff_PCB7 = tkinter.OptionMenu(master, option_Feststoff_PCB7, "mg/kg TM", "μg/kg TM",
                                                    command=Auswahl_Einheit_Feststoff_PCB7_def)
        Options_Feststoff_TOC = tkinter.OptionMenu(master, option_Feststoff_TOC, "Masse-% TM",
                                                   command=Auswahl_Einheit_Feststoff_TOC_def)
        Options_Feststoff_Gluehverlust = tkinter.OptionMenu(master, option_Feststoff_Gluehverlust, "Masse-% TM",
                                                            command=Auswahl_Einheit_Feststoff_Gluehverlust_def)
        Options_Feststoff_Saeuren = tkinter.OptionMenu(master, option_Feststoff_Saeureneutralisationskapazitaet, "mmol/kg TM",
                                                       command=Auswahl_Einheit_Feststoff_Saeureneutralisationskapazitaet_def)
        Options_Feststoff_LipophileStoffe = tkinter.OptionMenu(master, option_Feststoff_LipophileStoffe, "Masse-%",
                                                               command=Auswahl_Einheit_Feststoff_LipophileStoffe_def)
        Options_Feststoff_Dioxine = tkinter.OptionMenu(master, option_Feststoff_Dioxine, "ng/kg TM","μg/kg TM","mg/kg TM",
                                                       command=Auswahl_Einheit_Feststoff_LipophileStoffe_def)
        Options_Eluat_Arsen = tkinter.OptionMenu(master, option_Eluat_Arsen, "μg/L","mg/L",
                                                 command=Auswahl_Einheit_Eluat_Arsen_def)
        Options_Eluat_Blei = tkinter.OptionMenu(master, option_Eluat_Blei, "μg/L","mg/L",
                                                command=Auswahl_Einheit_Eluat_Blei_def)
        Options_Eluat_Cadmium = tkinter.OptionMenu(master, option_Eluat_Cadmium, "μg/L","mg/L",
                                                   command=Auswahl_Einheit_Eluat_Cadmium_def)
        Options_Eluat_Chromgesamt = tkinter.OptionMenu(master, option_Eluat_Chromgesamt, "μg/L","mg/L",
                                                       command=Auswahl_Einheit_Eluat_Chromgesamt_def)
        Options_Eluat_Kupfer = tkinter.OptionMenu(master, option_Eluat_Kupfer, "μg/L","mg/L",
                                                  command=Auswahl_Einheit_Eluat_Kupfer_def)
        Options_Eluat_Nickel = tkinter.OptionMenu(master, option_Eluat_Nickel, "μg/L","mg/L",
                                                  command=Auswahl_Einheit_Eluat_Nickel_def)
        Options_Eluat_Quecksilber = tkinter.OptionMenu(master, option_Eluat_Quecksilber, "μg/L","mg/L",
                                                       command=Auswahl_Einheit_Eluat_Quecksilber_def)
        Options_Eluat_Zink = tkinter.OptionMenu(master, option_Eluat_Zink, "μg/L","mg/L",
                                                command=Auswahl_Einheit_Eluat_Zink_def)
        Options_Eluat_Cyanid = tkinter.OptionMenu(master, option_Eluat_Cyanid, "μg/L","mg/L",
                                                  command=Auswahl_Einheit_Eluat_Cyanid_def)
        Options_Eluat_Cyanidleichtf = tkinter.OptionMenu(master, option_Eluat_Cyanidleichtf, "μg/L","mg/L",
                                                         command=Auswahl_Einheit_Eluat_Cyanidleichtf_def)
        Options_Eluat_Phenolindex = tkinter.OptionMenu(master, option_Eluat_Phenolindex, "μg/L","mg/L",
                                                       command=Auswahl_Einheit_Eluat_Phenolindex_def)
        Options_Eluat_Chlorid = tkinter.OptionMenu(master, option_Eluat_Chlorid,"mg/L", "μg/L",
                                                   command=Auswahl_Einheit_Eluat_Chlorid_def)
        Options_Eluat_Sulfat = tkinter.OptionMenu(master, option_Eluat_Sulfat,"mg/L", "μg/L",
                                                  command=Auswahl_Einheit_Eluat_Sulfat_def)
        Options_Eluat_pH = tkinter.OptionMenu(master, option_Eluat_pH,"", "",
                                              command=Auswahl_Einheit_Eluat_pH_def)
        Options_Eluat_Leitfaehigkeit = tkinter.OptionMenu(master, option_Eluat_Leitf,"μS/cm",
                                                          command=Auswahl_Einheit_Eluat_Leitf_def)
        Options_Eluat_DOC = tkinter.OptionMenu(master, option_Eluat_DOC,"mg/L","μg/L",
                                               command=Auswahl_Einheit_Eluat_DOC_def)
        Options_Eluat_Fluorid = tkinter.OptionMenu(master, option_Eluat_Fluorid,"mg/L","μg/L",
                                                   command=Auswahl_Einheit_Eluat_Fluorid_def)
        Options_Eluat_Barium = tkinter.OptionMenu(master, option_Eluat_Barium,"mg/L","μg/L",
                                                  command=Auswahl_Einheit_Eluat_Barium_def)
        Options_Eluat_Molybdaen = tkinter.OptionMenu(master, option_Eluat_Molybdaen,"μg/L", "mg/L",
                                                     command=Auswahl_Einheit_Eluat_Molybdaen_def)
        Options_Eluat_Antimon = tkinter.OptionMenu(master, option_Eluat_Antimon,"μg/L", "mg/L",
                                                   command=Auswahl_Einheit_Eluat_Antimon_def)
        Options_Eluat_Selen = tkinter.OptionMenu(master, option_Eluat_Selen,"μg/L", "mg/L",
                                                 command=Auswahl_Einheit_Eluat_Selen_def)
        Options_Eluat_GesGehaltGelStoffe = tkinter.OptionMenu(master, option_Eluat_GesGehaltGelStoffe, "mg/L", "μg/L",
                                                              command=Auswahl_Einheit_Eluat_GesGehaltGelStoffe_def)

        Options_Feststoff_Arsen.grid(row=2, column=5)
        Options_Feststoff_Blei.grid(row=3, column=5)
        Options_Feststoff_Cadmium.grid(row=4, column=5)
        Options_Feststoff_Chromgesamt.grid(row=5, column=5)
        Options_Feststoff_Kupfer.grid(row=6, column=5)
        Options_Feststoff_Nickel.grid(row=7, column=5)
        Options_Feststoff_Quecksilber.grid(row=8, column=5)
        Options_Feststoff_Thallium.grid(row=9, column=5)
        Options_Feststoff_Zink.grid(row=10, column=5)
        Options_Feststoff_EOX.grid(row=11, column=5)
        Options_Feststoff_KWC1040.grid(row=12, column=5)
        Options_Feststoff_KWC1022.grid(row=13, column=5)
        Options_Feststoff_Cyanidgesamt.grid(row=14, column=5)
        Options_Feststoff_BTX.grid(row=15, column=5)
        Options_Feststoff_LHKW.grid(row=16, column=5)
        Options_Feststoff_PAK16.grid(row=17, column=5)
        Options_Feststoff_Benzoapyren.grid(row=18, column=5)
        Options_Feststoff_PCB6.grid(row=19, column=5)
        Options_Feststoff_PCB7.grid(row=20, column=5)
        Options_Feststoff_TOC.grid(row=21, column=5)
        Options_Feststoff_Gluehverlust.grid(row=22, column=5)
        Options_Feststoff_Saeuren.grid(row=23, column=5)
        Options_Feststoff_LipophileStoffe.grid(row=24, column=5)
        Options_Feststoff_Dioxine.grid(row=25, column=5)

        Options_Eluat_Arsen.grid(row=2, column=8)
        Options_Eluat_Blei.grid(row=3, column=8)
        Options_Eluat_Cadmium.grid(row=4, column=8)
        Options_Eluat_Chromgesamt.grid(row=5, column=8)
        Options_Eluat_Kupfer.grid(row=6, column=8)
        Options_Eluat_Nickel.grid(row=7, column=8)
        Options_Eluat_Quecksilber.grid(row=8, column=8)
        Options_Eluat_Zink.grid(row=9, column=8)
        Options_Eluat_Cyanid.grid(row=10, column=8)
        Options_Eluat_Cyanidleichtf.grid(row=11, column=8)
        Options_Eluat_Phenolindex.grid(row=12, column=8)
        Options_Eluat_Chlorid.grid(row=13, column=8)
        Options_Eluat_Sulfat.grid(row=14, column=8)
        Options_Eluat_pH.grid(row=15, column=8)
        Options_Eluat_Leitfaehigkeit.grid(row=16, column=8)
        Options_Eluat_DOC.grid(row=17, column=8)
        Options_Eluat_Fluorid.grid(row=18, column=8)
        Options_Eluat_Barium.grid(row=19, column=8)
        Options_Eluat_Molybdaen.grid(row=20, column=8)
        Options_Eluat_Antimon.grid(row=21, column=8)
        Options_Eluat_Selen.grid(row=22, column=8)
        Options_Eluat_GesGehaltGelStoffe.grid(row=23, column=8)

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

    def Zuruecksetzen(self):

        resultLabel.config(text = "", bg = "SystemButtonFace") # Labels löschen

        # Radiobuttons zurücksetzen
        var1.set(0)
        var2.set(0)
        var4.set(0)

        #Arsen.wert_TS = 0
        #Blei.wert_TS = 0
        #print(f"Arsenwertist: {Arsen.wert_TS}") ??????

        # Werte löschen
        entry1.delete(0, 'end')
        entry2.delete(0, 'end')
        entry3.delete(0, 'end')
        entry4.delete(0, 'end')
        entry5.delete(0, 'end')
        entry6.delete(0, 'end')
        entry8.delete(0, 'end')
        entry7.delete(0, 'end')
        entry9.delete(0, 'end')
        entry10.delete(0, 'end')
        entry11.delete(0, 'end')
        entry12.delete(0, 'end')
        entry13.delete(0, 'end')
        entry14.delete(0, 'end')
        entry15.delete(0, 'end')
        entry16.delete(0, 'end')
        entry17.delete(0, 'end')
        entry18.delete(0, 'end')
        entry19.delete(0, 'end')
        entry20.delete(0, 'end')
        entry21.delete(0, 'end')
        entry22.delete(0, 'end')
        entry23.delete(0, 'end')
        entry24.delete(0, 'end')
        entry25.delete(0, 'end')
        entry26.delete(0, 'end')
        entry27.delete(0, 'end')
        entry28.delete(0, 'end')
        entry29.delete(0, 'end')
        entry30.delete(0, 'end')
        entry31.delete(0, 'end')
        entry32.delete(0, 'end')
        entry33.delete(0, 'end')
        entry34.delete(0, 'end')
        entry35.delete(0, 'end')
        entry36.delete(0, 'end')
        entry37.delete(0, 'end')
        entry38.delete(0, 'end')
        entry39.delete(0, 'end')
        entry40.delete(0, 'end')
        entry41.delete(0, 'end')
        entry42.delete(0, 'end')
        entry43.delete(0, 'end')
        entry44.delete(0, 'end')
        entry45.delete(0, 'end')
        entry46.delete(0, 'end')

        # Einheitenfarben zurücksetzen
        Options_Feststoff_Arsen.config(fg = "BLACK")
        Options_Feststoff_Blei.config(fg = "BLACK")
        Options_Feststoff_Cadmium.config(fg = "BLACK")
        Options_Feststoff_EOX.config(fg = "BLACK")
        Options_Feststoff_KWC1040.config(fg = "BLACK")
        Options_Feststoff_KWC1022.config(fg = "BLACK")
        Options_Feststoff_Cyanidgesamt.config(fg = "BLACK")
        Options_Feststoff_BTX.config(fg = "BLACK")
        Options_Feststoff_LHKW.config(fg = "BLACK")
        Options_Feststoff_PAK16.config(fg = "BLACK")
        Options_Feststoff_Benzoapyren.config(fg = "BLACK")
        Options_Feststoff_PCB6.config(fg = "BLACK")
        Options_Feststoff_Chromgesamt.config(fg = "BLACK")
        Options_Feststoff_Kupfer.config(fg = "BLACK")
        Options_Feststoff_Nickel.config(fg = "BLACK")
        Options_Feststoff_Quecksilber.config(fg = "BLACK")
        Options_Feststoff_Thallium.config(fg = "BLACK")
        Options_Feststoff_Zink.config(fg = "BLACK")
        Options_Feststoff_TOC.config(fg = "BLACK")
        Options_Feststoff_PCB7.config(fg = "BLACK")
        Options_Feststoff_Gluehverlust.config(fg = "BLACK")
        Options_Feststoff_Saeuren.config(fg = "BLACK")
        Options_Feststoff_LipophileStoffe.config(fg = "BLACK")
        Options_Eluat_Leitfaehigkeit.config(fg = "BLACK")
        Options_Feststoff_Dioxine.config(fg = "BLACK")
        Options_Eluat_Arsen.config(fg = "BLACK")
        Options_Eluat_Blei.config(fg = "BLACK")
        Options_Eluat_Cadmium.config(fg = "BLACK")
        Options_Eluat_Chromgesamt.config(fg = "BLACK")
        Options_Eluat_Kupfer.config(fg = "BLACK")
        Options_Eluat_Nickel.config(fg = "BLACK")
        Options_Eluat_Quecksilber.config(fg = "BLACK")
        Options_Eluat_Zink.config(fg = "BLACK")
        Options_Eluat_Cyanid.config(fg = "BLACK")
        Options_Eluat_Cyanidleichtf.config(fg = "BLACK")
        Options_Eluat_Phenolindex.config(fg = "BLACK")
        Options_Eluat_Chlorid.config(fg = "BLACK")
        Options_Eluat_Sulfat.config(fg = "BLACK")
        Options_Eluat_DOC.config(fg = "BLACK")
        Options_Eluat_Fluorid.config(fg = "BLACK")
        Options_Eluat_Barium.config(fg = "BLACK")
        Options_Eluat_Molybdaen.config(fg = "BLACK")
        Options_Eluat_Antimon.config(fg = "BLACK")
        Options_Eluat_Selen.config(fg = "BLACK")
        Options_Eluat_GesGehaltGelStoffe.config(fg = "BLACK")

        # Listen leeren
        del Z0_TS[:]
        del Z0_Stern_TS[:]
        del Z1_TS[:]
        del Z2_TS[:]
        del Higher_Z2_TS[:]
        del LAGA_TS_Anmerkungen[:]
        del Z0_EL[:]
        del Z11_EL[:]
        del Z12_EL[:]
        del Z2_EL[:]
        del Higher_Z2_EL[:]
        del LAGA_EL_Anmerkungen[:]
        del BBSchG_Eingehalten[:]
        del BBSchG_Ueberschritten[:]
        del BBSchG_Vorsorgewerte_ueberschritten[:]
        del BBSchG_Anmerkungen[:]
        del DK0_TS[:]
        del DK1_TS[:]
        del DK2_TS[:]
        del DK3_TS[:]
        del Higher_DK3_TS[:]
        del REK_TS_Eingehalten[:]
        del GEO_TS_Eingehalten[:]
        del REK_TS_Ueberschritten[:]
        del GEO_TS_Ueberschritten[:]
        del DK0_EL[:]
        del DK1_EL[:]
        del DK2_EL[:]
        del DK3_EL[:]
        del Higher_DK3_EL[:]
        del REK_EL_Eingehalten[:]
        del GEO_EL_Eingehalten[:]
        del REK_EL_Ueberschritten[:]
        del GEO_EL_Ueberschritten[:]
        del REK_TS_Vorsorgewerte_ueberschritten[:]
        del REK_EL_Vorsorgewerte_ueberschritten[:]
        del GEO_TS_Vorsorgewerte_ueberschritten[:]
        del GEO_EL_Vorsorgewerte_ueberschritten[:]
        del DepV_Anmerkungen[:]
        del GefAbf_HH_SH_Eingehalten[:]
        del GefAbf_HH_SH_Ueberschritten[:]
        del GefAbf_HH_SH_Ueberschritten_Stoffe[:]
        del GefAbf_NDS_Eingehalten[:]
        del GefAbf_NDS_Ueberschritten[:]
        del GefAbf_NDS_Ueberschritten_Stoffe[:]
        del GefAbf_Anmerkungen[:]
        #del Bodenart[:]

    def Bodenart(self):
        global Bodenart_auswahl  # Die globale Variable kann ausserhalb der Funktion genutzt werden
        Bodenart_auswahl = var1.get()
        if Bodenart_auswahl == 1:
            Bodenart_auswahl = "Bodenart: Ton"
            print(Bodenart_auswahl)
        elif Bodenart_auswahl == 2:
            Bodenart_auswahl = "Bodenart: Schluff"
            print(Bodenart_auswahl)
        elif Bodenart_auswahl == 3:
            Bodenart_auswahl = "Bodenart: Sand"
            print(Bodenart_auswahl)

    def Bodenart_ergaenzung(self):
        global Bodenart_auswahl_ergaenzung
        Bodenart_auswahl_ergaenzung = var4.get()
        if Bodenart_auswahl_ergaenzung == 1:
            Bodenart_auswahl_ergaenzung = "Nicht stark schluffhaltiger Sand (<40%)"
            print(Bodenart_auswahl_ergaenzung)
        elif Bodenart_auswahl_ergaenzung == 2:
            Bodenart_auswahl_ergaenzung = "Stark schluffhaltiger Sand (40 bis <50%)"
            print(Bodenart_auswahl_ergaenzung)

    def Humus(self):
        global Humus
        Humus = var2.get()
        if Humus == 1:
            Humus = "Anteil Humus (TOC): >8% (>4%)"
            print(Humus)
        elif Humus == 2:
            Humus = "Anteil Humus (TOC): <=8% (<=4%)"
            print(Humus)

    def loadexcel(self):
        name = askopenfilename(filetypes=[('Excel', ('*.xls', '*.xlsx'))])
        self.excelfile = pd.read_excel(name)
        self.filename = name
        print(self.filename)
        excel_file = pd.read_excel(str(self.filename))
        print(excel_file)

        # https://www.geeksforgeeks.org/open-a-new-window-with-a-button-in-python-tkinter/
        newWindow = Toplevel(root)
        newWindow.title("")
        newWindow.geometry("350x200")
        newWindow.iconbitmap("C:/Users/Johannes/Documents/Programmieren/Python/Deklarationsanalyse/icon2.ico")
        Label(newWindow, text="Probenbezeichnung eingeben (exakt):").pack()

        entry47 = Entry(newWindow)
        entry47.pack()

        def extractdatafromexcelfile():
            # Werte und Einheiten-Farben löschen, falls diese schon einmal hineingeladen worden sind
            entry1.delete(0, 'end')
            entry2.delete(0, 'end')
            entry3.delete(0, 'end')
            entry4.delete(0, 'end')
            entry5.delete(0, 'end')
            entry6.delete(0, 'end')
            entry7.delete(0, 'end')
            entry8.delete(0, 'end')
            entry9.delete(0, 'end')
            entry10.delete(0, 'end')
            entry11.delete(0, 'end')
            entry12.delete(0, 'end')
            entry13.delete(0, 'end')
            entry14.delete(0, 'end')
            entry15.delete(0, 'end')
            entry16.delete(0, 'end')
            entry17.delete(0, 'end')
            entry18.delete(0, 'end')
            entry19.delete(0, 'end')
            entry20.delete(0, 'end')
            entry21.delete(0, 'end')
            entry22.delete(0, 'end')
            entry23.delete(0, 'end')
            entry24.delete(0, 'end')
            entry25.delete(0, 'end')
            entry26.delete(0, 'end')
            entry27.delete(0, 'end')
            entry28.delete(0, 'end')
            entry29.delete(0, 'end')
            entry30.delete(0, 'end')
            entry31.delete(0, 'end')
            entry32.delete(0, 'end')
            entry33.delete(0, 'end')
            entry34.delete(0, 'end')
            entry35.delete(0, 'end')
            entry36.delete(0, 'end')
            entry37.delete(0, 'end')
            entry38.delete(0, 'end')
            entry39.delete(0, 'end')
            entry40.delete(0, 'end')
            entry41.delete(0, 'end')
            entry42.delete(0, 'end')
            entry43.delete(0, 'end')
            entry44.delete(0, 'end')
            entry45.delete(0, 'end')
            entry46.delete(0, 'end')

            Options_Feststoff_Arsen.config(fg = "BLACK")
            Options_Feststoff_Blei.config(fg = "BLACK")
            Options_Feststoff_Cadmium.config(fg = "BLACK")
            Options_Feststoff_EOX.config(fg = "BLACK")
            Options_Feststoff_KWC1040.config(fg = "BLACK")
            Options_Feststoff_KWC1022.config(fg = "BLACK")
            Options_Feststoff_Cyanidgesamt.config(fg = "BLACK")
            Options_Feststoff_BTX.config(fg = "BLACK")
            Options_Feststoff_LHKW.config(fg = "BLACK")
            Options_Feststoff_PAK16.config(fg = "BLACK")
            Options_Feststoff_Benzoapyren.config(fg = "BLACK")
            Options_Feststoff_PCB6.config(fg = "BLACK")
            Options_Feststoff_Chromgesamt.config(fg = "BLACK")
            Options_Feststoff_Kupfer.config(fg = "BLACK")
            Options_Feststoff_Nickel.config(fg = "BLACK")
            Options_Feststoff_Quecksilber.config(fg = "BLACK")
            Options_Feststoff_Thallium.config(fg = "BLACK")
            Options_Feststoff_Zink.config(fg = "BLACK")
            Options_Feststoff_TOC.config(fg = "BLACK")
            Options_Feststoff_PCB7.config(fg = "BLACK")
            Options_Feststoff_Gluehverlust.config(fg = "BLACK")
            Options_Feststoff_Saeuren.config(fg = "BLACK")
            Options_Feststoff_LipophileStoffe.config(fg = "BLACK")
            Options_Eluat_Leitfaehigkeit.config(fg = "BLACK")
            Options_Feststoff_Dioxine.config(fg = "BLACK")
            Options_Eluat_Arsen.config(fg = "BLACK")
            Options_Eluat_Blei.config(fg = "BLACK")
            Options_Eluat_Cadmium.config(fg = "BLACK")
            Options_Eluat_Chromgesamt.config(fg = "BLACK")
            Options_Eluat_Kupfer.config(fg = "BLACK")
            Options_Eluat_Nickel.config(fg = "BLACK")
            Options_Eluat_Quecksilber.config(fg = "BLACK")
            Options_Eluat_Zink.config(fg = "BLACK")
            Options_Eluat_Cyanid.config(fg = "BLACK")
            Options_Eluat_Cyanidleichtf.config(fg = "BLACK")
            Options_Eluat_Phenolindex.config(fg = "BLACK")
            Options_Eluat_Chlorid.config(fg = "BLACK")
            Options_Eluat_Sulfat.config(fg = "BLACK")
            Options_Eluat_DOC.config(fg = "BLACK")
            Options_Eluat_Fluorid.config(fg = "BLACK")
            Options_Eluat_Barium.config(fg = "BLACK")
            Options_Eluat_Molybdaen.config(fg = "BLACK")
            Options_Eluat_Antimon.config(fg = "BLACK")
            Options_Eluat_Selen.config(fg = "BLACK")
            Options_Eluat_GesGehaltGelStoffe.config(fg = "BLACK")

            # Create dictionaries with concentrations
            ### Fuer Feststoffe
            Analysenergebnisse_index = excel_file[excel_file.iloc[:, 0] == "Analysenergebnisse"].index.values
            startrow_names = int(Analysenergebnisse_index[0] + 1)

            Eluat_index = excel_file[excel_file.iloc[:, 0] == "Eluat"].index.values
            endrow_names = int(Eluat_index[0])

            Einheiten_index = excel_file[excel_file.iloc[:, 1] == "Einheit"].index.values
            startrow_einheiten = int(Einheiten_index[0] + 1)

            Probenbezeichnung_index = excel_file[excel_file.iloc[:, 0] == "Probenbezeichnung"].index.values
            startcolumn_values = excel_file.loc[[int(Probenbezeichnung_index[0])]]

            Bodenart_index = excel_file[excel_file.iloc[:, 0] == "Zuordnung gemäß"].index.values
            #Bodenartcolumn_values = int(Bodenart_index[0] + 1)
            print(" Bodenart_index:   ",  Bodenart_index)

            a = startcolumn_values.values.tolist()
            flat_list_a = [item for sublist in a for item in sublist]
            global resultLabel2
            resultLabel2 = Label(newWindow, text="Import erfolgreich")
            resultLabel3 = Label(newWindow, text="Bitte eine gültige Probenbezeichnung eingeben")

            if entry47.get() in flat_list_a:  # Wenn Eingabe in Liste mit gueltiger Probenbezeichnung, dann...
                b = entry47.get()

                # Import Probename
                #entry0 = tkinter.StringVar(root)
                #entry0.set("test")

                column_values = flat_list_a.index(b)  # final column index with the desired values

                Liste_Stoffnamen_TS = excel_file.iloc[startrow_names:endrow_names,
                                      0].values.tolist()  # Stoffnamen Feststoffe
                Liste_Stoffnamen_EL = excel_file.iloc[endrow_names + 1:, 0].values.tolist()  # Stoffnamen Eluat
                Liste_Gehalte_TS = excel_file.iloc[startrow_names:endrow_names,
                                   column_values].values.tolist()  # Gehalte (Werte) Feststoff
                Liste_Gehalte_EL = excel_file.iloc[endrow_names + 1:,
                                   column_values].values.tolist()  # Gehalte (Werte) Eluat

                # Remove/replace characters which are not wished in the column (Feststoff)
                rep1, rep2, rep3, rep4, rep5, rep6 = "-", " ", "Z0", "Z1", ">Z2", "Z2"
                Liste_Gehalte_TS_clean1 = [str(elem).replace(rep1, '') for elem in Liste_Gehalte_TS]
                Liste_Gehalte_TS_clean2 = [str(elem).replace(rep2, '') for elem in Liste_Gehalte_TS_clean1]
                Liste_Gehalte_TS_clean3 = [str(elem).replace(rep3, '') for elem in Liste_Gehalte_TS_clean2]
                Liste_Gehalte_TS_clean4 = [str(elem).replace(rep4, '') for elem in Liste_Gehalte_TS_clean3]
                Liste_Gehalte_TS_clean5 = [str(elem).replace(rep5, '') for elem in Liste_Gehalte_TS_clean4]
                Liste_Gehalte_TS_clean6 = [str(elem).replace(rep6, '') for elem in Liste_Gehalte_TS_clean5]

                # Remove/replace characters which are not wished in the column (Eluat)
                rep7, rep8, rep9, rep10, rep11, rep12, rep13, rep14 = "-", " ", "Z0", "Z1", "Z1.1", "Z1.2", ">Z2", "Z2"
                Liste_Gehalte_EL_clean7 = [str(elem).replace(rep7, '') for elem in Liste_Gehalte_EL]
                Liste_Gehalte_EL_clean8 = [str(elem).replace(rep8, '') for elem in Liste_Gehalte_EL_clean7]
                Liste_Gehalte_EL_clean9 = [str(elem).replace(rep9, '') for elem in Liste_Gehalte_EL_clean8]
                Liste_Gehalte_EL_clean10 = [str(elem).replace(rep10, '') for elem in Liste_Gehalte_EL_clean9]
                Liste_Gehalte_EL_clean11 = [str(elem).replace(rep11, '') for elem in Liste_Gehalte_EL_clean10]
                Liste_Gehalte_EL_clean12 = [str(elem).replace(rep12, '') for elem in Liste_Gehalte_EL_clean11]
                Liste_Gehalte_EL_clean13 = [str(elem).replace(rep13, '') for elem in Liste_Gehalte_EL_clean12]
                Liste_Gehalte_EL_clean14 = [str(elem).replace(rep14, '') for elem in Liste_Gehalte_EL_clean13]

                Liste_Einheiten = excel_file.iloc[startrow_einheiten:, 1].values.tolist()  # Einheiten Feststoff und Eluat
                Liste_Einheiten_TS = excel_file.iloc[startrow_einheiten:endrow_names, 1].values.tolist()  # Einheiten Feststoff
                Liste_Einheiten_EL = excel_file.iloc[endrow_names + 1:, 1].values.tolist()  # Einheiten Eluat

                Zip_Gehalte_TS = zip(Liste_Stoffnamen_TS, Liste_Gehalte_TS_clean6)
                Zip_Gehalte_EL = zip(Liste_Stoffnamen_EL, Liste_Gehalte_EL_clean14)

                Zip_Einheiten_TS = zip(Liste_Stoffnamen_TS, Liste_Einheiten_TS)
                Zip_Einheiten_EL = zip(Liste_Stoffnamen_EL, Liste_Einheiten_EL)
                Dictionary_Gehalte_TS = dict(Zip_Gehalte_TS)
                Dictionary_Gehalte_EL = dict(Zip_Gehalte_EL)
                Dictionary_Einheiten_TS = dict(Zip_Einheiten_TS)
                Dictionary_Einheiten_EL = dict(Zip_Einheiten_EL)
                #print("Dictionary_Einheiten_EL:",Dictionary_Einheiten_EL)

                resultLabel2.pack()

                # Automatically import values into the entries

                for i in Dictionary_Gehalte_TS:
                    DictStoffnamenGUI_TS = {"Arsen": entry1, "Blei": entry2, "Cadmium": entry3, "Chrom ges.": entry4,
                                            "Kupfer": entry5,
                                            "Nickel": entry6, "Quecksilber": entry7, "Thallium": entry8, "Zink": entry9,
                                            "EOX": entry10, "Kohlenwasserstoffe": entry11,
                                            "mobiler Anteil bis C22": entry12,
                                            "Cyanid ges.": entry13, "Summe BTEX": entry14, "Summe LHKW": entry15,
                                            "Summe PAK (EPA)": entry16, "Benzo(a)pyren": entry17,
                                            "PCB Summe 6 Kongenere": entry18,
                                            "TOC": entry20}
                    DictStoffnamenGUI_TS_keys = DictStoffnamenGUI_TS.keys()
                    if i in DictStoffnamenGUI_TS_keys:  # DictStoffnamenGUI_TS muss als key entry haben (entry34 zb.)
                        DictStoffnamenGUI_TS[i].insert(0, Dictionary_Gehalte_TS[i])

                for i in Dictionary_Gehalte_EL:
                    DictStoffnamenGUI_EL = {"Arsen": entry25, "Blei": entry26, "Cadmium": entry27,
                                            "Chrom ges.": entry28, "Kupfer": entry29,
                                            "Nickel": entry30, "Quecksilber": entry31, "Zink": entry32,
                                            "Cyanid ges.": entry33, "Cyanid l. freis. (CFA)": entry34,
                                            "Phenolindex": entry35, "Chlorid": entry36, "Sulfat": entry37,
                                            "pH-Wert": entry38,
                                            "Leitfähigkeit": entry39, "DOC": entry40, "Fluorid": entry41,
                                            "Barium": entry42,
                                            "Molybdän": entry43, "Antimon": entry44, "Selen": entry45,
                                            "Säureneutralisationskapazität": entry22, "PCB Summe 7 Kongenere": entry19,
                                            "Glühverlust": entry21,
                                            "Lipophile Stoffe": entry23, "Dioxine": entry24,
                                            "Ges.-Gehalt an gel. Feststoffen": entry46}
                    DictStoffnamenGUI_EL_keys = DictStoffnamenGUI_EL.keys()
                    if i in DictStoffnamenGUI_EL_keys:  # DictStoffnamenGUI_EL muss als key entry haben (entry34 zb.)
                        DictStoffnamenGUI_EL[i].insert(0, Dictionary_Gehalte_EL[i])

                # Einheiten auswählen
                    #### Hier weitermachen, robust machen -> wenn Stoff nicht da seinsollte, dann sollte es nicht crashen
                    list_MoeglicheEinheiten = ["mg/kg TM", "µg/kg TM", "ng/kg TM", "Masse-% TM", "Masse-%", "µS/cm",'', "µg/L", "mg/L", "mmol/kg TM"]
                    list_MoeglicheEinheiten_Stoffe = ["Arsen", "Blei", "Cadmium",'EOX','Kohlenwasserstoffe','mobiler Anteil bis C22','Cyanid ges.','Summe BTEX'
                                                          ,'Summe LHKW','Summe PAK (EPA)','Benzo(a)pyren','PCB Summe 6 Kongenere'
                                                          ,'Chrom ges.','Kupfer','Nickel','Quecksilber','Thallium','Zink','TOC']
                    # Prüfen ob der Stoff in dem Excel-Sheet existiert und ob die Einheiten in korrekt sind (Liste), wenn alles OK dann .set Einheiten
                    if "Arsen" in Dictionary_Einheiten_TS:
                        if Dictionary_Einheiten_TS["Arsen"] in list_MoeglicheEinheiten:
                            option_Feststoff_Arsen.set(Dictionary_Einheiten_TS["Arsen"])
                            Options_Feststoff_Arsen.config(fg = "GREEN")
                        else:
                            Options_Feststoff_Arsen.config(fg = "RED")
                    else:
                        Options_Feststoff_Arsen.config(fg = "RED")

                    if "Blei" in Dictionary_Einheiten_TS:
                        if Dictionary_Einheiten_TS["Blei"] in list_MoeglicheEinheiten:
                            option_Feststoff_Blei.set(Dictionary_Einheiten_TS["Blei"])
                            Options_Feststoff_Blei.config(fg = "GREEN")
                        else:
                            Options_Feststoff_Blei.config(fg = "RED")
                    else:
                        Options_Feststoff_Blei.config(fg = "RED")

                    if "Cadmium" in Dictionary_Einheiten_TS:
                        if Dictionary_Einheiten_TS["Cadmium"] in list_MoeglicheEinheiten:
                            option_Feststoff_Cadmium.set(Dictionary_Einheiten_TS["Cadmium"])
                            Options_Feststoff_Cadmium.config(fg = "GREEN")
                        else:
                            Options_Feststoff_Cadmium.config(fg = "RED")
                    else:
                        Options_Feststoff_Cadmium.config(fg = "RED")

                    if "EOX" in Dictionary_Einheiten_TS:
                        if Dictionary_Einheiten_TS["EOX"] in list_MoeglicheEinheiten:
                            option_Feststoff_EOX.set(Dictionary_Einheiten_TS["EOX"])
                            Options_Feststoff_EOX.config(fg = "GREEN")
                        else:
                            Options_Feststoff_EOX.config(fg = "RED")
                    else:
                        Options_Feststoff_EOX.config(fg = "RED")

                    if "Kohlenwasserstoffe" in Dictionary_Einheiten_TS:
                        if Dictionary_Einheiten_TS["Kohlenwasserstoffe"] in list_MoeglicheEinheiten:
                            option_Feststoff_Kohlenwasserstoffe_C10C40.set(Dictionary_Einheiten_TS["Kohlenwasserstoffe"])
                            Options_Feststoff_KWC1040.config(fg = "GREEN")
                        else:
                            Options_Feststoff_KWC1040.config(fg = "RED")
                    else:
                        Options_Feststoff_KWC1040.config(fg = "RED")

                    if "mobiler Anteil bis C22" in Dictionary_Einheiten_TS:
                        if Dictionary_Einheiten_TS["mobiler Anteil bis C22"] in list_MoeglicheEinheiten:
                            option_Feststoff_Kohlenwasserstoffe_C10C22.set(Dictionary_Einheiten_TS["mobiler Anteil bis C22"])
                            Options_Feststoff_KWC1022.config(fg = "GREEN")
                        else:
                            Options_Feststoff_KWC1022.config(fg = "RED")
                    else:
                        Options_Feststoff_KWC1022.config(fg = "RED")

                    if "Cyanid ges." in Dictionary_Einheiten_TS:
                        if Dictionary_Einheiten_TS["Cyanid ges."] in list_MoeglicheEinheiten:
                            option_Feststoff_Cyanidegesamt.set(Dictionary_Einheiten_TS["Cyanid ges."])
                            Options_Feststoff_Cyanidgesamt.config(fg = "GREEN")
                        else:
                            Options_Feststoff_Cyanidgesamt.config(fg = "RED")
                    else:
                        Options_Feststoff_Cyanidgesamt.config(fg = "RED")

                    if "Summe BTEX" in Dictionary_Einheiten_TS:
                        if Dictionary_Einheiten_TS["Summe BTEX"] in list_MoeglicheEinheiten:
                            option_Feststoff_BTX.set(Dictionary_Einheiten_TS["Summe BTEX"])
                            Options_Feststoff_BTX.config(fg = "GREEN")
                        else:
                            Options_Feststoff_BTX.config(fg = "RED")
                    else:
                        Options_Feststoff_BTX.config(fg = "RED")

                    if "Summe LHKW" in Dictionary_Einheiten_TS:
                        if Dictionary_Einheiten_TS["Summe LHKW"] in list_MoeglicheEinheiten:
                            option_Feststoff_LHKW.set(Dictionary_Einheiten_TS["Summe LHKW"])
                            Options_Feststoff_LHKW.config(fg = "GREEN")
                        else:
                            Options_Feststoff_LHKW.config(fg = "RED")
                    else:
                        Options_Feststoff_LHKW.config(fg = "RED")

                    if "Summe PAK (EPA)" in Dictionary_Einheiten_TS:
                        if Dictionary_Einheiten_TS["Summe PAK (EPA)"] in list_MoeglicheEinheiten:
                            option_Feststoff_PAK16.set(Dictionary_Einheiten_TS["Summe PAK (EPA)"])
                            Options_Feststoff_PAK16.config(fg = "GREEN")
                        else:
                            Options_Feststoff_PAK16.config(fg = "RED")
                    else:
                        Options_Feststoff_PAK16.config(fg = "RED")

                    if "Benzo(a)pyren" in Dictionary_Einheiten_TS:
                        if Dictionary_Einheiten_TS["Benzo(a)pyren"] in list_MoeglicheEinheiten:
                            option_Feststoff_Benzoapyren.set(Dictionary_Einheiten_TS["Benzo(a)pyren"])
                            Options_Feststoff_Benzoapyren.config(fg = "GREEN")
                        else:
                            Options_Feststoff_Benzoapyren.config(fg = "RED")
                    else:
                        Options_Feststoff_Benzoapyren.config(fg = "RED")

                    if "PCB Summe 6 Kongenere" in Dictionary_Einheiten_TS:
                        if Dictionary_Einheiten_TS["PCB Summe 6 Kongenere"] in list_MoeglicheEinheiten:
                            option_Feststoff_PCB6.set(Dictionary_Einheiten_TS["PCB Summe 6 Kongenere"])
                            Options_Feststoff_PCB6.config(fg = "GREEN")
                        else:
                            Options_Feststoff_PCB6.config(fg = "RED")
                    else:
                        Options_Feststoff_PCB6.config(fg = "RED")

                    if "Chrom ges." in Dictionary_Einheiten_TS:
                        if Dictionary_Einheiten_TS["Chrom ges."] in list_MoeglicheEinheiten:
                            option_Feststoff_Chromgesamt.set(Dictionary_Einheiten_TS["Chrom ges."])
                            Options_Feststoff_Chromgesamt.config(fg = "GREEN")
                        else:
                            Options_Feststoff_Chromgesamt.config(fg = "RED")
                    else:
                        Options_Feststoff_Chromgesamt.config(fg = "RED")

                    if "Kupfer" in Dictionary_Einheiten_TS:
                        if Dictionary_Einheiten_TS["Kupfer"] in list_MoeglicheEinheiten:
                            option_Feststoff_Kupfer.set(Dictionary_Einheiten_TS["Kupfer"])
                            Options_Feststoff_Kupfer.config(fg = "GREEN")
                        else:
                            Options_Feststoff_Kupfer.config(fg = "RED")
                    else:
                        Options_Feststoff_Kupfer.config(fg = "RED")

                    if "Nickel" in Dictionary_Einheiten_TS:
                        if Dictionary_Einheiten_TS["Nickel"] in list_MoeglicheEinheiten:
                            option_Feststoff_Nickel.set(Dictionary_Einheiten_TS["Nickel"])
                            Options_Feststoff_Nickel.config(fg = "GREEN")
                        else:
                            Options_Feststoff_Nickel.config(fg = "RED")
                    else:
                        Options_Feststoff_Nickel.config(fg = "RED")

                    if "Quecksilber" in Dictionary_Einheiten_TS:
                        if Dictionary_Einheiten_TS["Quecksilber"] in list_MoeglicheEinheiten:
                            option_Feststoff_Quecksilber.set(Dictionary_Einheiten_TS["Quecksilber"])
                            Options_Feststoff_Quecksilber.config(fg = "GREEN")
                        else:
                            Options_Feststoff_Quecksilber.config(fg = "RED")
                    else:
                        Options_Feststoff_Quecksilber.config(fg = "RED")

                    if "Thallium" in Dictionary_Einheiten_TS:
                        if Dictionary_Einheiten_TS["Thallium"] in list_MoeglicheEinheiten:
                            option_Feststoff_Thallium.set(Dictionary_Einheiten_TS["Thallium"])
                            Options_Feststoff_Thallium.config(fg = "GREEN")
                        else:
                            Options_Feststoff_Thallium.config(fg = "RED")
                    else:
                        Options_Feststoff_Thallium.config(fg = "RED")

                    if "Zink" in Dictionary_Einheiten_TS:
                        if Dictionary_Einheiten_TS["Zink"] in list_MoeglicheEinheiten:
                            option_Feststoff_Zink.set(Dictionary_Einheiten_TS["Zink"])
                            Options_Feststoff_Zink.config(fg = "GREEN")
                        else:
                            Options_Feststoff_Zink.config(fg = "RED")
                    else:
                        Options_Feststoff_Zink.config(fg = "RED")

                    if "TOC" in Dictionary_Einheiten_TS:
                        if Dictionary_Einheiten_TS["TOC"] in list_MoeglicheEinheiten:
                            option_Feststoff_TOC.set(Dictionary_Einheiten_TS["TOC"])
                            Options_Feststoff_TOC.config(fg = "GREEN")
                        else:
                            Options_Feststoff_TOC.config(fg = "RED")
                    else:
                        Options_Feststoff_TOC.config(fg = "RED")

                    if "PCB Summe 7 Kongenere" in Dictionary_Einheiten_EL:
                        if Dictionary_Einheiten_EL["PCB Summe 7 Kongenere"] in list_MoeglicheEinheiten:
                            option_Feststoff_PCB7.set(Dictionary_Einheiten_EL["PCB Summe 7 Kongenere"])
                            Options_Feststoff_PCB7.config(fg = "GREEN")
                        else:
                            Options_Feststoff_PCB7.config(fg = "RED")
                    else:
                        Options_Feststoff_PCB7.config(fg = "RED")

                    if "Glühverlust" in Dictionary_Einheiten_EL:
                        if Dictionary_Einheiten_EL["Glühverlust"] in list_MoeglicheEinheiten:
                            option_Feststoff_Gluehverlust.set(Dictionary_Einheiten_EL["Glühverlust"])
                            Options_Feststoff_Gluehverlust.config(fg = "GREEN")
                        else:
                            Options_Feststoff_Gluehverlust.config(fg = "RED")
                    else:
                        Options_Feststoff_Gluehverlust.config(fg = "RED")

                    if "Säureneutralisationskapazität" in Dictionary_Einheiten_EL:
                        if Dictionary_Einheiten_EL["Säureneutralisationskapazität"] in list_MoeglicheEinheiten:
                            option_Feststoff_Saeureneutralisationskapazitaet.set(Dictionary_Einheiten_EL["Säureneutralisationskapazität"])
                            Options_Feststoff_Saeuren.config(fg = "GREEN")
                        else:
                            Options_Feststoff_Saeuren.config(fg = "RED")
                    else:
                        Options_Feststoff_Saeuren.config(fg = "RED")

                    print("Lipohile Stoffe", Dictionary_Einheiten_EL["Leitfähigkeit"])
                    if "Lipophile Stoffe" in Dictionary_Einheiten_EL:
                        if Dictionary_Einheiten_EL["Lipophile Stoffe"] in list_MoeglicheEinheiten:
                            option_Feststoff_LipophileStoffe.set(Dictionary_Einheiten_EL["Lipophile Stoffe"])
                            Options_Feststoff_LipophileStoffe.config(fg = "GREEN")
                        else:
                            Options_Feststoff_LipophileStoffe.config(fg = "RED")
                    else:
                        Options_Feststoff_LipophileStoffe.config(fg = "RED")

                    print("Leitf", Dictionary_Einheiten_EL["Leitfähigkeit"])
                    print(Dictionary_Einheiten_EL)
                    if "Leitfähigkeit" in Dictionary_Einheiten_EL:
                        if Dictionary_Einheiten_EL["Leitfähigkeit"] in list_MoeglicheEinheiten:
                            option_Eluat_Leitf.set(Dictionary_Einheiten_EL["Leitfähigkeit"])
                            Options_Eluat_Leitfaehigkeit.config(fg = "GREEN")
                        else:
                            Options_Eluat_Leitfaehigkeit.config(fg = "RED")
                    else:
                        Options_Eluat_Leitfaehigkeit.config(fg = "RED")

                    if "Dioxine" in Dictionary_Einheiten_EL:
                        if Dictionary_Einheiten_EL["Dioxine"] in list_MoeglicheEinheiten:
                            option_Feststoff_Dioxine.set(Dictionary_Einheiten_EL["Dioxine"])
                            Options_Feststoff_Dioxine.config(fg = "GREEN")
                        else:
                            Options_Feststoff_Dioxine.config(fg = "RED")
                    else:
                        Options_Feststoff_Dioxine.config(fg = "RED")

                    if "Arsen" in Dictionary_Einheiten_EL:
                        if Dictionary_Einheiten_EL["Arsen"] in list_MoeglicheEinheiten:
                            option_Eluat_Arsen.set(Dictionary_Einheiten_EL["Arsen"])
                            Options_Eluat_Arsen.config(fg = "GREEN")
                        else:
                            Options_Eluat_Arsen.config(fg = "RED")
                    else:
                        Options_Eluat_Arsen.config(fg = "RED")

                    if "Blei" in Dictionary_Einheiten_EL:
                        if Dictionary_Einheiten_EL["Blei"] in list_MoeglicheEinheiten:
                            option_Eluat_Blei.set(Dictionary_Einheiten_EL["Blei"])
                            Options_Eluat_Blei.config(fg = "GREEN")
                        else:
                            Options_Eluat_Blei.config(fg = "RED")
                    else:
                        Options_Eluat_Blei.config(fg = "RED")

                    if "Cadmium" in Dictionary_Einheiten_EL:
                        if Dictionary_Einheiten_EL["Cadmium"] in list_MoeglicheEinheiten:
                            option_Eluat_Cadmium.set(Dictionary_Einheiten_EL["Cadmium"])
                            Options_Eluat_Cadmium.config(fg = "GREEN")
                        else:
                            Options_Eluat_Cadmium.config(fg = "RED")
                    else:
                        Options_Eluat_Cadmium.config(fg = "RED")

                    if "Chrom ges." in Dictionary_Einheiten_EL:
                        if Dictionary_Einheiten_EL["Chrom ges."] in list_MoeglicheEinheiten:
                            option_Eluat_Chromgesamt.set(Dictionary_Einheiten_EL["Chrom ges."])
                            Options_Eluat_Chromgesamt.config(fg = "GREEN")
                        else:
                            Options_Eluat_Chromgesamt.config(fg = "RED")
                    else:
                        Options_Eluat_Chromgesamt.config(fg = "RED")

                    if "Kupfer" in Dictionary_Einheiten_EL:
                        if Dictionary_Einheiten_EL["Kupfer"] in list_MoeglicheEinheiten:
                            option_Eluat_Kupfer.set(Dictionary_Einheiten_EL["Kupfer"])
                            Options_Eluat_Kupfer.config(fg = "GREEN")
                        else:
                            Options_Eluat_Kupfer.config(fg = "RED")
                    else:
                        Options_Eluat_Kupfer.config(fg = "RED")

                    if "Nickel" in Dictionary_Einheiten_EL:
                        if Dictionary_Einheiten_EL["Nickel"] in list_MoeglicheEinheiten:
                            option_Eluat_Nickel.set(Dictionary_Einheiten_EL["Nickel"])
                            Options_Eluat_Nickel.config(fg = "GREEN")
                        else:
                            Options_Eluat_Nickel.config(fg = "RED")
                    else:
                        Options_Eluat_Nickel.config(fg = "RED")

                    if "Quecksilber" in Dictionary_Einheiten_EL:
                        if Dictionary_Einheiten_EL["Quecksilber"] in list_MoeglicheEinheiten:
                            option_Eluat_Quecksilber.set(Dictionary_Einheiten_EL["Quecksilber"])
                            Options_Eluat_Quecksilber.config(fg = "GREEN")
                        else:
                            Options_Eluat_Quecksilber.config(fg = "RED")
                    else:
                        Options_Eluat_Quecksilber.config(fg = "RED")

                    if "Zink" in Dictionary_Einheiten_EL:
                        if Dictionary_Einheiten_EL["Zink"] in list_MoeglicheEinheiten:
                            option_Eluat_Zink.set(Dictionary_Einheiten_EL["Zink"])
                            Options_Eluat_Zink.config(fg = "GREEN")
                        else:
                            Options_Eluat_Zink.config(fg = "RED")
                    else:
                        Options_Eluat_Zink.config(fg = "RED")

                    if "Cyanid ges." in Dictionary_Einheiten_EL:
                        if Dictionary_Einheiten_EL["Cyanid ges."] in list_MoeglicheEinheiten:
                            option_Eluat_Cyanid.set(Dictionary_Einheiten_EL["Cyanid ges."])
                            Options_Eluat_Cyanid.config(fg = "GREEN")
                        else:
                            Options_Eluat_Cyanid.config(fg = "RED")
                    else:
                        Options_Eluat_Cyanid.config(fg = "RED")

                    if "Cyanid l. freis. (CFA)" in Dictionary_Einheiten_EL:
                        if Dictionary_Einheiten_EL["Cyanid l. freis. (CFA)"] in list_MoeglicheEinheiten:
                            option_Eluat_Cyanidleichtf.set(Dictionary_Einheiten_EL["Cyanid l. freis. (CFA)"])
                            Options_Eluat_Cyanidleichtf.config(fg = "GREEN")
                        else:
                            Options_Eluat_Cyanidleichtf.config(fg = "RED")
                    else:
                        Options_Eluat_Cyanidleichtf.config(fg = "RED")

                    if "Phenolindex" in Dictionary_Einheiten_EL:
                        if Dictionary_Einheiten_EL["Phenolindex"] in list_MoeglicheEinheiten:
                            option_Eluat_Phenolindex.set(Dictionary_Einheiten_EL["Phenolindex"])
                            Options_Eluat_Phenolindex.config(fg = "GREEN")
                        else:
                            Options_Eluat_Phenolindex.config(fg = "RED")
                    else:
                        Options_Eluat_Phenolindex.config(fg = "RED")

                    if "Chlorid" in Dictionary_Einheiten_EL:
                        if Dictionary_Einheiten_EL["Chlorid"] in list_MoeglicheEinheiten:
                            option_Eluat_Chlorid.set(Dictionary_Einheiten_EL["Chlorid"])
                            Options_Eluat_Chlorid.config(fg = "GREEN")
                        else:
                            Options_Eluat_Chlorid.config(fg = "RED")
                    else:
                        Options_Eluat_Chlorid.config(fg = "RED")

                    if "Sulfat" in Dictionary_Einheiten_EL:
                        if Dictionary_Einheiten_EL["Sulfat"] in list_MoeglicheEinheiten:
                            option_Eluat_Sulfat.set(Dictionary_Einheiten_EL["Sulfat"])
                            Options_Eluat_Sulfat.config(fg = "GREEN")
                        else:
                            Options_Eluat_Sulfat.config(fg = "RED")
                    else:
                        Options_Eluat_Sulfat.config(fg = "RED")

                    if "DOC" in Dictionary_Einheiten_EL:
                        if Dictionary_Einheiten_EL["DOC"] in list_MoeglicheEinheiten:
                            option_Eluat_DOC.set(Dictionary_Einheiten_EL["DOC"])
                            Options_Eluat_DOC.config(fg = "GREEN")
                        else:
                            Options_Eluat_DOC.config(fg = "RED")
                    else:
                        Options_Eluat_DOC.config(fg = "RED")

                    if "Fluorid" in Dictionary_Einheiten_EL:
                        if Dictionary_Einheiten_EL["Fluorid"] in list_MoeglicheEinheiten:
                            option_Eluat_Fluorid.set(Dictionary_Einheiten_EL["Fluorid"])
                            Options_Eluat_Fluorid.config(fg = "GREEN")
                        else:
                            Options_Eluat_Fluorid.config(fg = "RED")
                    else:
                        Options_Eluat_Fluorid.config(fg = "RED")

                    if "Barium" in Dictionary_Einheiten_EL:
                        if Dictionary_Einheiten_EL["Barium"] in list_MoeglicheEinheiten:
                            option_Eluat_Barium.set(Dictionary_Einheiten_EL["Barium"])
                            Options_Eluat_Barium.config(fg = "GREEN")
                        else:
                            Options_Eluat_Barium.config(fg = "RED")
                    else:
                        Options_Eluat_Barium.config(fg = "RED")

                    if "Molybdän" in Dictionary_Einheiten_EL:
                        if Dictionary_Einheiten_EL["Molybdän"] in list_MoeglicheEinheiten:
                            option_Eluat_Molybdaen.set(Dictionary_Einheiten_EL["Molybdän"])
                            Options_Eluat_Molybdaen.config(fg = "GREEN")
                        else:
                            Options_Eluat_Molybdaen.config(fg = "RED")
                    else:
                        Options_Eluat_Molybdaen.config(fg = "RED")

                    if "Antimon" in Dictionary_Einheiten_EL:
                        if Dictionary_Einheiten_EL["Antimon"] in list_MoeglicheEinheiten:
                            option_Eluat_Antimon.set(Dictionary_Einheiten_EL["Antimon"])
                            Options_Eluat_Antimon.config(fg = "GREEN")
                        else:
                            Options_Eluat_Antimon.config(fg = "RED")
                    else:
                        Options_Eluat_Antimon.config(fg = "RED")

                    if "Selen" in Dictionary_Einheiten_EL:
                        if Dictionary_Einheiten_EL["Selen"] in list_MoeglicheEinheiten:
                            option_Eluat_Selen.set(Dictionary_Einheiten_EL["Selen"])
                            Options_Eluat_Selen.config(fg = "GREEN")
                        else:
                            Options_Eluat_Selen.config(fg = "RED")
                    else:
                        Options_Eluat_Selen.config(fg = "RED")

                    if "Ges.-Gehalt an gel. Feststoffen" in Dictionary_Einheiten_EL:
                        if Dictionary_Einheiten_EL["Ges.-Gehalt an gel. Feststoffen"] in list_MoeglicheEinheiten:
                            option_Eluat_GesGehaltGelStoffe.set(Dictionary_Einheiten_EL["Ges.-Gehalt an gel. Feststoffen"])
                            Options_Eluat_GesGehaltGelStoffe.config(fg = "GREEN")
                        else:
                            Options_Eluat_GesGehaltGelStoffe.config(fg = "RED")
                    else:
                        Options_Eluat_GesGehaltGelStoffe.config(fg = "RED")

            else:
                print("Bitte eine gültige Probenbezeichnung eingeben")
                resultLabel3.pack()

        Button(newWindow, text="Bestätigen", fg="black", bg="white", padx=2, pady=2,
               command=extractdatafromexcelfile).pack()
        Button(newWindow, text="Schließen", command=newWindow.destroy, bg="white", padx=2, pady=2).pack()

    def Stoff(self):
        Liste_Stoffe = [EOX, KW_C10_C40, KW_mobiler_Anteil_C10_C22, Cyanid_gesamt, BTX_BTEX, LHKW,
                        PAK_16, Benzopyren, PCB6, PCB7, Arsen, Blei, Cadmium, Chrom_gesamt, Kupfer, Nickel, Quecksilber,
                        Thallium,
                        Zink, TOC, Gluehverlust, Lipohile_Stoffe, pH_Wert, Leitfaehigkeit, Cyanid, Cyanid_lf,
                        Phenolindex,
                        Chlorid, Sulfat, DOC, Fluorid, Barium, Molybdaen, Antimon, Selen,
                        Gesamtgehalt_geloeste_Feststoffe, Dioxine,
                        Saeureneutralisationskapazitaet]  # Liste mit allen Stoffen, benutzt fuer die unten stehenden Pruefungen (richtgie Dateneingabe etc.)

        Liste_Stoffe_LAGA = [Arsen, Blei, Cadmium, Chrom_gesamt, Kupfer, Nickel, Quecksilber,
                             Zink, EOX, KW_C10_C40, KW_mobiler_Anteil_C10_C22, Cyanid_gesamt, BTX_BTEX, LHKW,
                             PAK_16, Benzopyren, PCB6, Thallium, TOC, Leitfaehigkeit, pH_Wert, Cyanid, Phenolindex,
                             Chlorid, Sulfat]  # Liste benutzt fuer LAGA-Pruefung

        Liste_Stoffe_BBSchG_Schwermetalle = [Blei, Cadmium, Chrom_gesamt, Kupfer, Nickel, Quecksilber,
                                             Zink]  # Extra Liste fuer Pruefung BBSchG abhaengig von der Bodenart
        Liste_Stoffe_BBSchG_Kohlenwasserstoffe = [PAK_16, Benzopyren,
                                                  PCB6]  # Extra Liste fuer Pruefung BBSchG abhaengig vom Humusgehalt

        Liste_Stoffe_DepV = [KW_C10_C40, BTX_BTEX, PAK_16, PCB7, TOC, Gluehverlust,
                             Lipohile_Stoffe, Leitfaehigkeit, Cyanid_lf, Phenolindex, Arsen,
                             Blei, Cadmium, Chrom_gesamt, Kupfer, Nickel, Quecksilber, Zink, Chlorid, Sulfat,
                             DOC, Fluorid, Barium, Molybdaen, Antimon, Selen,
                             Gesamtgehalt_geloeste_Feststoffe]  # Liste benutzt fuer DepV-Pruefung (ohne pH-Wert)

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

        try:
            for i in Liste_Stoffe:
                # Kontrolle ob positive Zahl (float) eingegeben wurde, dann weiter, sonst Ausnahme (except)
                if i.wert_TS == str("n.n."):
                    i.wert_TS = float(0)
                if i.wert_TS == str(i.wert_TS) and i.wert_TS[0:1] == "<":
                    i.wert_TS = i.wert_TS.replace(",", ".")
                    i.wert_TS = float(i.wert_TS[1:])
                elif i.wert_TS == str(i.wert_TS) and "," in i.wert_TS:
                    i.wert_TS = i.wert_TS.replace(",", ".")
                    i.wert_TS = float(i.wert_TS)
                elif i.wert_TS == float(i.wert_TS):
                    pass

                # Ausnahme < (kleiner gleich zeichen)  hinzufügen und , (Komma) als Dezimalstelle akzeptieren
                if i.wert_EL == str("n.n."):
                    i.wert_EL = float(0)
                if i.wert_EL == str(i.wert_EL) and i.wert_EL[0:1] == "<":
                    i.wert_EL = i.wert_EL.replace(",", ".")
                    i.wert_EL = float(i.wert_EL[1:])
                elif i.wert_EL == str(i.wert_EL) and "," in i.wert_EL:
                    i.wert_EL = i.wert_EL.replace(",", ".")
                    i.wert_EL = float(i.wert_EL)
                elif i.wert_EL == float(i.wert_EL):
                    pass

                # Ueberpruefen ob eine Zahl als float eingegeben wurde und nicht negativ ist, sonst "except"
                i.wert_TS = float(i.wert_TS)
                i.wert_EL = float(i.wert_EL)
                if i.wert_TS < 0:
                    raise ValueError
                if i.wert_EL < 0:
                    raise ValueError

                # Listen für die Einheiten-Umrechnungen
                list_Einheit_mgkgTM = ["Arsen", "Blei", "Cadmium", "Chrom gesamt", "Kupfer", "Nickel", "Quecksilber",
                                       "Thallium",
                                       "Zink", "EOX", "Kohlenwasserstoffe (C10-C40)", "Kohlenwasserstoffe (C10-C22)",
                                       "Cyanide gesamt",
                                       "BTX (BTEX)", "LHKW", "PAK16 (EPA)", "Benzo(a)pyren", "PCB6", "PCB7"]
                list_Einheit_ngkgTM = ["Dioxine / Furane"]
                list_Einheit_Masse = ["TOC", "Gluehverlust", "Extrahierbare Lipohile Stoffe"]
                list_Einheit_pH = [""]
                list_Einheit_μScm = ["Leitfähigkeit"]
                list_Einheit_μgL = ["Arsen", "Blei", "Cadmium", "Chrom gesamt", "Kupfer","Nickel",
                                    "Quecksilber", "Zink", "Cyanid (leicht freisetzbar)", "Phenolindex",
                                    "Molybdaen", "Antimon", "Selen"]
                list_Einheit_mgL = ["Chlorid", "Sulfat", "DOC", "Fluorid", "Barium",
                                    "Gesamtgehalt an geloesten Feststoffen"]

                # Einheiten Umrechnung
                if i.name in list_Einheit_mgkgTM:
                    if dict_Auswahl_Einheiten[str(i.name)] == "mg/kg TM":
                        pass
                    elif dict_Auswahl_Einheiten[str(i.name)] == "μg/kg TM":
                        i.wert_TS = i.wert_TS / 1000
                if i.name in list_Einheit_ngkgTM:
                    if dict_Auswahl_Einheiten[str(i.name)] == "ng/kg TM":
                        pass
                    elif dict_Auswahl_Einheiten[str(i.name)] == "μg/kg TM":
                        i.wert_TS = i.wert_TS * 1000
                    elif dict_Auswahl_Einheiten[str(i.name)] == "mg/kg TM":
                        i.wert_TS = i.wert_TS * 1000000

                if i.name in list_Einheit_μgL:
                    if dict_Auswahl_Einheiten_Eluat[str(i.name)] == "mg/L":
                        print(f"Für {i.name} ist die Einheit {dict_Auswahl_Einheiten_Eluat[str(i.name)]} und der nicht umgerechnete Wert: {i.wert_EL}")
                        i.wert_EL = i.wert_EL * 1000
                        print(f"Für {i.name} ist die Einheit {dict_Auswahl_Einheiten_Eluat[str(i.name)]} und der umgerechnete Wert: {i.wert_EL}")
                elif i.name in list_Einheit_mgL:
                    if dict_Auswahl_Einheiten_Eluat[str(i.name)] != "mg/L":
                        print(f"Für {i.name} ist die Einheit {dict_Auswahl_Einheiten_Eluat[str(i.name)]} und der nicht umgerechnete Wert: {i.wert_EL}")
                        i.wert_EL = i.wert_EL / 1000
                        print(f"Für {i.name} ist die Einheit {dict_Auswahl_Einheiten_Eluat[str(i.name)]} und der umgerechnete Wert: {i.wert_EL}")


            # Ueberpruefen und Feedback, ob Schluffgehalt ausgewaehlt wurde, wenn Bodenart Sand ausgewaehlt wurde
            if var1.get() == 3 and var4.get() == 0: # var = 3 -> Sand, var4 = 0 -> Schluffgehalt nicht ausgewählt
                raise NameError
            elif var1.get() != 3 and var4.get() != 0: #var = 3 -> Sand, var4 != 0 -> Schluffgehalt ausgewählt ausgewählt
                resultLabel.config(text="Erfolgreich (Schluffg. nicht berücks.)", bg="green")
            elif var1.get() == 0 and var2.get() == 0 and var4.get() == 0:
                raise NameError
            elif var1.get() != 0 and var2.get() == 0:
                raise NameError
            elif var1.get() == 0 and var2.get() != 0:
                raise NameError
            elif var1.get() == 0 and var4.get() != 0:
                raise NameError
            elif var2.get() == 0 and var4.get() != 0:
                raise NameError
            else:
                resultLabel.config(text="Erfolgreich", bg="green")

            # LAGA Feststoff Einordnung
            for i in Liste_Stoffe_LAGA:

                if i.name in Z0_TS:  # First remove the results of the previous looping from the list (um zu verhindern, dass der Parameter mehrmals ins PDF geschrieben wird)
                    Z0_TS.remove(i.name)
                if i.name in Z0_Stern_TS:
                    Z0_Stern_TS.remove(i.name)
                if i.name in Z1_TS:
                    Z1_TS.remove(i.name)
                if i.name in Z2_TS:
                    Z2_TS.remove(i.name)
                if i.name in Higher_Z2_TS:
                    Higher_Z2_TS.remove(i.name)

                # Einstufung für Bodenart Sand
                if Bodenart_auswahl == "Bodenart: Sand":
                    # Für Einbauklassen Z0, Z1, Z2, >Z2
                    if i.wert_TS <= i.Limit_Z0_Sa_TS:
                        Z0_TS.extend({i.name})
                    elif i.Limit_Z0_Sa_TS < i.wert_TS <= i.Limit_Z1_TS:
                        Z1_TS.extend({i.name})
                    elif i.Limit_Z1_TS < i.wert_TS <= i.Limit_Z2_TS:
                        Z2_TS.extend({i.name})
                    elif i.wert_TS > i.Limit_Z2_TS and i.wert_TS != 10000000:
                        Higher_Z2_TS.extend({i.name})
                    # Für Einbauklasse Z0*
                    if i.wert_TS > i.Limit_Z0_Stern_TS and i.wert_TS != 10000000: # max. Feststoffgehalte für Abgrabungen (Z0*)
                        Z0_Stern_TS.extend({i.name})
                elif Bodenart_auswahl == "Bodenart: Schluff":
                    # Für Einbauklassen Z0, Z1, Z2, >Z2
                    if i.wert_TS <= i.Limit_Z0_SL_TS:
                        Z0_TS.extend({i.name})
                    elif i.Limit_Z0_SL_TS < i.wert_TS <= i.Limit_Z1_TS:
                        Z1_TS.extend({i.name})
                    elif i.Limit_Z1_TS < i.wert_TS <= i.Limit_Z2_TS:
                        Z2_TS.extend({i.name})
                    elif i.wert_TS > i.Limit_Z2_TS and i.wert_TS != 10000000:
                        Higher_Z2_TS.extend({i.name})
                    # Für Einbauklasse Z0*
                    if i.wert_TS > i.Limit_Z0_Stern_TS and i.wert_TS != 10000000: # max. Feststoffgehalte für Abgrabungen (Z0*)
                        Z0_Stern_TS.extend({i.name})
                elif Bodenart_auswahl == "Bodenart: Ton":
                    # Für Einbauklassen Z0, Z1, Z2, >Z2
                    if i.wert_TS <= i.Limit_Z0_T_TS:
                        Z0_TS.extend({i.name})
                    elif i.Limit_Z0_T_TS < i.wert_TS <= i.Limit_Z1_TS:
                        Z1_TS.extend({i.name})
                    elif i.Limit_Z1_TS < i.wert_TS <= i.Limit_Z2_TS:
                        Z2_TS.extend({i.name})
                    elif i.wert_TS > i.Limit_Z2_TS and i.wert_TS != 10000000:
                        Higher_Z2_TS.extend({i.name})
                    # Für Einbauklasse Z0*
                    if i.name == "Arsen" and i.wert_TS > 20 and i.wert_TS != 10000000: # Ausnahme Fußnote 2 (Arsen)
                        Z0_Stern_TS.extend({i.name})
                    if i.name == "Cadmium" and i.wert_TS > 1.5 and i.wert_TS != 10000000: # Ausnahme Fußnote 3 (Cadmium)
                        Z0_Stern_TS.extend({i.name})
                    if i.name == "Thallium" and i.wert_TS > 1 and i.wert_TS != 10000000: # Ausnahme Fußnote 4 (Thallium)
                        Z0_Stern_TS.extend({i.name})
                    elif i.name != "Arsen" and i.name != "Cadmium" and i.name != "Thallium" and i.wert_TS > i.Limit_Z0_Stern_TS and i.wert_TS != 10000000:
                        Z0_Stern_TS.extend({i.name})
                # Fußnote 6 (EOX)
                if i.name == "EOX" and i.Limit_Z1_TS >= i.wert_TS > i.Limit_Z0_Stern_TS:
                    if "Bei Einstufung von EOX in Z0* oder Z1 ist die Ursache für die Überschreitung zu prüfen." in LAGA_TS_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        LAGA_TS_Anmerkungen.remove("Bei Einstufung von EOX in Z0* oder Z1 ist die Ursache für die Überschreitung zu prüfen.")
                    LAGA_TS_Anmerkungen.extend(["Bei Einstufung von EOX in Z0* oder Z1 ist die Ursache für die Überschreitung zu prüfen."])
                # Fußnote Tabelle II.1.2-4: Fußnote 3 (PAK16)
                if i.name == "PAK16 (EPA)" and dict_Auswahl_Einheiten[str(i.name)] == "mg/kg TM" and 3 < i.wert_TS <= 9:
                    if "Bodenmaterial mit PAK16 Zuordnungswerten > 3 mg/kg und <= 9 mg/kg darf nur in Gebieten mit hydrogeologisch günstigen Deckschichten eingebaut werden." in LAGA_TS_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        LAGA_TS_Anmerkungen.remove("Bodenmaterial mit PAK16 Zuordnungswerten > 3 mg/kg und <= 9 mg/kg darf nur in Gebieten mit hydrogeologisch günstigen Deckschichten eingebaut werden.")
                    LAGA_TS_Anmerkungen.extend(["Bodenmaterial mit PAK16 Zuordnungswerten > 3 mg/kg und <= 9 mg/kg darf nur in Gebieten mit hydrogeologisch günstigen Deckschichten eingebaut werden."])
                    print(f"PAK-WERT IST: {i.wert_TS}")
                if i.name == "PAK16 (EPA)" and dict_Auswahl_Einheiten[str(i.name)] == "μg/kg TM" and 3000 < i.wert_TS <= 9000:
                    if "Bodenmaterial mit PAK16 Zuordnungswerten > 3 mg/kg und <= 9 mg/kg darf nur in Gebieten mit hydrogeologisch günstigen Deckschichten eingebaut werden." in LAGA_TS_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        LAGA_TS_Anmerkungen.remove("Bodenmaterial mit PAK16 Zuordnungswerten > 3 mg/kg und <= 9 mg/kg darf nur in Gebieten mit hydrogeologisch günstigen Deckschichten eingebaut werden.")
                    LAGA_TS_Anmerkungen.extend(["Bodenmaterial mit PAK16 Zuordnungswerten > 3 mg/kg und <= 9 mg/kg darf nur in Gebieten mit hydrogeologisch günstigen Deckschichten eingebaut werden."])
                    print(f"PAK-WERT IST: {i.wert_TS}")
                # Tabelle II.1.2-2: Fußnote 6
                if i.name == "TOC" and i.wert_TS <= i.Limit_Z0_Stern_TS: # Wert Z0* = Werte Z0 (Ton/Lehm/Sand) = 0.5
                    if "Zusätzliche Prüfung erforderlich: Bei TOC gleich Z0 oder Z0* und einem C:N-Verhältnis > 25 beträgt der Zuordnungswert für TOC 1 Masse-%." in LAGA_TS_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        LAGA_TS_Anmerkungen.remove("Zusätzliche Prüfung erforderlich: Bei TOC gleich Z0 oder Z0* und einem C:N-Verhältnis > 25 beträgt der Zuordnungswert für TOC 1 Masse-%.")
                    LAGA_TS_Anmerkungen.extend(["Zusätzliche Prüfung erforderlich: Bei TOC gleich Z0 oder Z0* und einem C:N-Verhältnis > 25 beträgt der Zuordnungswert für TOC 1 Masse-%."])

            # LAGA Eluat Einordnung
            for i in Liste_Stoffe_LAGA:

                if i.name in Z0_EL:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                    Z0_EL.remove(i.name)
                if i.name in Z11_EL:
                    Z11_EL.remove(i.name)
                if i.name in Z12_EL:
                    Z12_EL.remove(i.name)
                if i.name in Z2_EL:
                    Z2_EL.remove(i.name)
                if i.name in Higher_Z2_EL:
                    Higher_Z2_EL.remove(i.name)

                # Eluat (außer pH-Wert und Quecksilber, für diese gelten extra Regeln, siehe unten)
                if i.wert_EL <= i.Limit_Z0_EL and i.name != "Quecksilber" and i.name != "pH-Wert":
                    Z0_EL.extend({i.name})
                elif i.Limit_Z0_EL < i.wert_EL <= i.Limit_Z11_EL and i.name != "Quecksilber" and i.name != "pH-Wert":
                    Z11_EL.extend({i.name})
                elif i.Limit_Z11_EL < i.wert_EL <= i.Limit_Z12_EL and i.name != "Quecksilber" and i.name != "pH-Wert":
                    Z12_EL.extend({i.name})
                elif i.Limit_Z12_EL < i.wert_EL <= i.Limit_Z2_EL and i.name != "Quecksilber" and i.name != "pH-Wert":
                    Z2_EL.extend({i.name})
                elif i.wert_EL > i.Limit_Z2_EL and i.name != "Quecksilber" and i.name != "pH-Wert" and i.wert_EL != 10000000:
                    Higher_Z2_EL.extend({i.name})
                # Ausnahme für Quecksilber
                if i.wert_EL < i.Limit_Z0_EL and i.name == "Quecksilber":
                    Z0_EL.extend({i.name})
                elif i.Limit_Z0_EL <= i.wert_EL < i.Limit_Z11_EL and i.name == "Quecksilber" :
                    Z11_EL.extend({i.name})
                elif i.Limit_Z11_EL <= i.wert_EL <= i.Limit_Z12_EL and i.name == "Quecksilber":
                    Z12_EL.extend({i.name})
                elif i.Limit_Z12_EL < i.wert_EL <= i.Limit_Z2_EL and i.name == "Quecksilber":
                    Z2_EL.extend({i.name})
                elif i.wert_EL > i.Limit_Z2_EL and i.wert_EL != 10000000 and i.name == "Quecksilber":
                    Higher_Z2_EL.extend({i.name})

                # Tabelle II.1.2-5: Fußnoten 2 und 3
                if i.name == "Chlorid" and i.wert_EL > i.Limit_Z2_EL and i.wert_EL != 10000000:
                    if "Zusätzliche Prüfung erforderlich: Bei natürlichen Böden kann der Z2-Zuordnungswert für Chlorid im Eluat in Ausnahmefällen bis 300 mg/l betragen." in LAGA_EL_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        LAGA_EL_Anmerkungen.remove("Zusätzliche Prüfung erforderlich: Bei natürlichen Böden kann der Z2-Zuordnungswert für Chlorid im Eluat in Ausnahmefällen bis 300 mg/l betragen.")
                    LAGA_EL_Anmerkungen.extend(["Zusätzliche Prüfung erforderlich: Bei natürlichen Böden kann der Z2-Zuordnungswert für Chlorid im Eluat in Ausnahmefällen bis 300 mg/l betragen."])
                if i.name == "Arsen" and i.wert_EL > i.Limit_Z2_EL and i.wert_EL != 10000000:
                    if "Zusätzliche Prüfung erforderlich: Bei natürlichen Böden kann der Z2-Zuordnungswert für Arsen im Eluat in Ausnahmefällen bis 120 ug/l betragen." in LAGA_EL_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        LAGA_EL_Anmerkungen.remove("Zusätzliche Prüfung erforderlich: Bei natürlichen Böden kann der Z2-Zuordnungswert für Arsen im Eluat in Ausnahmefällen bis 120 ug/l betragen.")
                    LAGA_EL_Anmerkungen.extend(["Zusätzliche Prüfung erforderlich: Bei natürlichen Böden kann der Z2-Zuordnungswert für Arsen im Eluat in Ausnahmefällen bis 120 ug/l betragen."])

            # LAGA pH Wert Einordnung
            if pH_Wert.name in Z2_EL:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                Z2_EL.remove(i.name)
            if pH_Wert.name in Z12_EL:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                Z12_EL.remove(i.name)

            if 6.5 <= pH_Wert.wert_EL <= 9.5:
                Z0_EL.extend({pH_Wert.name})
            # Für Z1.1 gibt es keine Einstufung (gleich wie Z0)
            elif (6 <= pH_Wert.wert_EL < 6.5) or (9.5 < pH_Wert.wert_EL <= 12): #korrekt
                Z12_EL.extend({pH_Wert.name})
                #Z0*extend
            elif 6 > pH_Wert.wert_EL >= 5.5: # korrekt
                Z2_EL.extend({pH_Wert.name})
            elif 5.5 > pH_Wert.wert_EL or pH_Wert.wert_EL > 12 and pH_Wert.wert_EL != 10000000:
                Higher_Z2_EL.extend({pH_Wert.name})

            # BBSchG Einordnung Kohlenwasserstoffe (abhaengig vom Humusgehalt)
            for i in Liste_Stoffe_BBSchG_Kohlenwasserstoffe:

                if i.name in BBSchG_Ueberschritten:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                    BBSchG_Ueberschritten.remove(i.name)

                if Humus == "Anteil Humus (TOC): >8% (>4%)":
                    if i.wert_TS > i.Limit_BBSchG_HumusUE8 and i.wert_TS != 10000000:
                        BBSchG_Ueberschritten.extend({i.name})
                elif Humus == "Anteil Humus (TOC): <=8% (<=4%)":
                    if i.wert_TS > i.Limit_BBSchG_HumusU8 and i.wert_TS != 10000000:
                        BBSchG_Ueberschritten.extend({i.name})

            # BBSchG Einordnung Schwermetalle (abhaengig von Bodenart)
            for i in Liste_Stoffe_BBSchG_Schwermetalle:

                if i.name in BBSchG_Ueberschritten:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                    BBSchG_Ueberschritten.remove(i.name)

                # Ausnahme Fußnote d) Die Vorsorgewerte der Tabelle 4.1 finden für Böden und Bodenhorizonte mit einem Humusgehalt von mehr als 8 Prozent keine Anwendung. Für diese Böden können die zuständigen Behörden ggf. gebietsbezogene Festsetzungen treffen.
                if Humus == "Anteil Humus (TOC): <=8% (<=4%)" and (i.name == "Cadmium" or i.name == "Nickel" or i.name == "Zink" or i.name == "Blei" or i.name == "Quecksilber" or i.name == "Kupfer" or i.name == "Chrom gesamt"):

                    if "Die Vorsorgewerte für Schwermetalle finden für Böden und Bodenhorizonte mit einem Humusgehalt von mehr als 8 Prozent keine Anwendung. Für diese Böden können die zuständigen Behörden ggf. gebietsbezogene Festsetzungen treffen." in BBSchG_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        BBSchG_Anmerkungen.remove("Die Vorsorgewerte für Schwermetalle finden für Böden und Bodenhorizonte mit einem Humusgehalt von mehr als 8 Prozent keine Anwendung. Für diese Böden können die zuständigen Behörden ggf. gebietsbezogene Festsetzungen treffen.")

                    #print(f" Humusgehalt <=8% und Schwermetall: {i.name}")

                    if i.name in BBSchG_Ueberschritten:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        BBSchG_Ueberschritten.remove(i.name)

                    if Bodenart_auswahl == "Bodenart: Sand" and Bodenart_auswahl_ergaenzung != "Stark schluffhaltiger Sand (40 bis <50%)":
                        if i.wert_TS > i.Limit_BBSchG_Sa and i.wert_TS != 10000000:
                            BBSchG_Ueberschritten.extend({i.name})
                            if "Überschreitung für Schwermetalle unbedenklich bei Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen." in BBSchG_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                                BBSchG_Anmerkungen.remove("Überschreitung für Schwermetalle unbedenklich bei Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen.")
                            BBSchG_Anmerkungen.extend(["Überschreitung für Schwermetalle unbedenklich bei Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen."])

                    # Ausnahme Fußnote b) Stark schluffige Sande sind entsprechend der Bodenart Lehm/Schluff zu bewerten.
                    elif Bodenart_auswahl == "Bodenart: Sand" and Bodenart_auswahl_ergaenzung == "Stark schluffhaltiger Sand (40 bis <50%)": # bei stark schluffigem Sand Einstufung gemäß Grenzwerte für Schluff
                        if "Stark schluffige Sande wurden entsprechend der Bodenart Lehm/Schluff bewertet." in BBSchG_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                            BBSchG_Anmerkungen.remove("Stark schluffige Sande wurden entsprechend der Bodenart Lehm/Schluff bewertet.")
                        BBSchG_Anmerkungen.extend(["Stark schluffige Sande wurden entsprechend der Bodenart Lehm/Schluff bewertet."])
                        if i.wert_TS > i.Limit_BBSchG_SL and i.wert_TS != 10000000:
                            BBSchG_Ueberschritten.extend({i.name})
                            if "Überschreitung für Schwermetalle unbedenklich bei Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen." in BBSchG_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                                BBSchG_Anmerkungen.remove("Überschreitung für Schwermetalle unbedenklich bei Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen.")
                            BBSchG_Anmerkungen.extend(["Überschreitung für Schwermetalle unbedenklich bei Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen."])

                    # Ausnahme Fußnote c) (1) Bei Böden der Bodenart Ton mit einem pH-Wert von < 6,0 gelten für Cadmium, Nickel und Zink die Vorsorgewerte der Bodenart Lehm/Schluff
                    if Bodenart_auswahl == "Bodenart: Ton" and pH_Wert.wert_EL < 6.0 and (i.name == "Cadmium" or i.name == "Nickel" or i.name == "Zink"):
                        print(f"BBSchV Fußnote c) Bodenart Ton, pH-Wert <6.0 und Stoff: {i.name}")
                        if "Bei Böden der Bodenart Ton mit einem pH-Wert von < 6,0 wurde für Cadmium, Nickel und Zink im Feststoff anhand der Vorsorgewerte der Bodenart Lehm/Schluff bewertet." in BBSchG_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                            BBSchG_Anmerkungen.remove("Bei Böden der Bodenart Ton mit einem pH-Wert von < 6,0 wurde für Cadmium, Nickel und Zink im Feststoff anhand der Vorsorgewerte der Bodenart Lehm/Schluff bewertet.")
                        BBSchG_Anmerkungen.extend(["Bei Böden der Bodenart Ton mit einem pH-Wert von < 6,0 wurde für Cadmium, Nickel und Zink im Feststoff anhand der Vorsorgewerte der Bodenart Lehm/Schluff bewertet."])
                        if i.wert_TS > i.Limit_BBSchG_SL and i.wert_TS != 10000000:
                            BBSchG_Ueberschritten.extend({i.name})
                            if "Überschreitung für Schwermetalle unbedenklich bei Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen." in BBSchG_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                                BBSchG_Anmerkungen.remove("Überschreitung für Schwermetalle unbedenklich bei Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen.")
                            BBSchG_Anmerkungen.extend(["Überschreitung für Schwermetalle unbedenklich bei Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen."])

                    # Ausnahme Fußnote c) (2) Bei Böden der Bodenart Lehm/Schluff mit einem pH-Wert von < 6,0 gelten für Cadmium, Nickel und Zink die Vorsorgewerte der Bodenart Sand
                    if Bodenart_auswahl == "Bodenart: Schluff" and pH_Wert.wert_EL < 6.0 and (i.name == "Cadmium" or i.name == "Nickel" or i.name == "Zink"):
                        print(f"BBSchV Fußnote c) Bodenart Lehm/Schluff, pH-Wert <6.0 und Stoff: {i.name}")
                        if "Bei Böden der Bodenart Lehm/Schluff mit einem pH-Wert von < 6,0 wurde für Cadmium, Nickel und Zink anhand der Vorsorgewerte der Bodenart Sand bewertet." in BBSchG_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                            BBSchG_Anmerkungen.remove("Bei Böden der Bodenart Lehm/Schluff mit einem pH-Wert von < 6,0 wurde für Cadmium, Nickel und Zink anhand der Vorsorgewerte der Bodenart Sand bewertet.")
                        BBSchG_Anmerkungen.extend(["Bei Böden der Bodenart Lehm/Schluff mit einem pH-Wert von < 6,0 wurde für Cadmium, Nickel und Zink anhand der Vorsorgewerte der Bodenart Sand bewertet."])
                        if i.wert_TS > i.Limit_BBSchG_Sa and i.wert_TS != 10000000:
                            BBSchG_Ueberschritten.extend({i.name})
                            if "Überschreitung für Schwermetalle unbedenklich bei Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen." in BBSchG_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                                BBSchG_Anmerkungen.remove("Überschreitung für Schwermetalle unbedenklich bei Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen.")
                            BBSchG_Anmerkungen.extend(["Überschreitung für Schwermetalle unbedenklich bei Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen."])

                    # Ausnahme Fußnote c) (3) Bei Böden mit einem pH-Wert von < 5,0 sind die Vorsorgewerte für Blei entsprechend den ersten beiden Anstrichen herabzusetzen.
                    if (Bodenart_auswahl == "Bodenart: Schluff" or Bodenart_auswahl == "Bodenart: Ton") and pH_Wert.wert_EL < 5.0 and (i.name == "Blei"):
                        print(f"BBSchV Fußnote c) Bodenart Lehm/Schluff, pH-Wert <5.0 und Stoff: {i.name}")
                        if "Bei Böden der Bodenart Ton (Lehm/Schluff) mit einem pH-Wert von < 5,0 wurde für Blei anhand der Vorsorgewerte der Bodenart Lehm/Schluff (Sand) bewertet." in BBSchG_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                            BBSchG_Anmerkungen.remove("Bei Böden der Bodenart Ton (Lehm/Schluff) mit einem pH-Wert von < 5,0 wurde für Blei anhand der Vorsorgewerte der Bodenart Lehm/Schluff (Sand) bewertet.")
                        BBSchG_Anmerkungen.extend(["Bei Böden der Bodenart Ton (Lehm/Schluff) mit einem pH-Wert von < 5,0 wurde für Blei anhand der Vorsorgewerte der Bodenart Lehm/Schluff (Sand) bewertet."])
                        if Bodenart_auswahl == "Bodenart: Schluff" and i.wert_TS > i.Limit_BBSchG_Sa and i.wert_TS != 10000000:
                            BBSchG_Ueberschritten.extend({i.name})
                            if "Überschreitung für Schwermetalle unbedenklich bei Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen." in BBSchG_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                                BBSchG_Anmerkungen.remove("Überschreitung für Schwermetalle unbedenklich bei Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen.")
                            BBSchG_Anmerkungen.extend(["Überschreitung für Schwermetalle unbedenklich bei Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen."])
                        elif Bodenart_auswahl == "Bodenart: Ton" and i.wert_TS > i.Limit_BBSchG_SL and i.wert_TS != 10000000:
                            BBSchG_Ueberschritten.extend({i.name})
                            if "Überschreitung für Schwermetalle unbedenklich bei Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen." in BBSchG_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                                BBSchG_Anmerkungen.remove("Überschreitung für Schwermetalle unbedenklich bei Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen.")
                            BBSchG_Anmerkungen.extend(["Überschreitung für Schwermetalle unbedenklich bei Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen."])

                    elif Bodenart_auswahl == "Bodenart: Schluff":
                        if i.wert_TS > i.Limit_BBSchG_SL and i.wert_TS != 10000000:
                            BBSchG_Ueberschritten.extend({i.name})
                            if "Überschreitung für Schwermetalle unbedenklich bei Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen." in BBSchG_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                                BBSchG_Anmerkungen.remove("Überschreitung für Schwermetalle unbedenklich bei Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen.")
                            BBSchG_Anmerkungen.extend(["Überschreitung für Schwermetalle unbedenklich bei Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen."])

                    elif Bodenart_auswahl == "Bodenart: Ton":
                        if i.wert_TS > i.Limit_BBSchG_T and i.wert_TS != 10000000:
                            BBSchG_Ueberschritten.extend({i.name})
                            if "Überschreitung für Schwermetalle unbedenklich bei Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen." in BBSchG_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                                BBSchG_Anmerkungen.remove("Überschreitung für Schwermetalle unbedenklich bei Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen.")
                            BBSchG_Anmerkungen.extend(["Überschreitung für Schwermetalle unbedenklich bei Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen."])

                elif Humus == "Anteil Humus (TOC): >8% (>4%)" and (i.name == "Cadmium" or i.name == "Nickel" or i.name == "Zink" or i.name == "Blei" or i.name == "Quecksilber" or i.name == "Kupfer" or i.name == "Chrom gesamt") and i.wert_TS != 10000000:
                    print(f" Humusgehalt >8% und Schwermetall: {i.name}")
                    if "Überschreitung für Schwermetalle unbedenklich bei Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen." in BBSchG_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        BBSchG_Anmerkungen.remove("Überschreitung für Schwermetalle unbedenklich bei Böden mit naturbedingt und großflächig siedlungsbedingt erhöhten Hintergrundgehalten, soweit eine Freisetzung der Schadstoffe oder zusätzliche Einträge nach § 9 Abs. 2 und 3 dieser Verordnung keine nachteiligen Auswirkungen auf die Bodenfunktionen erwarten lassen.")
                    if "Bei Böden der Bodenart Ton mit einem pH-Wert von < 6,0 wurde für Cadmium, Nickel und Zink anhand der Vorsorgewerte der Bodenart Lehm/Schluff bewertet." in BBSchG_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        BBSchG_Anmerkungen.remove("Bei Böden der Bodenart Ton mit einem pH-Wert von < 6,0 wurde für Cadmium, Nickel und Zink anhand der Vorsorgewerte der Bodenart Lehm/Schluff bewertet.")
                    if "Bei Böden der Bodenart Lehm/Schluff mit einem pH-Wert von < 6,0 wurde für Cadmium, Nickel und Zink anhand der Vorsorgewerte der Bodenart Sand bewertet." in BBSchG_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        BBSchG_Anmerkungen.remove("Bei Böden der Bodenart Lehm/Schluff mit einem pH-Wert von < 6,0 wurde für Cadmium, Nickel und Zink anhand der Vorsorgewerte der Bodenart Sand bewertet.")
                    if "Bei Böden der Bodenart Ton (Lehm/Schluff) mit einem pH-Wert von < 5,0 wurde für Blei anhand der Vorsorgewerte der Bodenart Lehm/Schluff (Sand) bewertet." in BBSchG_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        BBSchG_Anmerkungen.remove("Bei Böden der Bodenart Ton (Lehm/Schluff) mit einem pH-Wert von < 5,0 wurde für Blei anhand der Vorsorgewerte der Bodenart Lehm/Schluff (Sand) bewertet.")
                    # BBSchG -> Falls Humus >8% Info, dass Schwermetalle nicht beruecksichtigt werden
                    if "Die Vorsorgewerte für Schwermetalle finden für Böden und Bodenhorizonte mit einem Humusgehalt von mehr als 8 Prozent keine Anwendung. Für diese Böden können die zuständigen Behörden ggf. gebietsbezogene Festsetzungen treffen." in BBSchG_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        BBSchG_Anmerkungen.remove("Die Vorsorgewerte für Schwermetalle finden für Böden und Bodenhorizonte mit einem Humusgehalt von mehr als 8 Prozent keine Anwendung. Für diese Böden können die zuständigen Behörden ggf. gebietsbezogene Festsetzungen treffen.")
                    BBSchG_Anmerkungen.extend(["Die Vorsorgewerte für Schwermetalle finden für Böden und Bodenhorizonte mit einem Humusgehalt von mehr als 8 Prozent keine Anwendung. Für diese Böden können die zuständigen Behörden ggf. gebietsbezogene Festsetzungen treffen."])

            # DepV Einordnung (DK, REK, GEO)
            for i in Liste_Stoffe_DepV:

                if i.name in DK0_TS:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                    DK0_TS.remove(i.name)
                if i.name in DK1_TS:
                    DK1_TS.remove(i.name)
                if i.name in DK2_TS:
                    DK2_TS.remove(i.name)
                if i.name in DK3_TS:
                    DK3_TS.remove(i.name)
                if i.name in Higher_DK3_TS:
                    Higher_DK3_TS.remove(i.name)
                if i.name in GEO_TS_Eingehalten:
                    GEO_TS_Eingehalten.remove(i.name)
                if i.name in GEO_TS_Ueberschritten:
                    GEO_TS_Ueberschritten.remove(i.name)
                if i.name in REK_TS_Eingehalten:
                    REK_TS_Eingehalten.remove(i.name)
                if i.name in REK_TS_Ueberschritten:
                    REK_TS_Ueberschritten.remove(i.name)
                if i.name in DK0_EL:
                    DK0_EL.remove(i.name)
                if i.name in DK1_EL:
                    DK1_EL.remove(i.name)
                if i.name in DK2_EL:
                    DK2_EL.remove(i.name)
                if i.name in DK3_EL:
                    DK3_EL.remove(i.name)
                if i.name in Higher_DK3_EL:
                    Higher_DK3_EL.remove(i.name)
                if i.name in GEO_EL_Eingehalten:
                    GEO_EL_Eingehalten.remove(i.name)
                if i.name in GEO_EL_Ueberschritten:
                    GEO_EL_Ueberschritten.remove(i.name)
                if i.name in REK_EL_Eingehalten:
                    REK_EL_Eingehalten.remove(i.name)
                if i.name in REK_EL_Ueberschritten:
                    REK_EL_Ueberschritten.remove(i.name)

                # DK Feststoff
                if i.wert_TS <= i.Limit_DK0_TS and i.Limit_DK0_TS != 0:
                    DK0_TS.extend({i.name})
                elif i.wert_TS <= i.Limit_DK1_TS and i.Limit_DK1_TS != 0:
                    DK1_TS.extend({i.name})
                elif i.wert_TS <= i.Limit_DK2_TS and i.Limit_DK2_TS != 0:
                    DK2_TS.extend({i.name})
                elif i.wert_TS <= i.Limit_DK3_TS and i.Limit_DK3_TS != 0:
                    DK3_TS.extend({i.name})
                elif i.wert_TS > i.Limit_DK3_TS and i.wert_TS != 10000000 and i.Limit_DK3_TS != 0:
                    Higher_DK3_TS.extend({i.name})

                # GEO Feststoff
                if i.wert_TS <= i.Limit_GEO_TS and i.Limit_GEO_TS != 0:
                    GEO_TS_Eingehalten.extend({i.name})
                elif i.wert_TS > i.Limit_GEO_TS and i.wert_TS != 10000000 and i.Limit_GEO_TS != 0:
                    GEO_TS_Ueberschritten.extend({i.name})

                # REK Feststoff
                if i.wert_TS <= i.Limit_REK_TS and i.Limit_REK_TS != 0:
                    REK_TS_Eingehalten.extend({i.name})
                elif i.wert_TS > i.Limit_REK_TS and i.wert_TS != 10000000 and i.Limit_REK_TS != 0:
                    REK_TS_Ueberschritten.extend({i.name})

                # DK Eluat
                if i.wert_EL <= i.Limit_DK0_EL and i.Limit_DK0_EL != 0:
                    DK0_EL.extend({i.name})
                elif i.wert_EL <= i.Limit_DK1_EL and i.Limit_DK1_EL != 0:
                    DK1_EL.extend({i.name})
                elif i.wert_EL <= i.Limit_DK2_EL and i.Limit_DK2_EL != 0:
                    DK2_EL.extend({i.name})
                elif i.wert_EL <= i.Limit_DK3_EL and i.Limit_DK3_EL != 0:
                    DK3_EL.extend({i.name})
                elif i.wert_EL > i.Limit_DK3_EL and i.wert_EL != 10000000 and i.Limit_DK3_EL != 0:
                    Higher_DK3_EL.extend({i.name})

                # GEO Eluat
                if i.wert_EL <= i.Limit_GEO_EL and i.Limit_GEO_EL != 0:
                    GEO_EL_Eingehalten.extend({i.name})
                elif i.wert_EL > i.Limit_GEO_EL and i.wert_EL != 10000000 and i.Limit_GEO_EL != 0:
                    GEO_EL_Ueberschritten.extend({i.name})

                # REK Eluat
                if i.wert_EL <= i.Limit_REK_EL and i.Limit_REK_EL != 0:
                    REK_EL_Eingehalten.extend({i.name})
                elif i.wert_EL > i.Limit_REK_EL and i.wert_EL != 10000000 and i.Limit_REK_EL != 0:
                    REK_EL_Ueberschritten.extend({i.name})

                # Fußnote 2a
                if i.name == "TOC":
                    if "2a (TOC)" in DepV_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        DepV_Anmerkungen.remove("2a (TOC)")
                if i.name == "TOC" and 3 >= i.wert_TS > 1:
                    DepV_Anmerkungen.extend(["2a (TOC)"])

                if i.name == "Gluehverlust":
                    if "2a (Glühverlust)" in DepV_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        DepV_Anmerkungen.remove("2a (Glühverlust)")
                if i.name == "Gluehverlust" and 5 >= i.wert_TS > 3:
                    DepV_Anmerkungen.extend(["2a (Glühverlust)"])

                # Fußnote 3 TOC und Glüverlust
                if i.name == "TOC":
                    if "3 (TOC)" in DepV_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        DepV_Anmerkungen.remove("3 (TOC)")
                if i.name == "TOC" and 6 >= i.wert_TS > 1:
                    DepV_Anmerkungen.extend(["3 (TOC)"])

                if i.name == "Gluehverlust":
                    if "3 (Glühverlust)" in DepV_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        DepV_Anmerkungen.remove("3 (Glühverlust)")
                if i.name == "Gluehverlust" and 10 >= i.wert_TS > 3:
                    DepV_Anmerkungen.extend(["3 (Glühverlust)"])

                # Fußnoten 3 und 10 DOC
                if i.name == "DOC":
                    if "3 und 10 (DOC)" in DepV_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        DepV_Anmerkungen.remove("3 und 10 (DOC)")
                if i.name == "DOC" and 100 >= i.wert_EL > 50:
                    DepV_Anmerkungen.extend(["3 und 10 (DOC)"])

                # Fußnote 11 DOC
                if i.name == "DOC":
                    if "11 (DOC)" in DepV_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        DepV_Anmerkungen.remove("11 (DOC)")
                if i.name == "DOC" and 100 >= i.wert_EL > 80:
                    DepV_Anmerkungen.extend(["11 (DOC)"])

                # Fußnoten 4 und 5 TOC und Glühverlust
                if i.name == "TOC":
                    if "4 und 5 (TOC)" in DepV_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        DepV_Anmerkungen.remove("4 und 5 (TOC)")
                if i.name == "TOC" and 1 < i.wert_TS and i.wert_TS != 10000000:
                    DepV_Anmerkungen.extend(["4 und 5 (TOC)"])

                if i.name == "Gluehverlust":
                    if "4 und 5 (Glühverlust)" in DepV_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        DepV_Anmerkungen.remove("4 und 5 (Glühverlust)")
                if i.name == "Gluehverlust" and 3 < i.wert_TS and i.wert_TS != 10000000:
                    DepV_Anmerkungen.extend(["4 und 5 (Glühverlust)"])

                # Fußnote 5 Extrahierbare Lipohile Stoffe
                if i.name == "Extrahierbare Lipohile Stoffe":
                    if "5 (Extr. Lipophile Stoffe)" in DepV_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        DepV_Anmerkungen.remove("5 (Extr. Lipophile Stoffe)")
                if i.name == "Extrahierbare Lipohile Stoffe" and 0.4 < i.wert_TS and i.wert_TS != 10000000:
                    DepV_Anmerkungen.extend(["5 (Extr. Lipophile Stoffe)"])

                # Fußnote 6 Summe PAK (EPA)
                if i.name == "PAK16 (EPA)":
                    if "6 (Summe PAK EPA)" in DepV_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        DepV_Anmerkungen.remove("6 (Summe PAK EPA)")
                if i.name == "PAK16 (EPA)" and 5 < i.wert_TS and i.wert_TS != 10000000:
                    DepV_Anmerkungen.extend(["6 (Summe PAK EPA)"])

                # Fußnote 13 Chlorid
                if i.name == "Chlorid":
                    if "13 (Chlorid)" in DepV_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        DepV_Anmerkungen.remove("13 (Chlorid)")
                if i.name == "Chlorid" and 2500 >= i.wert_EL > 1500:
                    DepV_Anmerkungen.extend(["13 (Chlorid)"])

                # Fußnote 14 Chlorid REK
                if i.name == "Chlorid":
                    if "14 (Chlorid)" in DepV_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        DepV_Anmerkungen.remove("14 (Chlorid)")
                if i.name == "Chlorid" and i.wert_EL > 10 and i.wert_EL != 10000000:
                    DepV_Anmerkungen.extend(["14 (Chlorid)"])

                # Fußnote 13 Sulfat
                if i.name == "Sulfat":
                    if "13 (Sulfat)" in DepV_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        DepV_Anmerkungen.remove("13 (Sulfat)")
                if i.name == "Sulfat" and 5000 >= i.wert_EL > 2000:
                    DepV_Anmerkungen.extend(["13 (Sulfat)"])

                # Fußnote 14 Sulfat REK
                if i.name == "Sulfat":
                    if "14 (Sulfat)" in DepV_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        DepV_Anmerkungen.remove("14 (Sulfat)")
                if i.name == "Sulfat" and i.wert_EL > 50 and i.wert_EL != 10000000:
                    DepV_Anmerkungen.extend(["14 (Sulfat)"])

                # Fußnote 15 Sulfat
                if i.name == "Sulfat":
                    if "15 (Sulfat)" in DepV_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        DepV_Anmerkungen.remove("15 (Sulfat)")
                if i.name == "Sulfat" and 2000 >= i.wert_EL > 100:
                    DepV_Anmerkungen.extend(["15 (Sulfat)"])

                # Fußnote 13 Barium
                if i.name == "Barium":
                    if "13 (Barium)" in DepV_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        DepV_Anmerkungen.remove("13 (Barium)")
                if i.name == "Barium" and 30 >= i.wert_EL > 5:
                    DepV_Anmerkungen.extend(["13 (Barium)"])

                # Fußnote 13 Molybdaen
                if i.name == "Molybdaen":
                    if "13 (Molybdän)" in DepV_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        DepV_Anmerkungen.remove("13 (Molybdän)")
                if i.name == "Molybdaen" and 3000 >= i.wert_EL > 300:
                    DepV_Anmerkungen.extend(["13 (Molybdän)"])

                # Fußnote 13 Antimon
                if i.name == "Antimon":
                    if "13 (Antimon)" in DepV_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        DepV_Anmerkungen.remove("13 (Antimon)")
                if i.name == "Antimon" and 500 >= i.wert_EL > 30:
                    DepV_Anmerkungen.extend(["13 (Antimon)"])

                # Fußnote 16 Antimon
                if i.name == "Antimon":
                    if "16 (Antimon)" in DepV_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        DepV_Anmerkungen.remove("16 (Antimon)")
                if i.name == "Antimon" and i.wert_EL > 6 and i.wert_EL != 10000000:
                    DepV_Anmerkungen.extend(["16 (Antimon)"])

                # Fußnote 13 Selen
                if i.name == "Selen":
                    if "13 (Selen)" in DepV_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                        DepV_Anmerkungen.remove("13 (Selen)")
                if i.name == "Selen" and 700 >= i.wert_EL > 30:
                    DepV_Anmerkungen.extend(["13 (Selen)"])



            # Fußnote 8 pH-Wert
            if "8 (pH-Wert)" in DepV_Anmerkungen:  # First remove the results of the previous looping (um zu verhindern, dass der Parameter mehrmal geschrieben wird)
                DepV_Anmerkungen.remove("8 (pH-Wert)")
            if 6.5 > pH_Wert.wert_EL:
                DepV_Anmerkungen.extend(["8 (pH-Wert)"])
            if 9 < pH_Wert.wert_EL and pH_Wert.wert_EL != 10000000:
                DepV_Anmerkungen.extend(["8 (pH-Wert)"])


            # DK Eluat pH Wert Einordnung
            if pH_Wert.name in DK0_EL:
                DK0_EL.remove(pH_Wert.name)
            if pH_Wert.name in DK1_EL:
                DK1_EL.remove(pH_Wert.name)
            if pH_Wert.name in DK2_EL:
                DK2_EL.remove(pH_Wert.name)
            if pH_Wert.name in DK3_EL:
                DK3_EL.remove(pH_Wert.name)
            if pH_Wert.name in Higher_DK3_EL:
                Higher_DK3_EL.remove(pH_Wert.name)
            if pH_Wert.name in GEO_EL_Eingehalten:
                GEO_EL_Eingehalten.remove(pH_Wert.name)
            if pH_Wert.name in GEO_EL_Ueberschritten:
                GEO_EL_Ueberschritten.remove(pH_Wert.name)
            if pH_Wert.name in REK_EL_Eingehalten:
                REK_EL_Eingehalten.remove(pH_Wert.name)
            if pH_Wert.name in REK_EL_Ueberschritten:
                REK_EL_Ueberschritten.remove(pH_Wert.name)

            if 5.5 <= pH_Wert.wert_EL <= 13 and i.wert_EL != 10000000:
                DK0_EL.extend({pH_Wert.name})
            # Für DK1 und DK2 gibt es keine Einstufung (gleich wie DK3)
            elif (4 <= pH_Wert.wert_EL < 5.5) and i.wert_EL != 10000000:
                DK3_EL.extend({pH_Wert.name})
            elif pH_Wert.wert_EL < 4 or pH_Wert.wert_EL > 13 and i.wert_EL != 10000000:
                Higher_DK3_EL.extend({pH_Wert.name})

            # pH Wert GEO
            print("ph-wert:", pH_Wert.wert_EL)
            if 6.5 <= pH_Wert.wert_EL <= 9:
                GEO_EL_Eingehalten.extend({pH_Wert.name})
            elif pH_Wert.wert_EL < 6.5:
                GEO_EL_Ueberschritten.extend({pH_Wert.name})
            elif pH_Wert.wert_EL > 9 and pH_Wert.wert_EL != 10000000:
                GEO_EL_Ueberschritten.extend({pH_Wert.name})

            # pH Wert REK
            if 6.5 <= pH_Wert.wert_EL <= 9:
                REK_EL_Eingehalten.extend({pH_Wert.name})
            elif pH_Wert.wert_EL < 6.5 or pH_Wert.wert_EL > 9 and pH_Wert.wert_EL != 10000000:
                REK_EL_Ueberschritten.extend({pH_Wert.name})

            # Create Z0*_EL List
            Z0_Stern_EL = Z11_EL + Z12_EL + Z2_EL + Higher_Z2_EL
            # Data Outpu
            strZ0_TS = ', '.join(Z0_TS)  # Liste in string konvertieren
            strZ0_Stern_TS = ', '.join(Z0_Stern_TS)
            strZ1_TS = ', '.join(Z1_TS)
            strZ2_TS = ', '.join(Z2_TS)
            strHigher_Z2_TS = ', '.join(Higher_Z2_TS)
            strLAGA_TS_Anmerkungen = ', '.join(LAGA_TS_Anmerkungen)
            strZ0_EL = ', '.join(Z0_EL)
            strZ11_EL = ', '.join(Z11_EL)
            strZ12_EL = ', '.join(Z12_EL)
            strZ2_EL = ', '.join(Z2_EL)
            strHigher_Z2_EL = ', '.join(Higher_Z2_EL)
            strZ0_Stern_EL = ', '.join(Z0_Stern_EL)
            strLAGA_EL_Anmerkungen = ', '.join(LAGA_EL_Anmerkungen)
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
            strBBSchG_Anmerkungen = ', '.join(BBSchG_Anmerkungen)
            strDepV_Anmerkungen = ', '.join(DepV_Anmerkungen)
            strGefAbf_HH_SH_Eingehalten = ', '.join(GefAbf_HH_SH_Eingehalten)
            strGefAbf_HH_SH_Ueberschritten = ', '.join(GefAbf_HH_SH_Ueberschritten)
            strGefAbf_HH_SH_Ueberschritten_Stoffe = ', '.join(GefAbf_HH_SH_Ueberschritten_Stoffe)
            strGefAbf_NDS_Eingehalten = ', '.join(GefAbf_NDS_Eingehalten)
            strGefAbf_NDS_Ueberschritten = ', '.join(GefAbf_NDS_Ueberschritten)
            strGefAbf_NDS_Ueberschritten_Stoffe = ', '.join(GefAbf_NDS_Ueberschritten_Stoffe)
            strGefAbf_Anmerkungen = ', '.join(GefAbf_Anmerkungen)


            # BBSchG -> Falls in Liste mehr als 0 items, dann Notiz: Vorsorgewerte ueberschritten
            del BBSchG_Vorsorgewerte_ueberschritten[:]  # Deletes contenct of the list
            if len(strBBSchG_Ueberschritten) > 0:
                BBSchG_Vorsorgewerte_ueberschritten.extend(["Ja"])
            elif len(strBBSchG_Ueberschritten) == 0:
                BBSchG_Vorsorgewerte_ueberschritten.extend(["Nein"])
            strBBSchG_Vorsorgewerte_ueberschritten = ', '.join(BBSchG_Vorsorgewerte_ueberschritten)

            # GefAbfall -> Falls in Liste mehr als 0 items, dann Notiz: Grenzwert ueberschritten
            del GefAbf_NDS_Ueberschritten[:]  # Deletes contenct of the list
            if len(strGefAbf_NDS_Ueberschritten) > 0:
                GefAbf_NDS_Ueberschritten.extend(["Ja"])
            elif len(strGefAbf_NDS_Ueberschritten) == 0:
                GefAbf_NDS_Ueberschritten.extend(["Nein"])
            strGefAbf_NDS_Ueberschritten = ', '.join(GefAbf_NDS_Ueberschritten)

            del GefAbf_HH_SH_Ueberschritten[:]  # Deletes contenct of the list
            if len(strGefAbf_HH_SH_Ueberschritten) > 0:
                GefAbf_HH_SH_Ueberschritten.extend(["Ja"])
            elif len(strGefAbf_HH_SH_Ueberschritten) == 0:
                GefAbf_HH_SH_Ueberschritten.extend(["Nein"])
            strGefAbf_HH_SH_Ueberschritten = ', '.join(GefAbf_HH_SH_Ueberschritten)

            # Create PDF
            pdf = fpdf.FPDF(format='letter')
            pdf.add_page()

            pdf.set_font('Arial', size=14)
            pdf.cell(w=0, h=8, border=1, align="L", txt='Probenbezeichnung:  ' + str(entry0.get()), ln=1)
            pdf.cell(w=0, h=8, border=1, align="L", txt='Probenahmedatum:  ' + str(entry00.get()), ln=1)
            pdf.cell(w=0, h=8, border=0, align="L", ln=1)

            pdf.set_fill_color(180)

            pdf.set_font('Arial', 'B', size=14)
            pdf.cell(w=0, h=8, border=1, align="L", txt='Vorsorgewerte für Böden nach § 8 Abs. 2 Nr. 1 des Bundes-Bodenschutzgesetzes', ln=1, fill=True)
            pdf.set_font('Arial', size=11)
            pdf.cell(w=55, h=8, border=1, align="L", txt='Vorsorgewerte überschritten:')
            pdf.cell(w=0, h=8, border=1, align="L", txt=strBBSchG_Vorsorgewerte_ueberschritten, ln=1)

            pdf.cell(w=55, h=8, border=1, align="L", txt='Überschreitung für:')
            pdf.multi_cell(w=0, h=8, border=1, align="L", txt=strBBSchG_Ueberschritten)
            pdf.cell(w=55, h=8, border=1, align="L", txt='Anmerkungen:')
            pdf.multi_cell(w=0, h=8, border=1, align="L", txt=strBBSchG_Anmerkungen)
            pdf.cell(w=0, h=8, border=0, align="L", ln=1)

            pdf.set_font('Arial', 'B', size=14)
            pdf.cell(w=0, h=8, border=1, align="L", txt='Einbauklasse nach LAGA TR Boden 2004', ln=1, fill=True)
            pdf.set_font('Arial', size=11)
            pdf.cell(w=30, h=8, border=1, align="L", txt='Feststoff')
            pdf.multi_cell(w=0, h=8, border=1, align="L", txt='>Z2: ' + strHigher_Z2_TS)
            pdf.cell(w=30, h=8, border=1, align="L")
            pdf.multi_cell(w=0, h=8, border=1, align="L", txt='Z2: ' + strZ2_TS)
            pdf.cell(w=30, h=8, border=1, align="L")
            pdf.multi_cell(w=0, h=8, border=1, align="L", txt='Z1: ' + strZ1_TS)
            pdf.cell(w=30, h=8, border=1, align="L")
            pdf.multi_cell(w=0, h=8, border=1, align="L", txt='>Z0*: ' + strZ0_Stern_TS)
            pdf.cell(w=30, h=8, border=1, align="L", txt='Anmerkungen:')
            pdf.multi_cell(w=0, h=8, border=1, align="L", txt=strLAGA_TS_Anmerkungen)
            pdf.cell(w=0, h=8, border=0, align="L", ln=1)

            pdf.cell(w=30, h=8, border=1, align="L", txt='Eluat')
            pdf.multi_cell(w=0, h=8, border=1, align="L", txt='>Z2: ' + strHigher_Z2_EL)
            pdf.cell(w=30, h=8, border=1, align="L")
            pdf.multi_cell(w=0, h=8, border=1, align="L", txt='Z2: ' + strZ2_EL)
            pdf.cell(w=30, h=8, border=1, align="L")
            pdf.multi_cell(w=0, h=8, border=1, align="L", txt='Z1.2: ' + strZ12_EL)
            pdf.cell(w=30, h=8, border=1, align="L")
            pdf.multi_cell(w=0, h=8, border=1, align="L", txt='Z1.1: ' + strZ11_EL)
            pdf.cell(w=30, h=8, border=1, align="L")
            pdf.multi_cell(w=0, h=8, border=1, align="L", txt='>Z0*: ' + strZ0_Stern_EL)
            pdf.cell(w=30, h=8, border=1, align="L", txt='Anmerkungen:')
            pdf.multi_cell(w=0, h=8, border=1, align="L", txt=strLAGA_EL_Anmerkungen)
            pdf.cell(w=0, h=8, border=0, align="L", ln=1)

            pdf.add_page()

            pdf.set_fill_color(180)

            pdf.set_font('Arial', 'B', size=14)
            pdf.cell(w=0, h=8, border=1, align="L", txt='Deponieverordnung', ln=1, fill=True)
            pdf.set_font('Arial', size=11)
            pdf.cell(w=19, h=8, border=1, align="L", txt='Feststoff')
            pdf.multi_cell(w=0, h=8, border=1, align="L", txt='>DK3: ' + strHigher_DK3_TS)
            pdf.cell(w=19, h=8, border=1, align="L")
            pdf.multi_cell(w=0, h=8, border=1, align="L", txt='DK3: ' + strDK3_TS)
            pdf.cell(w=19, h=8, border=1, align="L")
            pdf.multi_cell(w=0, h=8, border=1, align="L", txt='DK2: ' + strDK2_TS)
            pdf.cell(w=19, h=8, border=1, align="L")
            pdf.multi_cell(w=0, h=8, border=1, align="L", txt='DK1: ' + strDK1_TS)
            pdf.cell(w=19, h=8, border=1, align="L", txt='Eluat')
            pdf.multi_cell(w=0, h=8, border=1, align="L", txt='>DK3: ' + strHigher_DK3_EL)
            pdf.cell(w=19, h=8, border=1, align="L")
            pdf.multi_cell(w=0, h=8, border=1, align="L", txt='DK3: ' + strDK3_EL)
            pdf.cell(w=19, h=8, border=1, align="L")
            pdf.multi_cell(w=0, h=8, border=1, align="L", txt='DK2: ' + strDK2_EL)
            pdf.cell(w=19, h=8, border=1, align="L")
            pdf.multi_cell(w=0, h=8, border=1, align="L", txt='DK1: ' + strDK1_EL)

            pdf.set_font('Arial', 'B', size=11)
            pdf.cell(w=0, h=8, border=1, align="L", txt='Grenzwerüberschreitung Rekultivierungsschicht', ln=1)
            pdf.set_font('Arial', size=11)
            pdf.multi_cell(w=0, h=8, border=1, align="L", txt='Feststoff: ' + strREK_TS_Ueberschritten)
            pdf.multi_cell(w=0, h=8, border=1, align="L", txt='Eluat: ' + strREK_EL_Ueberschritten)

            pdf.set_font('Arial', 'B', size=11)
            pdf.multi_cell(w=0, h=8, border=1, align="L", txt='Grenzwertüberschreitung Geologische Barriere')
            pdf.set_font('Arial', size=11)
            pdf.multi_cell(w=0, h=8, border=1, align="L", txt='Feststoff: ' + strGEO_TS_Ueberschritten)
            pdf.multi_cell(w=0, h=8, border=1, align="L", txt='Eluat: ' + strGEO_EL_Ueberschritten)
            pdf.multi_cell(w=0, h=8, border=1, align="L", txt='Folgende Fußnoten der Tabelle 2 beachten: ' + strDepV_Anmerkungen)
            pdf.cell(w=0, h=8, border=0, align="L", ln=1)

            pdf.set_font('Arial', 'B', size=14)
            pdf.cell(w=0, h=8, border=1, align="L", txt='Gefährlicher Abfall', ln=1, fill=True)
            pdf.set_font('Arial', size=11)
            pdf.cell(w=90, h=8, border=1, align="L", txt='Vorsorgewerte für S-H / Hamburg eingehalten: ' + strGefAbf_HH_SH_Ueberschritten)
            pdf.cell(w=90, h=8, border=1, align="L", txt='Überschreitung für: ' + strGefAbf_HH_SH_Ueberschritten_Stoffe)
            pdf.cell(w=0, h=8, border=1, align="L", txt='Arsen, Kupfer, Blei', ln=1)
            pdf.cell(w=90, h=8, border=1, align="L", txt='Vorsorgewerte für Niedersachsen eingehalten:')
            pdf.cell(w=0, h=8, border=1, align="L", txt='Nein', ln=1)
            pdf.cell(w=90, h=8, border=1, align="L", txt='Überschreitung für:')
            pdf.cell(w=0, h=8, border=1, align="L", txt='Arsen, Kupfer, Blei', ln=1)

            safe_file = tkinter.filedialog.asksaveasfilename(initialdir="/", title="Speichern unter",
                                                             filetypes=(("PDF", "*.pdf"), ("all files", "*.*")))
            pdf.output(safe_file + ".pdf")

            # Create WORD-DOCUMENT
            

        except ValueError:
            resultLabel.config(text="Werte prüfen", bg="red")

        except NameError: #var1 bodenart, var2 humus, var4 schluffgehalt
            if var1.get() == 0 and var2.get() == 0:
                resultLabel.config(text="Bodenart/Humusanteil wählen", bg="red")
            if var1.get() == 0 and var2.get() != 0:
                resultLabel.config(text="Bodenart wählen", bg="red")
            if var1.get() != 0 and var2.get() == 0:
                resultLabel.config(text="Humusanteil wählen", bg="red")
            if var1.get() == 3 and var4.get() == 0 and var2.get() == 0:
                resultLabel.config(text="Humus/Schluffanteil wählen", bg="red")
            if var1.get() == 3 and var4.get() == 0 and var2.get() != 0:
                resultLabel.config(text="Schluffanteil wählen", bg="red")


# Run GUI-Programm
root = Tk()

# Frame title
root.title("  Boden- und abfallrechtliche Bewertung (Copyright: Johannes Krohn)")

# Icon
root.iconbitmap("C:/Users/Johannes/Documents/Programmieren/Python/Deklarationsanalyse/icon2.ico")

# Frame geometry
root.geometry(
    "1300x850+0+0")  # The first two parameters are the width and height of the window. The last two parameters are x and y screen coordinates. You can specify the required x and y coordinates
root.resizable(0, 0)  # Don't allow resizing in the x or y direction

# Frame icon
# root.iconbitmap

# input picture
# img = ImageTk.PhotoImage(Image.open(path))

# Variablen fuer Bodenart- und Humusfunktion
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4= IntVar()

# Objekte ("Instance") herstellen, welche das "self" in der Klasse GUI ersetzen
# Parameter Feststoff + Eluat
# 0 = Platzhalterwert

Arsen = GUI(root, "Arsen", 0, 0,
            20, 15, 10, 15, 45, 150,  # LAGA Feststoff Grenzwerte (Z0 Ton, Z0 Lehm/Schluff, Z0 Sa, Z0 Stern, Z1, Z2)
            14, 14, 20, 60,  # LAGA Eluat Grenzwerte (Z0, Z1.1, Z1.2, Z2)
            0, 0, 0, 0, 0, # BBSchG Grenzwerte (Limit_BBSchG_T, Limit_BBSchG_SL, Limit_BBSchG_Sa, Limit_BBSchG_HumusU8, Limit_BBSchG_HumusUE8)
            0, 0, 0, 0,  # DepV Feststoff Deponieklasse Grenzwerte (DK0, DKI, DKII, DKIII)
            0,  # DepV Feststoff Rekultivierungsschicht (REK) Grenzwert
            0,  # DepV Feststoff Geologische Barriere (GEO) Grenzwert
            50, 200, 200, 2500,  # DepV Eluat Deponieklasse Grenzwerte
            10,  # DepV Eluat Rekultivierungsschicht (REK) Grenzwert
            10,  # DepV Eluat Geologische Barriere (GEO) Grenzwert
            0,   # Gefährlicher Abfall SH+HH
            0)    # Gefährlicher Abfall NDS

Blei = GUI(root, "Blei", 0, 0,
           100, 70, 40, 140, 210, 700,
           40, 40, 80, 200,
           100, 70, 40, 0, 0,
           0, 0, 0, 0,
           140,
           0,
           50, 200, 1000, 5000,
           40,
           20,
           0,
           0)
Cadmium = GUI(root, "Cadmium", 0, 0,
              1.5, 1, 0.4, 1, 3, 10,
              1.5, 1.5, 3, 6,
              1.5, 1, 0.4, 0, 0,
              0, 0, 0, 0,
              1,
              0,
              4, 50, 100, 500,
              2,
              2,
              0,
              0)

Chrom_gesamt = GUI(root, "Chrom gesamt", 0, 0,
                   100, 60, 30, 120, 180, 600,
                   12.5, 12.5, 25, 60,
                   100, 60, 30, 0, 0,
                   0, 0, 0, 0,
                   120,
                   0,
                   50, 300, 1000, 7000,
                   30,
                   0,
                   0,
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
             50,
             0,
             0)
Nickel = GUI(root, "Nickel", 0, 0,
             70, 50, 15, 100, 150, 500,
             15, 15, 20, 70,
             70, 50, 15, 0, 0,
             0, 0, 0, 0,
             100,
             0,
             40, 200, 1000, 4000,
             50,
             40,
             0,
             0)
Quecksilber = GUI(root, "Quecksilber", 0, 0,
                  1, 0.5, 0.1, 1, 1.5, 5,
                  0.5, 0.5, 1, 2,
                  1, 0.5, 0.1, 0, 0,
                  0, 0, 0, 0,
                  1,
                  0,
                  1, 5, 20, 200,
                  0.2,
                  0.2,
                  0,
                  0)
Zink = GUI(root, "Zink", 0, 0,
           200, 150, 60, 300, 450, 1500,
           150, 150, 200, 600,
           200, 150, 60, 0, 0,
           0, 0, 0, 0,
           300,
           0,
           400, 2000, 5000, 20000,
           100,
           100,
           0,
           0)

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
          0,
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
                 0,
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
                                0,
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
                    0,
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
               0,
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
           0,
           0,
           0)
PAK_16 = GUI(root, "PAK16 (EPA)", 0, 0,
             3, 3, 3, 3, 3, 30,
             0, 0, 0, 0,
             0, 0, 0, 3, 10,
             30, 0, 0, 0,
             5,
             1,
             0, 0, 0, 0,
             0,
             0,
             0,
             0)
Benzopyren = GUI(root, "Benzo(a)pyren", 0, 0,
                 0.3, 0.3, 0.3, 0.6, 0.9, 3,
                 0, 0, 0, 0,
                 0, 0, 0, 0.3, 1,
                 0, 0, 0, 0,
                 0.6,
                 0,
                 0, 0, 0, 0,
                 0,
                 0,
                 0,
                 0)
PCB6 = GUI(root, "PCB6", 0, 0,
           0.05, 0.05, 0.05, 0.1, 0.15, 0.5,
           0, 0, 0, 0,
           0, 0, 0, 0.05, 0.1,
           0, 0, 0, 0,
           0,
           0,
           0, 0, 0, 0,
           0,
           0,
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
           0,
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
               0,
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
          0,
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
                   0,
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
                                      0,
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
                      0,
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
              0,
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
              0, 0, 0, 0,
              0,
              0,
              0,
              0)

Leitfaehigkeit = GUI(root, "Leitfähigkeit", 0, 0,
                     0, 0, 0, 0, 0, 0,
                     250, 250, 1500, 2000,
                     0, 0, 0, 0, 0,
                     0, 0, 0, 0,
                     0,
                     0,
                     0, 0, 0, 0,
                     500,
                     0,
                     0,
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
             0,
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
                10,
                0,
                0)
Phenolindex = GUI(root, "Phenolindex", 0, 0,
                  0, 0, 0, 0, 0, 0,
                  20, 20, 40, 100,
                  0, 0, 0, 0, 0,
                  0, 0, 0, 0,
                  0,
                  0,
                  100, 200, 50000, 100000,
                  0,
                  50,
                  0,
                  0)
Chlorid = GUI(root, "Chlorid", 0, 0,
              0, 0, 0, 0, 0, 0,
              30, 30, 50, 100,
              0, 0, 0, 0, 0,
              0, 0, 0, 0,
              0,
              0,
              80, 1500, 1500, 2500,
              10,
              10,
              0,
              0)
Sulfat = GUI(root, "Sulfat", 0, 0,
             0, 0, 0, 0, 0, 0,
             20, 20, 50, 200,
             0, 0, 0, 0, 0,
             0, 0, 0, 0,
             0,
             0,
             100, 2000, 2000, 5000,
             50,
             50,
             0,
             0)
DOC = GUI(root, "DOC", 0, 0,
          0, 0, 0, 0, 0, 0,
          0, 0, 0, 0,
          0, 0, 0, 0, 0,
          0, 0, 0, 0,
          0,
          0,
          50, 50, 80, 100,
          0,
          0,
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
              0,
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
             0,
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
                0,
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
              0,
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
            0,
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
                                       400,
                                       0,
                                       0)

print("Erfolgreich gestartet!")
# Laesst das GUI-Programm in einer loop laufen

root.mainloop()
