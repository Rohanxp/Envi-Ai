
# app.py — Envi AI (Premium Dark UI)

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from graph.graph_builder import build_graph
from ui.components import (
    render_how_it_works,
    render_agent_status,
    render_virtual_files,
    render_quality_badge,
    render_report
)

# ─────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────

st.set_page_config(
    page_title="Envi AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────
# GLOBAL DARK THEME
# ─────────────────────────────────────────

st.markdown("""
<style>

.stApp{
background:
linear-gradient(
180deg,
#060b14 0%,
#0a1020 100%
);

color:white;
}

.block-container{
max-width:1400px;
padding-top:1.5rem;
padding-bottom:2rem;
}

[data-testid="stSidebar"]{
background:
linear-gradient(
180deg,
#0b1325,
#111827
);
border-right:1px solid rgba(255,255,255,.05);
}

.hero{

padding:50px;
border-radius:28px;

background:
linear-gradient(
135deg,
rgba(20,28,45,.92),
rgba(14,22,36,.92)
);

border:
1px solid rgba(255,255,255,.06);

backdrop-filter: blur(20px);

text-align:center;

margin-bottom:20px;
}

.hero h1{
font-size:60px;
margin:0;

background:
linear-gradient(
90deg,
#79ffe1,
#64b5ff
);

-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.hero p{
color:#94a3b8;
font-size:18px;
}

.card{

background:
rgba(255,255,255,.03);

padding:18px;

border-radius:20px;

border:
1px solid rgba(255,255,255,.06);
}

.stButton>button{

height:52px;

border-radius:16px;

background:
linear-gradient(
90deg,
#2563eb,
#06b6d4
);

color:white;

border:none;

font-weight:600;
}

.stButton>button:hover{

transform:translateY(-1px);

box-shadow:
0 10px 30px rgba(37,99,235,.3);
}

input{

border-radius:18px !important;
}

footer{
visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────

with st.sidebar:

    st.markdown("""
    ## 🧠 Envi AI
    Deep Autonomous Research
    """)

    st.divider()

    st.markdown("""
### Capabilities

• Multi-Agent Research  
• Deep Analysis  
• Smart Reports  
• Quality Review  
• Fast Exploration
""")

    st.divider()

    st.markdown("### Explore")

    examples = [
        "Future of AGI",
        "Climate innovation",
        "Quantum computing",
        "AI startups",
        "Green energy",
        "Space economy"
    ]

    for ex in examples:
        if st.button(ex, use_container_width=True):
            st.session_state["query_input"] = ex

# ─────────────────────────────────────────
# HERO
# ─────────────────────────────────────────

st.markdown("""
<div class="hero">

<h1>Envi AI</h1>

<p>
Research • Think • Analyse • Generate
</p>

</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────

with st.expander("How Envi AI works"):

    render_how_it_works()

st.markdown("### Research Topic")

query = st.text_input(
    "",
    placeholder="Ask a research question...",
    key="query_input"
)

run = st.button(
    "Generate Research",
    use_container_width=True
)

# ─────────────────────────────────────────

if run and query.strip():

    left,right = st.columns([1,2])

    with st.spinner(
        "Envi AI is thinking..."
    ):

        graph = build_graph()

        state = {
            "user_query":query,
            "todos":[],
            "virtual_files":{},
            "final_report":None,
            "quality_score":None,
            "retry_count":0,
            "status_log":[]
        }

        result = graph.invoke(state)

    with left:

        st.markdown(
            "<div class='card'>",
            unsafe_allow_html=True
        )

        render_agent_status(
            result.get(
                "status_log",
                []
            ),

            result.get(
                "todos",
                []
            )
        )

        render_virtual_files(
            result.get(
                "virtual_files",
                {}
            )
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

    with right:

        st.markdown(
            "<div class='card'>",
            unsafe_allow_html=True
        )

        render_quality_badge(
            result.get(
                "quality_score"
            )
        )

        render_report(
            result.get(
                "final_report",
                "No report generated."
            )
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

elif run:

    st.warning(
        "Enter a topic first"
    )

else:

    st.markdown("""

<div style='
text-align:center;
padding-top:120px;
color:#64748b;
'>

<h2>
Start Research
</h2>

<p>
Enter a topic and generate a structured report
</p>

</div>

""", unsafe_allow_html=True)
