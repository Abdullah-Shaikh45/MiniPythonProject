def calculator():
    while True:
        try:
            print("\n" + "*" * 40)
            print("Simple Calculator Game")
            print("*" * 40)
            print("Type 'q' as operator to quit.")

            operator = input("Enter an operator (+, -, *, /) or 'q' to quit: ").strip().lower()

            if operator == "q":
                print("Exiting calculator. Goodbye!")
                break

            try:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter valid integers.")
                continue

            match operator:
                case "+":
                    result = num1 + num2
                    print(f"Result: {num1} + {num2} = {result}")
                case "-":
                    result = num1 - num2
                    print(f"Result: {num1} - {num2} = {result}")
                case "*":
                    result = num1 * num2
                    print(f"Result: {num1} * {num2} = {result}")
                case "/":
                    if num2 != 0:
                        result = num1 / num2
                        print(f"Result: {num1} / {num2} = {result}")
                    else:
                        print("Error: Division by zero is not allowed.")
                case _:
                    print("Invalid operator! Please choose from +, -, *, /.")

        except Exception as e:
            print("Unexpected error occurred:", str(e))

calculator()
