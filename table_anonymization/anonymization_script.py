# Diabazw to excel arxeio hospital_data.csv
import csv

with open('hospital_data.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    patients = list(reader)
print ("-----Erwthseis ergasias-----")
print ("H lista Patients periexei %d eisagwges." %len(patients)) # tupwnw to megethos ths listas

# Erwthma 2, apo th lista patiens elegxw poioi apo tous astheneis exoun: sex = male, age = 55 kai race = White: British
x = 0
for p in patients:
    if(p[0] == 'male') and (p[2] == '55') and (p[1]== 'White: British'):
        x=x+1
print ("Oi astheneis gia toys opoious isxyei oti: sex=male, age=55, race=White: British, einai: %d.") %x

# Gia kathe mia eggrafi ftiaxnw to qid tis kai to prosthetw se mia lista
races = []
for p in patients:
    qid = p[0]+'_'+p[1]+'_'+p[2]
    races.append(qid)
races_set = set(races) #setarw thn lista pou periexei ta qid

# Vriskw gia posous astheneis exw monadiko set qid gia to deyetro erwthma
b = []
for r in races_set:
    x = races.count(r)
    b[len(races_set):] = [x]
x=0
for b in b:
    if b==1:
        x=x+1
print "Gia %d periptwseis asthenwn, mporoume na eimaste sigouroi gia ton logo pou episkefthkan to nosokomeio. \n" %x
print "\n"


# Ypologismos tou k-anonymity
b = []
for r in races_set:
    x = races.count(r)
    b[len(races_set):] = [x]
print "-----Xarakthristika pinaka *Patients*-----"
print "To K-Anonymity tou pinaka Patients einai: %d" % (min(b))# einai to elaxisto k- anonymity



# Ypologismos l-diversity
b = []
diseases = []
for r in races_set:
    for p in patients:
        if (p[0]+'_'+p[1]+'_'+p[2]==r):# elegxos idiou qid
            diseases.append(p[3])
    b.append(len(diseases))
    diseases = []
print "To L-Diversity tou pinaka Patients einai: %d" % (min(b))


# Ypologismos entropy l-diversity
import math
y = 0
sum_log = 0
diseases = []
d = []
j = 0
for r in races_set:
    for p in patients:
        if (p[0]+'_'+p[1]+'_'+p[2]==r):
            diseases.append(p[3])
    diseases_set = set(diseases)
    for sd in diseases_set:
        j = diseases.count(sd)
        y = -(j / float(len(diseases)))*math.log(j / float(len(diseases)), 10)
        sum_log = y + sum_log
    l_entropy = 10**sum_log
    d.append(l_entropy)
    diseases = []
    sum_log = 0
    y = 0
    j = 0
print "To L-Entropy toy pinaka Patients einai: %f \n" % (min(d))


print "\n-----Xarakthristika pinaka *Patients* genikopoihmena kata hlikia-----"

# Genikopoihsh sthn Hlikia kata 10
gen_age10 = []
for p in patients:
    p[2]=int(p[2])
    p[2] = p[2]/10
    gen_age10.append(p)

# Gia kathe mia eggrafi ftiaxnw to qid tis kai to prosthetw se mia lista
races = []
iloss=0.0
for p in gen_age10:
    p[2]=str(p[2])
    qid = p[0]+'_'+p[1]+'_'+p[2]
    races.append(qid)
    iloss = iloss + (10-1)/float(89)
races_set = set(races)

# Ypologismos tou k-anonymity gia 1h genikopoihsh
b = []
for r in races_set:
    x = races.count(r)
    b[len(races_set):] = [x]
print "To K-Anonymity toy pinaka Patients einai: %d" % (min(b))# einai to elaxisto k- anonymity

# Ypologismos l-diversity
b = []
diseases = []
for r in races_set:
    for p in gen_age10:
        if (p[0]+'_'+p[1]+'_'+p[2]==r):# elegxos idiou qid
            diseases.append(p[3])
    b.append(len(diseases))
    diseases = []
print "To L-Diversity tou pinaka einai: %d" % (min(b))

# Ypologismos entropy l-diversity
import math
y = 0
sum_log = 0
diseases = []
d = []
j = 0
for r in races_set:
    for p in gen_age10:
        if (p[0]+'_'+p[1]+'_'+p[2]==r):
            diseases.append(p[3])
    diseases_set = set(diseases)
    for sd in diseases_set:
        j = diseases.count(sd)
        y = -(j / float(len(diseases)))*math.log(j / float(len(diseases)), 10)
        sum_log = y + sum_log
    l_entropy = 10**sum_log
    d.append(l_entropy)
    diseases = []
    sum_log = 0
    y = 0
    j = 0
print "To L-Entropy toy pinaka Patients einai: %f" % (min(d))
print "To I-Loss toy pinaka Patients einai: %f\n" %iloss

# Genikopihsh sthn Ethnikothta
print "\n-----Xarakthristika pinaka *Patients* genikopoihmena kata ethnikothta-----"
gen_race= []
for p in gen_age10:
    if p[1]=='White: Irish'or p[1]=='White: Other' or p[1]=='White:British':
        p[1]='White'
        iloss=iloss + (3-1)/float(18)
    else:
        p[1]='Other'
        iloss=iloss + (12-1)/float(18)
    gen_race.append(p)

# Gia kathe mia eggrafi ftiaxnw to qid tis kai to prosthetw se mia lista
races = []
for p in gen_race:
    qid = p[0]+'_'+p[1]+'_'+p[2]
    races.append(qid)
races_set = set(races)

# Ypologismos tou k-anonymity gia 2h genikopoihsh
b = []
for r in races_set:
    x = races.count(r)
    b[len(races_set):] = [x]
print "To K-Anonymity toy pinaka Patients einai: %d" % (min(b))# einai to elaxisto k- anonymity
#print (b)

# Ypologismos l-diversity
b = []
diseases = []
for r in races_set:
    for p in gen_race:
        if (p[0]+'_'+p[1]+'_'+p[2]==r):# elegxos idiou qid
            diseases.append(p[3])
    b.append(len(diseases))
    diseases = []
print "To L-Diversity tou pinaka einai: %d" % (min(b))

# Ypologismos entropy l-diversity
import math
y = 0
sum_log = 0
diseases = []
d = []
j = 0
for r in races_set:
    for p in gen_race:
        if (p[0]+'_'+p[1]+'_'+p[2]==r):
            diseases.append(p[3])
    diseases_set = set(diseases)
    for sd in diseases_set:
        j = diseases.count(sd)
        y = -(j / float(len(diseases)))*math.log(j / float(len(diseases)), 10)
        sum_log = y + sum_log
    l_entropy = 10**sum_log
    d.append(l_entropy)
    diseases = []
    sum_log = 0
    y = 0
    j = 0
print "To L-Entropy toy pinaka Patients einai: %f" % (min(d))
print "To I-Loss toy pinaka Patients einai: %f" % iloss
