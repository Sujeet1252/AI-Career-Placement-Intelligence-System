
import streamlit as st

st.set_page_config(
    page_title="Career Intelligence",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Career Intelligence Workspace")

st.caption(
    "Graduate outcomes • Career matching • Skill-gap analysis"
)

st.sidebar.title("Navigation")
st.sidebar.caption("AI Career & Placement Intelligence System")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Data validation", "Pending")

with col2:
    st.metric("ML model", "Not trained")

with col3:
    st.metric("Career engine", "In development")

st.divider()

st.subheader("Project development")

st.markdown(
    """
    Our platform will bring together:

    - Real-world employment and graduate-outcome analytics
    - Explainable machine-learning predictions
    - Occupation and skill matching
    - Personalized skill-gap and learning recommendations
    """
)

st.info(
    "Foundation stage: the next milestone is to acquire and "
    "validate the official datasets before building any model."
)
