import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set up the page
st.set_page_config(page_title="BudgetBuddy", page_icon="💰")

# Initialize session state for transactions if not already done
if 'transactions' not in st.session_state:
    st.session_state['transactions'] = []

# Title of the application
st.title("Money Manager 💰")

# Form to add a new transaction
st.header("Add New Transaction")
with st.form("transaction_form"):
    date = st.date_input("Date")
    category = st.selectbox("Category", ["Income", "Expense"])
    description = st.text_input("Description")
    amount = st.number_input("Amount", step=0.01, format="%.2f")
    submit = st.form_submit_button("Add Transaction")

    if submit:
        st.session_state['transactions'].append({"Date": date, "Category": category, "Description": description, "Amount": amount})
        st.success("Transaction added successfully!")

# Display transaction history
st.header("Transaction History")
if st.session_state['transactions']:
    df = pd.DataFrame(st.session_state['transactions'])
    st.dataframe(df)

    # Display summary
    st.header("Summary")
    income = df[df['Category'] == "Income"]['Amount'].sum()
    expense = df[df['Category'] == "Expense"]['Amount'].sum()
    balance = income - expense

    st.metric("Total Income", f"${income:,.2f}")
    st.metric("Total Expense", f"${expense:,.2f}")
    st.metric("Current Balance", f"${balance:,.2f}")

    # Display pie chart
    st.header("Expense vs Income")
    fig, ax = plt.subplots()
    ax.pie([income, expense], labels=["Income", "Expense"], autopct='%1.1f%%', colors=["#76c7c0", "#ff6f69"])
    st.pyplot(fig)
else:
    st.info("No transactions added yet.")

# Footer
st.markdown("---")
st.markdown("Developed with ❤️ using Streamlit")