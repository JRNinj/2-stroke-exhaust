import math
import tkinter as tk
import csv
import os
from tkinter import filedialog

def try_convert_to_float(input_string):
    try:
        float_value = float(input_string)
        return float_value
    except ValueError:
        return None  

def calc_exhaust():
    # ALL DATA IN 'mm'

    if try_convert_to_float(entry0.get()) == None or try_convert_to_float(entry1.get()) == None or try_convert_to_float(entry2.get()) == None:
        if lang_var.get() == "English":
            label4.config(text="Please enter the required data!")
        elif lang_var.get() == "Deutsch":
            label4.config(text="Bitte geben Sie die benötigten Daten ein!")
        return
    else:
        label4.config(text="")

    # Create Global Vars
    global outlet_surface
    global outlet_tax_time
    global n
    global temp_gases
    global pip_width_multiplicator
    global header_multiplicator
    global pipe_multiplicator
    global header_width
    global header_length
    global stinger_length
    global stinger_width
    global diffuser_length
    global pipe_length
    global pipe_width
    global reflector_length

    ## Important Data
    outlet_surface = float(entry0.get()) # Auslass Durchmesser
    outlet_tax_time = float(entry1.get()) # Auslasssteuerzeit (Winkel mit dem sich die Kurbelwelle dreht in °)
    n = float(entry2.get()) # Drehzahl in 1/min

    ## Settings Data
    temp_gases = float(entry3.get()) # Abgastemperatur in °C 200 - 300 °C normalerweise
    pip_width_multiplicator = float(entry4.get()) # Variabler Wert, umso größer -> schmaleres Drehzahlband, umso kleiner -> breiteres Drehzahlband
    header_multiplicator = float(entry5.get()) # ##Werte: 6 - 12## Variabler Wert, umso größer -> schmaleres Drehzahlband, umso kleiner -> breiteres Drehzahlband
    pipe_multiplicator = float(entry6.get()) # ##Werte: 0.2 - 0.4## Variabler Wert

    ## Calculation
    header_width = math.sqrt((outlet_surface * 1.2) / math.pi) * 2 # Krümmerdurchmesser
    header_length = header_width * header_multiplicator # Krümmerlänge
    stinger_width = header_width * 0.55 # Endrohr Durchmesser
    stinger_length = stinger_width * 12 # Endrohr Länge
    c = 331 + 0.6 * temp_gases # Schallgeschwindigkeit
    diffuser_reflector_length = ((c * outlet_tax_time) * 1000 / (12 * n)) - header_length # Länge von Konus bis 2/3 des Gegenkonus
    diffuser_length = (diffuser_reflector_length / 1.23) * (1 - pipe_multiplicator) # Konuslänge
    pipe_length = (diffuser_reflector_length / 1.23) * pipe_multiplicator # Länge des zylindrischen Rohres zw. Konus u. Gegenkonus
    pipe_width = math.pow((pip_width_multiplicator * math.pow(header_width, 2)), 0.5) # Breite des Mittelstücks und Konus
    reflector_length = diffuser_length * 0.5 # Gegenkonuslänge

    if lang_var.get() == "English":
        label_header_w.config(text="Header Width: {:.0f}mm".format(header_width))
        label_header_l.config(text="Header Length: {:.0f}mm".format(header_length))
        label_diffuser.config(text="Diffuser Length: {:.0f}mm".format(diffuser_length))
        label_pipe_w.config(text="Pipe Width: {:.0f}mm".format(pipe_width))
        label_pipe_l.config(text="Pipe Length: {:.0f}mm".format(pipe_length))
        label_reflector.config(text="Reflector Length: {:.0f}mm".format(reflector_length))
        label_stinger_w.config(text="Stinger Width: {:.0f}mm".format(stinger_width))
        label_stinger_l.config(text="Stinger Length: {:.0f}mm".format(stinger_length))
    elif lang_var.get() == "Deutsch":
        label_header_w.config(text="Krümmerbreite: {:.0f}mm".format(header_width))
        label_header_l.config(text="Krümmerlänge: {:.0f}mm".format(header_length))
        label_diffuser.config(text="Konuslänge: {:.0f}mm".format(diffuser_length))
        label_pipe_w.config(text="Rohrbreite: {:.0f}mm".format(pipe_width))
        label_pipe_l.config(text="Rohrlänge: {:.0f}mm".format(pipe_length))
        label_reflector.config(text="Gegenkonuslänge: {:.0f}mm".format(reflector_length))
        label_stinger_w.config(text="Endrohrbreite: {:.0f}mm".format(stinger_width))
        label_stinger_l.config(text="Endrohrlänge: {:.0f}mm".format(stinger_length))

    print("Your Exhaust Data: \nHeader - Length: {:.2f} - Width: {:.2f} \nDiffuser - Length: {:.2f} \nPipe - Length: {:.2f} - Width: {:.2f} \nReflector - Length: {:.2f} \nStinger - Length: {:.2f} - Width: {:.2f}".format(header_length, header_width, diffuser_length, pipe_length, pipe_width, reflector_length, stinger_length, stinger_width))

