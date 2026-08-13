birth=int(input("Enter your birth year: "))

if birth>=1900:
    if (birth-1900)%12==0:
        z1=("Rat (鼠 / Shǔ)")
        print(f"Your Chinese Zodiac Sign is: {z1} ")
    elif (birth-1900)%12==1:
        z2=("Ox (牛 / Niú)")
        print(f"Your Chinese Zodiac Sign is: {z2} ")
    elif birth%12==2:
        z3=("Tiger (虎 / Hǔ)")
        print(f"Your Chinese Zodiac Sign is: {z3} ")  
    elif (birth-1900)%12==3:
        z4=("Rabbit (兔 / Tù)")
        print(f"Your Chinese Zodiac Sign is: {z4} ")
    elif (birth-1900)%12==4:
        z5=("Dragon (龙 / Lóng)")
        print(f"Your Chinese Zodiac Sign is: {z5} ")
    elif (birth-1900)%12==5:
        z6=("Snake (蛇 / Shé)")
        print(f"Your Chinese Zodiac Sign is: {z6} ")
    elif (birth-1900)%12==6:
        z7=("Horse (马 / Mǎ)")
        print(f"Your Chinese Zodiac Sign is: {z7} ")
    elif (birth-1900)%12==7:
        z8=("Goat (羊 / Yáng)")
        print(f"Your Chinese Zodiac Sign is: {z8} ")
    elif (birth-1900)%12==8:
        z9=("Monkey (猴 / Hóu)")
        print(f"Your Chinese Zodiac Sign is: {z9} ")
    elif (birth-1900)%12==9:
        z10=("Rooster (鸡 / Jī)")
        print(f"Your Chinese Zodiac Sign is: {z10} ")
    elif (birth-1900)%12==10:
        z11=("Dog (狗 / Gǒu)")
        print(f"Your Chinese Zodiac Sign is: {z11} ")
    elif (birth-1900)%12==11:
        z12=("Pig (猪 / Zhū)")
        print(f"Your Chinese Zodiac Sign is: {z12} ")
else:
    print("Inalid Year, it should not be earlier than 1900")
      
