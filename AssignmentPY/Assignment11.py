# Global variable
counter = 0

# Function to increment the counter
def increment():
    global counter
    counter += 1
    print("Counter value:", counter)

# Calling the function three times
increment()
increment()
increment()
