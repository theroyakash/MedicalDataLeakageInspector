import pandas as pd

class LeakageInspector:

	def __init__(self, df1, df2, patient_col):
		
		"""
		Args:
			df1 (dataframe): dataframe describing first dataset
			df2 (dataframe): dataframe describing second dataset
			patient_col (str): string name of column with patient IDs
		
		"""
		self.df1 = df1
		self.df2 = df2
		self.patient_col = patient_col

	def check_for_leakage(self):
		"""
		Checks for leakage in patient data if same patient crosses
		into training and validation sets.
		
		Returns:
			leakage (bool): True if there is leakage, otherwise False
		"""

		df1_patients_unique = set(self.df1[self.patient_col].unique().tolist())
		df2_patients_unique = set(self.df2[self.patient_col].unique().tolist())
		
		patients_in_both_groups = df1_patients_unique.intersection(df2_patients_unique)

		# leakage contains true if there is patient overlap, otherwise false.
		leakage = len(patients_in_both_groups) >= 1  # boolean (true if there is at least 1 patient in both groups)

		return leakage


print("Test Case 1")

df1 = pd.DataFrame({'patient_id': [0, 1, 2]})
df2 = pd.DataFrame({'patient_id': [2, 3, 4]})

leakageinspector = LeakageInspector(df1, df2, 'patient_id')
print(f'This is df1 {df1}')
print("-------------------------------------")
print(f'This is df2 {df2}')
print(f"leakage output: {leakageinspector.check_for_leakage()}")
print("-------------------------------------")


print("-------------------------------------")
print("-------------------------------------")
print("-------------------------------------")

print("Test Case 2")


df1 = pd.DataFrame({'patient_id': [0, 1, 2]})
df2 = pd.DataFrame({'patient_id': [3, 4, 5]})

leakageinspector = LeakageInspector(df1, df2, 'patient_id')
print(f'This is df1 {df1}')
print("-------------------------------------")
print(f'This is df2 {df2}')
print(f"leakage output: {leakageinspector.check_for_leakage()}")
print("-------------------------------------")
