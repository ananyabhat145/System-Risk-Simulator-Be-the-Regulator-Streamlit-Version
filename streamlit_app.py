import streamlit as st
from solver.z3_engine import evaluate_constraints
import random

st.set_page_config(page_title="Systemic Risk Simulator", layout="wide")
st.title("🧩 Systemic Risk Simulator: Be the Regulator")

st.markdown("Simulate financial contagion and prevent systemic collapse using symbolic logic!")

# Create a synthetic network
def generate_network(n=10):
    return [
        {
            "id": f"Bank{i}",
            "L": random.uniform(50, 150),  # liquidity
            "O": random.uniform(100, 400),  # obligations
        }
        for i in range(n)
    ]

if "network" not in st.session_state:
    st.session_state.network = generate_network()

# Show table of banks
st.subheader("📊 Bank Status Table")
st.dataframe(st.session_state.network)

# Evaluate constraints
if st.button("🔍 Evaluate Network Constraints"):
    results = evaluate_constraints(st.session_state.network)

    st.subheader("🔬 Z3 Constraint Evaluation")
    for bank, result in results:
        color = "✅" if result == "sat" else "❌"
        st.markdown(f"- **{bank}**: {color} Constraint {'satisfied' if result == 'sat' else 'failed'}")

# Reset
if st.button("♻️ Reset Network"):
    st.session_state.network = generate_network()

