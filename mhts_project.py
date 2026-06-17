#importing libraries
import streamlit as st 
import numpy as np
import pandas as pd
import io
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#separator
st.markdown("""<hr style="border:2px solid purple; border-radius:5px;">""",unsafe_allow_html=True)

#setting title of project
st.markdown("<h2 style='color:purple; font-family:Times New Roman;'>Mental Health Analysis of IT Professionals</h2>", unsafe_allow_html=True)

#load dataset
df=pd.read_csv("Dataset_MHTS_PROJECT.csv")
df = pd.DataFrame(df)

# Display the image 
st.image("Mental-Health-At-Work.jpg", width=650)
st.markdown(
    """
    <style>
    img {
        display: block;
        margin: auto;
        border-radius: 15px; /* Rounded corners */
        box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3); /* Soft shadow */
        border: 4px solid purple; /* Purple border */
    }
    </style>
    """, unsafe_allow_html=True)

#set background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: Thistle; /* Celadon", a soft, light green shade. */
    }
    </style>
    """,unsafe_allow_html=True)

#animated text
st.markdown(
    """
    <style>
    @keyframes fade {
        0%, 100% { opacity: 0; }
        25%, 75% { opacity: 1; }
    }
    .slogan {
        font-family: 'Times New Roman', serif;
        font-size: 24px;
        font-weight: bold;
        color: DarkGreen;
        text-align: center;
        animation: fade 6s infinite alternate;
    }
    </style>
    <div class="slogan">"Work Hard, but Care for Your Mind Harder!"</div>
    """,
    unsafe_allow_html=True)

# Window border
st.markdown(
    """
    <style>
    .stApp {
        border: 5px solid purple; /* Border color */
        border-radius: 15px; /* Rounded corners */
        padding: 20px; /* Space inside the border */
        margin: 20px; /* Space outside the border */
    }
    </style>
    """,unsafe_allow_html=True)

#separator
st.markdown( """<hr style="border:2px solid purple; border-radius:5px;">""",unsafe_allow_html=True)

# Chart Headers
st.markdown(
    """
    <style>
    .custom-header {
        font-size: 26px;
        font-weight: bold;
        color: white;
        background-color: purple;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Display Custom Header
#st.markdown('<div class="custom-header">📊 Dataset Preview - First 5 Rows</div>', unsafe_allow_html=True)
#Display Head
#st.write(df.head())
#st.markdown('</div>', unsafe_allow_html=True)

#CONVERSION 1-0
df = pd.DataFrame(df)

df['Treatment'] = df['Treatment'].replace({'Yes': 1, 'No': 0})
df['Promotion Status'] = df['Promotion Status'].replace({'Yes': 1, 'No': 0})
df['Family History'] = df['Family History'].replace({'Yes': 1, 'No': 0})
df['Remote Work'] = df['Remote Work'].replace({'Yes': 1, 'No': 0})
df['Co-worker'] = df['Co-worker'].replace({'Yes': 1, 'No': 0})
df['Supervisor'] = df['Supervisor'].replace({'Yes': 1, 'No': 0})
df['Self employed'] = df['Self employed'].replace({'Yes': 1, 'No': 0})
df['Healthcare Availability'] = df['Healthcare Availability'].replace({'Yes': 1, 'No': 0})

#new column
#st.markdown('<div class="custom-header">📊 Newly Added Columns </div>', unsafe_allow_html=True)

#Depressed Person column creation
# Define the condition for depression
def check_depression(row):
    if (row["Deadline Status"] in ["Pending", "Outdated"]and 
        row["Mood Swings"] in ["Stressed", "Depressed", "Irritated"] and 
        row["Family History"] == 1 and 
        row["Treatment"] == 1):
        return "Depressed Person"
    else:
        return "Not Depressed Person"
# Apply the function to create the "depression" column
df["Depressed People"] = df.apply(check_depression, axis=1)
#st.dataframe(df)

# Function to highlight specific columns
def highlight_cols(s, cols=['Age Group','Depressed People']):
    styles = {col: 'background-color: #D8BFD8; font-weight: bold; color: black;' for col in cols}  # Thistle purple color highlight
    return s.style.apply(lambda x: [styles.get(col, '') for col in x.index], axis=1)

# Display Table with Highlighted Columns
#st.write(highlight_cols(df, cols=['Age Group','Depressed People']))  

#data visualization

#separator
#st.markdown( """<hr style="border:2px solid green; border-radius:5px;">""",unsafe_allow_html=True)

st.subheader("📊 Key Insights")
total_emp_color = "background-color: #1E3A8A; color: white; padding: 15px; border-radius: 10px; text-align: center; font-size: 18px; font-weight: bold;"
male_color = "background-color: #1E3A8A; color: white; padding: 15px; border-radius: 10px; text-align: center; font-size: 18px; font-weight: bold;"
female_color = "background-color: #1E3A8A; color: white; padding: 15px; border-radius: 10px; text-align: center; font-size: 18px; font-weight: bold;"
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f'<div style="{total_emp_color}"> 👥🤝Total Employees <br> <span style="font-size:24px;">1500</span> </div>', unsafe_allow_html=True)
    #st.metric(label="Total Employees", value="1500")
