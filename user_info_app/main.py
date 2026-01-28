def main():
    print("User Info Application")

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    if age >= 18:
        status = "Adult"
    else:
        status = "Minor"

    print("\n--- Result ---")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Status: {status}")

main()