def set_config_data(scale):
    if slider0.get() == 3:
        entry3.delete(0, tk.END)
        entry3.insert(0, 275)
        entry4.delete(0, tk.END)
        entry4.insert(0, 12)
        entry5.delete(0, tk.END)
        entry5.insert(0, 8)
        entry6.delete(0, tk.END)
        entry6.insert(0, 0.3)
    elif slider0.get() == 4:
        entry3.delete(0, tk.END)
        entry3.insert(0, 281.6)
        entry4.delete(0, tk.END)
        entry4.insert(0, 14)
        entry5.delete(0, tk.END)
        entry5.insert(0, 7)
        entry6.delete(0, tk.END)
        entry6.insert(0, 0.2)
    elif slider0.get() == 5:
        entry3.delete(0, tk.END)
        entry3.insert(0, 285)
        entry4.delete(0, tk.END)
        entry4.insert(0, 17)
        entry5.delete(0, tk.END)
        entry5.insert(0, 6)
        entry6.delete(0, tk.END)
        entry6.insert(0, 0.2)
    elif slider0.get() == 2:
        entry3.delete(0, tk.END)
        entry3.insert(0, 270)
        entry4.delete(0, tk.END)
        entry4.insert(0, 11)
        entry5.delete(0, tk.END)
        entry5.insert(0, 9)
        entry6.delete(0, tk.END)
        entry6.insert(0, 0.4)
    elif slider0.get() == 1:
        entry3.delete(0, tk.END)
        entry3.insert(0, 267.3)
        entry4.delete(0, tk.END)
        entry4.insert(0, 9)
        entry5.delete(0, tk.END)
        entry5.insert(0, 11)
        entry6.delete(0, tk.END)
        entry6.insert(0, 0.4)

