import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

@st.cache_data
def load_data():
    df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")
    return df

df = load_data()

# preprocess data
df["AgeGroup"] = pd.cut(df["Age"], bins=[18, 25, 35, 45, 55, 65], 
                        labels=["18-25", "26-35", "36-45", "46-55", "56-65"])

# main dashboard
st.title("📊 IBM HR Employee Attrition & Performance Dashboard")

st.write("### Data Preview")
st.dataframe(df)
st.write(f"👥 Dataset contains **{df.shape[0]} employees** and **{df.shape[1]} columns**.")

# attrition count plot
st.subheader("📌 Attrition Distribution")
fig = px.histogram(df, x="Attrition", color="Attrition", barmode="group")
st.plotly_chart(fig)

# age distribution
st.subheader("📌 Age Distribution of Employees")
fig2 = px.histogram(df, x="Age", nbins=20, color="Attrition", marginal="box")
st.plotly_chart(fig2)

# attrition by department
st.subheader("📌 Attrition by Department")
fig3 = px.bar(df, x="Department", color="Attrition", barmode="group")
st.plotly_chart(fig3)

# work-life balance vs Attrition
st.subheader("📌 Work-Life Balance Impact")
fig4 = px.box(df, x="WorkLifeBalance", y="TotalWorkingYears", color="Attrition")
st.plotly_chart(fig4)

# attrition by gender
st.subheader("📌 Attrition by Gender")
fig5 = px.histogram(df, x="Gender", color="Attrition", barmode="group")
st.plotly_chart(fig5)

# attrition by age group
st.subheader("📌 Attrition by Age Group")
fig6 = px.histogram(df, x="AgeGroup", color="Attrition", barmode="group")
st.plotly_chart(fig6)

# correlation heatmap
st.subheader("📌 Correlation Heatmap")
corr = df.select_dtypes(include=["number"]).corr()
plt.figure(figsize=(12,6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
st.pyplot(plt)

st.markdown("💡 *This dashboard provides insights into IBM HR data, analyzing attrition and employee performance.*")

st.markdown(
    """
    <hr>
    <div style='text-align: center;'>
        <p style='font-size: 1.2em; font-family: "Arial", sans-serif;'>
            © 2025 All rights reserved by <a href='https://github.com/Ironsoldier353' target='_blank'><img src='https://img.icons8.com/?size=100&id=LoL4bFzqmAa0&format=png&color=000000' height='30' style='vertical-align: middle;'></a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)