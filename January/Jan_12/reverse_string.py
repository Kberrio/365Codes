sentence = "Hello Spindrift, you are very refreshing!"
words = sentence.split()

reversed_words = words[::-1] #Reverse the list of words
reversed_sentence = ''.join(reversed_words)

print(reversed_sentence)  