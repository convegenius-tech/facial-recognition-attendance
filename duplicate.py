import pandas as pd
import csv


df_state = pd.read_csv(r"C:\Users\Reks\Desktop\myProj\Facial-Recognition-Based-Student-Attendance-System\Team23.csv")

DF_RM_DUP = df_state.drop_duplicates(keep=False)
DF_RM_DUP.to_csv('test1.csv', index=False) 








