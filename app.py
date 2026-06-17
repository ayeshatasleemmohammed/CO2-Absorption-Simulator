import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def f(Ls, G1):
    # Given Data
    y1 = 0.2  # Amount of C in solution(C+G)
    Y1 = (y1) / (1 - y1)
    Gs = (G1) / (1 + Y1)
    y2 = y1 - (0.95 * y1)
    Y2 = (y2) / (1 - y2)
    X2 = 0  # pure solvent inlet
    X_max = X2 + ((Gs / Ls) * (Y1 - Y2))

    def operating_line(X):
        return Y2 + ((Ls / Gs) * (X - X2))

    def equilibrium_line(K):
        return 1.32 * K

    X_equilibrium = np.linspace(X2, X_max, 200)
    Y_equilibrium = []
    for element in X_equilibrium:
        Y_equilibrium.append(equilibrium_line(element))
    X_current = X2
    Y_current = Y2
    X_step = [X_current]
    Y_step = [Y_current]
    n_ideal = 0
    while True:
        X_eq = (Y_current) / (1.32)
        X_step.append(X_eq)
        Y_step.append(Y_current)
        Y_op = operating_line(X_eq)
        X_step.append(X_eq)
        Y_step.append(Y_op)
        if Y_op >= Y1:
            break
        n_ideal += 1
        Y_current = Y_op
    return n_ideal, Ls / Gs


st.title("CO2 Absorption column Simulation(McCabe theile method)")
st.write("Enter the cases manually and analyse L/G vs number of trays")
n = st.number_input("Number of cases:", min_value=1, max_value=20, value=5)
Ls_list = []
G1_list = []
st.subheader("Input data:")
for i in range(int(n)):
    Ls = st.number_input(
        f"solvent flow rate in kg/h-case{i + 1}: ", value=7685.0, key=f"Ls{i}"
    )
    G1 = st.number_input(
        f"feed gas flow rate in kg/h-case{i + 1}: ", value=7685.0, key=f"G1{i}"
    )
    y1 = 0.2  # Amount of C in solution(C+G)
    Y1 = (y1) / (1 - y1)
    Gs = (G1) / (1 + Y1)
    Ls_list.append(Ls)
    G1_list.append(G1)
if st.button("Run simulation"):
    LG_list = []
    tray_list = []
    for i in range(int(n)):
        tray, LG = f(Ls_list[i], G1_list[i])
        tray_list.append(tray)
        LG_list.append(LG)
    LG_list = np.array(LG_list)
    trays_list = np.array(tray_list)
    sorted_index = np.argsort(LG)
    LG_list = LG_list[sorted_index]
    tray_list = tray_list[sorted_index]
    st.subheader("Results table")
    for i in range(int(n)):
        st.write(
            f"case{i + 1} L/G = {LG_list[i]:.3f},no.of ideal trays = {tray_list[i]}"
        )
    fig, ax = plt.subplots()
    ax.scatter(LG_list, tray_list, label="simulation points")
    ax.set_ylabel("No.of trays(n)")
    ax.set_xlabel("L/G(Ratio of flowrate of solvent to feed gas on mole free basis)")
    ax.plot(LG_list, tray_list, linestyle="--", alpha=0.6, label="change w.r.t L/G")
    ax.set_title("CHANGE IN NUMBER OF TRAYS WITH Ls,Gs")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)
