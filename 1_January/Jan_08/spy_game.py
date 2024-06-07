# SPY GAME: Write a function that takes in a list of integers and returns 
# True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(nums):
    firstZero = False
    secondZero = False

    for num in nums:
        if num == 0:
            if not firstZero:
                firstZero = True
            elif firstZero and not secondZero:
                secondZero = True
        elif num == 7:
            if firstZero and secondZero:
                return True
    return False

print(spy_game([1,2,4,0,0,7]))