import os
file = open("code.txt", "r")
s2 = file.read()
file.close()
s1=""
s=0
for x in s2:
    s=s+1
    if x=="{":
        sa=s2[:s-1]
        ss=s2[s:]
        break
    elif x=="#":
        sb3=s2[0:4]
    else:
        pass

r=0
for x in ss:
    r=r+1
    if x=="}":
        break
    else:
        pass
sb=ss[:r-1]
sg=sb

sb1=ss[r:]
last=sb1

with open('code.txt') as f_in:
    lines = (line.rstrip() for line in f_in) 
    lines = list(line for line in lines if line)
    for line5 in lines:
        word=line5
        break
file =open("code.txt","w")
file.write(last)
file.close()
with open('cnn.py','r+') as f: #r+ does the work of rw
    x=1
    
    lines = f.readlines()
    
    for i, line in enumerate(lines):
        if line5 in line:
            s2 = line
            s1=""
            m=0
            for x in s2:
                
                if x=="(" :
                    m=m+1
                    s1=s1+str(m)
                elif x==")":
                    m=m-1
                    s1=s1+str(m)
                elif m==0:
                    s1=s1+x
                else:
                    pass
            s=0
            for x in s1:
                s=s+1
                if x=="1":
                    print(s)
                    break
                else:
                    pass
            if '0' in s1[s:]:
                m="{"
            else:
                m="}"
            if m=="{":
                
                lines[i] = lines[i].strip() + '\n'+sg +'\n'
    f.seek(0)
    for line in lines:
        f.write(line)

os.system("./addline")