def switch_lang(lang):
    if lang == "English":
        lang_var.set("English")
        window.title("2-Stroke Exhaust Calculator   GUI")
        label.config(text="2-Stroke Exhaust Calculator")
        label1.config(text="Outlet Surface:")
        label2.config(text="Outlet Tax Time:")
        label3.config(text="RPM:")
        label4.config(text="")
        label26.config(text="")
        label7.config(text="Gas Temperature:")
        label8.config(text="Pipe Width Multiplicator:")
        label9.config(text="Header Multiplicator:")
        label10.config(text="Pipe Length Multiplicator")
        label5.config(text="flat")
        label6.config(text="sharp")
        button0.config(text="Calculate Exhaust >")
        button1.config(text="Exit")
        if "header_length" not in globals():
            label_header_l.config(text="Header Length: ---")
            label_header_w.config(text="Header Width: ---")
            label_diffuser.config(text="Diffuser Length: ---")
            label_pipe_l.config(text="Pipe Length: ---")
            label_pipe_w.config(text="Pipe Width: ---")
            label_reflector.config(text="Reflector Length: ---")
            label_stinger_l.config(text="Stinger Length: ---")
            label_stinger_w.config(text="Stinger Width: ---")
        else:
            label_header_l.config(text="Header Length: {:.0}mm".format(header_length))
            label_header_w.config(text="Header Width: {:.0f}mm".format(header_width))
            label_diffuser.config(text="Diffuser Length: {:.0f}mm".format(diffuser_length))
            label_pipe_l.config(text="Pipe Length: {:.0f}mm".format(pipe_length))
            label_pipe_w.config(text="Pipe Width: {:.0f}mm".format(pipe_width))
            label_reflector.config(text="Reflector Length: {:.0f}mm".format(reflector_length))
            label_stinger_l.config(text="Stinger Length: {:.0f}mm".format(stinger_length))
            label_stinger_w.config(text="Stinger Width: {:.0f}mm".format(stinger_width))
        label21.config(text="Header")
        label22.config(text="Diffuser")
        label23.config(text="Pipe")
        label24.config(text="Reflector")
        label25.config(text="Stinger")
        label100.config(text="created with 💛 by Jannick Richter")
        button2.config(text="Export Data")
        if label4.cget("text") != "":
            label4.config(text="Please enter the required data!")
        label11.config(text="All data in mm")
    elif lang == "Deutsch":
        lang_var.set("Deutsch")
        window.title("2-Takt Auspuff Rechner    GUI")
        label.config(text="2-Takt Auspuff Rechner")
        label1.config(text="Auslass Fläche:")
        label2.config(text="Auslasssteuerzeit:")
        label3.config(text="Drehzahl:")
        label4.config(text="")
        label26.config(text="")
        label7.config(text="Gas Temperatur:")
        label8.config(text="Rohrbreite Multiplikator:")
        label9.config(text="Krümmer Multiplikator:")
        label10.config(text="Rohrlänge Multiplikator:")
        label5.config(text="flach")
        label6.config(text="spitz")
        button0.config(text="Auspuff berechnen >")
        button1.config(text="Verlassen")
        if "header_length" not in globals():
            label_header_l.config(text="Krümmerlänge: ---")
            label_header_w.config(text="Krümmerbreite: ---")
            label_diffuser.config(text="Konuslänge: ---")
            label_pipe_l.config(text="Rohrlänge: ---")
            label_pipe_w.config(text="Rohrbreite: ---")
            label_reflector.config(text="Gegenkonuslänge: ---")
            label_stinger_l.config(text="Endrohrlänge: ---")
            label_stinger_w.config(text="Endrohrbreite: ---")
        else:
            label_header_l.config(text="Krümmerlänge: {:.0}mm".format(header_length))
            label_header_w.config(text="Krümmerbreite: {:.0f}mm".format(header_width))
            label_diffuser.config(text="Konuslänge: {:.0f}mm".format(diffuser_length))
            label_pipe_l.config(text="Rohrlänge: {:.0f}mm".format(pipe_length))
            label_pipe_w.config(text="Rohrbreite: {:.0f}mm".format(pipe_width))
            label_reflector.config(text="Gegenkonuslänge: {:.0f}mm".format(reflector_length))
            label_stinger_l.config(text="Endrohrlänge: {:.0f}mm".format(stinger_length))
            label_stinger_w.config(text="Endrohrbreite: {:.0f}mm".format(stinger_width))
        label21.config(text="Krümmer")
        label22.config(text="Konus")
        label23.config(text="Rohr")
        label24.config(text="Gegenkonus")
        label25.config(text="Endrohr")
        label100.config(text="programmiert mit 💛 von Jannick Richter")
        button2.config(text="Daten Exportieren")
        label11.config(text="Alle Angaben in mm")

