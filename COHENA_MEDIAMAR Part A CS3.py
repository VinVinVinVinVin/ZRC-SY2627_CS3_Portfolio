from typing import List, Optional

class AssignmentSubmission:
    def __init__(self, student_name: str, student_id: str, assignment_title: str, due_date: str, grade: Optional[float] = None, submitted_files: Optional[List[str]] = None):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__grade = float(grade) if grade is not None else None
        self.__submitted_files = list(submitted_files) if submitted_files else []
        self.__is_submitted = bool(self.__submitted_files)
        self.submission_count = len(self.__submitted_files)
        self.max_files_allowed: Optional[int] = None

    def __validate_grade(self, score: float) -> bool:
        if not isinstance(score, (int, float)):
            raise TypeError("score must be a number")
        if 0 <= float(score) <= 100:
            return True
        raise ValueError("grade must be between 0 and 100")

    def __check_submission_status(self) -> bool:
        return self.__is_submitted       

    def __is_duplicate_file(self, filename: str) -> bool:
        return filename in self.__submitted_files   

    def add_file(self, filename: str) -> bool:
        if self.__grade is not None:
            raise RuntimeError("cannot modify files after grading")
        if self.__is_duplicate_file(filename):
            return False
        if self.max_files_allowed is not None and len(self.__submitted_files) >= self.max_files_allowed:
            return False
        self.__submitted_files.append(filename)
        self.submission_count = len(self.__submitted_files)
        self.__is_submitted = True
        return True

    def remove_file(self, filename: str) -> bool:
        if self.__grade is not None:
            raise RuntimeError("cannot modify files after grading")
        if filename not in self.__submitted_files:
            return False
        self.__submitted_files.remove(filename)
        self.submission_count = len(self.__submitted_files)
        if not self.__submitted_files:
            self.__is_submitted = False
        return True

    def assign_grade(self, score: float):
        if not self.__submitted_files:
            raise RuntimeError("cannot grade: no files submitted")
        if self.__validate_grade(score):
            self.__grade = float(score)

    def get_grade(self) -> str:
        return "Ungraded" if self.__grade is None else f"{self.__grade:.2f}"

    def view_files(self) -> str:
        if not self.__submitted_files:
            return "No files submitted"
        return ", ".join(self.__submitted_files)

    @property
    def status_report(self) -> str:
        graded = "Graded" if self.__grade is not None else "Not graded"
        submitted = "Submitted" if self.__check_submission_status() else "Not submitted"
        return f"{self.student_name} ({self.student_id}) - {self._assignment_title} | {submitted}, {graded}, files={self.submission_count}"

student1 = AssignmentSubmission(
    student_name="Alex Gonzaga",
    student_id="pshs-1090-x",
    assignment_title="CS-101",
    due_date="2026-10-01",
)

student2 = AssignmentSubmission(
    student_name="Adelle",
    student_id="pshs-1920-x",
    assignment_title="CS-101",
    due_date="2026-10-01",
)


print("INITIALIZING DROPBOX FOR STUDENTS...")
student1 = AssignmentSubmission(student_name="Alex Gonzaga", student_id="pshs-1090-x", assignment_title="CS-101", due_date="2026-10-01")
student2 = AssignmentSubmission(student_name="Adelle", student_id="pshs-1920-x", assignment_title="CS-103", due_date="2026-10-01")
student3 = AssignmentSubmission(student_name="Juan Dela Cruz", student_id="pshs-1033-x", assignment_title="CS-101", due_date="2026-10-01")
student4 = AssignmentSubmission(student_name="Maria Santos", student_id="pshs-1044-x", assignment_title="CS-101", due_date="2026-10-01")
student5 = AssignmentSubmission(student_name="Jose Reyes", student_id="pshs-1055-x", assignment_title="CS-101", due_date="2026-10-01")
print()

print("Test scenario 1: Single file for Alex")
student1.add_file("MAIN.PY")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"[SUCCESS] {student1.student_name} attached {student1.view_files()}. Total files: {student1.submission_count}. Grade: {student1.get_grade()}")

print("Test scenario 2: Removing files from list")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.py")
student2.assign_grade(88)
print(f"[SUCCESS] {student2.student_name} attached {student2.view_files()}. Grade: {student2.get_grade()}")

print("Test scenario 3: Preventing duplicate files")
student3.add_file("script.py")
added_second = student3.add_file("script.py")
print(f"[SUCCESS] {student3.student_name} attached {student3.view_files()}. Total files: {student3.submission_count}")
if not added_second:
    print("[WARNING] 'script.py' is already attached")

print("Test scenario 4: Removing files after grading")
student4.add_file("exam_answers.pdf")
student4.assign_grade(75)
print(f"[SUCCESS] {student4.student_name} attached {student4.view_files()}. Total files: {student4.submission_count}. Grade: {student4.get_grade()} officially ASSIGNED TO {student4.student_name.upper()}")
try:
    student4.remove_file("exam_answers.pdf")
except Exception:
    print(f"[WARNING] {student4.student_name} cannot remove files. assignment is already graded")

print("Test scenario 5: Empty list handling")
student5.add_file("draft.txt")
print(f"[SUCCESS] {student5.student_name} attached {student5.view_files()}. Total files: {student5.submission_count}")
student5.remove_file("draft.txt")
print(f"[SUCCESS] {student5.student_name} removed draft.txt")
try:
    student5.assign_grade(100)
except Exception:
    print(f"[ERROR] cannot grade no files submitted for {student5.student_name}")


print("FINAL SYSTEM REPORT")
print(student1.status_report)
print(student2.status_report)
print(student3.status_report)
print(student4.status_report)
print(student5.status_report)