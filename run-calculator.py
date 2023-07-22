import math

# ALL DATA IN 'mm'

outlet_diameter = 28 # Auslass Durchmesser
temp_gases = 281.6 # Abgastemperatur in °C 200 - 300 °C normalerweise
outlet_tax_time = 165 # Auslasssteuerzeit (Winkel mit dem sich die Kurbelwelle dreht in °)
n = 9000 # Drehzahl in 1/min



outlet_surface = math.pi * math.pow((outlet_diameter / 2), 2) # Auslass Querschnittsfläche
manifold_width = math.sqrt((outlet_surface * 1.2) / math.pi) * 2 # Krümmerdurchmesser
manifold_lenght = manifold_width * 8 # Krümmerlänge
tailpipe_width = manifold_width * 0.55 # Endrohr Durchmesser
tailpipe_lenght = tailpipe_width * 12 # Endrohr Länge
c = 331 + 0.6 * temp_gases # Schallgeschwindigkeit
cone_counter_cone_length = (c * outlet_tax_time) / (12 * n) # Länge von Auslass bis 2/3 des Gegenkonus