def create_save_file():
    if not os.path.exists('save_data.csv'):
        with open('save_data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            data = [
        ['language'],
        ['English']
]

            # Daten in die CSV-Datei schreiben
            writer.writerows(data)
create_save_file()

window = tk.Tk()
window.geometry("700x800")
window.title("2-Stroke Exhaust Calculator   GUI")
window.iconbitmap("race.ico")

canvas1 =tk.Canvas(window, width=700, height=50, relief='raised')
canvas1.pack()

label = tk.Label(window, text="2-Stroke Exhaust Calculator", font=("Calibri", 25))
canvas1.create_window(350, 25, window=label)

#all in mm
label11 = tk.Label(window, text="All data in mm", foreground="white", background="gray", font=("Calibri", 14))
canvas1.create_window(80, 25, window=label11)

#dropdown language
lang_var = tk.StringVar()
lang_var.set("English")
dropdown0 = tk.OptionMenu(window, lang_var, "English", "Deutsch", command=switch_lang)
canvas1.create_window(650, 25, window=dropdown0)

canvas0 = tk.Canvas(window, width=700, height=800, relief='raised')
canvas0.pack()

# outlet 

label1 = tk.Label(window, text="Outlet Surface:")
label1.config(font=('helvetica', 14))
canvas0.create_window(150, 25, window=label1)

entry0 = tk.Entry(window)
canvas0.create_window(150, 65, window=entry0)

# outlet tax time
label2 = tk.Label(window, text="Outlet Tax Time:")
label2.config(font=('helvetica', 14))
canvas0.create_window(350, 25, window=label2)

entry1 = tk.Entry(window)
canvas0.create_window(350, 65, window=entry1)

# rpm
label3 = tk.Label(window, text="RPM:")
label3.config(font=('helvetica', 14))
canvas0.create_window(550, 25, window=label3)

entry2 = tk.Entry(window)
canvas0.create_window(550, 65, window=entry2)

#temp gases
label7 = tk.Label(window, text="Gas Temperature:", font=("helvetica", 11))
canvas0.create_window(100, 100, window=label7)
entry3 = tk.Entry(window, width=15)
entry3.insert(0, 281.6)
canvas0.create_window(100, 130, window=entry3)

#pipe multiplicator
label8 = tk.Label(window, text="Pipe Width Multiplicator:", font=("helvetica", 11))
canvas0.create_window(266, 100, window=label8)
entry4 = tk.Entry(window, width=15)
entry4.insert(0, 14)
canvas0.create_window(266, 130, window=entry4)

#header multiplicator
label9 = tk.Label(window, text="Header Multiplicator:", font=("helvetica", 11))
canvas0.create_window(432, 100, window=label9)
entry5 = tk.Entry(window, width=15)
entry5.insert(0, 8)
canvas0.create_window(432, 130, window=entry5)

#pipe multiplicator
label10 = tk.Label(window, text="Pipe Length Multiplicator:", font=("helvetica", 11))
canvas0.create_window(598, 100, window=label10)
entry6 = tk.Entry(window, width=15)
entry6.insert(0, 0.3)
canvas0.create_window(598, 130, window=entry6)


# spitz / flach
slider0 = tk.Scale(window, from_=1, to=5, orient="horizontal", length=200, command=set_config_data)
slider0.set(3)
canvas0.create_window(350, 175, window=slider0)

label5 = tk.Label(window, text="flat", font=("Calibri", 13))
canvas0.create_window(200, 179, window=label5)

label6 = tk.Label(window, text="sharp", font=("Calibri", 13))
canvas0.create_window(500, 179, window=label6)

#Calculate Button

button0 = tk.Button(window, text="Calculate Exhaust >", background="green", width=30, height=2, foreground="white", font=("Calibri", 14), command=calc_exhaust)
canvas0.create_window(350, 250, window=button0)

