# Gas Absorption Designer

When I first learned the McCabe–Thiele method for gas absorption, I found myself repeatedly doing the same calculations by hand and wondering how the number of trays would change if I changed the operating conditions.

This project came from that curiosity.

I built this application using Python and Streamlit to simulate the absorption of CO₂ into water and estimate the number of ideal trays required for a given separation. Instead of solving a single problem, the app allows users to try different flow rates and observe how the design changes.

## Live App

https://gas-absorption-designer.streamlit.app/

## What the App Does

The app allows users to:

* Enter solvent and gas flow rates
* Calculate the corresponding L/G ratio
* Estimate the number of ideal trays required
* Compare multiple operating cases
* Visualize the relationship between L/G ratio and tray requirements

## Why I Built This

I wanted to do more than just solve numerical problems from class.

While studying Mass Transfer Operations, I realized that many calculations become much more intuitive when you can change parameters and immediately see the results. Building this project helped me understand the effect of operating conditions on absorber design and gave me a chance to apply Python to a Chemical Engineering problem.

## Methodology

The simulation is based on the McCabe–Thiele approach for gas absorption.

To keep the model simple and focused on the fundamentals, the following assumptions were made:

* CO₂ is absorbed into water
* Ideal trays are assumed
* The solvent enters free of solute
* A linear equilibrium relationship is used
* The process operates at steady state
* 95% of the incoming CO₂ is removed

The program performs stage-by-stage calculations to estimate the number of ideal trays required to achieve the target separation.

## Tools Used

* Python
* NumPy
* Matplotlib
* Streamlit

## Running the Project

Install the required packages:

pip install streamlit numpy matplotlib

Run the application:

streamlit run app.py

## What I Learned

This project helped me connect concepts from Mass Transfer Operations with programming. More importantly, it showed me how engineering calculations can be turned into interactive tools rather than remaining as isolated textbook problems.

## Future Plans

Some improvements I would like to add:

* McCabe–Thiele staircase visualization
* Packed column design calculations
* Tray efficiency corrections
* Comparison with Aspen Plus results
* Additional mass transfer simulation tools

## Author

Mohammed Ayesha Tasleem

B.Tech Chemical Engineering

NIT Warangal
