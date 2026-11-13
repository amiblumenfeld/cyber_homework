def multiplication(num1, num2):
    if num2 == 0:
        return 0
    else:
        return num1 + multiplication(num1, num2 - 1)

    
def factorial(n):
    if n == 0:
        return 1
        
    else:
        return multiplication(n, factorial(n - 1))
    
    
def main():
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            raise ValueError
        result = factorial(num)
    except ValueError:
        print("Value Error")
        return
    except RecursionError:
        print("Recursion Error")
        return
    except Exception:
        print("There is a bug")
        return

    print("The factorial of", num, "is", result)
if __name__ == "__main__":
    main()