import os
import sys
import nbimporter

# 获取当前目录
current_dir = os.getcwd()  # 获取当前工作目录（适用于 Jupyter Notebook）

# 定位到 src 文件夹（当前目录的上一级目录下的 src 文件夹），添加src到系统路径
src_path = os.path.join(current_dir, "../src")  # 如果 src 和 notebook 平级
src_path = os.path.abspath(src_path)
sys.path.append(src_path)

# 导入自定义模块
from cal_cpi import fetch_cpi_data, calculate_inflation

# Step 2: 获取 US CPI 数据
print("Fetching US CPI data...")
cpi_data = fetch_cpi_data()

# 查看原始数据
cpi_data.tail()

# Step 3: 计算最近 4 个季度的通胀率
print("Calculating the last 4 quarters of inflation...")
last_4_quarters = calculate_inflation(cpi_data)

# 展示结果
print("Last 4 Quarters Inflation Report:")
print(last_4_quarters)

# Step 4: 数据可视化（使用 matplotlib）
import matplotlib.pyplot as plt

# 绘制 CPI 曲线
plt.figure(figsize=(10, 6))
plt.plot(cpi_data.index, cpi_data['CPI'], label='CPI')
plt.title('US CPI Over Time')
plt.xlabel('Year')
plt.ylabel('CPI')
plt.grid()
plt.legend()
plt.show()

# 绘制最近 4 个季度的通胀率
last_4_quarters['CPI_Change'].plot(kind='bar', figsize=(8, 5), title='Last 4 Quarters Inflation (%)')
plt.ylabel('Inflation (%)')
plt.grid()
plt.show()