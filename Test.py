def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "Fail"


def main():
    print("=== Student Grade Calculator ===")

    name = input("Enter student name: ")

    try:
        mark1 = float(input("Enter marks for Subject 1: "))
        mark2 = float(input("Enter marks for Subject 2: "))
        mark3 = float(input("Enter marks for Subject 3: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    average = (mark1 + mark2 + mark3) / 3
    grade = calculate_grade(average)

    print("\n--- Result ---")
    print(f"Student Name: {name}")
    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()