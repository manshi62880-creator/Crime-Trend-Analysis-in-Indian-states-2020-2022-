import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("/storage/emulated/0/Download/NCRB_Table_1A.1.csv")

# Remove total rows
clean_data = data[~data["State/UT"].str.contains("Total")].copy()

# Top 5 states by crimes in 2022
top5 = clean_data.sort_values(by="2022", ascending=False).head()
print("Top 5 States by Crimes (2022):")
print(top5[["State/UT","2022"]])

# Highest crime rates per population
top_rate = clean_data.sort_values(by="Rate of Cognizable Crimes (IPC) (2022)", ascending=False).head()
print("\nTop 5 States by Crime Rate (per 100,000 people):")
print(top_rate[["State/UT","Rate of Cognizable Crimes (IPC) (2022)"]])

# Safest states
safest = clean_data.sort_values(by="Rate of Cognizable Crimes (IPC) (2022)", ascending=True).head()
print("\nSafest 5 States by Crime Rate:")
print(safest[["State/UT","Rate of Cognizable Crimes (IPC) (2022)"]])

# Crime growth 2020→2022
clean_data["Crime Growth"] = clean_data["2022"] - clean_data["2020"]
growth = clean_data.sort_values(by="Crime Growth", ascending=False).head()
print("\nStates with Highest Crime Growth (2020→2022):")
print(growth[["State/UT","Crime Growth"]])

# Compare trends for Kerala, Delhi, Uttar Pradesh
states = ["Kerala","Delhi","Uttar Pradesh"]
years = ["2020","2021","2022"]

for s in states:
    row = clean_data[clean_data["State/UT"] == s]
    values = row[years].values.flatten()
    plt.plot(years, values, marker='o', label=s)

plt.title("Crime Trends Comparison (2020–2022)")
plt.xlabel("Year")
plt.ylabel("Number of Crimes")
plt.legend()
plt.show()
