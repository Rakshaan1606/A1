# Rosa's Pizza Delivery Promise Optimizer

This project converts the analysis in `A1.ipynb` into a Streamlit app for finding the most profitable promised delivery time.

## Commands

- Use the existing project environment and dependencies.
- App: `uv run streamlit run app.py`
- Keep `streamlit`, `numpy`, and `rosa-starter` in `requirements.txt` for
  Streamlit Community Cloud deployment.

## Architecture

- `A1.ipynb` contains the original analysis and calculation logic.
- `app.py` is the Streamlit interface. It should reuse the notebook's logic
  rather than introduce a different analytical approach.
- Use the `notebook-to-streamlit` skill at
  `.github/skills/notebook-to-streamlit/SKILL.md`.
- Import `ZONES`, `TIME_BLOCKS`, `COSTS`, `PROMISE`, and `delivery_times`
  from `starter`. Do not recreate them.
- Use the exact keys provided by `COSTS`.
- Keep calculation functions separate from the Streamlit interface where
  practical.
- Use `seed=1` with `delivery_times()` so comparisons are reproducible.

## App Behaviour

- Select a delivery zone from `ZONES`.
- Select a time block from `TIME_BLOCKS`.
- Let the user set minimum and maximum promised delivery times, evaluated
  in 5-minute increments.
- Let the user adjust profit margin, churn, and refund cost, using `COSTS`
  as the defaults.
- A "Find Best Promise" button runs the existing optimization.
- Display the recommended promise and estimated net profit.
- Store results in `st.session_state` so they remain visible after reruns.
- Validate inputs and show clear errors for invalid promise ranges.

## Constraints

- Preserve the calculations and methodology from `A1.ipynb`.
- Do not modify the `starter` package.
- Do not modify the original `COSTS` dictionary.
- Reuse existing code rather than duplicating logic.
- Do not add unnecessary pages, dependencies, databases, authentication or other features.
- Keep the interface simple and readable.