with col2:
    st.markdown(f'<div style="{male_color}"> ♂️Total Male <br> <span style="font-size:24px;">857</span> </div>', unsafe_allow_html=True)
    #st.metric(label="Total Male", value="857")
with col3:
    st.markdown(f'<div style="{female_color}"> ♀️Total Female <br> <span style="font-size:24px;">643</span> </div>', unsafe_allow_html=True)
    #st.metric(label="Total Female", value="643")
    
#separator
st.markdown( """<hr style="border:2px solid green; border-radius:5px;">""",unsafe_allow_html=True)

#chart 1
st.markdown('<div class="custom-header">📊 Depressed People Vs Not Depressed People </div>', unsafe_allow_html=True)
fig, ax = plt.subplots()
sns.countplot(x="Depressed People", data=df, ax=ax, color="MediumSeaGreen")
st.pyplot(fig)
st.markdown("<h5>From the above chart, We can see that the number of people who are depressed is less. So, this problem can be solved by taking appropriate actions.</h5>", unsafe_allow_html=True)

#chart 2
st.markdown('<div class="custom-header">📊 Promotion Status of Employees </div>', unsafe_allow_html=True)
data = df["Promotion Status"].value_counts()
labels = ["Not Promoted", "Promoted"]  
colors = ["#3CB371", "#1E3A8A"]  # MediumSeaGreen & Deep Navy Blue
fig, ax = plt.subplots()
ax.pie(data, labels=labels, autopct="%1.1f%%", startangle=90, colors=colors)
st.pyplot(fig)
st.markdown("<h5>From the above chart, we can see that the percentage of promoted employees is less i.e. 30% and the ratio of not promoted employees is more i.e. 70%.</h5>", unsafe_allow_html=True)

