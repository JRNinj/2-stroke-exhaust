import math
import tkinter as tk
from tkinter import filedialog
import time

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
    global outlet_diameter
    global outlet_tax_time
    global n
    global temp_gases
    global pip_width_multiplicator
    global manifold_multiplicator
    global pipe_multiplicator
    global manifold_width
    global manifold_length
    global tailpipe_length
    global tailpipe_width
    global cone_length
    global pipe_length
    global pipe_width
    global counter_cone_length

    ## Important Data
    outlet_diameter = float(entry0.get()) # Auslass Durchmesser
    outlet_tax_time = float(entry1.get()) # Auslasssteuerzeit (Winkel mit dem sich die Kurbelwelle dreht in °)
    n = float(entry2.get()) # Drehzahl in 1/min

    ## Settings Data
    temp_gases = float(entry3.get()) # Abgastemperatur in °C 200 - 300 °C normalerweise
    pip_width_multiplicator = float(entry4.get()) # Variabler Wert, umso größer -> schmaleres Drehzahlband, umso kleiner -> breiteres Drehzahlband
    manifold_multiplicator = float(entry5.get()) # ##Werte: 6 - 12## Variabler Wert, umso größer -> schmaleres Drehzahlband, umso kleiner -> breiteres Drehzahlband
    pipe_multiplicator = float(entry6.get()) # ##Werte: 0.2 - 0.4## Variabler Wert

    ## Calculation
    outlet_surface = math.pi * math.pow((outlet_diameter / 2), 2) # Auslass Querschnittsfläche
    manifold_width = math.sqrt((outlet_surface * 1.2) / math.pi) * 2 # Krümmerdurchmesser
    manifold_length = manifold_width * manifold_multiplicator # Krümmerlänge
    tailpipe_width = manifold_width * 0.55 # Endrohr Durchmesser
    tailpipe_length = tailpipe_width * 12 # Endrohr Länge
    c = 331 + 0.6 * temp_gases # Schallgeschwindigkeit
    cone_counter_cone_length = ((c * outlet_tax_time) * 1000 / (12 * n)) - manifold_length # Länge von Konus bis 2/3 des Gegenkonus
    cone_length = (cone_counter_cone_length / 1.23) * (1 - pipe_multiplicator) # Konuslänge
    pipe_length = (cone_counter_cone_length / 1.23) * pipe_multiplicator # Länge des zylindrischen Rohres zw. Konus u. Gegenkonus
    pipe_width = math.pow((pip_width_multiplicator * math.pow(manifold_width, 2)), 0.5) # Breite des Mittelstücks und Konus
    counter_cone_length = cone_length * 0.5 # Gegenkonuslänge

    if lang_var.get() == "English":
        label_manifold_w.config(text="Manifold Width: {:.0f}mm".format(manifold_width))
        label_manifold_l.config(text="Manifold Length: {:.0f}mm".format(manifold_length))
        label_cone.config(text="Cone Length: {:.0f}mm".format(cone_length))
        label_pipe_w.config(text="Pipe Width: {:.0f}mm".format(pipe_width))
        label_pipe_l.config(text="Pipe Length: {:.0f}mm".format(pipe_length))
        label_counter_cone.config(text="Counter-Cone Length: {:.0f}mm".format(counter_cone_length))
        label_tailpipe_w.config(text="Tailpipe Width: {:.0f}mm".format(tailpipe_width))
        label_tailpipe_l.config(text="Tailpipe Length: {:.0f}mm".format(tailpipe_length))
    elif lang_var.get() == "Deutsch":
        label_manifold_w.config(text="Krümmerbreite: {:.0f}mm".format(manifold_width))
        label_manifold_l.config(text="Krümmerlänge: {:.0f}mm".format(manifold_length))
        label_cone.config(text="Konuslänge: {:.0f}mm".format(cone_length))
        label_pipe_w.config(text="Rohrbreite: {:.0f}mm".format(pipe_width))
        label_pipe_l.config(text="Rohrlänge: {:.0f}mm".format(pipe_length))
        label_counter_cone.config(text="Gegenkonuslänge: {:.0f}mm".format(counter_cone_length))
        label_tailpipe_w.config(text="Endrohrbreite: {:.0f}mm".format(tailpipe_width))
        label_tailpipe_l.config(text="Endrohrlänge: {:.0f}mm".format(tailpipe_length))

    print("Your Exhaust Data: \nManifold - Length: {:.2f} - Width: {:.2f} \nCone - Length: {:.2f} \nPipe - Length: {:.2f} - Width: {:.2f} \nCounter-Cone - Length: {:.2f} \nTailpipe - Length: {:.2f} - Width: {:.2f}".format(manifold_length, manifold_width, cone_length, pipe_length, pipe_width, counter_cone_length, tailpipe_length, tailpipe_width))

