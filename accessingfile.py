with open("D:/testing/testing.txt","r+") as f:
    data = f.readline()
    print(data,type(data))
    # f.write(" Ahem...gentlemens changes are being made")  
    f.close()  #when using "with" closing is optional
    