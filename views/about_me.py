import streamlit as st
from forms.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/z_marvel.jpg", width=230)
with col2:
    st.title("Vin Bolisetti", anchor=False)
    st.write(
        "Lead Software Developer, developing cloud & data driven enterprise applications."
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - A dynamic working professional Lead Python Developer with 9+ years of experience in the IT Industry
    - Worked with different domains like Enterprise, CRM, ERP, Sales, and e-commerce
    - Full stack development experience in enterprise development projects with a product development background
    - Experience in DevOps, CI/CD, Configuration and Release Management roles, Configure, Deploy, and maintain Cloud SaaS
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Languages: Python3, HTML, Bootstrap, Tailwind CSS, YAML
    - Frameworks: Django, Django Rest Framework, REST APIs
    - Databases: PostgreSQL, AWS RDS, SQLServer, MySQL
    - OS: Unix, Linux Shell Scripting
    - Cloud: most AWS services like EC2, Load Balancers, ECS/ECR, Lambda, API Gateway, S3, RDS, Athena, SNS, Microsoft Azure
    - CI/CD: AWS CodePipeline, CodeDeploy, GitHub Actions
    - Version Control: GitHub
    """
)
