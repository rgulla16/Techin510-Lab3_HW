# Techin510-Lab3_HW

Data storage and retrieval using Python.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
```

# Ravinder's Winter Quarter Assignments Reminder

Welcome to Ravinder's Winter Quarter Assignments Reminder! This Streamlit app helps you manage your assignments efficiently.

## Overview
This app allows you to:
- Add new tasks with details like name, description, state, created date, creator, and category.
- Toggle the state of tasks (e.g., mark them as done or pending).
- View all tasks in a tabular format.

## How to Run
1. Make sure you have Python installed.
2. Install the required packages using `pip install streamlit streamlit-pydantic psycopg2`.
3. Clone this repository.
4. Set up your database configuration (SQLite or PostgreSQL) by updating the environment variables.
5. Run the app using `streamlit run app.py`.

## Lessons Learned
- Pydantic models simplify data validation and form handling.
- Streamlit provides an intuitive way to create interactive web apps.
- Connecting to databases (SQLite or PostgreSQL) is straightforward.
- Displaying data in columns using `st.dataframe` is convenient.

## Questions/Future Improvements
- How can we enhance the user interface?
- Are there additional features we can add (e.g., sorting, filtering)?
- How can we improve error handling?

Feel free to explore and contribute to this project! 🚀
