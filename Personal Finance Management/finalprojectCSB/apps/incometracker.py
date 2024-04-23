import streamlit as st

def app():
    st.title("Income Tracker")

    # Get user input for income.
    income = get_user_income()

    # Button to save the income
    if st.button("Save Income"):
        save_income_to_file(income, "income.csv")
        st.success("Income saved successfully!")

def get_user_income():
    st.subheader("Enter Income Details")
    income_name = st.text_input("Enter income source:")
    income_amount = st.number_input("Enter income amount:", min_value=0.0, step=0.01)
    income_categories = [
        "Salary",
        "Freelance",
        "Investment",
        "Bonus",
        "Other",
    ]
    selected_category = st.selectbox("Select an income category:", income_categories)

    return {
        "name": income_name,  # Added this line to include the name field # type: ignore
        "amount": income_amount,
        "category": selected_category
    }

def save_income_to_file(income, income_file_path):
    st.subheader("Saving User Income")
    with open(income_file_path, "a", encoding="utf-8") as f:
        f.write(f"{income['name']},{income['amount']},{income['category']}\n")

# if __name__ == "__main__":
#     app()
