import numpy as np

print("Q1")
marks = np.array([[88, 96, 95],
                  [72, 99, 91],
                  [98, 85, 97],
                  [60, 75, 80]])
bonus = np.array([5, 2, 8])
marks_with_bonus = marks + bonus  # Broadcasting adds subject-wise bonus to each row.
capped_count = np.sum(marks_with_bonus > 100)
marks_capped = np.clip(marks_with_bonus, None, 100)
print("Marks after bonus and cap:\n", marks_capped)
print("Number of capped marks:", capped_count)
print()




print("Q2")
border_matrix = np.ones((5, 5), dtype=int)
border_matrix[1:4, 1:4] = 0
print(border_matrix)
print()




print("Q3")
# Prediction: np.arange(30).reshape(5, -1).T will have shape (6, 5).
q3 = np.arange(30).reshape(5, -1).T
print("Verified shape:", q3.shape)
# np.arange(30).reshape(4, -1) fails because 30 elements cannot be split into 4 equal rows.
print()




print("Q4")
heights = np.array([172, 158, 181, 166])
weights = np.array([68, 52, 84, 59])
joined_hstack = np.hstack((heights, weights))
print("hstack result:", joined_hstack)
print("hstack shape:", joined_hstack.shape)
two_col_table = np.column_stack((heights, weights))
print("Two-column table:\n", two_col_table)
print("Two-column table shape:", two_col_table.shape)
# hstack on 1D arrays concatenates into one longer 1D array, so it does not create columns.
print()




print("Q5")
sales = np.array([120, 135, 98, 160, 175, 190, 88, 92, 105, 210, 198, 230])
quarters = sales.reshape(4, 3)
print("Quarters shape:", quarters.shape)
quarter_avg = quarters.mean(axis=1)
best_quarter_idx = np.argmax(quarter_avg)
print("Quarter averages:", quarter_avg)
print("Highest average quarter index:", best_quarter_idx)
print("Highest average value:", quarter_avg[best_quarter_idx])
print()



print("Q6")
a = np.array([2, 3, 4])
mult_table = a.reshape(-1, 1) * a
print(mult_table)
print("Multiplication table shape:", mult_table.shape)
print()



print("Q7")
arr_1_20 = np.arange(1, 21)
arr_1_20[arr_1_20 % 3 == 0] = -1
print(arr_1_20)
print()



print("Q8")
X = np.array([[50, 1200, 3],
              [80, 1500, 9],
              [65, 900, 5],
              [95, 2000, 7]])
col_min = X.min(axis=0)
col_max = X.max(axis=0)
X_norm = (X - col_min) / (col_max - col_min)
print("Normalized matrix:\n", X_norm)
print("Column mins:", X_norm.min(axis=0))
print("Column maxs:", X_norm.max(axis=0))
print()



print("Q9")
scores = np.array([94, 61, 77, 45, 90, 88, 59, 72])
medals = np.where(scores >= 90, "Gold",
         np.where(scores >= 75, "Silver",
         np.where(scores >= 60, "Bronze", "None")))
print("Medals:", medals)
labels, counts = np.unique(medals, return_counts=True)
print("Medal counts:", dict(zip(labels, counts)))
print()



print("Q10")
m = np.array([[10, 80, 45],
              [55, 20, 99],
              [70, 33, 12]])
rows, cols = np.where(m > 50)
print("Row indices:", rows)
print("Col indices:", cols)
print("Elements > 50:", m[rows, cols])
m_copy = m.copy()
m_copy[rows, cols] = 0
print("Modified copy:\n", m_copy)
print("Original unchanged:\n", m)
print()



print("Q11")
s1 = np.array([12, 15, 11, 19, 14])
s2 = np.array([22, 18, 25, 21, 20])
s3 = np.array([31, 35, 29, 33, 30])
rows_stack = np.vstack((s1, s2, s3))
cols_stack = np.column_stack((s1, s2, s3))
print("Sensor-as-rows shape:", rows_stack.shape)
print(rows_stack)
print("Sensor-as-cols shape:", cols_stack.shape)
print(cols_stack)
print("Is rows_stack the transpose of cols_stack?", np.array_equal(rows_stack, cols_stack.T))
print()

print("Q12")
np.random.seed(1)
rand_6x6 = np.random.randint(1, 101, (6, 6))
print("Random 6x6:\n", rand_6x6)
print("Row-wise max:", rand_6x6.max(axis=1))
print("Column-wise min:", rand_6x6.min(axis=0))
print()



print("Q13")
A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[7, 8, 9],
              [1, 0, 2]])
