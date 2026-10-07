import numpy as np
import streamlit as st
from starter import ZONES, TIME_BLOCKS, COSTS, PROMISE, delivery_times


# ---- Functions copied unchanged from the A1 notebook ----

def late_order_cost(costs):
    refund = costs["refund"]
    churn = costs["churn_orders"]
    margin = costs["margin"]

    lost_profit = churn * margin
    total_cost = refund + lost_profit

    return total_cost


def best_promise(zone, time_block, promises, costs):
    results = []
    cost_per_late = late_order_cost(costs)
    for p in promises:
        times = delivery_times(zone, time_block, p, seed=1)  # same seed every time
        late_orders = times > p
        number_late = np.sum(late_orders)
        order_profit = len(times) * costs["margin"]
        late_cost = number_late * cost_per_late
        net_profit = order_profit - late_cost
        results.append((net_profit, p))
    results.sort(reverse=True)
    best_net_profit = results[0][0]
    best_time = results[0][1]

    return best_time, best_net_profit


# ---- Streamlit app ----

st.title("🍕 Rosa's Pizza Delivery Promise Optimizer")
st.write(
    "This app finds the promised delivery time that maximizes estimated "
    "net profit for a delivery zone and time block."
)

# Zone and time block
zone = st.selectbox("Delivery zone", ZONES)
time_block = st.selectbox("Time block", TIME_BLOCKS)

# Promise range (5-minute increments)
col1, col2 = st.columns(2)
min_promise = col1.number_input("Minimum promise (minutes)", min_value=5, value=30, step=5)
max_promise = col2.number_input("Maximum promise (minutes)", min_value=5, value=75, step=5)

# Cost assumptions, defaulting to the imported COSTS
st.subheader("Cost assumptions")
margin = st.number_input("Profit margin per order ($)", min_value=0.0, value=float(COSTS["margin"]), step=0.5)
churn = st.number_input("Future orders lost after a late order (churn)", min_value=0.0, value=float(COSTS["churn_orders"]), step=0.1)
refund = st.number_input("Refund cost per late order ($)", min_value=0.0, value=float(COSTS["refund"]), step=0.5)

if st.button("Find Best Promise"):
    # Validate the promise range before calculating
    if min_promise > max_promise:
        st.error("Minimum promise cannot be greater than the maximum promise.")
        st.stop()

    promises = list(range(int(min_promise), int(max_promise) + 1, 5))

    # New costs dictionary; the imported COSTS is not modified
    user_costs = {"margin": margin, "churn_orders": churn, "refund": refund}

    best_time, best_profit = best_promise(zone, time_block, promises, user_costs)

    st.session_state["result"] = {
        "zone": zone,
        "time_block": time_block,
        "promises": promises,
        "best_time": best_time,
        "best_profit": best_profit,
    }

# Show the stored result (stays visible after reruns)
if "result" in st.session_state:
    result = st.session_state["result"]
    st.divider()
    st.caption(
        f"{result['zone']} · {result['time_block']} · "
        f"promises tested: {result['promises'][0]} to {result['promises'][-1]} minutes"
    )
    st.success(f"Recommended promise: {result['best_time']} minutes")
    st.metric("Estimated net profit", f"${result['best_profit']:,.2f}")
