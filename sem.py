import csv


with open('lab1output.csv','r',newline='') as ifp,open('neoSimasiologikos.csv','w',newline='') as ofp:
    reader = csv.reader(ifp)
    writer = csv.writer(ofp)
    headers = next(reader)
    for i,row in enumerate(reader):
        for j,header in enumerate(headers):
            writer.writerow([i+1,header,row[j]])
            #print([i+1,header,row[j]])
            

with open('neoSimasiologikos.csv','r',newline='') as ifp,open('neoSimasiologikos2V.csv','w',newline='') as ofp:
    reader = csv.reader(ifp)
    writer = csv.writer(ofp)
    for row in reader:
        if row[1] == "Ημέρα" or row[1] == "Ωρα Απο" or row[1] == "Ωρα Εως":
            writer.writerow(["b:" + row[0]  , row[1]  ," l: " + row[2]])
        else:
             writer.writerow(["b:" + row[0]  , row[1] ," u: " + row[2]])
    
    

    
with open('neoSimasiologikos2V.csv','r',newline='') as ifp,open('neoSimasiologikos3V.csv','w',newline='') as ofp:
    reader = csv.reader(ifp)
    writer = csv.writer(ofp)
    for s,p,o in reader:
        p = p.strip()
        temp_string = "http://host/sw/you/myvocab#"
        p =  temp_string+p.replace(" ","_")
        #print(o)
        if o.startswith(' u:'):
            #print("ok")
            temp_string = 'http://host/sw/you/resource/'
            o = o.replace("u: "," ")
            #print(temp_string + o)
            o = o.replace("  ","",1)
            o = temp_string+o
            o = o.replace(" ","_") 
            #print(o)
            
        #print(s,p,o)
        writer.writerow([s,p,o])

with open('neoSimasiologikos3V.csv','r',newline='') as ifp:
    reader = csv.reader(ifp)
    for s,p,o in reader:
        if "#Ωρα_" in p:
            o = o.replace('l: ','')
            o = o.strip()
            lista = list(o)
            #print(lista)
            if len(lista) == 4:
                lista.insert(0,'0')
                o = ''.join(lista)
            #o = '"' + o +':00"^^<'+p+'#time'+'>'
            time = 'http://www.w3.org/2001/XMLSchema#time'
            o = '"' + o +':00"^^<'+time+'>'
        elif "#Ημέρα" in p:
            o = o.replace('l: ','')
            o = o.strip()
            o = '"' + o + '"'

        if  s.startswith('b'):
            s = s.replace("b","_")
            #print(s)
        if o.startswith('http://'):
            o = "<"+o+">"
        p = "<"+p+">"
        #print(s,p,o+'.')
        print(s,p,o + " .")
        
   # python3 final.py> out.txt