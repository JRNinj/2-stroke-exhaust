import math

# ALL DATA IN 'mm'

outlet_diameter = 28 # Auslass Durchmesser
temp_gases = 281.6 # Abgastemperatur in °C 200 - 300 °C normalerweise
outlet_tax_time = 165 # Auslasssteuerzeit (Winkel mit dem sich die Kurbelwelle dreht in °)
n = 9000 # Drehzahl in 1/min
specific_usage_number = 12 # Variabler Wert, umso größer -> schmaleres Drehzahlband, umso kleiner -> breiteres Drehzahlband


outlet_surface = math.pi * math.pow((outlet_diameter / 2), 2) # Auslass Querschnittsfläche
manifold_width = math.sqrt((outlet_surface * 1) / math.pi) * 2 # Krümmerdurchmesser
manifold_lenght = manifold_width * 8 # Krümmerlänge
tailpipe_width = manifold_width * 0.55 # Endrohr Durchmesser
tailpipe_lenght = tailpipe_width * 12 # Endrohr Länge
c = 331 + 0.6 * temp_gases # Schallgeschwindigkeit
cone_counter_cone_length = ((c * outlet_tax_time) * 1000 / (12 * n)) - manifold_lenght # Länge von Konus bis 2/3 des Gegenkonus
cone_lenght = (cone_counter_cone_length / 1.23) * 0.7 # Konuslänge
pipe_lenght = (cone_counter_cone_length / 1.23) * 0.3 # Länge des zylindrischen Rohres zw. Konus u. Gegenkonus
pipe_width = math.pow((specific_usage_number * math.pow(manifold_width, 2)), 0.5) # Breite des Mittelstücks und Konus
counter_cone_lenght = cone_lenght * 0.5 # Gegenkonuslänge

print("Your Exhaust Data: \nManifold - Lenght: {:.2f} - Width: {:.2f} \nCone - Lenght: {:.2f} \nPipe - Lenght: {:.2f} - Width: {:.2f} \nCounter-Cone - Lenght: {:.2f} \nTailpipe - Lenght: {:.2f} - Width: {:.2f}".format(manifold_lenght, manifold_width, cone_lenght, pipe_lenght, pipe_width, counter_cone_lenght, tailpipe_lenght, tailpipe_width))