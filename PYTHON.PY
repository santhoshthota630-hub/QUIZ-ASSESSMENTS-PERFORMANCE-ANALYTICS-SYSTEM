# QAPAS - Quiz Assessment & Performance Analytics System

class QuizSystem:
    def __init__(self):
        self.questions = []
        self.scores = {}

    def add_question(self, question, options, answer):
        self.questions.append({
            "question": question,
            "options": options,
            "answer": answer
        })

    def conduct_quiz(self, student_name):
        print(f"\nWelcome {student_name} to QAPAS Quiz\n")
        score = 0

        for i, q in enumerate(self.questions, start=1):
            print(f"\nQ{i}: {q['question']}")
            for idx, option in enumerate(q['options'], start=1):
                print(f"{idx}. {option}")

            user_ans = int(input("Enter your answer (1-4): "))
            if q['options'][user_ans - 1].lower() == q['answer'].lower():
                score += 1

        self.scores[student_name] = score
        print(f"\nYour Score: {score}/{len(self.questions)}")

    def show_analytics(self):
        print("\n--- Performance Analytics ---")
        total_students = len(self.scores)
        total_score = sum(self.scores.values())
        avg_score = total_score / total_students if total_students > 0 else 0

        print(f"Total Students: {total_students}")
        print(f"Average Score: {avg_score:.2f}")

        for student, score in self.scores.items():
            print(f"{student}: {score}")


quiz = QuizSystem()

quiz.add_question("What is the capital of India?",
                  ["Mumbai", "Delhi", "Chennai", "Kolkata"], "Delhi")

quiz.add_question("Which language is used for web development?",
                  ["Python", "HTML", "C", "Java"], "HTML")

quiz.add_question("2 + 2 = ?",
                  ["3", "4", "5", "6"], "4")

while True:
    print("\n--- QAPAS MENU ---")
    print("1. Take Quiz")
    print("2. View Analytics")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter your name: ")
        quiz.conduct_quiz(name)

    elif choice == '2':
        quiz.show_analytics()

    elif choice == '3':
        print("Exiting QAPAS...")
        break

    else:
        print("Invalid choice!")
