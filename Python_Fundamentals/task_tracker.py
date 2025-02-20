import datetime
import logging

# Configure logging to capture errors
logging.basicConfig(filename="error_log.txt", level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class StudentHelper:
    def __init__(self):
        self.tasks = []  # Stores tasks as dictionaries
        self.scores = {}  # Stores scores per subject

    # Phase 1: Task Management
    def add_task(self, task_name, deadline, priority):
        """Adds a task with a deadline and priority."""
        try:
            deadline = datetime.datetime.strptime(deadline, "%Y-%m-%d")  # Convert string to datetime
            priority = int(priority)  # Ensure priority is an integer
            self.tasks.append({"task": task_name, "deadline": deadline, "priority": priority})
            print("Task added successfully!")
        except ValueError:
            logging.error("Invalid deadline format or priority value.")
            print("Error: Enter a valid date (YYYY-MM-DD) and priority as a number.")

    def display_tasks(self):
        """Displays tasks sorted by deadline and priority."""
        if not self.tasks:
            print("No tasks available.")
            return
        sorted_tasks = sorted(self.tasks, key=lambda x: (x['deadline'], -x['priority']))
        print("\nPrioritized Task List:")
        for task in sorted_tasks:
            print(f"{task['task']} - Due: {task['deadline'].strftime('%Y-%m-%d')} - Priority: {task['priority']}")

    # Phase 2: Performance Tracking
    def add_score(self, subject, score):
        """Adds a score for a subject and calculates averages."""
        try:
            score = float(score)  # Ensure score is a number
            if subject not in self.scores:
                self.scores[subject] = []
            self.scores[subject].append(score)
            print("Score added successfully!")
        except ValueError:
            logging.error("Invalid score input.")
            print("Error: Please enter a numeric score.")

    def display_performance(self):
        """Displays the average score per subject and highlights weak areas."""
        if not self.scores:
            print("No scores recorded yet.")
            return
        print("\nPerformance Tracking:")
        for subject, scores in self.scores.items():
            avg_score = sum(scores) / len(scores)
            print(f"{subject}: Average Score = {avg_score:.2f}")
            if avg_score < 50:
                print(f"Warning: Your performance in {subject} needs improvement!")

# Phase 3: Error Handling and User Interaction
def main():
    helper = StudentHelper()
    while True:
        print("\nStudent Task & Performance Tracker")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Add Score")
        print("4. View Performance")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            task = input("Enter task description: ")
            deadline = input("Enter deadline (YYYY-MM-DD): ")
            priority = input("Enter priority (higher number = more priority): ")
            helper.add_task(task, deadline, priority)
        
        elif choice == "2":
            helper.display_tasks()
        
        elif choice == "3":
            subject = input("Enter subject name: ")
            score = input("Enter score: ")
            helper.add_score(subject, score)
        
        elif choice == "4":
            helper.display_performance()
        
        elif choice == "5":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice, please select a valid option.")

if __name__ == "__main__":
    main()
