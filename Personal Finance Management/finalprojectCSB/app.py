import streamlit as st
from multiapp import MultiApp
from apps import analysis, expensesummary, expensetracker, incometracker, incomesummary

app = MultiApp()

st.markdown("""
# Personal Finance Management

This Personal Finance Management is using the [streamlit-multiapps]
""")

# Add all your applications here

app.add_app("Expense Summary", expensesummary.app)
app.add_app("Income Summary", incomesummary.app)
app.add_app("Expense Tracker", expensetracker.app)
app.add_app("Income Tracker", incometracker.app)
app.add_app("Analysis", analysis.app)


# Run the main app
app.run()