def set_config_data(scale):
    if slider0.get() == 3:
        entry3.delete(0, tk.END)
        entry3.insert(0, 275)
        entry4.delete(0, tk.END)
        entry4.insert(0, 14)
        entry5.delete(0, tk.END)
        entry5.insert(0, 8)
        entry6.delete(0, tk.END)
        entry6.insert(0, 0.3)
    elif slider0.get() == 4:
        entry3.delete(0, tk.END)
        entry3.insert(0, 281.6)
        entry4.delete(0, tk.END)
        entry4.insert(0, 16)
        entry5.delete(0, tk.END)
        entry5.insert(0, 7)
        entry6.delete(0, tk.END)
        entry6.insert(0, 0.2)
    elif slider0.get() == 5:
        entry3.delete(0, tk.END)
        entry3.insert(0, 285)
        entry4.delete(0, tk.END)
        entry4.insert(0, 18)
        entry5.delete(0, tk.END)
        entry5.insert(0, 6)
        entry6.delete(0, tk.END)
        entry6.insert(0, 0.2)
    elif slider0.get() == 2:
        entry3.delete(0, tk.END)
        entry3.insert(0, 270)
        entry4.delete(0, tk.END)
        entry4.insert(0, 12)
        entry5.delete(0, tk.END)
        entry5.insert(0, 9)
        entry6.delete(0, tk.END)
        entry6.insert(0, 0.4)
    elif slider0.get() == 1:
        entry3.delete(0, tk.END)
        entry3.insert(0, 267.3)
        entry4.delete(0, tk.END)
        entry4.insert(0, 10)
        entry5.delete(0, tk.END)
        entry5.insert(0, 11)
        entry6.delete(0, tk.END)
        entry6.insert(0, 0.4)

