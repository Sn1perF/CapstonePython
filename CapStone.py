def main():
    print("USD to Other Currency Converter")
    print()
    dollar = eval(input("Enter dollar amount: "))
    print("Choose the currency to convert to:")
    print("1 | British Pounds")
    print("2 | Euros")
    print("3 | Japanese Yen")
    print("4 | Chinese Yuan")
    choice = input("Enter your choice : ")
    if choice == '1':
        result = convert_to_pounds(dollar)
        currency = "British Pounds"
    elif choice == '2':
        result = convert_to_euros(dollar)
        currency = "Euros"
    elif choice == '3':
        result = convert_to_yen(dollar)
        currency = "Japanese Yen"
    elif choice == '4':
        result = convert_to_Yuan(dollar)
        currency = "Chinese Yuan"
    else:
        print("Invalid choice")
        return

    print(f"\n{dollar} USD is worth {result:.2f} {currency}")


convert_to_pounds = lambda dollars: dollars * 0.78
convert_to_euros = lambda dollars: dollars * 0.91
convert_to_yen = lambda dollars: dollars * 144.86
convert_to_Yuan = lambda dollars: dollars * 7.11

if __name__ == "__main__":
    main()
