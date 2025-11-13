from datetime import datetime
from utils import parse_student_data, calculate_stats

def main():
    print("📊 Student Score Analyzer")
    print(f"🕒 Execution Time: {datetime.now()}\n")

    try:
        students = parse_student_data("app/data.txt")
        highest, lowest, average = calculate_stats(students)

        print(f"Total Students: {len(students)}")
        print(f"Highest Score: {highest}")
        print(f"Lowest Score: {lowest}")
        print(f"Average Score: {average}")
        print("\n✔️ Analysis Completed Successfully!")

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()
