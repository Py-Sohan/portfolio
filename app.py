import streamlit as st
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Lutfor Rahman Sohan | Data & Business Analytics",
    page_icon="📶",
    layout="wide"
)

# Load custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# Header

def header_section():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://i.ibb.co/4RyrYPdw/lutfor-rahman-sohan.png", width=300)
    with col2:
        st.markdown("""
        <div class='neumorphic-box fade-in'>
            <h1>Md Lutfor Rahman Sohan</h1>
            <h3>Data & Business Analytics Professional</h3>
            <p>
                📞 +8801568009434 | ✉️ lutforsohan.contact@gmail.com<br>
                📍 B-7, Enayet Nagar, Siddhirganj, Narayanganj, Dhaka, Bangladesh
            </p>
            <p>
                <a href="https://github.com/Py-Sohan">GitHub</a> |
                <a href="https://www.linkedin.com/in/yourprofile" target="_blank">LinkedIn</a> |
                <a href="https://www.kaggle.com/yourprofile" target="_blank">Kaggle</a>
            </p>
        </div>
        """, unsafe_allow_html=True)


# About

def about_section():
    st.header("👋 About Me")
    st.markdown("""
    <div class='neumorphic-box slide-in'>
        I'm a results-driven Business Intelligence professional with over 1 year of experience in data analytics,
        visualization, modeling, reporting, web scraping, and working with AI tools. I love turning data into
        actionable insights that drive real business results.
    </div>
    """, unsafe_allow_html=True)

# Education

def education_section():
    st.header("🎓 Education")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='neumorphic-box'>
            <h4>National University of Bangladesh</h4>
            <p>Bachelor of Social Science in Economics (2018 – 2024)</p>
            <p>CGPA: 2.86</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='neumorphic-box'>
            <h4>Govt. Tolaram College</h4>
            <p>HSC in Science (2016 – 2018)</p>
            <p>Grade: 4.07</p>
        </div>
        """, unsafe_allow_html=True)

# Experience

def experience_section():
    st.header("🏛️ Experience")
    with st.expander("Data & Business Analytics Internship – Digital Hill Valley (Feb-Apr 2025)", expanded=True):
        st.markdown("""
        <ul>
            <li>Business data analysis using Python, Power BI, Excel & SQL</li>
            <li>Support data-driven decision-making</li>
            <li>Participate in training, meetings, and report preparation</li>
        </ul>
        """, unsafe_allow_html=True)

# Projects

def projects_section():
    st.header("🚀 Key Projects")
    projects = [
    {
        "title": "Bangladesh Bank Branch Insights",
        "desc": "Power BI Dashboard to analyze bank branch distribution and performance",
        "link": "https://shorturl.at/g7znl",
        "tags": ["Power BI", "Data Visualization"]
    },
    {
        "title": "Adventure Works Sales and Management",
        "desc": "Power BI dashboard for sales and operations insights",
        "link": "https://shorturl.at/wKU0L",
        "tags": ["Power BI", "Sales"]
    },
    {
        "title": "iFlix User Engagement and Content Performance",
        "desc": "Analyzing content performance and user behavior with Power BI",
        "link": "https://shorturl.at/8PH1g",
        "tags": ["Power BI", "User Analytics"]
    },
    {
        "title": "Bank Loan Analysis Dashboard",
        "desc": "Power BI Project analyzing loan approvals and trends",
        "link": "https://shorturl.at/SV593",
        "tags": ["Power BI", "Finance"]
    },
    {
        "title": "Supply Chain and Sales Management Analysis",
        "desc": "Retail chain analysis with sales and supply chain KPIs",
        "link": "https://shorturl.at/zgLMF",
        "tags": ["Power BI", "Retail"]
    },
    {
        "title": "Automated Data Analysis with Python",
        "desc": "Live project showcasing automation as an alternative to Power BI",
        "link": "https://shorturl.at/UWmwu",
        "tags": ["Python", "Automation"]
    },
    {
        "title": "Pizza Sales Analysis Dashboard",
        "desc": "Power BI dashboard visualizing pizza sales data and performance",
        "link": "https://shorturl.at/hsaAD",
        "tags": ["Power BI", "Sales Analysis"]
    },
    {
        "title": "Awesome Chocolate Sales Analysis",
        "desc": "Power BI dashboard exploring chocolate product sales trends",
        "link": "https://shorturl.at/HyXDZ",
        "tags": ["Power BI", "Sales"]
    },
    {
        "title": "Flipkart Data Analysis and Prediction App",
        "desc": "E-commerce product analysis and ML-based prediction using Python",
        "link": "https://shorturl.at/6nMPz",
        "tags": ["Python", "E-commerce", "ML"]
    }
]


    cols = st.columns(3)
    for idx, project in enumerate(projects):
        with cols[idx % 3]:
            st.markdown(f"""
                <div class="project-card animated-glow">
                    <h3>{project['title']}</h3>
                    <p>{project['desc']}</p>
                    <div class="tags">{" ".join(f'<span class="tag">{tag}</span>' for tag in project["tags"])} </div>
                    <a class="project-link" href="{project['link']}" target="_blank" style="color:black">View Project →</a>
                </div>
            """, unsafe_allow_html=True)

# Skills

def skills_section():
    st.header("🔧 Skills")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.markdown("""
        <div class='neumorphic-box skill-box'>
            <h4>Languages</h4>
            <ul><li>Python</li><li>SQL</li></ul>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='neumorphic-box skill-box'>
            <h4>Visualization</h4>
            <ul><li>Power BI</li><li>Excel</li><li>Looker Studio</li></ul>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class='neumorphic-box skill-box'>
            <h4>Statistical Analysis</h4>
            <ul><li>Regression</li><li>Time Series</li><li>Hypothesis Testing</li></ul>
        </div>
        """, unsafe_allow_html=True)

# Training

def training_section():
    st.header("📅 Training & Certifications")
    st.markdown("""
    <div class='neumorphic-box'>
        <ul>
            <li><strong>Professional Data & Business Analytics</strong> – Digital Hill Valley, 2025</li>
            <li><strong>AI Agent Development Bootcamp</strong> – Ostad, 2025</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Languages
def languages_section():
    st.header("🌐 Languages")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='neumorphic-box'>
            <ul>
                <li><strong>Bengali:</strong> Native</li>
                <li><strong>English:</strong> Fluent</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Recommendations
def recommendation_section():
    st.header("📝 Recommendations")
    st.markdown("""
    <div class='neumorphic-box'>
        <p><strong>Joy Dhon Chakma</strong><br>
        Executive – Business Analyst, Anwar Group of Industries</p>
        <p>Read Recommendation: 
            <a href="https://shorturl.at/vqGls" target="_blank" style="color:#2c3e50; font-weight: bold;">
            View on LinkedIn →</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

# Contact (Google Form Embed)

def contact_section():
    st.header("📬 Get In Touch")
    st.markdown("""
        <div class="form-container">
            <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSdDo_n_rI2pNO_Tz5SfkcroH2kUaHpOT--wWkxLgN6enn1GKQ/viewform?embedded=true"
            width="100%" height="730" frameborder="0" marginheight="0" marginwidth="0" style="border-radius: 12px;">Loading…</iframe>
        </div>
    """, unsafe_allow_html=True)

# Main App Runner
def main():
    header_section()
    about_section()
    education_section()
    experience_section()
    projects_section()
    skills_section()
    languages_section()         # ✅ Added
    training_section()
    recommendation_section()    # ✅ Added
    contact_section()

if __name__ == "__main__":
    main()
