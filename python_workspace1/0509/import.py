import pandas as pd

# CSV 파일 경로를 실제 경로로 바꿔주세요
df = pd.read_csv("auto-mpg.csv")

# 실린더 갯수별로 카운트
cylinder_counts = df['cylinders'].value_counts().sort_index()
print(cylinder_counts)