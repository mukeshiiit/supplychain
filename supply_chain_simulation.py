import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate neutrosophic mean and variance
def neutrosophic_mean_variance(k, theta_L, I_N):
    mu_N = k / (theta_L * (1 + I_N))  # Neutrosophic mean
    var_N = k / ((theta_L ** 2) * (1 + I_N) ** 2)  # Neutrosophic variance
    return round(mu_N, 4), round(var_N, 4)

# Classical model calculation (fixed processing rate)
def classical_mean_variance(k, theta_L):
    mu = k / theta_L  # Mean time in classical model
    var = k / (theta_L ** 2)  # Variance in classical model
    return round(mu, 4), round(var, 4)

# Initialize Streamlit UI components
st.title("Supply Chain Simulation System")

# Parameters for each stage
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

# Plot the results
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
