---
name: notebook-to-streamlit
description: Use when converting an existing Jupyter Notebook into a Streamlit
  app. Reuse the notebook's logic, map inputs to widgets, and preserve results
  across reruns.
---

## Step 1 — Reuse notebook logic

Read the existing notebook and reuse its functions and calculations.

Keep calculations separate from the Streamlit interface where possible.
Do not change formulas, assumptions, imported values, or optimization logic.

For simulations, use `seed=1` to keep results reproducible.


## Step 2 — Map inputs to Streamlit

Convert user inputs into appropriate Streamlit widgets.

| Notebook | Streamlit |
|---|---|
| categorical input | `st.selectbox` |
| numeric input | `st.number_input` or `st.slider` |
| value range | minimum and maximum inputs |
| `print(result)` | `st.write`, `st.metric`, or `st.success` |
| invalid input | `st.error(...)` then `st.stop()` |

Use notebook or imported values as defaults and validate inputs before performing calculations.


## Step 3 — Preserve results

Streamlit reruns the script after widget interactions.

When a button runs a calculation, save the result in `st.session_state` and
display it outside the button block so it remains visible after reruns.


## Done when

- [ ] The original notebook remains unchanged
- [ ] The app uses the notebook's existing calculations
- [ ] Required inputs are mapped to Streamlit widgets
- [ ] Inputs are validated
- [ ] Simulation results are reproducible
- [ ] Results remain visible after reruns
- [ ] Changing inputs changes the result appropriately
- [ ] The final result is clearly shown