import sqlite3
import random

class SeatingArranger:
    ExamID = ""

    @staticmethod
    def arrange():
        # showing wait screen ...
        wait_screen = ExamSeatingArrangerWaitScreen()
        wait_screen.show()

        # commom variables
        # ####### delete previous seating arrangements
        DB.execute("DELETE FROM seatings WHERE examid = ?", (SeatingArranger.ExamID,))

        # ####### select all students
        students = []
        student_index = 0

        # select all batches for the exam
        batches = DB.execute("SELECT DISTINCT batchid FROM examsubjectandbatches WHERE examid = ?", (SeatingArranger.ExamID,)).fetchall()

        # select students of each batch
        for batch in batches:
            students.extend([student[0] for student in DB.execute("SELECT regno FROM students WHERE batchid = ? ORDER BY regno", batch).fetchall()])

        # ####### select all halls
        halls = [hall[0] for hall in DB.execute("SELECT hallname FROM selectedexamhalls WHERE examid = ?", (SeatingArranger.ExamID,)).fetchall()]

        # ###### select all non-registered students
        non_reg_students = [nrs[0] for nrs in DB.execute("SELECT studentregno FROM nonregisteredstudents WHERE examid = ?", (SeatingArranger.ExamID,)).fetchall()]

        # ####### arrange
        # removing non-registered students
        students = [student for student in students if student not in non_reg_students]

        # shuffling the halls
        random.shuffle(halls)

        # arrange for left side seat
        for hall in halls:
            # seat no initialization
            seat_no = 1

            # get no of rows and cols
            no_of_row, no_of_col = DB.execute("SELECT noofrow, noofcol FROM halls WHERE name = ?", (hall,)).fetchone()

            # for rows * cols
            for _ in range(no_of_col):
                for _ in range(no_of_row):
                    # seat no L
                    DB.execute("INSERT INTO seatings VALUES (NULL, ?, ?, ?, ?)", (SeatingArranger.ExamID, students[student_index], hall, f"{seat_no}L"))
                    seat_no += 1
                    student_index += 1

                    # break if students are finished
                    if student_index == len(students):
                        break

                if student_index == len(students):
                    break

            # break if students are finished
            if student_index == len(students):
                break

        # arrange for right side seat
        for hall in halls:
            # break if students are finished
            if student_index == len(students):
                break

            # seat no initialization
            seat_no = 1

            # get no of rows and cols
            no_of_row, no_of_col = DB.execute("SELECT noofrow, noofcol FROM halls WHERE name = ?", (hall,)).fetchone()

            # for rows * cols
            for _ in range(no_of_col):
                for _ in range(no_of_row):
                    # seat no R
                    DB.execute("INSERT INTO seatings VALUES (NULL, ?, ?, ?, ?)", (SeatingArranger.ExamID, students[student_index], hall, f"{seat_no}R"))
                    seat_no += 1
                    student_index += 1

                    # break if students are finished
                    if student_index == len(students):
                        break

                if student_index == len(students):
                    break

        # on finishing arrangement closing the wait screen
        wait_screen.close()

# Replace the ExamSeatingArrangerWaitScreen class with your actual implementation

# Example usage:
# SeatingArranger.ExamID = "your_exam_id"
# SeatingArranger.arrange()
