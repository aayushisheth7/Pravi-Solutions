# 🏛️ Government Central Helpline
### AI-Powered Multi-Channel Grievance Redressal System
**Pravi AI Builder Assessment | March 2026**

---

## 📌 Problem Statement

Citizens face daily issues — water leakage, road damage, power failures — but current government complaint systems are broken:

| Problem | Impact |
|---------|--------|
| ❌ No single entry point | Citizens don't know whom to contact |
| ❌ No complaint tracking | Complaints disappear — no status updates |
| ❌ No accountability | Officers delay without consequence |
| ❌ Manual sorting | Slow, error-prone, 5 complaints/min max |
| ❌ No data insights | Government can't identify systemic issues |

> **Core Question:** *How to manage and track public complaints efficiently, transparently, and at scale?*

---

## 💡 Solution Overview

A **centralized, AI-powered system** where all complaints come in, get auto-processed by AI, routed to the correct officer, and monitored by supervisors — with full citizen transparency.

> *"Like Amazon customer support — but for government grievances."*

---

## 🔄 System Workflow

```
┌──────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  CITIZEN  │───▶│ MULTI-CHANNEL│───▶│   CENTRAL    │───▶│     AI       │───▶│    AUTO      │───▶│   OFFICER    │───▶│  SUPERVISOR  │
│  Submits  │    │    INPUT     │    │  DATABASE    │    │  PROCESSING  │    │  ASSIGNMENT  │    │   ACTION     │    │  DASHBOARD   │
│ Complaint │    │ Phone/Web/WA │    │ Stores All   │    │ Categorize   │    │ Route to Dept│    │ Investigate  │    │ Monitor All  │
└──────────┘    └──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
                                                                                                       │                    │
                                                                                                       ▼                    ▼
                                                                                                ┌──────────────┐    ┌──────────────┐
                                                                                                │ Update Status│    │  Escalation  │
                                                                                                │ Add Notes    │    │  If Delayed   │
                                                                                                └──────────────┘    └──────────────┘
```

### Step-by-Step Flow:

| Step | Action | Who | What Happens |
|------|--------|-----|-------------|
| 1 | **Collect** | Citizen | Files complaint via Phone / WhatsApp / Email / Web / Walk-in |
| 2 | **Store** | System | Saved in central database with unique Complaint ID |
| 3 | **Process** | AI Engine | Auto-categorizes → assigns priority → detects sentiment |
| 4 | **Route** | AI Engine | Auto-assigns to correct department officer |
| 5 | **Act** | Officer | Investigates on field, updates status, adds notes |
| 6 | **Monitor** | Supervisor | Real-time dashboard, flags delays, reads AI insights |
| 7 | **Track** | Citizen | Checks status anytime using Complaint ID |

---

## 👥 System Users & Roles

| User | Role | What They Do |
|------|------|-------------|
| 👤 **Citizen** | Complainant | Submits complaint, tracks status using ID |
| 📞 **GC Operator** | Data Entry | Receives from all channels, enters into system |
| 🤖 **AI Engine** | Auto-Processor | Categorizes, prioritizes, detects sentiment |
| 👷 **Background Officer** | Field Action | Investigates assigned complaints, resolves issues |
| 📊 **Supervisor** | Monitor | Watches KPIs, flags delays, makes policy decisions |

---

## 🤖 AI Engine — The Smart Brain

### Feature 1: Auto-Categorization
AI reads complaint text → identifies the correct department automatically.

| Complaint Text | AI Category | Routed To |
|---------------|-------------|-----------|
| "Water pipe burst in colony" | Water Supply | Water Dept - Sh. Mehta |
| "Pothole on MG Road near school" | Roads & Infrastructure | Roads Dept - Sh. Shah |
| "Streetlight not working since 2 weeks" | Electricity | Electricity Dept - Sh. Joshi |
| "Garbage not collected for 1 week" | Sanitation & Waste | Sanitation Dept - Sh. Verma |

**How:** Keyword-based NLP engine that matches complaint text against category keyword dictionaries.  
**Future:** Replace with GPT-4/Claude API for 99% accuracy.

### Feature 2: Smart Priority Scoring
AI detects urgency from keywords and assigns priority level.

| Priority | Trigger Keywords | Example |
|----------|-----------------|---------|
| 🔴 **Urgent** | emergency, danger, fire, children, elderly, flood | "No water since 5 days, children suffering" |
| 🟠 **High** | broken, leaked, not working, 3 days, health risk | "Transformer broken, power outage" |
| 🟡 **Medium** | general complaints without urgency indicators | "Irregular water timing" |

**Value:** Urgent cases get attention FIRST — not just first-come-first-served.

### Feature 3: Sentiment Analysis
AI detects citizen frustration level from the language used.

| Sentiment | Detection | Action |
|-----------|-----------|--------|
| 😡 **Very Frustrated** | 2+ anger words (pathetic, negligent, worst) | Immediate escalation to Supervisor |
| 😠 **Frustrated** | 1 anger word (angry, terrible, useless) | Flag for priority communication |
| 😐 **Neutral** | Calm, factual complaint | Normal processing |

**Value:** Flags frustrated citizens BEFORE they escalate to media/courts. Proactive governance.

---

## 📱 Application Modules (5 Pages)

### Module 1: 🏠 Home & Overview
- KPI Dashboard (Total, Open, In Progress, Resolved, Resolution Rate)
- System Workflow visualization (4-step flow with arrows)
- Multi-Channel support showcase (Phone, WhatsApp, Email, Web, Walk-in)
- AI Capabilities cards with examples
- Recent Complaints list with status indicators

