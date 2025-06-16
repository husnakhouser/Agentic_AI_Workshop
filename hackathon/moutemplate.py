# 📄 streamlit_mou_generator.py

import streamlit as st
from datetime import date

# ------------------ Page Configuration ------------------
st.set_page_config(
    page_title="MoU Generator | SNSCT",
    layout="centered"
)

# ------------------ Title Section ------------------
st.title("📄 MoU Template Generator - SNS College of Technology")

st.markdown("Use this tool to quickly generate a customized MoU outline by selecting type and filling in organization details.")

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

# ------------------ MoU Description Templates ------------------
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

st.markdown(f"""
### Memorandum of Understanding (MoU)

**Between SNS College of Technology, Coimbatore and {company_name}**

**Type of MoU:** {selected_mou_type}  
**Date of Signing:** {signing_date.strftime('%B %d, %Y')}

**Objective:**  
{mou_descriptions[selected_mou_type]}

_Further sections like Scope, Roles, and Signatures will be dynamically filled in final documents._
""")

# ------------------ Download & Future Features ------------------
if st.button("✅ Generate Full MoU Draft"):
    st.success("Template preview generated! Export options (Word/PDF) coming soon.")

