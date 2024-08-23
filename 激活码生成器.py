
def cai():
    import random
    a = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M","1","2","3","4","5","6","7","8","9","0"]
    out = ""
    for i in range(NUM):
        for time in range(5):
            out += a[random.randint(0,35)] 
        out += "-"
    substring = out[0:(NUM*6)-1]
    return substring
with open ("激活码",'w') as a:
    NUM = int(input ("分为几组？ "))
    for num in range(int(input("你要生成多少: "))):
        a.write(cai())
        a.write("\n")