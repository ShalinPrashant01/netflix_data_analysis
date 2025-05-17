# 📊 Netflix Data Analysis Project

This project performs data analysis on Netflix titles using Python and popular data science libraries like Pandas and Matplotlib. The goal is to extract insights and visualize trends from the publicly available dataset.

## 📁 Dataset

- **Source:** [Netflix Titles Dataset on Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- **File:** `netflix_titles.csv`
- **Columns:** show_id, type, title, director, cast, country, date_added, release_year, rating, duration, genres, description

---

## 🛠️ Features & Steps

### ✅ Step 1: Set Up the Environment
- Create a virtual environment:
  ```bash
  python -m venv venv
Activate the environment:

bash
Copy
Edit
venv\Scripts\activate  # On Windows
Install required libraries:

bash
Copy
Edit
pip install pandas numpy matplotlib
✅ Step 2: Load the Dataset
python
Copy
Edit
import pandas as pd
df = pd.read_csv('data/netflix_titles.csv')
print(df.head())
✅ Step 3: Clean the Data
Handle missing values

Convert date_added to datetime

Fill in Unknown for missing directors or countries

python
Copy
Edit
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['director'].fillna('Unknown', inplace=True)
df.dropna(inplace=True)
✅ Step 4: Exploratory Data Analysis (EDA)
Most frequent countries

Trend of new titles over the years

Type breakdown (Movie vs TV Show)

Top genres

python
Copy
Edit
import matplotlib.pyplot as plt
# Example: Plot count of Movies vs TV Shows
df['type'].value_counts().plot(kind='bar')
plt.title('Content Type Breakdown')
plt.show()
📸 Sample Output
📈 Charts for types of content

📅 Year-wise trend of new content

🌍 Top countries with most content

📂 Project Structure
kotlin
Copy
Edit
netflix_data_analysis/
│
├── data/
│   └── netflix_titles.csv
├── 01_load_clean.py
├── venv/
└── README.md
🚀 How to Run
Clone the repo:

bash
Copy
Edit
git clone https://github.com/ShalinPrashant01/netflix_data_analysis.git
cd netflix_data_analysis
Activate virtual environment and install dependencies:

bash
Copy
Edit
venv\Scripts\activate
pip install -r requirements.txt  # (if requirements.txt is added)
Run the script:

bash
Copy
Edit
python 01_load_clean.py
✨ Future Improvements
Add Spotify data for cross-platform insights

Use Seaborn or Plotly for better visuals

Deploy on Streamlit or Flask

🧑‍💻 Author
Shalin Prashant

📜 License
This project is open-source and available under the MIT License.

yaml
Copy
Edit

---

Let me know if you want to:

- Add a `requirements.txt`
- Generate fancier charts with Seaborn or Plotly
- Write a blog or publish this as a portfolio project

I'm happy to help!
