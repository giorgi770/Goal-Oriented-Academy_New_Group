# 1) ფორ ლუპის გამოყენებით დამიპრინტეთ 1-დან 10000-მდე,
# დამიპრინტეთ მხოლოდ ლუწი ციფრები 
# 2) ფორ ლუპის გამოყენებით დამიპრინტეთ 1-დან 10000-მდე,
# დამიპრინტეთ მხოლოდ კენტი ციფრები

# 1-დან 10000-მდე მხოლოდ ლუწი ციფრები
for i in range(1,1001):
    if i % 2 == 0:
        print(i)

# 1-დან 10000-მდე მხოლოდ კენტი ციფრები
for i in range(1,1001):
    if i % 2 != 0:
        print(i)



# 1)while ლუპის გამოყენებით დამიპრინტეთ 1-დან 10000-მდე,
# დამიპრინტეთ მხოლოდ ლუწი ციფრები 
# 2) while ლუპის გამოყენებით დამიპრინტეთ 1-დან 10000-მდე,
# დამიპრინტეთ მხოლოდ კენტი ციფრები

# ლუწი ციფრების დაბეჭდვა
i = 1
while 1 <= 1000:
    if i % 2 == 0:
        print(i)

        i += 1

# კენტი ციფრების დაბეჭდვა
i = 1
while 1 <= 1000:
    if i % 2 != 0:
        print(i)

        i += 1