import streamlit as st
import pandas as pd
import datetime
import random

# ============================================================
# 🏛️ GOVERNMENT CENTRAL HELPLINE - AI-Powered Grievance System
# Pravi AI Builder Assessment | Aayushi Sheth | March 2026
# ============================================================

st.set_page_config(page_title="Government Central Helpline", page_icon="🏛️", layout="wide", initial_sidebar_state="expanded")

# Safe minimal CSS — only custom cards, NO overrides on Streamlit defaults
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
    .hero {background:linear-gradient(135deg,#1e3a5f,#2563eb);padding:30px 40px;border-radius:14px;margin-bottom:22px;box-shadow:0 6px 25px rgba(37,99,235,0.25)}
    .hero h2{color:#fff!important;font-size:26px;font-weight:800;margin:0 0 4px 0;font-family:'Inter',sans-serif}
    .hero p{color:#bfdbfe!important;font-size:14px;margin:0;font-family:'Inter',sans-serif}
    .hero .tag{display:inline-block;background:rgba(255,255,255,0.15);color:#e0f2fe;padding:4px 14px;border-radius:20px;font-size:11px;font-weight:600;margin-top:10px;letter-spacing:0.5px}
    .kpi{background:#fff;border-radius:12px;padding:20px;text-align:center;border:1px solid #e5e7eb;border-bottom:4px solid;margin-bottom:5px}
    .kpi .num{font-size:34px;font-weight:800;color:#111827;font-family:'Inter',sans-serif}
    .kpi .lbl{font-size:11px;color:#6b7280;text-transform:uppercase;letter-spacing:1px;font-weight:600;margin-top:2px}
    .ai-box{background:#faf5ff;border-left:5px solid #7c3aed;padding:16px 20px;border-radius:0 10px 10px 0;margin:12px 0}
    .ai-box .ai-t{font-weight:700;color:#5b21b6;font-size:15px;margin-bottom:8px}
    .ai-box p{color:#374151;font-size:13px;margin:4px 0;line-height:1.6}
    .ok-box{background:#f0fdf4;border-left:5px solid #16a34a;padding:16px 20px;border-radius:0 10px 10px 0;margin:12px 0}
    .ok-box .ok-t{font-weight:700;color:#15803d;font-size:16px;margin-bottom:4px}
    .ok-box p{color:#166534;font-size:13px;margin:3px 0}
    .warn-box{background:#fffbeb;border-left:5px solid #f59e0b;padding:14px 18px;border-radius:0 10px 10px 0;margin:10px 0}
    .warn-box p{color:#92400e;font-size:13px;margin:3px 0}
    .flow-step{background:#f8fafc;border:2px solid #e2e8f0;border-radius:12px;padding:16px;text-align:center}
    .flow-step .emoji{font-size:28px;margin-bottom:6px;display:block}
    .flow-step .title{font-weight:700;font-size:13px;color:#1e3a5f;margin-bottom:3px}
    .flow-step .desc{font-size:11px;color:#64748b;line-height:1.4}
    .arrow-col{display:flex;align-items:center;justify-content:center;font-size:24px;color:#2563eb;font-weight:800}
</style>
""", unsafe_allow_html=True)

# ============================================================
# AI ENGINE — Categorization + Priority + Sentiment
# ============================================================
CATEGORIES = {
    "Water Supply": ["water","pipe","tap","supply","tanker","leakage","sewage","drainage","flood","pipeline","drinking"],
    "Roads & Infrastructure": ["road","pothole","bridge","footpath","traffic","signal","construction","pavement","highway"],
    "Electricity": ["electricity","power","light","streetlight","transformer","voltage","outage","blackout","meter","wire"],
    "Sanitation & Waste": ["garbage","waste","cleaning","dump","dustbin","toilet","sanitation","drain","smell","mosquito"],
    "Public Safety": ["crime","theft","police","safety","harassment","accident","fire","emergency"],
    "Healthcare": ["hospital","doctor","medicine","clinic","ambulance","health","disease"],
}
DEPT = {"Water Supply":"Water Dept - Sh. Mehta","Roads & Infrastructure":"Roads Dept - Sh. Shah",
        "Electricity":"Electricity Dept - Sh. Joshi","Sanitation & Waste":"Sanitation Dept - Sh. Verma",
        "Public Safety":"Police - SI Rao","Healthcare":"Health Dept - Dr. Gupta","Other":"General Admin"}

def ai_categorize(text):
    t = text.lower()
    scores = {c:sum(1 for k in kw if k in t) for c,kw in CATEGORIES.items()}
    scores = {k:v for k,v in scores.items() if v>0}
    return max(scores,key=scores.get) if scores else "Other"

def ai_priority(text):
    t = text.lower()
    if any(k in t for k in ["emergency","danger","fire","death","accident","collapse","flood","no water since","4 days","5 days","week","children","elderly"]): return "🔴 Urgent"
    if any(k in t for k in ["broken","leaked","blocked","overflowing","not working","3 days","serious","health risk"]): return "🟠 High"
    return "🟡 Medium"

def ai_sentiment(text):
    t = text.lower()
    angry = ["frustrated","angry","pathetic","worst","useless","terrible","disgusting","fed up","shameful","corrupt","negligent"]
    s = sum(1 for w in angry if w in t)
    if s>=2: return "😡 Very Frustrated"
    if s==1: return "😠 Frustrated"
    return "😐 Neutral"

# ============================================================
# DEMO DATA — 6 realistic complaints
# ============================================================
if "complaints" not in st.session_state:
    st.session_state.complaints = [
        {"id":"GHC-2026-1001","name":"Rajesh Kumar","phone":"9876543210","channel":"Phone Call","area":"Zone A - North",
         "text":"No water supply in our colony since 4 days. Children and elderly are suffering. We have complained many times but no action taken. Very frustrated with the negligent system.",
         "category":"Water Supply","priority":"🔴 Urgent","sentiment":"😡 Very Frustrated","status":"Open",
         "officer":"Water Dept - Sh. Mehta","notes":"","date":"14 Mar 2026","updated":""},
        {"id":"GHC-2026-1002","name":"Priya Patel","phone":"9123456789","channel":"WhatsApp","area":"Zone B - South",
         "text":"Large pothole on MG Road near school. Two accidents last week. Very dangerous for school children.",
         "category":"Roads & Infrastructure","priority":"🟠 High","sentiment":"😠 Frustrated","status":"In Progress",
         "officer":"Roads Dept - Sh. Shah","notes":"Site visited 15th March. Repair ordered.","date":"13 Mar 2026","updated":"15 Mar 2026"},
        {"id":"GHC-2026-1003","name":"Amit Singh","phone":"9988776655","channel":"Web Portal","area":"Zone C - East",
         "text":"Streetlight not working on Ring Road for 2 weeks. Very dark at night, safety concern for women.",
         "category":"Electricity","priority":"🟠 High","sentiment":"😠 Frustrated","status":"Open",
         "officer":"Electricity Dept - Sh. Joshi","notes":"","date":"15 Mar 2026","updated":""},
        {"id":"GHC-2026-1004","name":"Meena Devi","phone":"9871234567","channel":"Phone Call","area":"Zone A - North",
         "text":"Garbage not collected since 1 week. Bad smell and mosquitoes increasing. Health risk for locality.",
         "category":"Sanitation & Waste","priority":"🟠 High","sentiment":"😠 Frustrated","status":"Open",
         "officer":"Sanitation Dept - Sh. Verma","notes":"","date":"16 Mar 2026","updated":""},
        {"id":"GHC-2026-1005","name":"Suresh Reddy","phone":"9090909090","channel":"Email","area":"Zone D - West",
         "text":"Irregular power supply in industrial area. Voltage fluctuation damaging machines.",
         "category":"Electricity","priority":"🟡 Medium","sentiment":"😐 Neutral","status":"Resolved",
         "officer":"Electricity Dept - Sh. Joshi","notes":"Transformer replaced 16th March. Citizen confirmed.","date":"10 Mar 2026","updated":"16 Mar 2026"},
        {"id":"GHC-2026-1006","name":"Fatima Begum","phone":"9191919191","channel":"Walk-in","area":"Zone B - South",
         "text":"Sewage overflow in Indira Nagar for 3 days. Dirty water entering houses. Children getting sick.",
         "category":"Water Supply","priority":"🔴 Urgent","sentiment":"😠 Frustrated","status":"Open",
         "officer":"Water Dept - Sh. Mehta","notes":"","date":"17 Mar 2026","updated":""},
    ]

# ============================================================
# SIDEBAR — 100% native Streamlit
# ============================================================
with st.sidebar:
    st.title("🏛️ Central Helpline")
    st.caption("AI-Powered Grievance Redressal System")
    st.divider()
    page = st.radio("**📌 Modules**", [
        "🏠 Home & Overview",
        "📝 File Complaint",
        "🔍 Track Complaint",
        "👷 Officer Panel",
        "📊 Supervisor Dashboard"
    ])
    st.divider()
    st.caption("🤖 AI-Powered Engine")
    st.caption("📡 Multi-Channel Support")
    st.caption("📊 Real-Time Analytics")

# ============================================================
# PAGE 1: HOME & OVERVIEW
# ============================================================
if page == "🏠 Home & Overview":
    st.markdown("""<div class="hero"><h2>🏛️ Government Central Helpline</h2>
    <p>AI-Powered Multi-Channel Grievance Redressal System</p>
    <span class="tag">🤖 AUTO-CATEGORIZATION  •  PRIORITY SCORING  •  SENTIMENT ANALYSIS  •  SMART ROUTING</span></div>""", unsafe_allow_html=True)

    total = len(st.session_state.complaints)
    open_c = sum(1 for c in st.session_state.complaints if c['status']=='Open')
    prog_c = sum(1 for c in st.session_state.complaints if c['status']=='In Progress')
    res_c = sum(1 for c in st.session_state.complaints if c['status']=='Resolved')
    rate = round((res_c/total*100)) if total>0 else 0

    k1,k2,k3,k4,k5 = st.columns(5)
    k1.markdown(f'<div class="kpi" style="border-bottom-color:#2563eb"><div class="num">{total}</div><div class="lbl">📋 Total</div></div>',unsafe_allow_html=True)
    k2.markdown(f'<div class="kpi" style="border-bottom-color:#dc2626"><div class="num">{open_c}</div><div class="lbl">🔴 Open</div></div>',unsafe_allow_html=True)
    k3.markdown(f'<div class="kpi" style="border-bottom-color:#ea580c"><div class="num">{prog_c}</div><div class="lbl">⏳ Progress</div></div>',unsafe_allow_html=True)
    k4.markdown(f'<div class="kpi" style="border-bottom-color:#16a34a"><div class="num">{res_c}</div><div class="lbl">✅ Resolved</div></div>',unsafe_allow_html=True)
    k5.markdown(f'<div class="kpi" style="border-bottom-color:#7c3aed"><div class="num">{rate}%</div><div class="lbl">📈 Rate</div></div>',unsafe_allow_html=True)

    st.markdown("")

    # === SYSTEM WORKFLOW ===
    st.subheader("🔄 System Workflow — How It Works")
    s1,a1,s2,a2,s3,a3,s4 = st.columns([2,0.5,2,0.5,2,0.5,2])
    with s1:
        st.markdown('<div class="flow-step"><span class="emoji">👤</span><div class="title">1. Citizen Submits</div><div class="desc">Files complaint via Phone, WhatsApp, Email, Web, or Walk-in</div></div>', unsafe_allow_html=True)
    with a1:
        st.markdown('<div class="arrow-col">→</div>', unsafe_allow_html=True)
    with s2:
        st.markdown('<div class="flow-step"><span class="emoji">🤖</span><div class="title">2. AI Processes</div><div class="desc">Auto-categorizes, assigns priority, detects citizen frustration</div></div>', unsafe_allow_html=True)
    with a2:
        st.markdown('<div class="arrow-col">→</div>', unsafe_allow_html=True)
    with s3:
        st.markdown('<div class="flow-step"><span class="emoji">👷</span><div class="title">3. Officer Resolves</div><div class="desc">Gets auto-assigned, investigates on field, updates status</div></div>', unsafe_allow_html=True)
    with a3:
        st.markdown('<div class="arrow-col">→</div>', unsafe_allow_html=True)
    with s4:
        st.markdown('<div class="flow-step"><span class="emoji">📊</span><div class="title">4. Supervisor Monitors</div><div class="desc">Dashboard analytics, delay alerts, AI insights</div></div>', unsafe_allow_html=True)

    st.divider()

    # === CHANNELS ===
    st.subheader("📡 Multi-Channel Support")
    ch1,ch2,ch3,ch4,ch5 = st.columns(5)
    ch1.info("📞 **Phone Call**")
    ch2.info("💬 **WhatsApp**")
    ch3.info("📧 **Email**")
    ch4.info("🌐 **Web Portal**")
    ch5.info("🏢 **Walk-in**")

    st.divider()

    # === AI CAPABILITIES ===
    st.subheader("🤖 AI Capabilities")
    ai1,ai2,ai3 = st.columns(3)
    with ai1:
        with st.container(border=True):
            st.markdown("**📂 Auto-Categorization**")
            st.caption("AI reads complaint text and routes to the correct department automatically")
            st.code('"Water pipe burst" → Water Dept\n"Pothole on road"  → Roads Dept\n"Streetlight off"  → Electricity', language=None)
    with ai2:
        with st.container(border=True):
            st.markdown("**🎯 Smart Priority**")
            st.caption("Detects urgency keywords and assigns priority levels")
            st.code('🔴 Urgent: "children", "emergency"\n🟠 High:   "broken", "not working"\n🟡 Medium: general complaints', language=None)
    with ai3:
        with st.container(border=True):
            st.markdown("**😡 Sentiment Analysis**")
            st.caption("Flags frustrated citizens for immediate attention")
            st.code('😡 Very Frustrated: multiple anger words\n😠 Frustrated: one anger indicator\n😐 Neutral: calm complaint', language=None)

    st.divider()

    # === RECENT COMPLAINTS ===
    st.subheader("📋 Recent Complaints")
    for c in st.session_state.complaints[:4]:
        icon = {"Open":"🔴","In Progress":"🟡","Resolved":"✅"}.get(c['status'],"⚪")
        with st.container(border=True):
            l,r = st.columns([5,1])
            with l:
                st.markdown(f"**{c['id']}** — {c['name']} — _{c['channel']}_")
                st.caption(c['text'][:160])
                st.caption(f"📂 {c['category']}  •  {c['priority']}  •  👷 {c['officer']}")
            with r:
                st.markdown(f"### {icon}")
                st.caption(c['status'])


# ============================================================
# PAGE 2: FILE COMPLAINT
# ============================================================
elif page == "📝 File Complaint":
    st.markdown("""<div class="hero"><h2>📝 File a New Complaint</h2>
    <p>Submit your grievance — our AI engine will instantly categorize, prioritize, and route it</p></div>""", unsafe_allow_html=True)

    with st.container(border=True):
        st.subheader("📋 Complaint Form")
        with st.form("form", clear_on_submit=True):
            c1,c2 = st.columns(2)
            with c1:
                name = st.text_input("👤 Full Name *", placeholder="Enter your name")
                phone = st.text_input("📱 Phone Number *", placeholder="10-digit number")
            with c2:
                channel = st.selectbox("📡 Channel", ["Web Portal","Phone Call","WhatsApp","Email","Walk-in"])
                area = st.selectbox("📍 Area", ["Zone A - North","Zone B - South","Zone C - East","Zone D - West","Zone E - Central"])
            complaint = st.text_area("📄 Complaint Details *", placeholder="Describe your problem in detail...", height=130)
            submitted = st.form_submit_button("🚀 Submit Complaint", use_container_width=True, type="primary")

    if submitted and name and complaint and phone:
        cat = ai_categorize(complaint)
        pri = ai_priority(complaint)
        sent = ai_sentiment(complaint)
        cid = f"GHC-{datetime.date.today().strftime('%Y%m%d')}-{random.randint(1000,9999)}"
        off = DEPT.get(cat, "General Admin")
        new = {"id":cid,"name":name,"phone":phone,"channel":channel,"area":area,"text":complaint,
               "category":cat,"priority":pri,"sentiment":sent,"status":"Open","officer":off,
               "notes":"","date":datetime.date.today().strftime("%d %b %Y"),"updated":""}
        st.session_state.complaints.insert(0, new)

        st.markdown(f"""<div class="ok-box"><div class="ok-t">✅ Complaint Registered Successfully!</div>
        <p><strong>Complaint ID:</strong> {cid} — Save this to track your status</p></div>""", unsafe_allow_html=True)

        st.markdown(f"""<div class="ai-box"><div class="ai-t">🤖 AI Analysis Results</div>
        <p>📂 <strong>Category:</strong> {cat}</p><p>🎯 <strong>Priority:</strong> {pri}</p>
        <p><strong>Sentiment:</strong> {sent}</p><p>👷 <strong>Auto-Assigned:</strong> {off}</p>
        <p>📅 <strong>Date:</strong> {new['date']}</p></div>""", unsafe_allow_html=True)

        if "Urgent" in pri:
            st.error("⚡ URGENT — Auto-escalated to Supervisor for immediate action!")
    elif submitted:
        st.error("❌ Please fill all required fields")


# ============================================================
# PAGE 3: TRACK COMPLAINT (New Interactive Feature!)
# ============================================================
elif page == "🔍 Track Complaint":
    st.markdown("""<div class="hero"><h2>🔍 Track Your Complaint</h2>
    <p>Enter your Complaint ID to check real-time status and updates</p></div>""", unsafe_allow_html=True)

    with st.container(border=True):
        search_id = st.text_input("🔎 Enter Complaint ID", placeholder="e.g. GHC-2026-1001")
        search_btn = st.button("Search", type="primary", use_container_width=True)

    if search_btn and search_id:
        found = [c for c in st.session_state.complaints if c['id'] == search_id.strip()]
        if found:
            c = found[0]
            icon = {"Open":"🔴","In Progress":"🟡","Resolved":"✅"}.get(c['status'],"⚪")
            st.markdown(f"""<div class="ok-box"><div class="ok-t">{icon} Complaint Found — Status: {c['status']}</div>
            <p><strong>ID:</strong> {c['id']}</p></div>""", unsafe_allow_html=True)

            with st.container(border=True):
                st.subheader("📋 Complaint Details")
                d1,d2 = st.columns(2)
                with d1:
                    st.markdown(f"**👤 Name:** {c['name']}")
                    st.markdown(f"**📱 Phone:** {c['phone']}")
                    st.markdown(f"**📡 Channel:** {c['channel']}")
                    st.markdown(f"**📍 Area:** {c['area']}")
                    st.markdown(f"**📅 Submitted:** {c['date']}")
                with d2:
                    st.markdown(f"**📂 Category:** {c['category']}")
                    st.markdown(f"**🎯 Priority:** {c['priority']}")
                    st.markdown(f"**{c['sentiment'].split(' ')[0]} Sentiment:** {c['sentiment']}")
                    st.markdown(f"**👷 Officer:** {c['officer']}")
                    if c['updated']:
                        st.markdown(f"**🔄 Last Updated:** {c['updated']}")

            st.markdown("**📄 Complaint Text:**")
            st.info(c['text'])

            if c['notes']:
                st.markdown(f"""<div class="ai-box"><div class="ai-t">📝 Officer Notes</div>
                <p>{c['notes']}</p></div>""", unsafe_allow_html=True)

            # Status timeline
            st.subheader("📶 Status Timeline")
            t1,t2,t3 = st.columns(3)
            if c['status'] in ["Open","In Progress","Resolved"]:
                t1.success("✅ Step 1: Complaint Received")
            if c['status'] in ["In Progress","Resolved"]:
                t2.success("✅ Step 2: Officer Investigating")
            else:
                t2.warning("⏳ Step 2: Awaiting Officer")
            if c['status'] == "Resolved":
                t3.success("✅ Step 3: Resolved!")
            else:
                t3.warning("⏳ Step 3: Pending Resolution")
        else:
            st.error(f"❌ No complaint found with ID: {search_id}")
    elif not search_btn:
        st.caption("💡 Try searching: GHC-2026-1001, GHC-2026-1002, etc.")
        st.divider()
        st.subheader("📋 All Complaint IDs")
        for c in st.session_state.complaints:
            icon = {"Open":"🔴","In Progress":"🟡","Resolved":"✅"}.get(c['status'],"⚪")
            st.caption(f"{icon} **{c['id']}** — {c['name']} — {c['status']}")


# ============================================================
# PAGE 4: OFFICER PANEL
# ============================================================
elif page == "👷 Officer Panel":
    st.markdown("""<div class="hero"><h2>👷 Officer Panel</h2>
    <p>Manage and resolve complaints assigned to your department</p></div>""", unsafe_allow_html=True)

    f1,f2,f3 = st.columns(3)
    with f1: fs = st.selectbox("Status",["All","Open","In Progress","Resolved"])
    with f2: fc = st.selectbox("Category",["All"]+list(CATEGORIES.keys()))
    with f3: fp = st.selectbox("Priority",["All","🔴 Urgent","🟠 High","🟡 Medium"])

    fl = st.session_state.complaints.copy()
    if fs!="All": fl=[c for c in fl if c['status']==fs]
    if fc!="All": fl=[c for c in fl if c['category']==fc]
    if fp!="All": fl=[c for c in fl if c['priority']==fp]

    st.info(f"📋 **{len(fl)}** complaint(s) found")

    for i,c in enumerate(fl):
        si = {"Open":"🔴","In Progress":"🟡","Resolved":"✅"}.get(c['status'],"⚪")
        with st.expander(f"{si} {c['id']} | {c['category']} | {c['priority']} | {c['name']}", expanded=(i==0)):
            left,right = st.columns([3,2])
            with left:
                st.info(c['text'])
                st.caption(f"📍 {c['area']} | 📞 {c['phone']} | 📡 {c['channel']} | 📅 {c['date']}")
                if c['notes']:
                    st.success(f"📝 **Notes:** {c['notes']}")
            with right:
                st.markdown(f"""<div class="ai-box"><div class="ai-t">🤖 AI Analysis</div>
                <p>📂 {c['category']}</p><p>🎯 {c['priority']}</p>
                <p>{c['sentiment']}</p><p>👷 {c['officer']}</p></div>""", unsafe_allow_html=True)

            if c['status']!="Resolved":
                a1,a2 = st.columns(2)
                with a1: ns = st.selectbox("Status",["Open","In Progress","Resolved"],index=["Open","In Progress","Resolved"].index(c['status']),key=f"s{c['id']}")
                with a2: nn = st.text_input("Notes",value=c['notes'],key=f"n{c['id']}")
                if st.button("💾 Save",key=f"b{c['id']}",type="primary"):
                    for j,comp in enumerate(st.session_state.complaints):
                        if comp['id']==c['id']:
                            st.session_state.complaints[j]['status']=ns
                            st.session_state.complaints[j]['notes']=nn
                            st.session_state.complaints[j]['updated']=datetime.date.today().strftime("%d %b %Y")
                    st.success(f"✅ Updated to **{ns}**!")
                    st.rerun()
            else:
                st.success(f"✅ Resolved on {c['updated']}")


# ============================================================
# PAGE 5: SUPERVISOR DASHBOARD
# ============================================================
elif page == "📊 Supervisor Dashboard":
    st.markdown("""<div class="hero"><h2>📊 Supervisor Dashboard</h2>
    <p>Real-time analytics, performance monitoring, and AI-generated governance insights</p></div>""", unsafe_allow_html=True)

    complaints = st.session_state.complaints
    total = len(complaints)
    open_c = sum(1 for c in complaints if c['status']=='Open')
    prog_c = sum(1 for c in complaints if c['status']=='In Progress')
    res_c = sum(1 for c in complaints if c['status']=='Resolved')
    urgent_c = sum(1 for c in complaints if 'Urgent' in c['priority'])
    rate = round((res_c/total*100)) if total>0 else 0

    m1,m2,m3,m4,m5 = st.columns(5)
    m1.metric("📋 Total",total)
    m2.metric("🔴 Open",open_c)
    m3.metric("⏳ In Progress",prog_c)
    m4.metric("✅ Resolved",res_c)
    m5.metric("📈 Resolution",f"{rate}%")

    st.divider()

    c1,c2 = st.columns(2)
    with c1:
        st.subheader("📊 By Category")
        cd = {}
        for c in complaints: cd[c['category']]=cd.get(c['category'],0)+1
        st.bar_chart(pd.DataFrame({"Complaints":cd},index=cd.keys()))
    with c2:
        st.subheader("📍 By Area")
        ad = {}
        for c in complaints: ad[c['area']]=ad.get(c['area'],0)+1
        st.bar_chart(pd.DataFrame({"Complaints":ad},index=ad.keys()))

    c3,c4 = st.columns(2)
    with c3:
        st.subheader("📶 By Status")
        st.bar_chart(pd.DataFrame({"Count":{"Open":open_c,"In Progress":prog_c,"Resolved":res_c}}))
    with c4:
        st.subheader("🎯 By Priority")
        pd2 = {}
        for c in complaints: pd2[c['priority']]=pd2.get(c['priority'],0)+1
        st.bar_chart(pd.DataFrame({"Count":pd2},index=pd2.keys()))

    st.divider()

    # AI Insights
    cc = {}
    for c in complaints: cc[c['category']]=cc.get(c['category'],0)+1
    top_cat = max(cc,key=cc.get) if cc else "N/A"
    ac = {}
    for c in complaints: ac[c['area']]=ac.get(c['area'],0)+1
    top_area = max(ac,key=ac.get) if ac else "N/A"
    frust = sum(1 for c in complaints if 'Frustrated' in c.get('sentiment',''))

    st.markdown(f"""<div class="ai-box"><div class="ai-t">🤖 AI-Generated Governance Insights — {datetime.date.today().strftime('%d %B %Y')}</div>
    <p>📊 <strong>Overview:</strong> {total} total complaints — {open_c} open, {prog_c} in progress, {res_c} resolved ({rate}% resolution).</p>
    <p>🏆 <strong>Top Issue:</strong> {top_cat} ({cc.get(top_cat,0)} complaints) — requires immediate resource allocation.</p>
    <p>📍 <strong>Hotspot:</strong> {top_area} ({ac.get(top_area,0)} complaints) — dispatch additional field officers.</p>
    <p>⚠️ <strong>Urgent:</strong> {urgent_c} complaint(s) need immediate supervisor attention.</p>
    <p>😡 <strong>Sentiment:</strong> {frust} frustrated citizen(s) — prioritize to prevent escalation.</p>
    <p>💡 <strong>Recommendation:</strong> Focus on {top_cat} in {top_area}. Schedule review meeting. Proactive maintenance can reduce volume by ~30%.</p></div>""", unsafe_allow_html=True)

    st.divider()

    st.subheader("🚨 Complaints Requiring Attention")
    att = [c for c in complaints if c['status']!='Resolved']
    if att:
        st.dataframe(pd.DataFrame([{"ID":c['id'],"Citizen":c['name'],"Category":c['category'],
            "Priority":c['priority'],"Status":c['status'],"Area":c['area'],
            "Officer":c['officer'],"Date":c['date']} for c in att]),use_container_width=True,hide_index=True)
    else:
        st.balloons()
        st.success("🎉 All complaints resolved!")

    st.divider()
    csv = pd.DataFrame(complaints).to_csv(index=False)
    st.download_button("📥 Export All Data (CSV)",csv,"helpline_data.csv","text/csv",use_container_width=True)
