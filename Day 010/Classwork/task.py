# 1)  დავპრინოტოთ "გოა" 1000 ჯერ და ოღონდ ყოველ ჯერზე დაიპრინტოს ჩვენი გოა
# "გოა0"
# "გოა1"
# "გოა2"
# "გოა3" 

# ეს პირველი ვარიანტი იყოს მაინც '_'
for i in range(1,101):
    print("გოა")

# ესეც მეორე
for i in range(1, 1001): 
    print(f"{i}: გოა")