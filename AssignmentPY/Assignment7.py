# Assignment 5: Tuple Unpacking & Conversion

def main():
    t = ("Widget", 19.99, 4)
    product, price, quantity = t
    print(f"Product: {product}, Price: {price}, Quantity: {quantity}")

    total = price * quantity
    print("Total cost:", total)

    lst = list(t)
    lst[2] = 10  # modify quantity
    t = tuple(lst)
    print("Updated tuple:", t)

if __name__ == "__main__":
    main()