def switch_lang(lang):
    if lang == "English":
        lang_var.set("English")
        window.title("2-Stroke Exhaust Calculator   GUI")
        label.config(text="2-Stroke Exhaust Calculator")
        label1.config(text="Outlet Diameter:")
        label2.config(text="Outlet Tax Time:")
        label3.config(text="RPM:")
        label4.config(text="")
        label26.config(text="")
        label7.config(text="Gas Temperature:")
        label8.config(text="Pipe Width Multiplicator:")
        label9.config(text="Manifold Multiplicator:")
        label10.config(text="Pipe Length Multiplicator")
        label5.config(text="flat")
        label6.config(text="sharp")
        button0.config(text="Calculate Exhaust >")
        button1.config(text="Exit")
        if "manifold_length" not in globals():
            label_manifold_l.config(text="Manifold Length: ---")
            label_manifold_w.config(text="Manifold Width: ---")
            label_cone.config(text="Cone Length: ---")
            label_pipe_l.config(text="Pipe Length: ---")
            label_pipe_w.config(text="Pipe Width: ---")
            label_counter_cone.config(text="Counter-Cone Length: ---")
            label_tailpipe_l.config(text="Tailpipe Length: ---")
            label_tailpipe_w.config(text="Tailpipe Width: ---")
        else:
            label_manifold_l.config(text="Manifold Length: {:.0}mm".format(manifold_length))
            label_manifold_w.config(text="Manifold Width: {:.0f}mm".format(manifold_width))
            label_cone.config(text="Cone Length: {:.0f}mm".format(cone_length))
            label_pipe_l.config(text="Pipe Length: {:.0f}mm".format(pipe_length))
            label_pipe_w.config(text="Pipe Width: {:.0f}mm".format(pipe_width))
            label_counter_cone.config(text="Counter-Cone Length: {:.0f}mm".format(counter_cone_length))
            label_tailpipe_l.config(text="Tailpipe Length: {:.0f}mm".format(tailpipe_length))
            label_tailpipe_w.config(text="Tailpipe Width: {:.0f}mm".format(tailpipe_width))
        label21.config(text="Manifold")
        label22.config(text="Cone")
        label23.config(text="Pipe")
        label24.config(text="Counter-Cone")
        label25.config(text="Tailpipe")
        label100.config(text="created with 💛 by Jannick Richter")
        button2.config(text="Export Data")
        if label4.cget("text") != "":
            label4.config(text="Please enter the required data!")
    elif lang == "Deutsch":
        lang_var.set("Deutsch")
        window.title("2-Takt Auspuff Rechner    GUI")
        label.config(text="2-Takt Auspuff Rechner")
        label1.config(text="Auslass Größe:")
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
        if "manifold_length" not in globals():
            label_manifold_l.config(text="Krümmerlänge: ---")
            label_manifold_w.config(text="Krümmerbreite: ---")
            label_cone.config(text="Konuslänge: ---")
            label_pipe_l.config(text="Rohrlänge: ---")
            label_pipe_w.config(text="Rohrbreite: ---")
            label_counter_cone.config(text="Gegenkonuslänge: ---")
            label_tailpipe_l.config(text="Endrohrlänge: ---")
            label_tailpipe_w.config(text="Endrohrbreite: ---")
        else:
            label_manifold_l.config(text="Krümmerlänge: {:.0}mm".format(manifold_length))
            label_manifold_w.config(text="Krümmerbreite: {:.0f}mm".format(manifold_width))
            label_cone.config(text="Konuslänge: {:.0f}mm".format(cone_length))
            label_pipe_l.config(text="Rohrlänge: {:.0f}mm".format(pipe_length))
            label_pipe_w.config(text="Rohrbreite: {:.0f}mm".format(pipe_width))
            label_counter_cone.config(text="Gegenkonuslänge: {:.0f}mm".format(counter_cone_length))
            label_tailpipe_l.config(text="Endrohrlänge: {:.0f}mm".format(tailpipe_length))
            label_tailpipe_w.config(text="Endrohrbreite: {:.0f}mm".format(tailpipe_width))
        label21.config(text="Krümmer")
        label22.config(text="Konus")
        label23.config(text="Rohr")
        label24.config(text="Gegenkonus")
        label25.config(text="Endrohr")
        label100.config(text="programmiert mit 💛 von Jannick Richter")
        button2.config(text="Daten Exportieren")


window = tk.Tk()
window.geometry("700x800")
window.title("2-Stroke Exhaust Calculator   GUI")

canvas1 =tk.Canvas(window, width=700, height=50, relief='raised')
canvas1.pack()

label = tk.Label(window, text="2-Stroke Exhaust Calculator", font=("Calibri", 25))
canvas1.create_window(350, 25, window=label)

#dropdown language
lang_var = tk.StringVar()
lang_var.set("English")
dropdown0 = tk.OptionMenu(window, lang_var, "English", "Deutsch", command=switch_lang)
canvas1.create_window(650, 25, window=dropdown0)

canvas0 = tk.Canvas(window, width=700, height=800, relief='raised')
canvas0.pack()

# outlet 

label1 = tk.Label(window, text="Outlet Diameter:")
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

#manifold multiplicator
label9 = tk.Label(window, text="Manifold Multiplicator:", font=("helvetica", 11))
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
label_manifold_w = tk.Label(window, text="Manifold Width: ---", font=("Calibri", 14))
canvas0.create_window(200, 340, window=label_manifold_w)
label_manifold_l = tk.Label(window, text="Manifold Length: ---", font=("Calibri", 14))
canvas0.create_window(200, 370, window=label_manifold_l)

