import animalType_Test_classStructure

def main():
    print("Welcome to the Animal Personality Quiz!")
    name = input("What is your name or what would you liked to be called? ").strip()
    gender = input("Pick your gender (M/F/N [Nonbinary]/ P [Prefer not to say or don't use anything]): ").strip()
    

    user = User(name, gender)
    quiz = Quiz(user)

    # Example questions
    quiz.add_question(Question("What's your favorite environment?", {
                "a": "Forest",
                "b": "Ocean",
                "c": "Mountains",
                "d": "Plains"
            }
        )
    )
    quiz.add_question(Question("Which trait describes you best?", 
            {
                "a": "Tenacious",
                "b": "Cheerful",
                "c": "Calm",
                "d": "Energetic"
            }
        )
    )
    quiz.add_question(Question("How would your friends describe you?", 
            {
                "a": "Oddly Composed",
                "b": "A ray of sunshine",
                "c": "A cool breeze",
                "d": "Off the walls"
            }
        )
    )

    quiz.run()


if __name__ == "__main__":
    main()