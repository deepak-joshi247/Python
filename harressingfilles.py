with open("D:/testing/poem.txt","r+") as poem:
    words = poem.read()
    if "twinkling"  in words :  print("found")
    else:   print("sorry mate")