import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="EEHC Smart Grid Roadmap Dashboard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom Modern UI Styles matching the original Roadmap Slide
st.markdown("""
    <style>
    /* Global App Background & Typography */
    .stApp {
        background-color: #F8FAFC;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }

    /* Executive Top Banner */
    .top-banner {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        border-radius: 16px;
        padding: 24px 32px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .top-banner h1 {
        color: #FFFFFF !important;
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.5px;
    }
    .top-banner p {
        color: #94A3B8;
        font-size: 1.05rem;
        margin-top: 6px;
        margin-bottom: 0;
    }

    /* Domain Headers */
    .domain-header {
        border-radius: 12px 12px 0 0;
        padding: 14px 16px;
        color: white;
        font-weight: 700;
        font-size: 0.95rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .dh-1 { background: #DC2626; } /* Policy & Regulatory */
    .dh-2 { background: #0284C7; } /* Organizational Support */
    .dh-3 { background: #D97706; } /* Infrastructure */
    .dh-4 { background: #B91C1C; } /* Technology */
    .dh-5 { background: #15803D; } /* Customer Engagement */

    /* Domain Box Frame */
    .domain-container {
        background: white;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        padding: 12px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        min-height: 520px;
    }

    /* Benefit Badges at the Bottom */
    .benefit-card {
        background: white;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 12px 14px;
        margin-bottom: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .benefit-code {
        font-weight: 800;
        font-size: 1rem;
        color: #D9381E;
    }
    .benefit-title {
        font-size: 0.85rem;
        color: #334155;
        font-weight: 600;
    }

    /* Active Highlight Badge */
    .gis-highlight {
        background: #EFF6FF;
        border: 2px solid #2563EB !important;
        border-radius: 8px;
        padding: 4px;
        margin-bottom: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Smart Grid Roadmap Data Structure
DOMAINS = [
    {
        "id": 1,
        "title": "1. POLICY AND REGULATORY SUPPORT",
        "count": "4 PROJECTS",
        "header_class": "dh-1",
        "projects": [
            {"code": "PS1", "name": "Policy and regulatory review", "type": "support"},
            {"code": "PS2", "name": "Technical standards and regulation", "type": "support"},
            {"code": "PS3", "name": "Privacy and customer data ownership", "type": "support"},
            {"code": "PS4", "name": "Cybersecurity", "type": "support"}
        ]
    },
    {
        "id": 2,
        "title": "2. ORGANIZATIONAL SUPPORT",
        "count": "4 PROJECTS",
        "header_class": "dh-2",
        "projects": [
            {"code": "OS1", "name": "Business goals and use cases", "type": "support"},
            {"code": "OS2", "name": "Organizational KPIs", "type": "support"},
            {"code": "OS3", "name": "Asset management strategy", "type": "support"},
            {"code": "OS4", "name": "Smart grid governance", "type": "support"}
        ]
    },
    {
        "id": 3,
        "title": "3. INFRASTRUCTURE",
        "count": "6 PROJECTS",
        "header_class": "dh-3",
        "projects": [
            {"code": "IF1", "name": "Smart meters: commercial and industrial", "type": "direct"},
            {"code": "IF2", "name": "Asset management design and implementation", "type": "support", "active": True, "tag": "Includes GIS"},
            {"code": "IF3", "name": "Smart meters: residential >200 kWh/month", "type": "direct"},
            {"code": "IF4", "name": "Asset management and monitoring", "type": "direct"},
            {"code": "IF5", "name": "Smart Meter Plus: residential <200 kWh/month", "type": "direct"},
            {"code": "IF6", "name": "Phasor measurement units", "type": "direct"}
        ]
    },
    {
        "id": 4,
        "title": "4. TECHNOLOGY",
        "count": "7 PROJECTS",
        "header_class": "dh-4",
        "projects": [
            {"code": "TE1", "name": "Technology evaluation and selection", "type": "support"},
            {"code": "TE2", "name": "Integrated solution selection", "type": "support"},
            {"code": "TE3", "name": "Smart meter analytics", "type": "direct"},
            {"code": "TE4", "name": "PV and EV monitoring", "type": "direct"},
            {"code": "TE5", "name": "Demand response", "type": "direct"},
            {"code": "TE6", "name": "Demand-side management pilot", "type": "direct"},
            {"code": "TE7", "name": "Energy storage pilots", "type": "direct"}
        ]
    },
    {
        "id": 5,
        "title": "5. CUSTOMER ENGAGEMENT & ENV.",
        "count": "5 PROJECTS",
        "header_class": "dh-5",
        "projects": [
            {"code": "C1", "name": "Green DISCO", "type": "direct"},
            {"code": "C2", "name": "AMI lessons learned", "type": "support"},
            {"code": "C3", "name": "Buy REN@DISCO", "type": "direct"},
            {"code": "C4", "name": "Advanced smart meter analytics", "type": "direct"},
            {"code": "C5", "name": "Interactive energy applications", "type": "direct"}
        ]
    }
]

BENEFITS = [
    {"code": "B1", "title": "Deferred grid investment"},
    {"code": "B2", "title": "Avoided grid investment"},
    {"code": "B3", "title": "Reduced electricity losses"},
    {"code": "B4", "title": "Reduced planned outages"},
    {"code": "B5", "title": "Reduced unplanned outages"},
    {"code": "B6", "title": "Improved customer satisfaction"},
    {"code": "B7", "title": "Reduced CO₂ emissions"},
    {"code": "B8", "title": "Improved organizational efficiency"},
    {"code": "B9", "title": "EV integration benefits"}
]

# 4. State Management
if 'selected_project' not in st.session_state:
    st.session_state.selected_project = "Dashboard Home"

def select_project(code):
    st.session_state.selected_project = code

# 5. Sidebar Navigation
with st.sidebar:
    st.title("⚡ EEHC GIS Control")
    st.markdown("**Egyptian Electricity Holding Company**\nStrategic Portfolio Management")
    st.divider()

    if st.button("🏠 Smart Grid Roadmap Dashboard", use_container_width=True, type="primary" if st.session_state.selected_project == "Dashboard Home" else "secondary"):
        select_project("Dashboard Home")
        st.rerun()

    st.subheader("Quick Navigation")
    for domain in DOMAINS:
        with st.expander(domain["title"]):
            for proj in domain["projects"]:
                prefix = "🟢 " if proj.get("active") else ""
                if st.button(f"{prefix}{proj['code']}: {proj['name'][:22]}...", key=f"sb_{proj['code']}", use_container_width=True):
                    select_project(proj['code'])
                    st.rerun()

# 6. Main Dashboard View (Recreating the PPT Roadmap Visual Layout)
if st.session_state.selected_project == "Dashboard Home":

    # Top Header
    st.markdown("""
        <div class="top-banner">
            <div>
                <h1>Smart Grid Roadmap</h1>
                <p>5 domains • 26 projects • 9 potential benefits | EEHC and Egypt's nine DISCOs</p>
            </div>
            <div style="text-align: right;">
                <span style="background: #2563EB; color: white; padding: 6px 14px; border-radius: 20px; font-weight: 700; font-size: 0.85rem;">
                    EEHC + 9 DISCOs
                </span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 5 Column Grid Layout matching the slide
    cols = st.columns(5)

    for idx, domain in enumerate(DOMAINS):
        with cols[idx]:
            # Domain Card Header
            st.markdown(f"""
                <div class="domain-header {domain['header_class']}">
                    <span>{domain['title']}</span>
                </div>
            """, unsafe_allow_html=True)
            
            st.caption(f"📌 {domain['count']}")

            # List of Interactive Project Buttons
            for proj in domain["projects"]:
                is_active = proj.get("active", False)
                icon = "🔵" if proj["type"] == "direct" else "⭕"
                
                # Special Layout for GIS Active Project (IF2)
                if is_active:
                    st.markdown('<div class="gis-highlight">', unsafe_allow_html=True)
                    st.markdown(f"<span style='color:#2563EB; font-size:0.75rem; font-weight:800; float:right;'>{proj['tag']}</span>", unsafe_allow_html=True)
                    if st.button(f"{icon} **{proj['code']}** - {proj['name']}", key=f"rm_{proj['code']}", use_container_width=True, type="primary"):
                        select_project(proj['code'])
                        st.rerun()
                    st.markdown('</div>', unsafe_allow_html=True)
                else:
                    if st.button(f"{icon} **{proj['code']}** - {proj['name']}", key=f"rm_{proj['code']}", use_container_width=True):
                        select_project(proj['code'])
                        st.rerun()

    st.markdown("---")

    # Lower Section: Potential Benefits Portfolio
    st.subheader("Potential Benefits of the Smart-Grid Portfolio")
    
    b_cols = st.columns(9)
    for i, benefit in enumerate(BENEFITS):
        with b_cols[i]:
            st.markdown(f"""
                <div class="benefit-card">
                    <div class="benefit-code">{benefit['code']}</div>
                    <div class="benefit-title">{benefit['title']}</div>
                </div>
            """, unsafe_allow_html=True)

    # Legend
    st.caption("🔴 **⭕ 12 Support Projects** enable delivery | 🔵 **14 Direct Projects** deliver assessed benefits")

# 7. GIS Detailed View Page (IF2: Asset Management Design & Implementation)
elif st.session_state.selected_project == "IF2":
    
    st.button("← Back to Roadmap Dashboard", on_click=select_project, args=("Dashboard Home",))
    
    st.markdown("""
        <div style="background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%); padding: 24px; border-radius: 12px; color: white; margin-top: 10px;">
            <span style="background: #DBEAFE; color: #1E40AF; padding: 4px 10px; border-radius: 12px; font-weight: 700; font-size: 0.8rem;">INFRASTRUCTURE DOMAIN (IF2)</span>
            <h1 style="color: white !important; margin-top: 8px;">Asset Management Design & Implementation (GIS Rollout)</h1>
            <p style="color: #BFDBFE; margin: 0;">Unified Network Record across EEHC and the 9 Distribution Companies (DISCOs)</p>
        </div>
    """, unsafe_allow_html=True)

    st.write("")

    # Strategic Metrics
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric("Target MV Network Record", "100%", "Target: June 2027")
    with m2:
        st.metric("DISCO Integration Routes", "3 Routes", "Established / Partial / No GIS")
    with m3:
        st.metric("R&D Core Team", "7 Specialists", "Smouha Pilot Proven")
    with m4:
        st.metric("Database Integration", "SQL + Enterprise", "ArcGIS Pro Upgrade")

    # Module Tabs derived directly from presentation slides
    t1, t2, t3, t4 = st.tabs(["📌 Executive Overview", "🗺️ Delivery Roadmap", "🏛️ DISCO Readiness Routes", "📊 Monitoring & Apps"])

    with t1:
        st.subheader("Strategic Objectives")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            * **Unified Network Record:** Nine DISCOs operating on one common standard model.
            * **Trusted Network Data:** Verified geographic locations and stable asset identities.
            """)
        with c2:
            st.markdown("""
            * **Continuous Updates:** Workflow covering field capture ➔ verify ➔ approve ➔ publish.
            * **Sector Applications:** Powering asset management, operations, OMS, and grid planning.
            """)

    with t2:
        st.subheader("Three Horizons Timeline")
        st.markdown("""
        | Horizon | Delivery Window | Program Focus | Gate Evidence to Advance |
        | :--- | :--- | :--- | :--- |
        | **Short Term** | Jan 2026 – Jun 2027 | Central foundation; nine pilots; full MV coverage | Accepted MV network records in all nine DISCOs[cite: 1] |
        | **Medium Term** | Jun 2027 – May 2030 | LV coverage; operating applications; RE/PQ/BESS pilots | Measured value and validated electrical models[cite: 1] |
        | **Long Term** | May 2030 Onward | ADMS/restoration; voltage and peak management; AMI | Approved investment cases and operating readiness[cite: 1] |
        """)

    with t3:
        st.subheader("Three Integration Routes for DISCOs")
        st.markdown("""
        1. **Established GIS:** Map IDs and schema, retain local tools, synchronize approved updates to SQL[cite: 1].
        2. **Partial / Fragmented GIS:** Consolidate existing work, fill survey gaps, supply equipment and training[cite: 1].
        3. **No GIS:** Survey components from scratch, build local team capacity, utilize central platform[cite: 1].
        """)

    with t4:
        st.subheader("Continuous Update & Monitoring Workflow")
        st.info("Field change ➔ DISCO Verification ➔ Joint Acceptance QA Checklist ➔ Publish in SQL/GIS[cite: 1]")

# 8. Dynamic View for All Other 25 Projects (Reserved Workspaces)
else:
    st.button("← Back to Roadmap Dashboard", on_click=select_project, args=("Dashboard Home",))
    
    code = st.session_state.selected_project
    proj_name = "Selected Project"
    for domain in DOMAINS:
        for p in domain["projects"]:
            if p["code"] == code:
                proj_name = p["name"]

    st.markdown(f"""
        <div style="background: white; border-left: 6px solid #64748B; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-top: 15px;">
            <h2 style="margin: 0; color: #0F172A;">📌 {code}: {proj_name}</h2>
            <p style="color: #64748B; margin-top: 5px;">Smart Grid Roadmap Portfolio Reserved Workspace</p>
        </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.info(f"Workspace reserved for project `{code}`. Configure project details below:")

    c1, c2 = st.columns(2)
    with c1:
        st.text_input("Project Lead", placeholder="Specify lead engineer/manager...")
        st.selectbox("Implementation Phase", ["1. Planning & Scope", "2. Technical Standards", "3. Pilot Execution", "4. Full Deployment"])
    with c2:
        st.date_input("Target Delivery Date")
        st.text_area("Scope & Objectives", placeholder="Enter key deliverables...")

    st.button("Save Configuration", type="primary")
