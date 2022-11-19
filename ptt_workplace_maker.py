print("hi")
f=open("idf_basefile.txt","r",encoding="utf-8")
data=""
getin=False
count=0
for i in f:
    
    if "\"date\"" in i :
        getin=False
        print(count)
        g=open("./workplace/output_"+str(count)+".txt","w",encoding="utf-8")
        g.write(data)
        g.close()
        data=''
        count+=1
        #if count==50:
        #    break
    elif getin ==True and len(i)!=1:
        data=data+i
    if "content" in i:
        data=data+i
        getin=True
          
f.close()
g=open("./workplace/output.txt","w",encoding="utf-8")
g.write(data)
g.close()
