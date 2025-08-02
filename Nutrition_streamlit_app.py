
import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Health Nutrition Dashboard", layout="wide")

st.sidebar.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGS5X0kpv1wGuNck4E3QsFJZY84Ndh4xdbow&s", width=100)
st.sidebar.title("🥗 Health Nutrition Dashboard")

def get_db_connection():
    return mysql.connector.connect(
        host="gateway01.us-east-1.prod.aws.tidbcloud.com",
        port=4000,
        user="2RF9f3Nuh4kLJBe.root",
        password="3nvycLptvyoI59Us",
        database="Health_Database"
    )

def run_query(query):
    conn = get_db_connection()
    try:
        df = pd.read_sql(query, conn)
        return df
    except Exception as e:
        st.error(f"Error executing query: {e}")
        return None
    finally:
        conn.close()

page = st.sidebar.radio("Navigate", ["Home", "Queries", "Combined Insights", "About"])

# ✅ Fixed variable name
obesity_queries = [
    "Top 5 regions with highest obesity in 2022",
    "Top 5 countries by max obesity",
    "Obesity trend in India",
    "Obesity by gender",
    "Country count by obesity level & age",
    "Countries with highest & lowest CI width",
    "Obesity by age group",
    "Consistently low obesity countries",
    "Female obesity much higher than male",
    "Global yearly average obesity"
]

obesity_queries_ans = [
    "SELECT Region, AVG(Mean_Estimate) AS avg_obesity FROM obesity WHERE Year = 2022 GROUP BY Region ORDER BY avg_obesity DESC LIMIT 5;",
    "SELECT Country, MAX(Mean_Estimate) AS max_obesity FROM obesity GROUP BY Country ORDER BY max_obesity DESC LIMIT 5;",
    "SELECT Year, Mean_Estimate FROM obesity WHERE Country = 'India' ORDER BY Year;",
    "SELECT Gender, AVG(Mean_Estimate) AS avg_obesity FROM obesity GROUP BY Gender;",
    "SELECT Country, age_group, COUNT(*) AS country_count FROM obesity GROUP BY Country, age_group;",
    "SELECT Country, AVG(CI_Width) AS avg_ci_width FROM obesity GROUP BY Country ORDER BY avg_ci_width ASC LIMIT 5;",
    "SELECT age_group, AVG(Mean_Estimate) AS avg_obesity FROM obesity GROUP BY age_group;",
    "SELECT Country, AVG(Mean_Estimate) AS avg_obesity FROM obesity GROUP BY Country ORDER BY avg_obesity ASC LIMIT 10;",
    "SELECT Year, Country, Mean_Estimate FROM obesity WHERE Gender = 'Female' AND Mean_Estimate > (SELECT MAX(Mean_Estimate) FROM obesity AS m WHERE m.Gender = 'Male' AND m.Year = obesity.Year AND m.Country = obesity.Country);",
    "SELECT Year, AVG(Mean_Estimate) AS global_avg_obesity FROM obesity GROUP BY Year ORDER BY Year;"
]

Malnutrition_Queries = [
    "Avg. malnutrition by age group",
    "Top 5 countries with highest malnutrition",
    "Malnutrition trend in Africa",
    "Gender-based average malnutrition",
    "CI Width by malnutrition level & age",
    "Malnutrition trend in India, Nigeria, Brazil",
    "Regions with lowest malnutrition",
    "Countries with increasing malnutrition",
    "Yearly min/max comparison",
    "High CI width cases"
]

Malnutrition_Queries_ans = [
    "SELECT age_group, AVG(Mean_Estimate) AS avg_malnutrition FROM malnutrition GROUP BY age_group;",
    "SELECT Country, AVG(Mean_Estimate) AS avg_malnutrition FROM malnutrition GROUP BY Country ORDER BY avg_malnutrition DESC LIMIT 5;",
    "SELECT Year, AVG(Mean_Estimate) AS avg_malnutrition FROM malnutrition WHERE Region = 'Africa' GROUP BY Year;",
    "SELECT Gender, AVG(Mean_Estimate) AS avg_malnutrition FROM malnutrition GROUP BY Gender;",
    "SELECT age_group, AVG(CI_Width) AS avg_ci_width FROM malnutrition GROUP BY age_group;",
    "SELECT Year, Country, AVG(Mean_Estimate) AS avg_malnutrition FROM malnutrition WHERE Country IN ('India', 'Nigeria', 'Brazil') GROUP BY Year, Country;",
    "SELECT Region, AVG(Mean_Estimate) AS avg_malnutrition FROM malnutrition GROUP BY Region ORDER BY avg_malnutrition ASC LIMIT 5;",
    "SELECT Country, MIN(Mean_Estimate), MAX(Mean_Estimate) FROM malnutrition GROUP BY Country HAVING MIN(Mean_Estimate) < MAX(Mean_Estimate);",
    "SELECT Year, MIN(Mean_Estimate), MAX(Mean_Estimate) FROM malnutrition GROUP BY Year;",
    "SELECT * FROM malnutrition WHERE CI_Width > 5 ORDER BY CI_Width DESC;"
]

