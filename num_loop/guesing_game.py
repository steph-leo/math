secret_number = 8
guessing_count = 0
guess = 0

while guess != secret_number:
    guessing_count +=1
    guess = int (input("Enter the number(use rhe number between 1 up to 10): "))

print(f"enter the number in {guessing_count} tries")