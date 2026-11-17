gs1 = input("dime el grupo sanguineo: ").lower()
gs2 = input("dime el grupo sanguineo: ").upper()

a= ["A","AB"]
b = ["B", "AB"]
ab = ["AB"]
cero = ["A", "B", "AB", "0"]

if gs1 == "a" and gs2 in a:
    print (gs1, "puede donar a",gs2)
elif gs1 == "b" and gs2 in b:
    print (gs1, "puede donar a",gs2)
elif gs1 == "ab" and gs2 in ab:
    print (gs1, "puede donar a",gs2)
elif gs1 == "cero" and gs2 in cero:
    print (gs1, "puede donar a",gs2)
else:
    print("no puede donar")