### Module 2: 📝 File Complaint (Citizen Portal)
- Complaint form: Name, Phone, Channel, Area, Description
- On submit → AI instantly processes:
  - Auto-categorizes to correct department
  - Assigns priority (Urgent/High/Medium)
  - Detects sentiment (Frustrated/Neutral)
  - Auto-assigns to officer
- Returns unique Complaint ID for tracking

### Module 3: 🔍 Track Complaint
- Search by Complaint ID
- Shows: full details, AI analysis, officer notes
- **Status Timeline**: Step 1 (Received) → Step 2 (Investigating) → Step 3 (Resolved)
- Visual progress indicators (✅ complete, ⏳ pending)

### Module 4: 👷 Officer Panel
- Filter complaints by Status / Category / Priority
- Expand any complaint to see:
  - Full complaint text
  - AI analysis (category, priority, sentiment)
  - Citizen contact details
- Update status (Open → In Progress → Resolved)
- Add investigation notes

### Module 5: 📊 Supervisor Dashboard
- Real-time KPIs (Total, Open, Progress, Resolved, Rate)
- Analytics Charts:
  - Complaints by Category (bar chart)
  - Complaints by Area (bar chart)
  - Status Distribution (bar chart)
  - Priority Distribution (bar chart)
- AI-Generated Daily Insights:
  - Top issue category & hotspot area
  - Urgent cases count
  - Frustrated citizen alerts
  - Recommendations for resource allocation
- Attention Table (unresolved complaints)
- CSV Export for offline analysis

---

## 📊 Data Model

```
Complaint {
    complaint_id     : String     → Unique ID (GHC-YYYYMMDD-XXXX)
    citizen_name     : String     → Who complained
    phone            : String     → Contact number
    channel          : Enum       → Phone | WhatsApp | Email | Web | Walk-in
    area             : String     → Zone / Location
    complaint_text   : Text       → Detailed description
    category         : String     → AI-assigned (Water, Roads, Electricity...)
    priority         : Enum       → Urgent | High | Medium | Low
    sentiment        : String     → AI-detected (Very Frustrated, Frustrated, Neutral)
    status           : Enum       → Open → In Progress → Resolved
    assigned_officer : String     → Auto-assigned by department
    officer_notes    : Text       → Investigation updates
    submitted_date   : DateTime   → When filed
    updated_date     : DateTime   → Last action date
}
```

---

## 🛠️ Current Tech Stack (Prototype)

| Layer | Technology | Reason |
|-------|-----------|--------|
| Frontend + Backend | **Python + Streamlit** | Rapid prototyping — working app in 2 hours |
| AI Engine | **Keyword-based NLP** | Lightweight, no API needed, works offline |
| Data | **Pandas + Session State** | In-memory storage, fast analytics |
| Charts | **Streamlit built-in** | Bar charts, metrics, dataframes |
| Deployment | **Streamlit Cloud** | Free, instant, GitHub-integrated |

---

## 🚀 Production Tech Stack (Future)

### Frontend
| Technology | Purpose |
|-----------|---------|
| React.js / Next.js | Production web UI with responsive design |
| React Native / Flutter | Mobile app for citizens & field officers |

### Backend
| Technology | Purpose |
|-----------|---------|
| FastAPI / Django | REST API with authentication |
| JWT + OAuth 2.0 | Role-based access control |
| Celery + Redis | Async notifications & auto-escalation |

### AI/ML Layer
| Technology | Purpose |
|-----------|---------|
| GPT-4 / Claude API | 99% accurate categorization via LLM |
| Hugging Face Transformers | Fine-tuned sentiment model |
| Scikit-learn | Predictive analytics for complaint volume forecasting |

### Database & Infrastructure
| Technology | Purpose |
|-----------|---------|
| PostgreSQL | Relational database for complaints |
| Redis | Caching for dashboard performance |
| AWS / Azure | Cloud hosting with auto-scaling |
| Docker + Kubernetes | Containerized microservices |

### Communication
| Technology | Purpose |
|-----------|---------|
| Twilio API | SMS status updates to citizens |
| WhatsApp Business API | Receive complaints via WhatsApp |
| Firebase | Push notifications for mobile app |

---

## 📈 Expected Impact

| Metric | Before (Manual) | After (Our System) |
|--------|-----------------|-------------------|
| Complaint tracking | ~40% | **100%** |
| Categorization speed | 5/min (manual) | **100+/min (AI)** |
| Resolution time | 7-15 days | **3-5 days** |
| Lost complaints | Many | **Zero** |
| Citizen satisfaction | Low | **70%+ improvement** |
| Policy insights | None | **Real-time AI analytics** |

---

## ⚠️ Escalation Rules

| Condition | Action |
|-----------|--------|
| Complaint open > 3 days | Auto-escalate to Supervisor |
| Sentiment = Very Frustrated | Flag for immediate attention |
| Officer no update in 48 hours | Auto-notify Supervisor |
| Complaint resolved | Notify citizen via SMS |

---

## 🧠 Design Thinking Approach

| Phase | What I Did |
|-------|-----------|
| **1. Empathize** | Understood citizen pain — complaints lost, no tracking, no accountability |
| **2. Define** | Core problem: no centralized, intelligent complaint management system |
| **3. Ideate** | AI can automate categorization, priority, and routing — replacing manual GC work |
| **4. Prototype** | Built working Streamlit app with 5 interactive modules |
| **5. Validate** | Tested with 6 realistic complaints across all categories and priorities |

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run helpline_app.py
```
