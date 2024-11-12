def raise_error():
    num = int(input("type in a number: "))
    return num

def calculate(num) -> float:
    while True:
        try:
            res = num / 5
            return res
        except Exception:
            print("cant calculate with type(str)")
            raise_error()

raise_error()
calculate(raise_error())