import tkinter as tk
from tkinter import messagebox
import time

class AssignmentProblemTrial9:
    colfreeze = [0] * 10
    rowfreeze = [0] * 10
    finalsum = 0
    count = 0
    k = 0
    lines = 0
    finalstr = ""

    @staticmethod
    def smallr(r, c, mat):
        small = mat[r][0]
        for j in range(c):
            if small > mat[r][j]:
                small = mat[r][j]
        return small

    @staticmethod
    def smallc(r, c, mat):
        small = mat[0][c]
        for i in range(r):
            if small > mat[i][c]:
                small = mat[i][c]
        return small

    @staticmethod
    def smallest(length, mat):
        small = mat[0]
        for i in range(length):
            if small > mat[i]:
                small = mat[i]
        return small

    @staticmethod
    def iscolfreeze(j):
        for i in range(len(AssignmentProblemTrial9.colfreeze)):
            if AssignmentProblemTrial9.colfreeze[i] == j:
                return 1
        return 1111

    @staticmethod
    def isrowfreeze(j):
        for i in range(len(AssignmentProblemTrial9.rowfreeze)):
            if AssignmentProblemTrial9.rowfreeze[i] == j:
                return 1
        return 1111

    @staticmethod
    def noofzero(r, c, mat):
        count = 0
        for j in range(c):
            if AssignmentProblemTrial9.iscolfreeze(j) != 1:
                if mat[r][j] == 0:
                    count += 1
        return count

    @staticmethod
    def noofzeroincol(r, c, mat):
        count = 0
        for i in range(r):
            if AssignmentProblemTrial9.isrowfreeze(i) != 1:
                if mat[i][c] == 0:
                    count += 1
        return count

    @staticmethod
    def colcoordinate(r, c, mat):
        for j in range(c):
            if AssignmentProblemTrial9.iscolfreeze(j) == 1:
                continue
            elif mat[r][j] == 0:
                return j
        return 111

    @staticmethod
    def rowcoordinate(r, c, mat):
        for i in range(r):
            if AssignmentProblemTrial9.isrowfreeze(i) == 1:
                continue
            if mat[i][c] == 0:
                return i
        return 111

    @staticmethod
    def rowtraverseoptimize(r, c, mat, mat3):
        k=0
        for i in range(r):
            if AssignmentProblemTrial9.noofzero(i, c, mat3) == 1 and AssignmentProblemTrial9.isrowfreeze(i) != 1:
                print("(", i, ",", AssignmentProblemTrial9.colcoordinate(i, c, mat3), ")")
                AssignmentProblemTrial9.finalstr += "(" + str(i) + "," + str(AssignmentProblemTrial9.colcoordinate(i, c, mat3)) + ")"
                AssignmentProblemTrial9.finalsum += mat[i][AssignmentProblemTrial9.colcoordinate(i, c, mat3)]
                AssignmentProblemTrial9.colfreeze[k] = AssignmentProblemTrial9.colcoordinate(i, c, mat3)
                k += 1
                AssignmentProblemTrial9.lines += 1
                AssignmentProblemTrial9.count += 1

    @staticmethod
    def coltraverseoptimize(r, c, mat, mat3):
        k=0
        for j in range(c):
            if AssignmentProblemTrial9.noofzeroincol(r, j, mat3) == 1 and AssignmentProblemTrial9.iscolfreeze(j) != 1:
                print("(", AssignmentProblemTrial9.rowcoordinate(r, j, mat3), ",", j, ")")
                AssignmentProblemTrial9.finalsum += mat[AssignmentProblemTrial9.rowcoordinate(r, j, mat3)][j]
                AssignmentProblemTrial9.finalstr += "(" + str(AssignmentProblemTrial9.rowcoordinate(r, j, mat3)) + "," + str(j) + ")"
                AssignmentProblemTrial9.rowfreeze[k] = AssignmentProblemTrial9.rowcoordinate(r, j, mat3)
                k += 1
                AssignmentProblemTrial9.lines += 1
                AssignmentProblemTrial9.count += 1

    @staticmethod
    def createmorezeros(r, c, mat, mat3):
        leftcount = 0
        leftover = [0] * (r * c) 
        for i in range(r):
            for j in range(c):
                if AssignmentProblemTrial9.isrowfreeze(i) == 1 and AssignmentProblemTrial9.iscolfreeze(j) == 1:
                    continue
                elif AssignmentProblemTrial9.isrowfreeze(i) == 1:
                    continue
                elif AssignmentProblemTrial9.iscolfreeze(j) == 1:
                    continue
                else:
                    leftover[leftcount] = mat3[i][j]
                    leftcount += 1

        print("Leftover numbers are ")
        for i in range(leftcount):
            print(leftover[i], end=" ")
        print()

        print("Smallest no from leftovers is ", AssignmentProblemTrial9.smallest(leftcount, leftover))
        AssignmentProblemTrial9.finalsum = 0
        if AssignmentProblemTrial9.smallest(leftcount, leftover) == 0:
            AssignmentProblemTrial9.rowtraverseoptimize(r, c, mat, mat3)
            AssignmentProblemTrial9.coltraverseoptimize(r, c, mat, mat3)

        sfl = AssignmentProblemTrial9.smallest(leftcount, leftover)
        for i in range(r):
            for j in range(c):
                if AssignmentProblemTrial9.isrowfreeze(i) == 1 and AssignmentProblemTrial9.iscolfreeze(j) == 1:
                    mat3[i][j] += sfl
                elif AssignmentProblemTrial9.isrowfreeze(i) != 1 and AssignmentProblemTrial9.iscolfreeze(j) != 1:
                    mat3[i][j] -= sfl
        for i in range(len(AssignmentProblemTrial9.colfreeze)):
            AssignmentProblemTrial9.colfreeze[i] = 99
        for i in range(len(AssignmentProblemTrial9.rowfreeze)):
            AssignmentProblemTrial9.rowfreeze[i] = 99

    @staticmethod
    def rcdisplay(r, c):
        for i in range(r):
            for j in range(c):
                if AssignmentProblemTrial9.isrowfreeze(i) == 1 and AssignmentProblemTrial9.iscolfreeze(j) == 1:
                    print("rc ", end="")
                elif AssignmentProblemTrial9.isrowfreeze(i) == 1:
                    print("r  ", end="")
                elif AssignmentProblemTrial9.iscolfreeze(j) == 1:
                    print("c  ", end="")
                else:
                    print(" . ", end="")
            print()

    @staticmethod
    def main():
        def create_matrix():
            global r, c
            r = int(rows_entry.get())
            c = int(cols_entry.get())
            
            for i in range(r):
                for j in range(c):
                    entry = tk.Entry(matrix_frame, width=5, bg="lightgray")
                    entry.grid(row=i, column=j, padx=5, pady=5)
                    entry.bind('<Return>', lambda event, entry=entry: focus_next_entry(event, entry))
                    mat_entries.append(entry)
            
            # Remove the "Create Matrix" button
            create_matrix_button.pack_forget()

        def focus_next_entry(event, entry):
            grid_info = entry.grid_info()
            current_row, current_col = int(grid_info["row"]), int(grid_info["column"])
            next_col = current_col + 1
            next_row = current_row if next_col < c else current_row + 1
            if next_row < r:
                mat_entries[next_row * c + next_col % c].focus_set()

        def compute():
            mat = []
            
            for i in range(r):
                row = []
                for j in range(c):
                    value = mat_entries[i * c + j].get()
                    if value.strip() == "":
                        value = 0
                    else:
                        value = float(value)
                    row.append(value)
                mat.append(row)
            
            # Perform computation here
            final_str = "Entered matrix:\n"
            for i in range(r):
                for j in range(c):
                    final_str += str(mat[i][j]) + " "
                final_str += "\n"
            final_str += "\n"

            mat2 = [[0] * 10 for _ in range(10)]
            final_str += "After row reduction:\n"
            for i in range(r):
                for j in range(c):
                    mat2[i][j] = mat[i][j] - AssignmentProblemTrial9.smallr(i, c, mat)
                    final_str += str(mat2[i][j]) + " "
                final_str += "\n"

            mat3 = [[0] * 10 for _ in range(10)]
            final_str += "\nAfter col reduction:\n"
            for i in range(r):
                for j in range(c):
                    mat3[i][j] = mat2[i][j] - AssignmentProblemTrial9.smallc(r, j, mat2)
                    final_str += str(mat3[i][j]) + " "
                final_str += "\n"

            final_str += "\nOptimized coordinates are: \n"
            for i in range(len(AssignmentProblemTrial9.colfreeze)):
                AssignmentProblemTrial9.colfreeze[i] = 99
            for i in range(len(AssignmentProblemTrial9.rowfreeze)):
                AssignmentProblemTrial9.rowfreeze[i] = 99

            while(AssignmentProblemTrial9.lines < r):
                AssignmentProblemTrial9.lines = 0
                AssignmentProblemTrial9.finalstr = "Optimized Coordinates are "
                AssignmentProblemTrial9.rowtraverseoptimize(r, c, mat, mat3)
                AssignmentProblemTrial9.coltraverseoptimize(r, c, mat, mat3)
                final_str += "No. of lines is " + str(AssignmentProblemTrial9.lines) + "\n"
                AssignmentProblemTrial9.rcdisplay(r, c)
                if(AssignmentProblemTrial9.lines == r):
                    continue
                else:
                    AssignmentProblemTrial9.createmorezeros(r, c, mat, mat3)
                    final_str += "\n"
                    for i in range(r):
                        for j in range(c):
                            final_str += str(mat3[i][j]) + " "
                        final_str += "\n"
            final_str += "\n" + AssignmentProblemTrial9.finalstr

            optimized_cost = "Optimized cost is " + str(AssignmentProblemTrial9.finalsum)
            result_label.config(text=final_str, font=("Helvetica", 12), fg="blue")
            optimized_cost_label.config(text=optimized_cost, font=("Helvetica", 14, "bold"), fg="green")

        root = tk.Tk()
        root.title("Assignment समस्या😨😩")
        root.configure(bg="lightblue")

        input_frame = tk.Frame(root, pady=10, bg="lightblue")
        input_frame.pack()

        rows_label = tk.Label(input_frame, text="No. of Rows:", bg="lightblue")
        rows_label.grid(row=0, column=0, padx=5)

        rows_entry = tk.Entry(input_frame, width=5)
        rows_entry.grid(row=0, column=1, padx=5)

        cols_label = tk.Label(input_frame, text="No. of Columns:", bg="lightblue")
        cols_label.grid(row=0, column=2, padx=5)

        cols_entry = tk.Entry(input_frame, width=5)
        cols_entry.grid(row=0, column=3, padx=5)

        matrix_frame = tk.Frame(root, padx=10, pady=10, bg="lightblue")
        matrix_frame.pack()

        mat_entries = []

        create_matrix_button = tk.Button(root, text="Create Matrix", command=create_matrix, bg="orange")
        create_matrix_button.pack(pady=5)

        compute_button = tk.Button(root, text="Compute", command=compute, bg="orange")
        compute_button.pack(pady=5)

        result_label = tk.Label(root, text="", bg="lightblue", font=("Helvetica", 10))
        result_label.pack(pady=10)

        optimized_cost_label = tk.Label(root, text="", bg="lightblue", font=("Helvetica", 12, "bold"))
        optimized_cost_label.pack(pady=5)

        root.mainloop()

AssignmentProblemTrial9.main()
'''
9 11 14 
6 15 13
12 13 6

8 4 2 6 1
0 9 5 5 4 
3 8 9 2 6
4 3 1 0 3
9 5 8 9 5

9 11 14 11 7
6 15 13 13 10 
12 13 6 8 8 
11 9 10 12 9
7 12 14 10 14'''