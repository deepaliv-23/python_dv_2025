# Assignment 3: String Methods
from datetime import datetime

def main():
    # 1. Combine first and last name
    first = input("First name: ")
    last = input("Last name: ")
    fullname = first + " " + last
    print("Full name:", fullname)

    # 2. Formatted price statement
    item = input("Item name: ")
    price = float(input("Price: "))
    print(f"The price of {item} is ${price:.2f}")

    # 3. Uppercase conversion
    s = "hello world"
    print(s.upper())

    # 4. Join list into sentence
    words = ['Python', 'is', 'awesome']
    sentence = " ".join(words)
    print(sentence)

    # 5. Print today's date
    today = datetime.now()
    print("Today's date:", today.strftime("%d-%m-%Y"))

if __name__ == "__main__":
    main()
