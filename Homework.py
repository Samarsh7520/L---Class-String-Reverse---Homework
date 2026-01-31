class Reverse:
    def __init__(self, s=""):
        self.s = s

    def reverse_string(self):
        return self.s[::-1]


# Take input from the user
user_input = input("Enter a word: ")

# Create an object of the class with user input
obj = Reverse(user_input)

# Print the reversed string
print("Reversed string:", obj.reverse_string())
