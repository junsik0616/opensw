def input_scores():
    students = [] #학생들의 정보를 저장할 빈 리스트를 생성합니다.
    print("\n성적관리 프로그램\n")
    print("=" * 85)
    print("학번\t\t이름\t\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
    print("=" * 85)
    for i in range(5): #학생들에 대한 각 정보를 입력받는 부분입니다.
        print(f"\n학생 {i+1}")
        number = input("학번을 입력하세요: ")
        name = input("이름을 입력하세요: ")
        eng = int(input("영어점수를 입력하세요: "))
        c = int(input("C언어점수를 입력하세요: "))
        py = int(input("파이썬점수를 입력하세요: "))
        students.append((number, name, eng, c, py))#students[0]~[4]에 number~py가 각각 저장됨/입력받은 학생의 정보를 튜플로 묶고, 리스트에 추가합니다.
    return students

def calculate_total_score(student):
    return student[2] + student[3] + student[4]

def calculate_average_score(student):
    return calculate_total_score(student) / 3

def calculate_grade(average_score):
    if average_score >= 90:
        return 'A'
    elif average_score >= 80:
        return 'B'
    elif average_score >= 70:
        return 'C'
    elif average_score >= 60:
        return 'D'
    else:
        return 'F'

def calculate_rank(students):  # 학생들을 총점을 기준으로 내림차순으로 정렬합니다.
    sorted_students = sorted(students, key=lambda x: calculate_total_score(x), reverse=True)
    return [sorted_students.index(student) + 1 for student in students]

def print_result(students, ranks):
    print("=" * 85)
    for i, student in enumerate(students):
        total_score = calculate_total_score(student)
        average_score = calculate_average_score(student)
        grade = calculate_grade(average_score)
        print(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}\t"
              f"{total_score}\t{average_score:.2f}\t{grade}\t{ranks[i]}")
    print("=" * 85)

def main():
    students = input_scores()
    ranks = calculate_rank(students)
    print_result(students, ranks)

main()
