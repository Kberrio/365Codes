# ANIMAL CRACKERS: Write a function takes a two-word string 
# and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(text):
    #Divides the string in two words
    words = text.split() 

    if len(words) != 2:
        return False
    
    firstLetterWord_One = words[0][0].lower()
    firstLetterWord_Two = words[1][0].lower()

    return firstLetterWord_One == firstLetterWord_Two

#testing
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))