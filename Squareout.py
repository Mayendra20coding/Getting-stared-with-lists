start = int(input("enter starting number of range "))
end = int(input("enter ending number of range "))
square_values = []
odd_squares = []
even_squares = []
for num in range(start, end + 1):
    square = num ** 2
    square_values.append(square)
    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)
print("\nAll square vales:", square_values)
print("even square vales:", even_squares)
print("odd square vales:", odd_squares)