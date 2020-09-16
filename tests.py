import unittest
import pandas as pd
import LeakageInspector

class Test(unittest.TestCase):
    def test_case_1(self):
        df1 = pd.DataFrame({'patient_id': [0, 1, 2]})
        df2 = pd.DataFrame({'patient_id': [2, 3, 4]})
        self.assertEqual(LeakageInspector.LeakageInspector(df1, df2, 'patient_id').check_for_leakage(), True)

    def test_case_2(self):
        df1 = pd.DataFrame({'patient_id': [0, 1, 2]})
        df2 = pd.DataFrame({'patient_id': [3, 4, 5]})
        self.assertEqual(LeakageInspector.LeakageInspector(df1, df2, 'patient_id').check_for_leakage(), False)

if __name__ == '__main__':
    unittest.main()