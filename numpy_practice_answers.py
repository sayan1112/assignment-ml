import numpy as np


print("Q1. Building the class register")
s1 = [72, 85, 60, 91]
s2 = [45, 30, 98, 55]
s3 = [88, 66, 74, 100]
old = np.array([['62', '71', '55', '80'], ['49', '58', '66', '73']])
class_marks = np.array([s1, s2, s3])
print("1.", class_marks)
print("2.", class_marks.shape[0], class_marks.shape[1])
print("3.", class_marks.size)
print("4.", class_marks.astype(float))
old_numeric = old.astype(int)
print("5.", old_numeric.sum(axis=1))
all_marks = np.vstack((class_marks, old_numeric))
print("6.\n", all_marks)


print("\nQ2. Templates and sequences")
blank_sheet = np.zeros((6, 4), dtype=int)
temporary_sheet = np.full((6, 4), 35)
roll_numbers = np.arange(101, 131, 2)
time_markers = np.linspace(0, 3, 7)
diagonal_10 = np.eye(5, dtype=int) * 10
diagonal_100 = np.where(np.eye(4, dtype=bool), 100, 35)
print("1.\n", blank_sheet)
print("2.\n", temporary_sheet)
print("3.", roll_numbers, "\n", roll_numbers.size)
print("4.", time_markers)
print("5.\n", diagonal_10)
print("6.\n", diagonal_100)


