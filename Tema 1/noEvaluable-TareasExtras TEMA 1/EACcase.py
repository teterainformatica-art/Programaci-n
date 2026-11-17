http = int(input("introduce numero: "))
if http == 400:
    mensajerror = "badrequest"
elif http == 404:
    mensajerror = "notfound"
elif http == 401 or http == 403 or http == 407:
    mensajerror = "notallowed"
else:
    mensajerror = "somethingwentwrong"
print (mensajerror)
#case pintado con if