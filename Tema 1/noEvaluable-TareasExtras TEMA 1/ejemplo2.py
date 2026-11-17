temperatura = float(input("dime la temperatura"))
if temperatura >26:
    print ("aire")
elif temperatura <26 and temperatura >18:
        print ("poner ventilador")
elif temperatura == 20:
    print ("hace buen tiempo")
elif temperatura <16:
    print ("encender calentador")
else:
    print ("no hacer nada")