testitems = { "valve1":True,"valve2":True,"valve3":True,
"valve4":True,"valve5":True,"valve6":False,"valve7":True,
"valve8":True,"valve9":True, }


for i in testitems.keys():
    if not testitems[i]:
        continue
    print(i,"Is Ok: ",testitems[i])

print("End program")