print("\nQ3. The attendance row")
present = np.array([22, 18, 25, 12, 20, 24, 9, 21, 17, 23])
print("1.", present[0], present[-1])
print("2.", present[1::2])
print("3.", present[-4:])
print("4.", present[::-1][::3])
present_middle_changed = present.copy()
present_middle_changed[present_middle_changed.size // 2 - 1:present_middle_changed.size // 2 + 1] = 30
print("5.", present_middle_changed)
print("6.", present[:present.size // 2] - present[present.size // 2:])
print("7.", np.sort(present[::-1])[-3:][::-1])


print("\nQ4. Reading the mark sheet")
marks = np.array([[72, 85, 60, 91],
                  [45, 30, 98, 55],
                  [88, 66, 74, 100],
                  [95, 92, 55, 40],
                  [30, 48, 62, 70]])
print("1.\n", marks[1:4, 1:3])
print("2.", marks[:, -1])
print("3.\n", marks[:, [0, -1]])
print("4.\n", marks[::-1])
chemistry_increased = marks.copy()
chemistry_increased[:, 2] += 5
print("5.\n", chemistry_increased)
print("6.", marks[-1, -2])
print("7.\n", marks[-2:, :2])


print("\nQ5. Scholarship shortlisting")
totals = np.array([245, 310, 178, 392, 140, 265, 199, 155, 288, 132])
merit = totals[totals > 250]
middle_band = totals[(totals > 180) & (totals < 250)]
extreme = totals[(totals < 150) | (totals > 380)]
print("1.", merit)
print("2.", middle_band)
print("3.", extreme)
print("4.", middle_band.size)
print("5.", totals[totals > 200].mean())
print("6.", np.where(totals < 150)[0])
print("7.", totals[totals <= 250].max())


print("\nQ6. After revaluation")
marks = np.array([40, 55, 62, 88, 95, 33, 71, 58])
increased = np.round(marks * 1.15, 2)
corrected = np.minimum(increased, 100)
print("1.", increased)
print("2.", corrected)
print("3.", np.sum(increased - marks < 10))
print("4.", np.sum(marks < 40), np.sum(corrected < 40))
print("5.", np.round(increased / increased.max() * 100, 1))
print("6.", np.round((corrected - marks).sum(), 2))


print("\nQ7. The result summary")
marks = np.array([72, 45, 88, 95, 30, 67, 91, 54, 78, 39])
class_average = marks.mean()
print("1.", class_average, np.median(marks))
print("2.", marks.max() - marks.min())
print("3.", np.argmax(marks), np.argmin(marks))
print("4.", np.sort(marks)[-2])
print("5.", np.sum(marks > class_average))
print("6.", np.sum(np.abs(marks - class_average) <= marks.std()))
print("7.", np.round((marks.sum() - marks.max()) / (marks.size - 1), 2))


print("\nQ8. Subject-wise and student-wise reports")
marks = np.array([[72, 85, 60, 91],
                  [45, 30, 98, 55],
                  [88, 66, 74, 100],
                  [95, 92, 55, 40],
                  [30, 48, 62, 70]])
subject_averages = marks.mean(axis=0)
student_totals = marks.sum(axis=1)
print("1.", subject_averages, student_totals)
print("2.", np.argmin(subject_averages))
print("3.", np.argmax(student_totals))
print("4.", marks.max(axis=0))
print("5.", np.sum(marks > 60, axis=0))
print("6.", np.argmax(np.ptp(marks, axis=0)))
chemistry_lowest_student = np.argmin(marks[:, 2])
print("7.", student_totals[chemistry_lowest_student])


print("\nQ9. The annual function draw")
participants = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
np.random.seed(42)
print("1.", participants[np.random.randint(0, participants.size, 3)])
np.random.seed(42)
attendance_percentages = np.random.randint(60, 101, 10)
print("2.", attendance_percentages)
np.random.seed(42)
random_marks = (np.random.rand(4, 3) * 100).astype(int)
print("3.\n", random_marks)
np.random.seed(42)
shuffled_participants = participants.copy()
np.random.shuffle(shuffled_participants)
print("4.", shuffled_participants[:4])
np.random.seed(42)
dice_rolls = np.random.randint(1, 7, 20)
print("5.", np.sum(dice_rolls == 6))
print("6.", participants[attendance_percentages > 80])


print("\nQ10. Grace marks and weightage")
marks = np.array([[72, 85, 60, 91],
                  [45, 30, 98, 55],
                  [88, 66, 74, 100],
                  [95, 92, 55, 40]])
grace = np.array([5, 0, 8, 3])
weightage = np.array([1.2, 1.0, 1.1, 1.0])
graced_marks = np.minimum(marks + grace, 100)
weighted_marks = np.round(graced_marks * weightage, 1)
deviations = marks - marks.mean(axis=0)
student_bonus = np.array([5, 0, 2, 0])[:, np.newaxis]
bonus_marks = marks + student_bonus
print("1.\n", graced_marks)
print("2.\n", weighted_marks)
print("3.\n", deviations)
print("4.\n", bonus_marks)
print("5.", np.sum(deviations < 0))
standardized = np.round((marks - marks.mean(axis=0)) / marks.std(axis=0), 2)
print("6.\n", standardized)


print("\nQ11. Distances and arrangements")
metres = np.array([200, 500, 900, 100, 700])
sanskrit = np.array([65, 70, 88, 92, 54])
distances = np.abs(metres[:, np.newaxis] - metres)
print("1.\n", distances)
print("2.", distances.max(axis=1))
distance_from_zero = distances[0].astype(float).copy()
distance_from_zero[0] = np.inf
print("3.", np.argmin(distance_from_zero))
upper_triangle = np.where(np.triu(np.ones(distances.shape, dtype=bool), 1), distances, np.inf)
print("4.", np.array(np.unravel_index(np.argmin(upper_triangle), upper_triangle.shape)))
print("5.\n", np.arange(1, 25).reshape(-1, 6))
print("6a.\n", sanskrit.reshape(-1, 1))
print("6b.\n", sanskrit[:, np.newaxis])
print("7.\n", sanskrit.reshape(1, -1))


print("\nQ12. The master mark sheet")
master = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])
master_original = master.copy()
flat_copy = master.flatten()
flat_copy[0] = 999
print("1.\n", master)
master = master_original.copy()
flat_view = master.ravel()
flat_view[-1] = 111
print("2.\n", master)
middle_row_zeroed = master_original.copy()
middle_row_zeroed[1] = 0
print("3.\n", middle_row_zeroed)
first_two_doubled_copy = master_original.copy()
first_two_doubled_copy[:, :2] *= 2
print("4.\n", first_two_doubled_copy)
master = master_original.copy()
master[:, :2] *= 2
print("5.\n", master)
reduced_copy = master_original.copy()
reduced_copy[reduced_copy > 50] -= 10
print("6.\n", reduced_copy)


print("\nQ13. Merging section records")
sec_A = np.array([[72, 85, 60],
                  [45, 30, 98],
                  [88, 66, 74]])
sec_B = np.array([[95, 92, 55],
                  [30, 48, 62]])
roll_C = np.array([201, 202, 203, 204])
marks_C = np.array([67, 82, 45, 91])
combined = np.vstack((sec_A, sec_B))
print("1.\n", combined, "\nshape:", combined.shape)
totals_column = combined.sum(axis=1, keepdims=True)
combined_with_totals = np.hstack((combined, totals_column))
print("2.\n", combined_with_totals)
roll_marks = np.column_stack((roll_C, marks_C))
print("3.\n", roll_marks)
new_roll_marks = np.vstack((roll_marks, [205, 73]))
print("4.\n", new_roll_marks)
serial_column = np.arange(1, combined.shape[0] + 1)[:, np.newaxis]
print("5.\n", np.hstack((serial_column, combined)))
print("6.\n", combined[totals_column[:, 0] > 200])
grades = np.where(totals_column >= 225, 'A', np.where(totals_column >= 150, 'B', 'C'))
print("7.\n", np.hstack((combined.astype(str), grades)))


print("\nQ14. Cleaning and grading")
marks = np.array([[70, 65, 80],
                  [55, 90, 32],
                  [88, 76, 91],
                  [40, 52, 45],
                  [60, 58, 66]])
attendance = np.array([88, -1, 105, 76, 45, -1, 92, 120, 67, 30])
repaired = np.where(attendance > 100, 100, attendance).astype(float)
genuine_average = repaired[repaired != -1].mean()
repaired = np.where(repaired == -1, genuine_average, repaired)
labels = np.where(repaired >= 85, 'Regular', np.where(repaired >= 60, 'Average', 'Short'))
short_indices = np.where(labels == 'Short')[0]
below_50_rows, below_50_cols = np.where(marks < 50)
print("1.", repaired)
print("2.", labels)
print("3.", short_indices, repaired[short_indices])
print("4. rows:", below_50_rows, "cols:", below_50_cols)
print("5.", marks[below_50_rows, below_50_cols])
clean_marks = marks.copy()
changed_count = np.sum(clean_marks < 35)
clean_marks[clean_marks < 35] = 35
print("6.\n", clean_marks, "\nchanged:", changed_count)
below_60_counts = np.sum(marks < 60, axis=1)
print("7.", np.where(below_60_counts == below_60_counts.max())[0][-1])


print("\nQ15. The final weighted result")
M = np.array([[70, 65, 80],
              [55, 90, 72],
              [88, 76, 91],
              [60, 58, 66]])
w = np.array([0.3, 0.3, 0.4])
W = np.array([[0.3, 0.5],
              [0.3, 0.2],
              [0.4, 0.3]])
final_scores = M @ w
scheme_scores = M @ W
print("1.", final_scores)
print("2.", np.argmax(final_scores))
print("3.", np.ones(M.shape[0]) @ M)
print("4.\n", scheme_scores)
print("5.", np.sum(scheme_scores[:, 1] > scheme_scores[:, 0]))
print("6.", np.round(scheme_scores[:, 1] - scheme_scores[:, 0], 2))
print("7.\n", np.hstack((M, scheme_scores.max(axis=1, keepdims=True))))