ABt = A @ B.T
AtB = A.T @ B
print("A @ B.T:\n", ABt)
print("A @ B.T shape:", ABt.shape)
print("A.T @ B:\n", AtB)
print("A.T @ B shape:", AtB.shape)
# A @ B.T is legal: (2x3) @ (3x2) -> (2x2). A.T @ B is legal: (3x2) @ (2x3) -> (3x3).
# A @ B is not legal because (2x3) @ (2x3) has mismatched inner dimensions 3 and 2.
print()



print("Q14")
hours = np.array([2, 8, 5, 10, 3, 7])
attendance = np.array([55, 92, 70, 98, 60, 85])
w = np.array([0.5, 0.2, 0.3])

hours_col = hours.reshape(-1, 1)
attendance_col = attendance.reshape(-1, 1)
print("hours_col shape:", hours_col.shape)
print("attendance_col shape:", attendance_col.shape)

table_2col = np.hstack((hours_col, attendance_col))
print("table_2col shape:", table_2col.shape)

totals_col = table_2col.sum(axis=1, keepdims=True)
print("totals_col shape:", totals_col.shape)

table_3col = np.hstack((table_2col, totals_col))
print("table_3col shape:", table_3col.shape)

scores_weighted = table_3col @ w
print("scores_weighted shape:", scores_weighted.shape)

avg_score = scores_weighted.mean()
flags = np.where(scores_weighted > avg_score, 1, 0)
print("Average score:", avg_score)
print("Scores:", scores_weighted)
print("Above-average flags:", flags)
print("flags shape:", flags.shape)
print()



print("Q15")
def min_max_normalize(x):
    x = np.asarray(x, dtype=float)
    x_min = x.min()
    x_max = x.max()
    if x_max == x_min:
        return np.zeros_like(x)
    return (x - x_min) / (x_max - x_min)

sample = np.array([4, 8, 15, 16, 23, 42])
print("Sample:", sample)
print("Normalized:", min_max_normalize(sample))
print()

print("Q16")
m = np.array([[4, 8, 15],
              [16, 23, 42]])
flat = m.flatten()
rav = m.ravel()
flat[0] = 999
rav[0] = -999
print("flatten result:", flat)
print("ravel result:", rav)
print("Original matrix after edits:\n", m)
# flatten() returns a copy, so editing flat does not affect m.
# ravel() usually returns a view for contiguous arrays, so editing rav changes m.
print()

print("Q17")
np.random.seed(7)
temps = np.random.randint(15, 41, 28)
weeks = temps.reshape(4, 7)
print("Weeks shape:", weeks.shape)
week_avg = weeks.mean(axis=1)
hottest_week = np.argmax(week_avg)
days_above_35 = np.sum(weeks > 35)
print("Temperatures:", temps)
print("Weekly averages:", week_avg)
print("Hottest week index:", hottest_week)
print("Days > 35:", days_above_35)
print()

print("Q18")
np.random.seed(21)
A_rand = np.random.randint(1, 10, (3, 3))
B_rand = np.random.randint(1, 10, (3, 3))
AB = A_rand @ B_rand
BA = B_rand @ A_rand
print("A:\n", A_rand)
print("B:\n", B_rand)
print("A @ B:\n", AB)
print("A @ B shape:", AB.shape)
print("B @ A:\n", BA)
print("B @ A shape:", BA.shape)
print("Are they equal?", np.array_equal(AB, BA))
# Conclusion: matrix multiplication is generally not commutative (A @ B != B @ A).
print()

print("Q19")
marks = np.array([[45, 28, 67, 80],
                  [33, 90, 55, 41],
                  [72, 66, 30, 58],
                  [88, 79, 91, 84],
                  [25, 40, 38, 52]])
marks_fixed = np.where(marks < 35, 35, marks)
student_totals = marks_fixed.sum(axis=1)
topper_idx = np.argmax(student_totals)
print("Marks after floor at 35:\n", marks_fixed)
print("Student totals:", student_totals)
print("Topper index:", topper_idx)
print("Topper total:", student_totals[topper_idx])
print()

print("Q20")
arr = np.arange(1, 11)
plain_slice = arr[2:6]
copied_slice = arr[2:6].copy()
plain_slice[0] = 999
copied_slice[0] = 999
print("Original array:", arr)
print("plain_slice:", plain_slice)
print("copied_slice:", copied_slice)
# The change through plain_slice survives in arr because slicing returns a view.
# The change through copied_slice does not affect arr because copy() creates independent data.
print()

print("Q21")
M4 = np.array([[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12],
               [13, 14, 15, 16]])
main_diag = np.diag(M4)
print("Extracted diagonal:", main_diag)

v = np.array([3, 6, 9, 12])
diag_matrix = np.diag(v)
print("Diagonal matrix from vector:\n", diag_matrix)
print("Diagonal matrix shape:", diag_matrix.shape)
