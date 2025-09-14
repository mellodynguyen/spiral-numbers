"""
Mellody Nguyen
COSC 2436
Program Set 1
References:
GeeksForGeeks for str(), map() functions
Python Docs for Try and Except
"""
# String Number Program

# access dictionary via number to print word
# Output the numbers in a spiral pattern (clockwise), no space or hyphens
# 1 = one, 2 = two, 49 = fortynine
num_to_word = { 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
               6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
               11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
               15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
               19: "nineteen", 20: "twenty",21: "twentyone", 22: "twentytwo",
               23: "twentythree", 24: "twentyfour", 25: "twentyfive",
               26: "twentysix", 27: "twentyseven", 28: "twentyeight",
               29: "twentynine", 30: "thirty", 31: "thirtyone", 32: "thirtytwo",
               33: "thirtythree", 34: "thirtyfour", 35: "thirtyfive",
               36: "thirtysix", 37: "thirtyseven", 38: "thirtyeight",
               39: "thirtynine", 40: "forty", 41: "fortyone", 42: "fortytwo",
               43: "fortythree", 44: "fortyfour", 45: "fortyfive",
               46: "fortysix", 47: "fortyseven", 48: "fortyeight",
               49: "fortynine", 50: "fifty", 51: "fiftyone", 52: "fiftytwo",
               53: "fiftythree", 54: "fiftyfour", 55: "fiftyfive", 
               56: "fiftysix", 57: "fiftyseven", 58: "fiftyeight", 
               59: "fiftynine", 60: "sixty", 61: "sixtyone", 62: "sixtytwo",
               63: "sixtythree", 64: "sixtyfour", 65: "sixtyfive",
               66: "sixtysix", 67: "sixtyseven", 68: "sixtyeight",
               69: "sixtynine", 70: "seventy",71: "seventyone", 
               72: "seventytwo", 73: "seventythree", 74: "seventyfour",
               75: "seventyfive", 76: "seventysix", 77: "seventyseven",
               78: "seventyeight", 79: "seventynine", 80: "eighty",
               81: "eightyone", 82: "eightytwo", 83: "eightythree", 
               84: "eightyfour", 85: "eightyfive", 86: "eightysix", 
               87: "eightyseven", 88: "eightyeight", 89: "eightynine",
               90: "ninety", 91: "ninetyone", 92: "ninetytwo",
               93: "ninetythree", 94: "ninetyfour", 95: "ninetyfive",
               96: "ninetysix", 97: "ninetyseven", 98: "ninetyeight",
               99: "ninetynine", 100: "onehundred" }


def main_game():
    # Input two numbers, range 1-100, separated by space
    # error check values, no negatives and must be in range
    def get_user_input():
        while True:
            user_input = input("Enter Two Values [1-100]: ").split()
            if len(user_input) != 2:
                print("Please enter exactly Two Integers separated by a space.")
            try:
                num1, num2 = map(int, user_input)
                #print(type(num1))
                if not (1 <= num1 <= 100 and 1 <= num2 <= 100):
                    print("Please enter a positive number between [1-100]")
                    continue
                    #print(type(num1, num2))
                if num1 > num2:
                    print("The first number must be less than or equal to the second number.")
                    continue
                
            except ValueError:
                print("Please enter valid integers only.")
            return num1, num2
    
    num1, num2 = get_user_input()
    
    # helper funciton to add grids
    def add_empty_border(grid):
        cols = len(grid[0])
        grid.insert(0, [" "] * cols)
        grid.append([" "] * cols)
        for row in grid:
            row.insert(0, " ")
            row.append(" ")

    # starting above the upper left corner of the previously completed
    # rectangle keep going until one has drawn a rectangle for each num
    # from start to stop input values
    def print_spiral(num1, num2):
        # first word goes horizontally to start the grid
        word = num_to_word[num1]
        grid = [[char for char in word]]

        # process the rest of the numbers
        for n in range(num1 + 1, num2 + 1):
            word = num_to_word[n]
            word_index = 0

            # expand grid
            add_empty_border(grid)

            # fill top row, left to right
            for col in range(len(grid[0])):
                grid[0][col] = word[word_index]
                word_index = (word_index + 1) % len(word)

            # fill right column, top to bottom 
            for row in range(1, len(grid)):
                grid[row][-1] = word[word_index]
                word_index = (word_index + 1) % len(word)

            # fill bottom row, right to left 
            for col in range(len(grid[0]) - 2, -1, -1):
                grid[-1][col] = word[word_index]
                word_index = (word_index + 1) % len(word)

            # fill left column, bottom to top 
            for row in range(len(grid) - 2, 0, -1):
                grid[row][0] = word[word_index]
                word_index = (word_index + 1) % len(word)

        
        for row in grid:
            print("".join(row))
    
    print_spiral(num1, num2)


    # Ask the user if they want to run the program again, check case
    player_answer = input("Do you want to play again? Y/N ").upper()
    if player_answer == "Y":
        main_game()
    else:
        print("Thanks for playing!")


main_game()