label4 = tk.Label(window, text="", foreground="red", font=("Calibri", 12))
canvas0.create_window(350, 300, window=label4)


# data
label_header_w = tk.Label(window, text="Header Width: ---", font=("Calibri", 14))
canvas0.create_window(200, 340, window=label_header_w)
label_header_l = tk.Label(window, text="Header Length: ---", font=("Calibri", 14))
canvas0.create_window(200, 370, window=label_header_l)

label_stinger_w = tk.Label(window, text="Stinger Width: ---", font=("Calibri", 14))
canvas0.create_window(200, 420, window=label_stinger_w)
label_stinger_l = tk.Label(window, text="Stinger Length: ---", font=("Calibri", 14))
canvas0.create_window(200, 450, window=label_stinger_l)

label_diffuser = tk.Label(window, text="Diffuser Length: ---", font=("Calibri", 14))
canvas0.create_window(500, 340, window=label_diffuser)

label_pipe_w = tk.Label(window, text="Pipe Width: ---", font=("Calibri", 14))
canvas0.create_window(500, 380, window=label_pipe_w)
label_pipe_l = tk.Label(window, text="Pipe Length: ---", font=("Calibri", 14))
canvas0.create_window(500, 410, window=label_pipe_l)

label_reflector = tk.Label(window, text="Reflector Length: ---", font=("Calibri", 14))
canvas0.create_window(500, 450, window=label_reflector)

# Exhaust Blueprint

canvas0.create_rectangle(100, 550, 200, 565)
canvas0.create_line(200, 550, 350, 520)
canvas0.create_line(200, 565, 350, 595)
canvas0.create_rectangle(350, 520, 400, 595)
canvas0.create_line(400, 595, 475, 560)
canvas0.create_line(400, 520, 475, 555)
canvas0.create_rectangle(475, 555, 575, 560)

label21 = tk.Label(window, text="Header", font=("Calibri", 8))
canvas0.create_window(150, 557, window=label21)
label22 = tk.Label(window, text="Diffuser", font=("Calibri", 8))
canvas0.create_window(275, 557, window=label22)
label23 = tk.Label(window, text="Pipe", font=("Calibri", 8))
canvas0.create_window(375, 557, window=label23)
label24 = tk.Label(window, text="Reflector", font=("Calibri", 8))
canvas0.create_window(435, 557, window=label24)
label25 = tk.Label(window, text="Stinger", font=("Calibri", 8))
canvas0.create_window(525, 557, window=label25)

#Exit Button

def quit_program():
    with open('save_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        data = [
        ['language'],
        [lang_var.get()]
]

        # Daten in die CSV-Datei schreiben
        writer.writerows(data)
    window.quit()

button1 = tk.Button(window, text="Exit", background="gray", foreground="red", width=20, height=1, font=("Calibri", 14), command=quit_program)
canvas0.create_window(200, 650, window=button1)

#Export Button

def export_successful():
    popup = tk.Toplevel()
    if lang_var.get() == "English":
        popup.title("Success")
        popup.geometry("250x100")
        popup.resizable(False, False)#

        canvas10 =tk.Canvas(popup, width=250, height=100, relief='raised')
        canvas10.pack()

        message_label = tk.Label(popup, text="Export was successful!", foreground="black", font=("Calibri", 14))
        canvas10.create_window(125, 30, window=message_label)

        ok_button = tk.Button(popup, text="Okay", background="green", foreground="white", border=5, command=popup.destroy)
        canvas10.create_window(125, 70, window=ok_button)
    elif lang_var.get() == "Deutsch":
        popup.title("Erfolg")
        popup.geometry("250x100")
        popup.resizable(False, False)#

        canvas10 =tk.Canvas(popup, width=250, height=100, relief='raised')
        canvas10.pack()

        message_label = tk.Label(popup, text="Export war erfolgreich!", foreground="black", font=("Calibri", 14))
        canvas10.create_window(125, 30, window=message_label)

        ok_button = tk.Button(popup, text="Okay", background="green", foreground="white", border=5, command=popup.destroy)
        canvas10.create_window(125, 70, window=ok_button)

