# AI-Based Smart Study Planner

##  Overview

The **AI-Based Smart Study Planner** is a machine learning project designed to help students organize their study schedule efficiently. It predicts the priority of subjects based on their difficulty and deadlines, and generates an optimized study plan.

This project applies concepts from Artificial Intelligence and Machine Learning to solve a real-world problem of time management.

##  Problem Statement

Students often struggle with:

* Managing multiple subjects
* Prioritizing difficult topics
* Handling deadlines effectively

This project provides an intelligent solution that automatically generates a study plan based on user inputs.

##  Features

* Input multiple subjects with difficulty and deadlines
* Predict subject priority using Machine Learning
* Generate optimized study schedule
* Display results in sorted order
* Visualize priorities using graphs

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* Matplotlib

##  Project Structure

```
Smart-Study-Planner/
│
├── app.py
├── model.py
├── planner.py
├── student_data.csv
├── requirements.txt
└── README.md
```
##  Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/your-username/smart-study-planner.git
cd smart-study-planner
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run the Application

```
streamlit run app.py
```

## Usage

1. Enter the number of subjects
2. Provide:

   * Subject name
   * Difficulty level (1–5)
   * Days left
3. Click **Generate Plan**
4. View:

   * Priority scores
   * Sorted study plan
   * Graph visualization

##  Output
<img width="322" height="809" alt="Screenshot 2026-03-28 210605" src="https://github.com/user-attachments/assets/1f888f83-1a9e-4139-9afd-672fc50dc0a6" />


##  Algorithms Used

* **Linear Regression** (for priority prediction)
* **Heuristic Sorting** (for schedule optimization)

##  Challenges Faced

* Handling Python import errors
* Managing file paths
* Debugging Streamlit rendering issues
* Structuring the project properly

##  Future Improvements

* Calendar integration
* Reminder notifications
* Advanced ML models
* Chatbot support

##  Conclusion

This project demonstrates how Artificial Intelligence can be used to improve productivity and decision-making in everyday life. It provides an effective and user-friendly way to plan studies efficiently.