#chart 3
st.markdown('<div class="custom-header">📊 Depressed People Distribution by Designation </div>', unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(x="Designation", hue="Depressed People", data=df, palette=["#1E3A8A", "#3CB371"], ax=ax)
plt.xticks(rotation=90)  
st.pyplot(fig)
st.markdown("<h5>The above chart shows that the depressed people distribution by designation. Here we can see that the Account Manager, QA, Analyst and Developer designation employees are more depressed and the employees of designation CS Engineer is very less depressed. </h5>", unsafe_allow_html=True)

#chart 4
st.markdown('<div class="custom-header">📊Family History vs Treatment Status </div>', unsafe_allow_html=True)
df["Family History"] = df["Family History"].map({1: "Yes", 0: "No"})
df["Treatment"] = df["Treatment"].map({1: "Received", 0: "Not Received"})
fig, ax = plt.subplots(figsize=(6, 4))
sns.countplot(data=df, x="Family History", hue="Treatment", palette=["#1E3A8A", "#3CB371"], ax=ax)
plt.xlabel("Family History")
plt.ylabel("Number of People")
st.pyplot(fig)
st.markdown("<h5>As family history can affect the mental health of the employees and their treatment should be known. Here we have created a chart of Family history by Treatment. From this chart it is clear that the people with family history are very less and the people having treatment are also very less. It is concluded that the people may not be suffering this genetically.So other factors are affecting the mental health most.</h5>", unsafe_allow_html=True)

#chart 5
st.markdown('<div class="custom-header">Deadline Status Vs Depressed People </div>', unsafe_allow_html=True)
fig = px.sunburst(df, path=["Deadline Status", "Depressed People"])
st.plotly_chart(fig)
st.markdown("<h5>Workload can be the reason affecting the mental health of employees. So, we have created a chart of Deadline status Vs Depressed people to find the relation betweeen these two factors. So, it is clear that the employees who have completed their task and who completed their work before deadline are not depressed. If their work is pending or their work is outdated then they feel depressed. So the workload affects the most. So, for improving the mental health workload should be managed.</h5>", unsafe_allow_html=True)

#chart 6
st.markdown('<div class="custom-header">Company Rating </div>', unsafe_allow_html=True)
color_map = {
    "1": "#7E22CE","2": "#22C55E","3": "#FACC15","4": "#EF4444"}
fig = px.pie(df, names="Company Rating", hole=0.5,
             color="Company Rating",
             color_discrete_map=color_map)
st.plotly_chart(fig, use_container_width=True)
st.markdown("<h5>As the company environment may be reponsible for mental health. So, we created a donut chart showing company rating. The percentage of company rating 5 is more. From this , it is clear that the company environment is not affecting the mental health.</h5>", unsafe_allow_html=True)

#chart 7
st.markdown('<div class="custom-header">Relationship with collegues </div>', unsafe_allow_html=True)
fig = px.pie(df, names="Relationship with collegues", hole=0.4,
             color_discrete_sequence=px.colors.qualitative.Pastel)
st.plotly_chart(fig, use_container_width=True)
st.markdown("<h5>The next factor which can affect the mental health can be the relationship with collegues. From this chart, 60% people are having good relationship with their collegues and 40% people are having bad relationship wih their collegues.</h5>", unsafe_allow_html=True)

#chart 8
st.markdown('<div class="custom-header">Correlation Heatmap (Numeric Columns) </div>', unsafe_allow_html=True)
numeric_cols = df.select_dtypes(include='number')
corr = numeric_cols.corr()
fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, ax=ax)
st.pyplot(fig)
st.markdown("<h5>Here, in the above correlation heatmap we have taken numeric columns for better understanding the solution of the problem. \n(1) Employees who got promoted tend to have better relationship with co-workers. (2) Worse supervisor relationships are seen in those who got promoted. (3) Age, Remote Work, Salary, Leave, Working Hours, Company Rating, Self Employed, Healthcare Availability- mostly show no significant correlation with each other or with the Promotion status. (4) It is observed that as tasks get more difficult, satisfaction or rating drops slightly. </h5>", unsafe_allow_html=True)
st.markdown("<h5>(1) Also, people who have been promoted seem to have better relationships with coworkers (a strong positive link), but oddly, they report worse relationships with supervisors. This could mean that peers play a bigger role in someone's growth, or that once someone is promoted, tensions might grow with their boss.(2)On the other hand, most practical things like salary, remote work, working hours, and even healthcare availability don’t seem to have strong links to other factors. That tells us that in this data, emotional and social experiences at work matter more than logistical or financial ones when it comes to mental health and workplace satisfaction.</h5>", unsafe_allow_html=True)

#chart 9
st.markdown('<div class="custom-header">Depressed People by Gender & Age Group</div>', unsafe_allow_html=True)
fig = px.sunburst(
    df,
    path=['Gender', 'Age Group', 'Depressed People'],
    color='Depressed People',
    color_continuous_scale='RdBu',
)
st.plotly_chart(fig, use_container_width=True)
st.markdown("<h5>Here we have created an advance sunburst chart to find the results. From this we can see that, (1)Male ratio is more than female. (2) Age group 1 has more employees in both gender. (3) Male are more depressed than females. (4) Male who belong to age group 1 are more depressed . So, need to take a note on this while making health related policies.</h5>", unsafe_allow_html=True )

#chart 10
st.markdown('<div class="custom-header">Promotion Distribution by Designation</div>', unsafe_allow_html=True)
fig = px.treemap(df, path=['Designation', 'Promotion Status'],  color='Promotion Status')
st.plotly_chart(fig)
st.markdown("<h5>From the above chart, it is clear that we can see the different designation employee's promotion status. We have analyzed that Developer, Data Analyst and QA employees got more promotion than other designation employees.</h5>", unsafe_allow_html=True)

#separator
st.markdown("""<hr style="border:2px solid purple; border-radius:5px;">""",unsafe_allow_html=True)

#animated text
st.markdown(
    """
    <style>
    @keyframes fade {
        0%, 100% { opacity: 0; }
        25%, 75% { opacity: 1; }
    }
    .slogan {
        font-family: 'Times New Roman', serif;
        font-size: 24px;
        font-weight: bold;
        color: DarkGreen;
        text-align: center;
        animation: fade 6s infinite alternate;
    }
    </style>
    <div class="slogan">"Peace of mind isn't something you find. It’s something you create"</div>
    """,
    unsafe_allow_html=True)

#separator
st.markdown("""<hr style="border:2px solid purple; border-radius:5px;">""",unsafe_allow_html=True)

