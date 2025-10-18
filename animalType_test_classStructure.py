#This is a test file for committing to the branch. 


print("Hello New Person! Welcome!")

print("How has your day been today?")

class User:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.animal = ""


class Question:
    def __init__(self, prompt, options):
        self.prompt = prompt
        self.options = options  # e.g., {"a": "Calm", "b": "Adventurous", "c": "Playful"}

    def ask(self):
        print("\n" + self.prompt)
        for key, value in self.options.items():
            print(f"{key}) {value}")
        answer = input("Choose an option: ").lower().strip()
        while answer not in self.options:
            answer = input("Invalid choice. Try again: ").lower().strip()
        return answer


class Quiz:
    def __init__(self, user):
        self.user = user
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def run(self):
        print(f"\nLet's start the quiz, {self.user.name}!")
        answers = []
        for q in self.questions:
            answers.append(q.ask())
        self.determine_animal(answers)

    def determine_animal(self, answers):
        

        for i, ans in enumerate(answers):
            if i == 0:
                if ans == "a":
                    self.scores += 1
                elif ans == "b":   
                    self.scores += 2
                elif ans == "c":   
                    self.scores += 3
                elif ans == "d":   
                    self.scores += 4
            elif i == 1:
                if ans == "a":
                    self.scores += 1
                elif ans == "b":   
                    self.scores += 2
                elif ans == "c":   
                    self.scores += 3
                elif ans == "d":   
                    self.scores += 4
            elif i == 2:
                if ans == "a":
                    self.scores += 1
                elif ans == "b":   
                    self.scores += 2
                elif ans == "c":   
                    self.scores += 3
                elif ans == "d":   
                    self.scores += 4
        
        if self.score <=3:
            self.animal = "Brown Bear"
        elif self.score <=6:
            self.animal = "Seal"
        elif self.score <=9:
            self.animal = "Elk"
        elif self.score <=12:
            self.animal = "Rabbit"


        print("\nAnalyzing your personality...")
        print(f"\n{self.user.name}, based on your answers, your spirit animal is a 🦊 {self.animal}!")