label_tailpipe_w = tk.Label(window, text="Tailpipe Width: ---", font=("Calibri", 14))
canvas0.create_window(200, 420, window=label_tailpipe_w)
label_tailpipe_l = tk.Label(window, text="Tailpipe Length: ---", font=("Calibri", 14))
canvas0.create_window(200, 450, window=label_tailpipe_l)

label_cone = tk.Label(window, text="Cone Length: ---", font=("Calibri", 14))
canvas0.create_window(500, 340, window=label_cone)

label_pipe_w = tk.Label(window, text="Pipe Width: ---", font=("Calibri", 14))
canvas0.create_window(500, 380, window=label_pipe_w)
label_pipe_l = tk.Label(window, text="Pipe Length: ---", font=("Calibri", 14))
canvas0.create_window(500, 410, window=label_pipe_l)

label_counter_cone = tk.Label(window, text="Counter-Cone Length: ---", font=("Calibri", 14))
canvas0.create_window(500, 450, window=label_counter_cone)

# Exhaust Blueprint

canvas0.create_rectangle(100, 550, 200, 565)
canvas0.create_line(200, 550, 350, 520)
canvas0.create_line(200, 565, 350, 595)
canvas0.create_rectangle(350, 520, 400, 595)
canvas0.create_line(400, 595, 475, 560)
canvas0.create_line(400, 520, 475, 555)
canvas0.create_rectangle(475, 555, 575, 560)

label21 = tk.Label(window, text="Manifold", font=("Calibri", 8))
canvas0.create_window(150, 557, window=label21)
label22 = tk.Label(window, text="Cone", font=("Calibri", 8))
canvas0.create_window(275, 557, window=label22)
label23 = tk.Label(window, text="Pipe", font=("Calibri", 8))
canvas0.create_window(375, 557, window=label23)
label24 = tk.Label(window, text="Counter-Cone", font=("Calibri", 8))
canvas0.create_window(435, 557, window=label24)
label25 = tk.Label(window, text="Tailpipe", font=("Calibri", 8))
canvas0.create_window(525, 557, window=label25)

#Exit Button

button1 = tk.Button(window, text="Exit", background="gray", foreground="red", width=20, height=1, font=("Calibri", 14), command=window.quit)
canvas0.create_window(200, 650, window=button1)

#Export Button

def export_data():
    if "manifold_length" not in globals():
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
                file.write("Input Values:\n\nOutlet Diameter: {:.0f}mm\nOutlet Tax Time: {:.0f}°\nRPM: {:.0f} 1/min\n\n".format(outlet_diameter, outlet_tax_time, n))
                file.write("Program Settings:\n\nGas Temperature: {:.1f}°C\nPipe Width Multiplicator: {:.1f}\nManifold Multiplicator: {:.1f}\nPipe Length Multiplicator: {:.1f}\n\n".format(temp_gases, pip_width_multiplicator, manifold_multiplicator, pipe_multiplicator))
                file.write("Export Values:\n\nManifold Width: {:.0f}mm\nManifold Length: {:.0f}mm\nTailpipe Width: {:.0f}mm\nTailpipe Length: {:.0f}mm\nCone Length: {:.0f}mm\nPipe Width: {:.0f}mm\nPipe Length: {:.0f}mm\nCounter-Cone Length: {:.0f}mm\n".format(manifold_width, manifold_length, tailpipe_width, tailpipe_length, cone_length, pipe_width, pipe_length, counter_cone_length))
                file.write("\n----------------------------------------------------\n\nThanks for using 2-Stroke Exhaust Calculator by Jannick Richter")


label26 = tk.Label(window, text="", foreground="red", font=("Calibri", 10))
canvas0.create_window(500, 620, window=label26)

button2 = tk.Button(window, text="Export Data", background="gray", foreground="white", width=20, height=1, font=("Calibri", 14), command=export_data)
canvas0.create_window(500, 650, window=button2)

#sign

label100 = tk.Label(window, text="created with 💛 by Jannick Richter", font=("Times New Roman", 12))
canvas0.create_window(350, 700, window=label100)

window.mainloop()