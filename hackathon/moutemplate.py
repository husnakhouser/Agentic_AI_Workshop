import streamlit as st
from datetime import date
import requests

# ------------------ Page Configuration ------------------
st.set_page_config(
    page_title="MoU Generator | SNSCT",
    layout="centered"
)

# ------------------ Fixed Webhook URL ------------------
# Replace this URL with your actual webhook receiver (n8n, Make, Zapier, or test URL)
WEBHOOK_URL = "https://husnak.app.n8n.cloud/webhook-test/https://agenticaiworkshop-9x9odmlqcndnpqbpttyemq.streamlit.app/"  # 🔁 Replace with your real URL

# ------------------ Title Section ------------------
st.title("📄 MoU Template Generator - SNS College of Technology")
st.markdown("Fill in the MoU details and send them to an external system via webhook.")

# ------------------ Input: Company Details ------------------
company_name = st.text_input("Enter Partner Company Name:", value="InnovaTech Pvt. Ltd.")
signing_date = st.date_input("Select MoU Signing Date:", value=date.today())

# ------------------ Input: MoU Type ------------------
mou_types = [
    "Academic–Industry Collaboration",
    "Internship & Placement Support",
    "Research Collaboration",
    "Entrepreneurship & Incubation",
    "Training & Skill Development",
    "Hackathon / Innovation Partnership",
    "International Collaboration",
    "IPR & Patent Filing Support",
    "Faculty Development / Guest Lectures"
]
selected_mou_type = st.selectbox("Select Type of MoU:", mou_types)

# ------------------ MoU Description ------------------
mou_descriptions = {
    "Academic–Industry Collaboration": "Collaboration for industrial projects, domain-specific mentoring, and applied learning.",
    "Internship & Placement Support": "To provide internships, career guidance, and placement opportunities for students.",
    "Research Collaboration": "To pursue joint research, publications, and patent filings in emerging technologies.",
    "Entrepreneurship & Incubation": "To promote student startups, incubator support, and entrepreneurial mentoring.",
    "Training & Skill Development": "To enhance technical competencies through hands-on training, certification, and FDPs.",
    "Hackathon / Innovation Partnership": "To host joint hackathons, ideathons, and innovation challenges.",
    "International Collaboration": "To facilitate global student/faculty exchange and joint academic programs.",
    "IPR & Patent Filing Support": "To jointly identify, mentor, and file patents from student and faculty innovations.",
    "Faculty Development / Guest Lectures": "To enable regular industry interaction and expert-led sessions for faculty and students."
}

# ------------------ Preview Section ------------------
st.markdown("---")
st.subheader("🖨️ MoU Preview")

description = mou_descriptions[selected_mou_type]

st.markdown(f"""
### Memorandum of Understanding (MoU)

**Between SNS College of Technology, Coimbatore and {company_name}**

**Type of MoU:** {selected_mou_type}  
**Date of Signing:** {signing_date.strftime('%B %d, %Y')}
Official Contact Email:** {company_email}

**Objective:**  
{description}
""")

# ------------------ Webhook Submission ------------------
if st.button("🚀 Submit to Webhook"):
    data = {
        "institution": "SNS College of Technology",
        "partner_company": company_name,
        "signing_date": signing_date.isoformat(),
        "mou_type": selected_mou_type,
        "description": description
    }

    try:
        response = requests.post(WEBHOOK_URL, json=data)
        if response.status_code == 200:
            st.success("✅ MoU details successfully sent to webhook!")
        else:
            st.warning(f"⚠️ Webhook call failed: Status code {response.status_code}")
    except Exception as e:
        st.error(f"🚫 Error: {str(e)}")
