import pandas as pd


try:
    df = pd.read_csv("student_data.csv")
except FileNotFoundError:
    print("Error: 'student_data.csv' not found. Please run data_entry.py first.")
    exit()


def get_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'


subject_cols = df.columns[2:]  
df['Average'] = df[subject_cols].mean(axis=1)
df['Grade'] = df['Average'].apply(get_grade)


df.to_csv("student_results.csv", index=False)


print("\nTop 5 Students by Average:")
print(df.sort_values(by='Average', ascending=False).head())

print("\nGrade Distribution:")
print(df['Grade'].value_counts())

print("\nResults saved to 'student_results.csv'")
