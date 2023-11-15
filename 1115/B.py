from A import get_input, is_prime, print_value 
def main():
               
    x = get_input()

    boolean = is_prime(x)

    print_value(boolean)

main()

for n in range(2, 101):
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
    if prime == True:
        print(n)