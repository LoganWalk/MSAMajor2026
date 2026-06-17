import random
def game_level():
    while True:
        try:
            level = int(input("Enter level 1,2,3: "))
            if(level > 3 or level < 1 ):
                print("Error: Enter a level in the range")
                continue
            return level
        except:
            print("Error: Enter a number")
            continue
def amount_of_questions():
    while True:
        try:
            amount_of_questions = int(input("Enter number of questions to ask: 3 to 10: "))
            if(amount_of_questions < 3 or amount_of_questions > 10):
                print("Error: Enter a number of questions in the range")
                continue
            return amount_of_questions
        except:
            print("Error: Enter a number")
            continue
def random_numbers():
    level = game_level()
    amount = amount_of_questions()
    wrong = 0
    correct = 0
    if (level == 1):
        random_generator = random.Random()
        random_number_1 = random_generator.randint(0,9)
        random_generator = random.Random()
        random_number_2 = random_generator.randint(0,9)
    i = 0
    while True:
        if (level == 1):
            random_generator = random.Random()
            random_number_1 = random_generator.randint(0,9)
            random_generator = random.Random()
            random_number_2 = random_generator.randint(0,9)

            while i < amount:
                try:
                    answer = int(input(f"{random_number_1} + {random_number_2} = "))
                    if(answer != random_number_1 + random_number_2):
                        print("WRONG!!!")
                        wrong += 1
                        i += 1
                        if(wrong == 3):
                            print(f"Correct Answer: {random_number_1} + {random_number_2} = {random_number_1 + random_number_2}")
                            break
                        continue
                    if(answer == random_number_1 + random_number_2):
                        print("CORRECT!!!")
                        correct += 1
                        i += 1
                        random_generator = random.Random()
                        random_number_1 = random_generator.randint(0,9)
                        random_generator = random.Random()
                        random_number_2 = random_generator.randint(0,9)
                        wrong = 0
                        continue
                except:
                    print("WRONG!!!")
                    wrong += 1
                    i += 1
                    if(wrong == 3):
                        print(f"Correct Answer: {random_number_1} + {random_number_2} = {random_number_1 + random_number_2}")
                        break
                    continue
            if(i == amount):
                print(f"You got {correct} out of {amount} correct: {correct / amount}")
                break
        elif (level == 2):
            random_generator = random.Random()
            random_number_1 = random_generator.randint(10,99)
            random_generator = random.Random()
            random_number_2 = random_generator.randint(10,99)

            while i < amount:
                try:
                    answer = int(input(f"{random_number_1} + {random_number_2} = "))
                    if(answer != random_number_1 + random_number_2):
                        print("WRONG!!!")
                        wrong += 1
                        i += 1
                        if(wrong == 3):
                            print(f"Correct Answer: {random_number_1} + {random_number_2} = {random_number_1 + random_number_2}")
                            break
                        continue
                    if(answer == random_number_1 + random_number_2):
                        print("CORRECT!!!")
                        correct += 1
                        i += 1
                        random_generator = random.Random()
                        random_number_1 = random_generator.randint(10,99)
                        random_generator = random.Random()
                        random_number_2 = random_generator.randint(10,99)
                        wrong = 0
                        continue
                except:
                    print("WRONG!!!")
                    wrong += 1
                    i += 1
                    if(wrong == 3):
                        print(f"Correct Answer: {random_number_1} + {random_number_2} = {random_number_1 + random_number_2}")
                        break
                    continue
            if(i == amount):
                print(f"You got {correct} out of {amount} correct: {correct / amount:.2f}%")
                break
        elif (level == 3):
            random_generator = random.Random()
            random_number_1 = random_generator.randint(100,999)
            random_generator = random.Random()
            random_number_2 = random_generator.randint(100,999)

            while i < amount:
                try:
                    answer = int(input(f"{random_number_1} + {random_number_2} = "))
                    if(answer != random_number_1 + random_number_2):
                        print("WRONG!!!")
                        wrong += 1
                        if(wrong == 3):
                            print(f"Correct Answer: {random_number_1} + {random_number_2} = {random_number_1 + random_number_2}")
                            i += 1
                            wrong = 0
                            break
                            
                        continue
                    if(answer == random_number_1 + random_number_2):
                        print("CORRECT!!!")
                        correct += 1
                        i += 1
                        random_generator = random.Random()
                        random_number_1 = random_generator.randint(100,999)
                        random_generator = random.Random()
                        random_number_2 = random_generator.randint(100,999)
                        wrong = 0
                        continue
                except:
                    print("WRONG!!!")
                    wrong += 1
                    i += 1
                    if(wrong == 3):
                        print(f"Correct Answer: {random_number_1} + {random_number_2} = {random_number_1 + random_number_2}")
                        i += 1
                        wrong = 0
                        break
                    continue
            if(i == amount):
                print(f"You got {correct} out of {amount} correct: {(correct / amount)* 100:.2f}%")
                break


        continue
            
        
        
                
    



random_numbers()
        

