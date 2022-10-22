# You are driving a little too fast, and a police officer stops you. Write a function to return one of 3 possible
# results: "No ticket", "Small ticket", or "Big Ticket". If your speed is 60 or less, the result
# is "No Ticket". If speed is between 61 and 80 inclusive, the result is "Small Ticket".
# If speed is 81 or more, the result is "Big Ticket". Unless it is your birthday
# (encoded as a boolean value in the parameters of the function) -- on your birthday,
# your speed can be 5 higher in all cases.


def caught_speeding(speed, is_birthday):
    if is_birthday == "True":
        speeding = speed - 5
    else:
        speeding = speed

    if speeding < 60:
        return "No Ticket"
    elif 61 <= speeding <= 80:
        return "Small Ticket"
    elif speeding >= 81:
        return "Big Ticket"


CarSpeed = int(input("What is car\'s speed: "))
Birthday = input("Is it your birthday (True/False) ")

print(caught_speeding(CarSpeed, Birthday))
