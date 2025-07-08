def main():
    temps = []
    for i in range(7):
        while True:
            try:
                t = float(input(f"Temp for day {i+1}: "))
                temps.append(t)
                break
            except ValueError:
                print("Please enter a valid number.")

    hottest = max(temps)
    coldest = min(temps)
    avg = sum(temps) / len(temps)
    above_avg = sum(1 for x in temps if x > avg)

    print(f"Hottest: {hottest}")
    print(f"Coldest: {coldest}")
    print(f"Days above average: {above_avg}")
    # Slicing days 2–5 inclusive
    print("Temps days 2 to 5:", temps[1:5])

if __name__ == "__main__":
    main()
