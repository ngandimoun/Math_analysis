import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# Set up Streamlit layout
st.set_page_config(layout="wide")

# Title and description
st.title("Interactive Data Analysis Dashboard")
st.write("This dashboard displays visualizations in two columns.")

# First column
column1, column2 = st.columns(2)

# Interactive element:Slider
range_start = column1.slider("Select range start", min_value=0, max_value=10, value=0)
range_end = column1.slider("Select range end", min_value=0, max_value=10, value=10)

with column1:
    st.subheader("Visualization 1: Sine Function")
    fig1, ax1 = plt.subplots()
    ax1.plot(x, y1)
    ax1.set_xlim([range_start, range_end])
    ax1.set_xlabel("X-axis")
    ax1.set_ylabel("Y-axis")
    ax1.set_title("Sine Function")
    st.pyplot(fig1)

    st.subheader("Visualization 2: Cosine Function")
    fig2, ax2 = plt.subplots()
    ax2.plot(x, y2)
    ax2.set_xlim([range_start, range_end])
    ax2.set_xlabel("X-axis")
    ax2.set_ylabel("Y-axis")
    ax2.set_title("Cosine Function")
    st.pyplot(fig2)

    st.subheader("Visualization 3: Tangent Function")
    fig3, ax3 = plt.subplots()
    ax3.plot(x, y3)
    ax3.set_xlim([range_start, range_end])
    ax3.set_xlabel("X-axis")
    ax3.set_ylabel("Y-axis")
    ax3.set_title("Tangent Function")
    st.pyplot(fig3)

# Second column
# Interactive element: Checkbox
plot_negative = column2.checkbox("Plot negative", value=False)

with column2:
    st.subheader("Visualization 4: Sine Function")
    fig4, ax4 = plt.subplots()
    ax4.plot(x, -y1 if plot_negative else y1)
    ax4.set_xlim([range_start, range_end])
    ax4.set_xlabel("X-axis")
    ax4.set_ylabel("Y-axis")
    ax4.set_title("Sine Function (Negative)")
    st.pyplot(fig4)

    st.subheader("Visualization 5: Cosine Function")
    fig5, ax5 = plt.subplots()
    ax5.plot(x, -y2 if plot_negative else y2)
    ax5.set_xlim([range_start, range_end])
    ax5.set_xlabel("X-axis")
    ax5.set_ylabel("Y-axis")
    ax5.set_title("Cosine Function (Negative)")
    st.pyplot(fig5)

    st.subheader("Visualization 6: Tangent Function")
    fig6, ax6 = plt.subplots()
    ax6.plot(x, -y3 if plot_negative else y3)
    ax6.set_xlim([range_start, range_end])
    ax6.set_xlabel("X-axis")
    ax6.set_ylabel("Y-axis")
    ax6.set_title("Tangent Function (Negative)")
    st.pyplot(fig6)