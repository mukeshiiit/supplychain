import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate neutrosophic mean and variance for a given stage
def neutrosophic_mean_variance(k, theta_L, I_N):
    mu_N = k / (theta_L * (1 + I_N))  # Neutrosophic mean: Average time considering uncertainty
    var_N = k / ((theta_L ** 2) * (1 + I_N) ** 2)  # Neutrosophic variance: How much time varies
    return round(mu_N, 4), round(var_N, 4)

# Classical model calculation (fixed processing rate, no uncertainty)
def classical_mean_variance(k, theta_L):
    # Classical Mean: Average time to process one unit through the stage
    if theta_L != 0:
        mu = k / theta_L  # Mean time in classical model
    else:
        mu = 0  # Handling edge case where processing rate is 0
    
    # Classical Variance: How much the processing time varies in a deterministic system
    if theta_L != 0:
        var = k / (theta_L ** 2)  # Variance in classical model
    else:
        var = 0  # Handling edge case where processing rate is 0
    
    return round(mu, 4), round(var, 4)

# Streamlit UI Setup
st.title("Supply Chain Simulation System")

# Description of the project
st.markdown("""
### Project Overview
This simulation models a **supply chain system** consisting of **four stages**:
1. **Receiving** - When goods are received from suppliers.
2. **Storage** - When goods are stored in the warehouse.
3. **Sorting/Processing** - When goods are sorted and prepared for shipment.
4. **Shipping** - When goods are shipped to customers.

Each of these stages can have **uncertainty** in the form of delays or variability in processing times. The goal of this project is to model these stages using two approaches:
1. **Classical Model**: Assumes fixed processing times with no uncertainty.
2. **Neutrosophic Model**: Accounts for **uncertainty** in the processing times, modeling real-world disruptions such as worker efficiency, machine failures, or environmental delays.

### Input Parameters
- **Number of Subtasks (k)**: Represents the number of tasks or steps in the processing stage. A higher value of \( k \) means more tasks are involved at each stage.
- **Processing Rate (θ_L)**: The rate at which packages are processed at each stage. A higher value means the stage can process more packages per unit time (faster).
- **Indeterminacy (I_N)**: This represents the **uncertainty** or **variability** in the processing time. A higher \( I_N \) value means more **uncertainty** in processing times.

### Output
- **Mean (μ_N)**: The **average time** it takes for a package to be processed at each stage. The **Neutrosophic Mean** incorporates the uncertainty in the system.
- **Variance (σ²_N)**: Measures how much the **processing time varies** from the mean. A higher variance means there is more **fluctuation** in the processing time.

You can adjust the sliders below to see how different values for each parameter affect the **processing times** (Mean and Variance) for both the **Classical Model** and the **Neutrosophic Model**.
""")

# Sidebar for input parameters
st.sidebar.header("Adjust Parameters")
k_value = st.sidebar.slider("Number of Subtasks (k)", 2, 5, 3)
theta_L_value = st.sidebar.slider("Processing Rate (θ_L)", 1, 5, 3)
I_N_value = st.sidebar.slider("Indeterminacy (I_N)", 0.0, 0.5, 0.2, 0.01)

# Simulate the system for the selected parameters
mu_neutro, var_neutro = neutrosophic_mean_variance(k_value, theta_L_value, I_N_value)
mu_classical, var_classical = classical_mean_variance(k_value, theta_L_value)

# Create DataFrame for displaying the results
simulation_results = {
    "Stage": ["Receiving", "Sorting", "Processing", "Shipping"],
    "Classical Mean (μ)": [mu_classical, mu_classical, mu_classical, mu_classical],
    "Neutrosophic Mean (μ_N)": [mu_neutro, mu_neutro, mu_neutro, mu_neutro],
    "Classical Variance (σ²)": [var_classical, var_classical, var_classical, var_classical],
    "Neutrosophic Variance (σ²_N)": [var_neutro, var_neutro, var_neutro, var_neutro],
}

df_simulation = pd.DataFrame(simulation_results)

# Display the result table
st.subheader("Simulation Results")
st.write(df_simulation)

# Plot the results for classical vs. neutrosophic mean times
fig, ax = plt.subplots(figsize=(10, 6))
st.subheader("Comparison of Classical and Neutrosophic Models")

ax.bar(df_simulation["Stage"], df_simulation["Classical Mean (μ)"], width=0.3, label="Classical Mean", align="center")
ax.bar(df_simulation["Stage"], df_simulation["Neutrosophic Mean (μ_N)"], width=0.3, label="Neutrosophic Mean", align="edge")

ax.set_xlabel('Stage')
ax.set_ylabel('Mean Processing Time (Seconds)')
ax.legend()

# Display the plot
st.pyplot(fig)

# Optional: Run this code locally by saving it in a file (e.g., `app.py`) and running the command `streamlit run app.py`