def export_data():
    if "header_length" not in globals():
        if lang_var.get() == "English":
            label26.config(text="No data")
        elif lang_var.get() == "Deutsch":
            label26.config(text="Keine Daten")
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Dateien", "*.txt"), ("Alle Dateien", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            if lang_var.get() == "English":
                file.write("&&2-Stroke Exhaust Calculator by Jannick Richter - Export Data&&\n\n----------------------------------------------------\n\n")
                file.write("Input Values:\n\nOutlet Surface: {:.0f}mm\nOutlet Tax Time: {:.0f}°\nRPM: {:.0f} 1/min\n\n".format(outlet_surface, outlet_tax_time, n))
                file.write("Program Settings:\n\nGas Temperature: {:.1f}°C\nPipe Width Multiplicator: {:.1f}\nHeader Multiplicator: {:.1f}\nPipe Length Multiplicator: {:.1f}\n\n".format(temp_gases, pip_width_multiplicator, header_multiplicator, pipe_multiplicator))
                file.write("Export Values:\n\nHeader Width: {:.0f}mm\nHeader Length: {:.0f}mm\nStinger Width: {:.0f}mm\nStinger Length: {:.0f}mm\nDiffuser Length: {:.0f}mm\nPipe Width: {:.0f}mm\nPipe Length: {:.0f}mm\nReflector Length: {:.0f}mm\n".format(header_width, header_length, stinger_width, stinger_length, diffuser_length, pipe_width, pipe_length, reflector_length))
                file.write("\n----------------------------------------------------\n\nThanks for using 2-Stroke Exhaust Calculator by Jannick Richter")
            elif lang_var.get() == "Deutsch":
                file.write("&&2-Takt Auspuff Rechner von Jannick Richter - Export Daten&&\n\n----------------------------------------------------\n\n")
                file.write("Eingabewerte:\n\nAuslass Fläche: {:.0f}mm\nAuslasssteuerzeit: {:.0f}°\nDrehzahl: {:.0f} 1/min\n\n".format(outlet_surface, outlet_tax_time, n))
                file.write("Programm Einstellungen:\n\nGas Temperatur: {:.1f}°C\nRohrbreite Multiplikator: {:.1f}\nKrümmer Multiplikator: {:.1f}\nRohrlänge Multiplikator: {:.1f}\n\n".format(temp_gases, pip_width_multiplicator, header_multiplicator, pipe_multiplicator))
                file.write("Export Daten:\n\nKrümmerbreite: {:.0f}mm\nKrümmerlänge: {:.0f}mm\nEndrohrbreite: {:.0f}mm\nEndrohrlänge: {:.0f}mm\nKonuslänge: {:.0f}mm\nRohrbreite: {:.0f}mm\nRohrlänge: {:.0f}mm\nGegenkonuslänge: {:.0f}mm\n".format(header_width, header_length, stinger_width, stinger_length, diffuser_length, pipe_width, pipe_length, reflector_length))
                file.write("\n----------------------------------------------------\n\nDanke für die Benutzung vom 2-Takt Auspuff Rechner von Jannick Richter")
        export_successful()


label26 = tk.Label(window, text="", foreground="red", font=("Calibri", 10))
canvas0.create_window(500, 620, window=label26)

button2 = tk.Button(window, text="Export Data", background="gray", foreground="white", width=20, height=1, font=("Calibri", 14), command=export_data)
canvas0.create_window(500, 650, window=button2)

#sign

label100 = tk.Label(window, text="created with 💛 by Jannick Richter", font=("Times New Roman", 12))
canvas0.create_window(350, 700, window=label100)

#Set lang
with open('save_data.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    data = list(reader)

    for row in data:
        switch_lang(row[0])

window.mainloop()