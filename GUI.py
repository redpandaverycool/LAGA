import tkinter
from tkinter import *

# Class main window
class GUI_main():
    def __init__(self, master):

        Label(master, text="").grid(row=0, sticky=E)
        Label(master, text="Probenbezeichnung:").grid(column= 0, row=2, sticky=N, padx=(100, 0))
        Label(master, text="Probenahmedatum:").grid(row=3, sticky=N, padx=(100, 0))
        Label(master, text="Hauptbodenart (HB):").grid(row=4, sticky=E)
        Label(master, text="Schluffgehalt wenn HB Sand:").grid(row=7, sticky=E)
        Label(master, text="Anteil Humus (TOC):").grid(row=9, sticky=E)
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
        Label(master, text="   Gesamtgehalt an gel. Stoffen").grid(row=23, column=6, sticky=E)
        Label(master, text="    Hinweise zur Werteeingabe:",fg="grey38", padx=0, pady=0).grid(row=18, column=0)
        Label(master, text="       Nachkommastellen: Komma oder Punkt",fg="grey38", padx=0, pady=0).grid(row=19, column=0)
        Label(master, text="Unter Bestimmungsgrenze: z.B. <0,5",fg="grey38", padx=0, pady=0).grid(row=20, column=0)
        Label(master, text="Nicht nachweisbar: n.n.",fg="grey38", padx=0, pady=0).grid(row=21, column=0)

        resultLabel = Label(root, text="")
        resultLabel.grid(row=21, column=1)

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

        Button(master, text="Lade GBA Prüfbericht", fg="black", bg="white", padx=2, pady=2).grid(row=18, column=1)
        Button(master, text="Zurücksetzen", bg="white", padx=2, pady=2).grid(row=19, column=1)
        Button(master, text="Bewertung", fg="black", bg="white", padx=2, pady=2).grid(row=20,column=1)
        Button(master, text="Beenden", command=root.destroy, bg="white", padx=2, pady=2).grid(row=22, column=1)
        Radiobutton(master, text="Ton", value=1).grid(row=6, column=1, sticky=W)
        Radiobutton(master, text="Schluff/Lehm", value=2).grid(row=5, column=1,sticky=W)
        Radiobutton(master, text="Sand", value=3).grid(row=4, column=1, sticky=W)
        Radiobutton(master, text="Nicht stark schluffhaltig (<40%)", value=4).grid(row=7, column=1, sticky=W)
        Radiobutton(master, text="Stark schluffhaltig (40 bis <50%)", value=5).grid(row=8, column=1, sticky=W)
        Radiobutton(master, text=">8% (>4%)", value=6).grid(row=9, column=1, sticky=W)
        Radiobutton(master, text="<=8% (<=4%)", value=7).grid(row=10, column=1,sticky=W)

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

        Options_Feststoff_Arsen = tkinter.OptionMenu(master,option_Feststoff_Arsen, "mg/kg TM", "μg/kg TM")
        Options_Feststoff_Blei = tkinter.OptionMenu(master, option_Feststoff_Blei,"mg/kg TM", "μg/kg TM")
        Options_Feststoff_Cadmium = tkinter.OptionMenu(master, option_Feststoff_Cadmium, "mg/kg TM", "μg/kg TM")
        Options_Feststoff_Chromgesamt = tkinter.OptionMenu(master, option_Feststoff_Chromgesamt, "mg/kg TM", "μg/kg TM")
        Options_Feststoff_Kupfer = tkinter.OptionMenu(master, option_Feststoff_Kupfer, "mg/kg TM", "μg/kg TM")
        Options_Feststoff_Nickel = tkinter.OptionMenu(master, option_Feststoff_Nickel, "mg/kg TM", "μg/kg TM",)
        Options_Feststoff_Quecksilber = tkinter.OptionMenu(master, option_Feststoff_Quecksilber, "mg/kg TM", "μg/kg TM")
        Options_Feststoff_Thallium = tkinter.OptionMenu(master, option_Feststoff_Thallium, "mg/kg TM", "μg/kg TM")
        Options_Feststoff_Zink = tkinter.OptionMenu(master, option_Feststoff_Zink, "mg/kg TM", "μg/kg TM")
        Options_Feststoff_EOX = tkinter.OptionMenu(master, option_Feststoff_EOX, "mg/kg TM", "μg/kg TM")
        Options_Feststoff_KWC1040 = tkinter.OptionMenu(master, option_Feststoff_Kohlenwasserstoffe_C10C40, "mg/kg TM", "μg/kg TM")
        Options_Feststoff_KWC1022 = tkinter.OptionMenu(master, option_Feststoff_Kohlenwasserstoffe_C10C22, "mg/kg TM", "μg/kg TM")
        Options_Feststoff_Cyanidgesamt = tkinter.OptionMenu(master, option_Feststoff_Cyanidegesamt, "mg/kg TM", "μg/kg TM")
        Options_Feststoff_BTX = tkinter.OptionMenu(master, option_Feststoff_BTX, "mg/kg TM", "μg/kg TM")
        Options_Feststoff_LHKW = tkinter.OptionMenu(master, option_Feststoff_LHKW, "mg/kg TM", "μg/kg TM")
        Options_Feststoff_PAK16 = tkinter.OptionMenu(master, option_Feststoff_PAK16, "mg/kg TM", "μg/kg TM")
        Options_Feststoff_Benzoapyren = tkinter.OptionMenu(master, option_Feststoff_Benzoapyren, "mg/kg TM", "μg/kg TM")
        Options_Feststoff_PCB6 = tkinter.OptionMenu(master, option_Feststoff_PCB6, "mg/kg TM", "μg/kg TM")
        Options_Feststoff_PCB7 = tkinter.OptionMenu(master, option_Feststoff_PCB7, "mg/kg TM", "μg/kg TM")
        Options_Feststoff_TOC = tkinter.OptionMenu(master, option_Feststoff_TOC, "Masse-% TM")
        Options_Feststoff_Gluehverlust = tkinter.OptionMenu(master, option_Feststoff_Gluehverlust, "Masse-% TM")
        Options_Feststoff_Saeuren = tkinter.OptionMenu(master, option_Feststoff_Saeureneutralisationskapazitaet, "mmol/kg TM")
        Options_Feststoff_LipophileStoffe = tkinter.OptionMenu(master, option_Feststoff_LipophileStoffe, "Masse-%")
        Options_Feststoff_Dioxine = tkinter.OptionMenu(master, option_Feststoff_Dioxine, "ng/kg TM","μg/kg TM","mg/kg TM")
        Options_Eluat_Arsen = tkinter.OptionMenu(master, option_Eluat_Arsen, "μg/L","mg/L")
        Options_Eluat_Blei = tkinter.OptionMenu(master, option_Eluat_Blei, "μg/L","mg/L")
        Options_Eluat_Cadmium = tkinter.OptionMenu(master, option_Eluat_Cadmium, "μg/L","mg/L")
        Options_Eluat_Chromgesamt = tkinter.OptionMenu(master, option_Eluat_Chromgesamt, "μg/L","mg/L")
        Options_Eluat_Kupfer = tkinter.OptionMenu(master, option_Eluat_Kupfer, "μg/L","mg/L")
        Options_Eluat_Nickel = tkinter.OptionMenu(master, option_Eluat_Nickel, "μg/L","mg/L")
        Options_Eluat_Quecksilber = tkinter.OptionMenu(master, option_Eluat_Quecksilber, "μg/L","mg/L")
        Options_Eluat_Zink = tkinter.OptionMenu(master, option_Eluat_Zink, "μg/L","mg/L")
        Options_Eluat_Cyanid = tkinter.OptionMenu(master, option_Eluat_Cyanid, "μg/L","mg/L")
        Options_Eluat_Cyanidleichtf = tkinter.OptionMenu(master, option_Eluat_Cyanidleichtf, "μg/L","mg/L")
        Options_Eluat_Phenolindex = tkinter.OptionMenu(master, option_Eluat_Phenolindex, "μg/L","mg/L")
        Options_Eluat_Chlorid = tkinter.OptionMenu(master, option_Eluat_Chlorid,"mg/L", "μg/L")
        Options_Eluat_Sulfat = tkinter.OptionMenu(master, option_Eluat_Sulfat,"mg/L", "μg/L")
        Options_Eluat_Leitfaehigkeit = tkinter.OptionMenu(master, option_Eluat_Leitf,"μS/cm")
        Options_Eluat_DOC = tkinter.OptionMenu(master, option_Eluat_DOC,"mg/L","μg/L")
        Options_Eluat_Fluorid = tkinter.OptionMenu(master, option_Eluat_Fluorid,"mg/L","μg/L")
        Options_Eluat_Barium = tkinter.OptionMenu(master, option_Eluat_Barium,"mg/L","μg/L")
        Options_Eluat_Molybdaen = tkinter.OptionMenu(master, option_Eluat_Molybdaen,"μg/L", "mg/L")
        Options_Eluat_Antimon = tkinter.OptionMenu(master, option_Eluat_Antimon,"μg/L", "mg/L")
        Options_Eluat_Selen = tkinter.OptionMenu(master, option_Eluat_Selen,"μg/L", "mg/L")
        Options_Eluat_GesGehaltGelStoffe = tkinter.OptionMenu(master, option_Eluat_GesGehaltGelStoffe, "mg/L", "μg/L")

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
        Options_Eluat_Leitfaehigkeit.grid(row=16, column=8)
        Options_Eluat_DOC.grid(row=17, column=8)
        Options_Eluat_Fluorid.grid(row=18, column=8)
        Options_Eluat_Barium.grid(row=19, column=8)
        Options_Eluat_Molybdaen.grid(row=20, column=8)
        Options_Eluat_Antimon.grid(row=21, column=8)
        Options_Eluat_Selen.grid(row=22, column=8)
        Options_Eluat_GesGehaltGelStoffe.grid(row=23, column=8)

# Create and run main window in loop
if __name__ == "__main__":
    root = Tk()

    root.title("  BAB-Tool (Boden- und abfallrechtliche Bewertung)      © Johannes Krohn")# Frame title

    w = 1280 # width for the Tk root
    h = 820 # height for the Tk root
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    x = (ws/2) - (w/2) # calculate x and y coordinates for the Tk root window
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y)) # set the dimensions of the screen and where it is placed

    GUI_main(root)
    print("Erfolgreich gestartet!")
    root.mainloop() # loop function

