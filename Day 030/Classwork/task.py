# Highest and Lowest
# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
# Examples
# Input: "1 2 3 4 5" => Output: "5 1"
# Input: "1 2 -3" => Output: "2 -3"
# Input: "1 2 -39 33 11 223 -4 13" => Output: "-39 223"
def Highest_and_Lowest(numbers):
    num_list = numbers.split()
    num_list = [int(num) for num in num_list]
    Highest = max(num_list)
    Lowest = min(num_list)

    return f"{Highest} {Lowest}"

print(Highest_and_Lowest("1 2 3 4 5"))        
print(Highest_and_Lowest("1 2 -3"))    
print(Highest_and_Lowest("1 2 -39 33 11 223 -4 13"))