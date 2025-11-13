def parse_student_data(file_path):
    students = []
    with open(file_path, 'r') as file:
        for i, line in enumerate(file, 1):
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            if len(parts) != 2:
                raise ValueError(f"Invalid data on line {i}: {line}")
            name = parts[0].strip()
            try:
                score = int(parts[1].strip())
            except ValueError:
                raise ValueError(f"Invalid score on line {i}: {parts[1]}")
            students.append((name, score))
    if not students:
        raise ValueError("No student data found.")
    return students


def calculate_stats(students):
    scores = [score for _, score in students]
    highest = max(scores)
    lowest = min(scores)
    average = round(sum(scores) / len(scores), 2)
    return highest, lowest, average
