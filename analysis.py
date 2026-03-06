import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create charts folder if it doesn't exist
os.makedirs ("charts", exist_ok = True)

# Load dataset
df = pd.read_csv ("data/311_requests.csv", nrows = 100000)

# Convert date columns
df["open_date"] = pd.to_datetime (df["open_date"], errors = "coerce")
df["close_date"] = pd.to_datetime (df["close_date"], errors = "coerce")


# Chart 1: Top complaint topics

top_topics = df["case_topic"].value_counts().head(10)

plt.figure(figsize=(10, 5))
sns.barplot(x=top_topics.values, y=top_topics.index)
plt.title("Top Boston 311 Complaint Topics")
plt.xlabel("Number of Requests")
plt.ylabel("Topic")
plt.tight_layout()
plt.savefig("charts/top_topics.png")
plt.close()


# Chart 2: Requests by month

df["month"] = df["open_date"].dt.month
monthly = df["month"].value_counts().sort_index()

plt.figure(figsize = (10, 5))
sns.lineplot(x=monthly.index, y = monthly.values, marker = "o")
plt.title("Boston 311 Requests by Month")
plt.xlabel("Month")
plt.ylabel("Requests")
plt.tight_layout()
plt.savefig("charts/monthly_requests.png")
plt.close()

# Chart 3: Top assigned departments

top_departments = df["assigned_department"].value_counts().head(10)

plt.figure(figsize = (10, 5))
sns.barplot(x = top_departments.values, y = top_departments.index)
plt.title("Top Boston 311 Assigned Departments")
plt.xlabel("Number of Requests")
plt.ylabel("Department")
plt.tight_layout()
plt.savefig("charts/top_departments.png")
plt.close()

# Chart 4: Fastest average response times

df["response_time_hours"] = (
    (df["close_date"] - df["open_date"]).dt.total_seconds() / 3600
)

response_df = df.dropna(subset=["response_time_hours", "assigned_department"])
response_df = response_df[response_df["response_time_hours"] >= 0]

avg_response = (
    response_df.groupby("assigned_department")["response_time_hours"]
    .mean()
    .sort_values()
    .head(10)
)

plt.figure(figsize=(10, 5))
sns.barplot(x=avg_response.values, y=avg_response.index)
plt.title("Fastest Average Response Times by Department (Hours)")
plt.xlabel("Average Response Time (Hours)")
plt.ylabel("Department")
plt.tight_layout()
plt.savefig("charts/response_times.png")
plt.close()

print("All charts created")