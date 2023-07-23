import math
import tkinter as tk

def calc_exhaust():
    # ALL DATA IN 'mm'

    if entry0.get() == "" or entry1.get() == "" or entry2.get() == "":
        label4.config(text="Please enter the required data!")
        return
    else:
        label4.config(text="")

    ## Important Data
    outlet_diameter = 28 # Auslass Durchmesser
    outlet_tax_time = 130 # Auslasssteuerzeit (Winkel mit dem sich die Kurbelwelle dreht in °)
    n = 6000 # Drehzahl in 1/min

    ## Settings Data
    temp_gases = 281.6 # Abgastemperatur in °C 200 - 300 °C normalerweise
    pip_width_multiplicator = 14 # Variabler Wert, umso größer -> schmaleres Drehzahlband, umso kleiner -> breiteres Drehzahlband
    manifold_multiplicator = 8 # ##Werte: 6 - 12## Variabler Wert, umso größer -> schmaleres Drehzahlband, umso kleiner -> breiteres Drehzahlband
    pipe_multiplicator = 0.2 # ##Werte: 0.2 - 0.4## Variabler Wert

    ## Calculation
    outlet_surface = math.pi * math.pow((outlet_diameter / 2), 2) # Auslass Querschnittsfläche
    manifold_width = math.sqrt((outlet_surface * 1.2) / math.pi) * 2 # Krümmerdurchmesser
    manifold_lenght = manifold_width * manifold_multiplicator # Krümmerlänge
    tailpipe_width = manifold_width * 0.55 # Endrohr Durchmesser
    tailpipe_lenght = tailpipe_width * 12 # Endrohr Länge
    c = 331 + 0.6 * temp_gases # Schallgeschwindigkeit
    cone_counter_cone_length = ((c * outlet_tax_time) * 1000 / (12 * n)) - manifold_lenght # Länge von Konus bis 2/3 des Gegenkonus
    cone_lenght = (cone_counter_cone_length / 1.23) * (1 - pipe_multiplicator) # Konuslänge
    pipe_lenght = (cone_counter_cone_length / 1.23) * pipe_multiplicator # Länge des zylindrischen Rohres zw. Konus u. Gegenkonus
    pipe_width = math.pow((pip_width_multiplicator * math.pow(manifold_width, 2)), 0.5) # Breite des Mittelstücks und Konus
    counter_cone_lenght = cone_lenght * 0.5 # Gegenkonuslänge

    label_manifold_w.config(text="Manifold Width: {:.0f}mm".format(manifold_width))
    label_manifold_l.config(text="Manifold Lenght: {:.0f}mm".format(manifold_lenght))
    label_cone.config(text="Cone Length: {:.0f}mm".format(cone_lenght))
    label_pipe_w.config(text="Pipe Width: {:.0f}mm".format(pipe_width))
    label_pipe_l.config(text="Pipe Lenght: {:.0f}mm".format(pipe_lenght))
    label_counter_cone.config(text="Counter-Cone Length: {:.0f}mm".format(counter_cone_lenght))
    label_tailpipe_w.config(text="Tailpipe Width: {:.0f}mm".format(tailpipe_width))
    label_tailpipe_l.config(text="Tailpipe Lenght: {:.0f}mm".format(tailpipe_lenght))

    print("Your Exhaust Data: \nManifold - Lenght: {:.2f} - Width: {:.2f} \nCone - Lenght: {:.2f} \nPipe - Lenght: {:.2f} - Width: {:.2f} \nCounter-Cone - Lenght: {:.2f} \nTailpipe - Lenght: {:.2f} - Width: {:.2f}".format(manifold_lenght, manifold_width, cone_lenght, pipe_lenght, pipe_width, counter_cone_lenght, tailpipe_lenght, tailpipe_width))

window = tk.Tk()
window.geometry("700x800")
window.title("2-Stroke Exhaust Calculator   GUI")

label = tk.Label(window, text="2-Stroke Exhaust Calculator", font=("Calibri", 25))
label.pack(pady=10)

canvas0 = tk.Canvas(window, width=800, height=800, relief='raised')
canvas0.pack()

# outlet diameter

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

#Calculate Button

button0 = tk.Button(window, text="Calculate Exhaust >", background="green", width=30, height=2, foreground="white", font=("Calibri", 14), command=calc_exhaust)
canvas0.create_window(350, 200, window=button0)

label4 = tk.Label(window, text="", foreground="red", font=("Calibri", 12))
canvas0.create_window(350, 250, window=label4)


# data
label_manifold_w = tk.Label(window, text="Manifold Width: ---", font=("Calibri", 14))
canvas0.create_window(200, 300, window=label_manifold_w)
label_manifold_l = tk.Label(window, text="Manifold Lenght: ---", font=("Calibri", 14))
canvas0.create_window(200, 330, window=label_manifold_l)

label_tailpipe_w = tk.Label(window, text="Tailpipe Width: ---", font=("Calibri", 14))
canvas0.create_window(200, 380, window=label_tailpipe_w)
label_tailpipe_l = tk.Label(window, text="Tailpipe Lenght: ---", font=("Calibri", 14))
canvas0.create_window(200, 410, window=label_tailpipe_l)

label_cone = tk.Label(window, text="Cone Length: ---", font=("Calibri", 14))
canvas0.create_window(500, 300, window=label_cone)

label_pipe_w = tk.Label(window, text="Pipe Width: ---", font=("Calibri", 14))
canvas0.create_window(500, 340, window=label_pipe_w)
label_pipe_l = tk.Label(window, text="Pipe Lenght: ---", font=("Calibri", 14))
canvas0.create_window(500, 370, window=label_pipe_l)

label_counter_cone = tk.Label(window, text="Counter-Cone Length: ---", font=("Calibri", 14))
canvas0.create_window(500, 410, window=label_counter_cone)

canvas0.create_rectangle(100, 500, 200, 515)
canvas0.create_line(200, 500, 350, 470)
canvas0.create_line(200, 515, 350, 545)
canvas0.create_rectangle(350, 470, 400, 545)
canvas0.create_line(400, 545, 475, 510)
canvas0.create_line(400, 470, 475, 505)
canvas0.create_rectangle(475, 505, 575, 510)

#Exit Button

button1 = tk.Button(window, text="Exit", background="gray", foreground="red", width=20, height=1, font=("Calibri", 14), command=window.quit)
canvas0.create_window(350, 700, window=button1)

window.mainloop()