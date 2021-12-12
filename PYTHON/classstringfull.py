#write a class that stores a string and all its status
#such as number of uppercase/lowercase characters
#number of vowels
#number of consonantss
#number of spaces
#and display the status of the entered string 

class string:
    def __init__(self):
        self.vowels=0
        self.spaces=0
        self.uppercase=0
        self.lowercase=0
        self.consonants=0
        self.string=str(input("Enter the string: "))
        def count_upper(self):
            for letter in self.string:
                if(letter.isupper()):
                    self.uppercase+=1
        def count_lower(self):
            for letter in self.string:
                if(letter.islower()):
                    self.lowercase+=1
        def count_vowels(self):
            for letter in self.string:
                if(letter in ('a','e','i','o','u','A','E','I','O','U')):
                    self.vowels+=1
        def count_spaces(self):
            for letter in self.string:
                if(letter==' '):
                    self.spaces+=1
        def count_consonants(self):
            for letter in self.string:
                if(letter not in ('a','e','i','o','u','A','E','I','O','U')):
                    self.consonants+=1
        def compute(self):
            self.count_uppercase()
            self.count_lowercase()
            self.count_vowels()
            self.count_spaces()
            self.count_consonants()

        def display(self):
            print("vowels= ",self.vowels)
            print("consonants= ",self.consonants)
            print("spaces= ",self.spaces)
            print("lower case letters= ",self.lowercase)
            print("upper case letters= ",self.uppercase)
            
s=string() #creating a object
s.compute()
s.display()
