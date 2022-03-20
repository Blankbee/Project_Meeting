print("Katılımcı sayısını giriniz: ")
x1=int(input())
print("Katılımcı isimlerini giriniz: ")
liste=[]
liste1=[]
k=3
for i in range(0,x1):
    a=input()
    liste1.append(a)
print("*****************************************")
def lister(liste,x):
    b=int(((x/2)-1))
    c=int((x/2)-0.5)
    k=3
    print("*****************************************")
    for z in range(0,x):
        print("Sayın {} lütfen {} numaralı sandalyeye geçin.".format(liste[z],z+1))
    if(x%2==0):
        for j in range(0,b):
            print("********************************")
            for l in range(0,x):
                if(l%2==0):
                    if((l+k)>x):
                        print("Sayın {} lütfen {} numaralı sandalyeye geçin.".format(liste[l],((l+k)%x)))
                    else:
                        print("Sayın {} lütfen {} numaralı sandalyeye geçin.".format(liste[l],l+k))

                else:
                    print("Sayın {} lütfen yerinizde kalın".format(liste[l]))
            k=k+2
    else:
        for j in range(0,c):
            print("*****************************************")
            for l in range(0,x):
                if(l%2==0):
                    if((l+k)>x):
                        print("Sayın {} lütfen {} numaralı sandalyeye geçin.".format(liste[l],((l+k)%(x+1))))
                    else:
                        print("Sayın {} lütfen {} numaralı sandalyeye geçin.".format(liste[l],l+k))

                else:
                    print("Sayın {} lütfen yerinizde kalın".format(liste[l]))
            k=k+2
def lister1(v1):
    if(len(v1)>2):
        if(len(v1)%2!=0):
            for i in range(0,len(v1)-1,2):
                print("Sayın {},{} ile boş bir masaya geçiniz.".format(v1[i],v1[i+1]))
        else:
            for i in range(0,len(v1)-2,2):
                print("Sayın {},{} ile boş bir masaya geçiniz.".format(v1[i],v1[i+1]))  
    elif(len(v1)==2):
            print("Sayın {},{} ile boş bir masaya geçiniz.".format(v1[0],v1[1])) 


j=0
v=[]
u=[]
r=[]
t=[]
for f in range(0,x1,2):
    d=liste1[f]
    v.append(d)
for g in range(1,x1,2):
    d1=liste1[g]
    u.append(d1)
lister(liste1,x1)
lister(v,len(v))
lister(u,len(u))
while len(v)>2 or len(u)>2 or len(t)>2:
    r=[]
    if(len(v)>3):
        for i in range (0,len(v)):
            d=v[i]
            r.append(d)
        v=[]
        for i1 in range(0,len(r),2):
            d=r[i1]
            v.append(d)
        if(len(v)!=2):
            lister(v,len(v))
        t=[]
        for j in range(1,len(r),2):
            d=r[j]
            t.append(d)
        if(len(t)!=2):
            lister(t,len(t))
        r=[]
    if(len(u)>3):
        for i2 in range (0,len(u)):
            d=u[i2]
            r.append(d)
        u=[]
        for i3 in range(0,len(r),2):
            d=r[i3]
            u.append(d)
        if(len(u)!=2):
            lister(u,len(u))
        t=[]
        for j in range(1,len(r),2):
            d=r[j]
            t.append(d)
        if(len(t)!=2):
            lister(t,len(t))
        r=[]


    if(len(v)==3):
        for i in range (0,len(v)):
            d=v[i]
            r.append(d)
        v=[]
        for i1 in range(0,len(r),2):
            d=r[i1]
            v.append(d)
        if(len(v)!=2):
            lister(v,len(v))
        r=[]
    if(len(u)==3):
        for i2 in range (0,len(u)):
            d=u[i2]
            r.append(d)
        u=[]
        for i3 in range(0,len(r),2):
            d=r[i3]
            u.append(d)
        if(len(u)!=2):
            lister(u,len(u))
        r=[]


lister1(v)
lister1(t)
lister1(u)
        



