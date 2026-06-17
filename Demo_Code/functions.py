def add_numbers(number_1:int,number_2:int, number_3:int) -> int:
    total = number_1 + number_2 + number_3
    return total




def main():
    a = 5 
    b = 4
    c = 3
    answer = add_numbers(a, b, c)
    print(f"{a} + {b} + {c} = {answer}")
main()