# Rosa's Pizza Delivery Promise Optimizer

## Project Overview

This project is a Streamlit web application for Rosa's Pizza.

The purpose of the app is to help Rosa choose the most profitable promised
delivery time for a selected delivery zone and time block.

The application is based on analysis already completed in the A1 notebook.
The existing logic should be preserved when building the Streamlit application.

## Important Instructions

Before creating or modifying the Streamlit application:

1. Read the existing A1.ipynb to understand the analysis and functions.
2. Read and use the project-specific skill located at:

   `.github/skills/notebook-to-streamlit/SKILL.md`

3. Reuse the logic from the notebook when implementing calculations in the app.
4. Keep the Python code simple, readable, and appropriate for an introductory
   Python/data analytics course.
5. Do not unnecessarily refactor working notebook logic into advanced Python.
6. Do not modify the `starter` package.

## Starter Package

The project uses the `rosa-starter` package.

Import the required objects using:

    import numpy as np
    from starter import ZONES, TIME_BLOCKS, COSTS, PROMISE, delivery_times

Do not manually recreate:

- ZONES
- TIME_BLOCKS
- COSTS
- PROMISE
- delivery_times

These must come from the `starter` package.

The package is installed from:

    git+https://github.com/zhouy185/rosa-starter.git

Make sure this dependency is included in `requirements.txt` so that the
application can run on Streamlit Community Cloud.

## Existing Analysis

The notebook contains functions for:

- calculating the percentage of late orders
- calculating average delivery time
- calculating the cost associated with one late order
- evaluating net profit for different promised delivery times
- identifying the promised delivery time that produces the highest net profit

Use these existing calculations as the basis of the Streamlit application.

The main optimization logic is:

    profit from orders =
        number of orders * profit margin per order

    late delivery cost =
        number of late orders * cost per late order

    net profit =
        profit from orders - late delivery cost

The cost of one late order includes:

    refund cost + lost profit from customer churn

Use the exact keys contained in the imported COSTS dictionary. Do not assume
dictionary key names without checking them.

## Streamlit Application Requirements

Create the main application in:

    app.py

The application should have a clear title such as:

    Rosa's Pizza Delivery Promise Optimizer

Add a short explanation telling the user that the app finds the promised
delivery time that maximizes estimated net profit.

### 1. Zone Selection

Create a dropdown menu using `st.selectbox`.

The available choices must come directly from:

    ZONES

Do not hard-code the zone names.

### 2. Time Block Selection

Create another dropdown menu using `st.selectbox`.

The available choices must come directly from:

    TIME_BLOCKS

Do not hard-code the time-block names.

### 3. Promise Range

Allow the user to select:

- minimum promised delivery time
- maximum promised delivery time

Promises should be evaluated in 5-minute increments.

For example, if the user selects a minimum of 30 and maximum of 75, the app
should evaluate:

    30, 35, 40, 45, 50, 55, 60, 65, 70, 75

Validate the inputs so that the minimum cannot be greater than the maximum.

### 4. Cost Assumptions

Allow the user to adjust:

- profit margin per order
- estimated future orders lost after a late order (customer churn)
- refund cost per late order

The default values should come from the imported `COSTS` dictionary.

Create a new costs dictionary from the user's selected values and pass this
dictionary to the optimization function.

Do not modify the original imported COSTS dictionary.

### 5. Recommendation Button

Include a button such as:

    Find Best Promise

Do not calculate and display the final recommendation until the user clicks
this button.

When clicked, use the optimization function from the notebook to determine the
promised delivery time with the highest estimated net profit.

### 6. Results

Clearly display:

- recommended promised delivery time in minutes
- estimated net profit associated with that promise

Format monetary values to two decimal places.

For example:

    Recommended promise: 60 minutes
    Estimated net profit: $984.20

The result should be visually prominent and easy to understand.

## Simulation and Reproducibility

`delivery_times()` is a simulator and can produce different results on
different calls.

Use a consistent seed when comparing promised delivery times so that results
are reproducible and differences are caused by the promise being evaluated
rather than uncontrolled simulation randomness.

Keep the seed implementation consistent with the approach used in the
Jupyter Notebook.

## User Interface

Keep the interface clean, simple, and professional.

A small amount of pizza-themed styling or emoji is acceptable, but the app
should prioritize readability and usability.

Do not add unnecessary pages, animations, authentication, databases, or other
features that are outside the assignment requirements.

The app should be understandable without requiring the user to know Python.

## Error Handling

Handle basic invalid inputs gracefully.

For example:

- minimum promise greater than maximum promise
- empty promise range
- invalid numeric inputs

Display understandable Streamlit error messages instead of allowing the
application to crash.

## Code Style

Prioritize beginner-friendly Python.

Prefer:

- straightforward functions
- lists
- dictionaries
- loops
- if/else statements
- NumPy where appropriate

Avoid introducing advanced abstractions unless they are genuinely necessary.

Use descriptive variable names and brief comments explaining important
calculations.

## Files

The final project should contain at least:

    app.py
    requirements.txt
    CLAUDE.md
    .github/skills/notebook-to-streamlit/SKILL.md

The existing Jupyter Notebook should remain in the project.

## requirements.txt

Ensure `requirements.txt` includes the dependencies needed for deployment,
including:

    streamlit
    numpy
    git+https://github.com/zhouy185/rosa-starter.git

Do not add unnecessary dependencies.

## Final Checks

Before considering the application complete:

1. Verify that the app imports successfully.
2. Verify that every zone in ZONES can be selected.
3. Verify that every time block in TIME_BLOCKS can be selected.
4. Verify that changing the promise range changes the promises evaluated.
5. Verify that changing cost assumptions affects the optimization.
6. Verify that the recommendation is based on maximum net profit.
7. Verify that monetary output is formatted to two decimal places.
8. Verify that invalid promise ranges are handled gracefully.
9. Verify that the application can be run with Streamlit.
10. Verify that requirements.txt contains everything needed for deployment.
11. Keep the implementation consistent with the Jupyter Notebook.
12. Do not change the analytical methodology without a clear reason.