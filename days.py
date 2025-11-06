day_number = int(input("Enter a number (1 to 7): "))
days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}
print("Day:", days.get(day_number, "Invalid number"))
