import random
# Get guess
def get_guess():
    return list(input("What is your guess? "))

# Generate Computer code
def generate_code():
    digits = [str(num) for num in range (10)]
    
    # shuffle digits
    random.shuffle(digits)
    # Then grab the first 3
    return digits[:3]

# Generate Clues
def generate_clues(code,user_guess):
    if user_guess==code:
        return "Code Cracked!!!"
    clues = []
    for ind,num in enumerate(user_guess):
        if num==code[ind]:
            clues.append("match!")
        elif num in code:
            clues.append("Pretty close!!")
            
    if clues == []:
        return ["Nope!"]
    else:
        return clues


# Run game logic
print("Welcome code breaker!")
secret_code = generate_code()
clue_report = []
while clue_report != "Code Cracked!!!":
    guess = get_guess()
    clue_report = generate_clues(guess,secret_code)
    print("Here is the result of you guess: ")
    for clue in clue_report:
        print(clue)

