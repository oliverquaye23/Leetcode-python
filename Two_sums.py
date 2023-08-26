integers = input("Enter digits seperated by space:\n")
num = []
target = int(input("Enter your target value: "))
numbers = integers.split()  # splits input into individual elements

# converts the inputed strings into integer values
for digits in numbers:
    try:
        number = int(digits)
        num.append(number)
    except:
        print(f"Invalid input: {digits} is not an integer!")


def two_sums(num, target):
    num_to_index = {}  # stores numbers with their indexes

    # The enumerate function provides both numbers and their indexes.
    for index, nums in enumerate(num):
        Remainder = target - nums
        num_to_index[nums] = index
        if Remainder in num_to_index:
            return [num_to_index[Remainder], index]

    return None


result = two_sums(num, target)

print(result)