Combined_queries = [
    "1. Obesity vs malnutrition comparison by country(any 5 countries)",
    "2. Gender-based disparity in both obesity and malnutrition",
    "3. Region-wise avg estimates side-by-side(Africa and America)",
    "4. Countries with obesity up & malnutrition down",
    "5. Age-wise trend analysis"
]

Combined_queries_ans = [
    "SELECT o.Country, AVG(o.Mean_Estimate) AS avg_obesity, AVG(m.Mean_Estimate) AS avg_malnutrition FROM obesity o JOIN malnutrition m ON o.Country = m.Country AND o.Year = m.Year WHERE o.Country IN ('India', 'USA', 'Nigeria', 'Brazil', 'China') GROUP BY o.Country;",
    "SELECT o.Gender, AVG(o.Mean_Estimate) AS avg_obesity, AVG(m.Mean_Estimate) AS avg_malnutrition FROM obesity o JOIN malnutrition m ON o.Country = m.Country AND o.Year = m.Year GROUP BY o.Gender;",
    "SELECT o.Region, o.Country, AVG(o.Mean_Estimate) AS avg_obesity, AVG(m.Mean_Estimate) AS avg_malnutrition FROM obesity o JOIN malnutrition m ON o.Country = m.Country AND o.Year = m.Year GROUP BY o.Region, o.Country;",
    "SELECT o.Country, o.Year, o.Mean_Estimate AS obesity_estimate, m.Mean_Estimate AS malnutrition_estimate FROM obesity o JOIN malnutrition m ON o.Country = m.Country AND o.Year = m.Year;",
    "SELECT o.age_group, o.Year, o.Mean_Estimate AS obesity_estimate, m.Mean_Estimate AS malnutrition_estimate FROM obesity o JOIN malnutrition m ON o.Country = m.Country AND o.Year = m.Year;"
]

# Home Page
if page == "Home":
    st.title("📊 Nutrition Insights Explorer")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### Welcome to the Health Nutrition Dashboard
        Explore and compare **Obesity** and **Malnutrition** statistics across regions, age groups, genders, and time.
        Use the side menu to run pre-defined queries and visualize trends interactively.
        """)
    with col2:
        st.image("https://medicircle.in/uploads/2021/january2021/how-important-is-nutrition-for-health.jpg", width=300)

# Queries Page
elif page == "Queries":
    st.header("Predefined SQL Queries")
    category = st.radio("Choose Query Type", ["Obesity Queries", "Malnutrition Queries", "Combined Queries"])

    if category == "Obesity Queries":
        desc = st.selectbox("Select Query:", obesity_queries)
        query = obesity_queries_ans[obesity_queries.index(desc)]
    elif category == "Malnutrition Queries":
        desc = st.selectbox("Select Query:", Malnutrition_Queries)
        query = Malnutrition_Queries_ans[Malnutrition_Queries.index(desc)]
    elif category == "Combined Queries":
        desc = st.selectbox("Select Query:", Combined_queries)
        query = Combined_queries_ans[Combined_queries.index(desc)]

    if st.button("Run Query"):
        df = run_query(query)
        if df is not None and not df.empty:
            st.subheader(desc)
            st.dataframe(df, use_container_width=True)
            numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
            if len(numeric_cols) > 0:
                col = st.selectbox("Select column to plot", numeric_cols)
                fig = px.bar(df, x=df.columns[0], y=col, title="Visual Representation")
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No data found or query failed.")

# Combined Insights Page
elif page == "Combined Insights":
    st.header("📈 Obesity vs Malnutrition Comparison")
    query = """
    SELECT o.Country, AVG(o.Mean_Estimate) AS avg_obesity, AVG(m.Mean_Estimate) AS avg_malnutrition
    FROM obesity o
    JOIN malnutrition m ON o.Country = m.Country AND o.Year = m.Year
    GROUP BY o.Country ORDER BY o.Country;
    """
    df = run_query(query)
    if df is not None:
        st.dataframe(df, use_container_width=True)
        fig = px.scatter(df, x="avg_obesity", y="avg_malnutrition", text="Country", title="Obesity vs Malnutrition by Country")
        st.plotly_chart(fig, use_container_width=True)

# About Page
elif page == "About":
    st.header("📚 About This App")
    st.write("This dashboard is built using **Streamlit**, **Plotly**, and **MySQL**. It provides interactive visualizations and SQL-powered insights into global **obesity** and **malnutrition** trends.")
    st.write("**Data Source**: Health_Database (from TiDB Cloud)")
    st.markdown("---")
    st.write("Developed by **Arun Kumar**")
    st.caption("Thank you for visiting!")

st.markdown("---")
st.caption("Developed by Arun Kumar | Powered by GUVI")
