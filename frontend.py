import streamlit as st
import requests
import textwrap

BACKEND_URL = "http://127.0.0.1:8000/analyze"


def run_app():
    st.set_page_config(
        page_title="ScamLens",
        page_icon="🛡️",
        layout="wide"
    )

    st.markdown("""
    <style>

    .stApp {
        background:
            radial-gradient(circle at top left, #14213d 0%, transparent 35%),
            radial-gradient(circle at top right, #12302c 0%, transparent 30%),
            #080c14;
        color: white;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    .block-container {
        max-width: 1100px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }

    .logo {
        text-align: center;
        font-size: 4rem;
        margin-bottom: 0;
    }

    .main-title {
        text-align: center;
        font-size: 3.7rem;
        font-weight: 800;
        margin-top: -10px;
        margin-bottom: 5px;
        letter-spacing: -2px;
    }

    .main-title span {
        color: #5eead4;
    }

    .subtitle {
        text-align: center;
        color: #9ca3af;
        font-size: 1.15rem;
        margin-bottom: 15px;
    }

    .gemini-badge {
        text-align: center;
        margin-bottom: 35px;
    }

    .gemini-badge span {
        background: rgba(94, 234, 212, 0.08);
        border: 1px solid rgba(94, 234, 212, 0.25);
        color: #5eead4;
        padding: 7px 15px;
        border-radius: 100px;
        font-size: 0.85rem;
    }

    .info-card {
        background: rgba(16, 23, 34, 0.85);
        border: 1px solid #202b3a;
        padding: 22px;
        border-radius: 16px;
        height: 100%;
    }

    .info-title {
        font-size: 1.05rem;
        font-weight: 700;
        margin-bottom: 6px;
    }

    .info-text {
        color: #9ca3af;
        font-size: 0.9rem;
        line-height: 1.5;
    }

    textarea {
        background-color: #101722 !important;
        color: white !important;
        border: 1px solid #283444 !important;
        border-radius: 15px !important;
        font-size: 16px !important;
    }

    textarea:focus {
        border: 1px solid #5eead4 !important;
        box-shadow: 0 0 0 1px #5eead4 !important;
    }

    .stButton > button {
        background: linear-gradient(90deg, #2dd4bf, #3b82f6);
        color: white;
        border: none;
        border-radius: 12px;
        height: 55px;
        font-size: 17px;
        font-weight: 700;
        transition: 0.2s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0px 8px 25px rgba(45, 212, 191, 0.25);
        color: white;
        border: none;
    }

    .high-risk {
        background: rgba(239, 68, 68, 0.10);
        border: 1px solid rgba(239, 68, 68, 0.35);
        padding: 25px;
        border-radius: 16px;
        margin-top: 20px;
    }

    .medium-risk {
        background: rgba(245, 158, 11, 0.10);
        border: 1px solid rgba(245, 158, 11, 0.35);
        padding: 25px;
        border-radius: 16px;
        margin-top: 20px;
    }

    .low-risk {
        background: rgba(34, 197, 94, 0.10);
        border: 1px solid rgba(34, 197, 94, 0.35);
        padding: 25px;
        border-radius: 16px;
        margin-top: 20px;
    }

    .section-label {
        color: #9ca3af;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 600;
    }

    .footer-text {
        color: #596273;
        text-align: center;
        font-size: 0.8rem;
        margin-top: 50px;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="logo">🛡️</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="main-title">Scam<span>Lens</span></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Spot phishing before it gets you.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="gemini-badge"><span>✦ Powered by Google Gemini</span></div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="info-card">
            <div class="info-title">🔎 Detect Red Flags</div>
            <div class="info-text">
                Spot suspicious wording, urgency, impersonation,
                and phishing tactics.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-card">
            <div class="info-title">⚡ Instant Analysis</div>
            <div class="info-text">
                Gemini explains what makes an email suspicious.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="info-card">
            <div class="info-title">🛡️ Stay Protected</div>
            <div class="info-text">
                Get clear steps for what you should do next.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    st.markdown(
        '<div class="section-label">Analyze an email</div>',
        unsafe_allow_html=True
    )

    st.markdown("### Is this email legit?")

    email_text = st.text_area(
        "Email",
        label_visibility="collapsed",
        placeholder=(
            "Paste the suspicious email here...\n\n"
            "Example:\n"
            "Subject: URGENT — Your account has been suspended\n\n"
            "Dear Customer,\n"
            "Your account will be disabled unless you verify..."
        ),
        height=280
    )

    analyze = st.button(
        "✦ Analyze Email",
        use_container_width=True
    )

    if analyze:
        if not email_text.strip():
            st.warning("Paste an email first.")
        else:
            with st.spinner("Gemini is inspecting the email..."):
                try:
                    response = requests.post(
                        BACKEND_URL,
                        json={"message": email_text},
                        timeout=(5, 90)
                    )

                    if response.status_code == 200:
                        result = response.json()
                        display_results(result)

                    else:
                        st.error(
                            f"Backend error ({response.status_code}): "
                            f"{response.text}"
                        )

                except requests.exceptions.ConnectionError:
                    st.error(
                        "Could not connect to the backend. "
                        "Make sure backend.py is running."
                    )

                except requests.exceptions.Timeout:
                    st.error(
                        "The analysis took too long. Please try again."
                    )

                except Exception as error:
                    st.error(f"Something went wrong: {error}")

    st.markdown(
        """
        <div class="footer-text">
            ScamLens · AI-assisted scam detection
        </div>
        """,
        unsafe_allow_html=True
    )


def display_results(result):
    st.write("")
    st.write("")

    risk = result.get("risk_level", "UNKNOWN").upper()
    risk_score = result.get("risk_score", 0)

    if risk == "HIGH":
        css_class = "high-risk"
        emoji = "🔴"
    elif risk == "MEDIUM":
        css_class = "medium-risk"
        emoji = "🟡"
    else:
        css_class = "low-risk"
        emoji = "🟢"

    st.markdown(
        textwrap.dedent(
            f"""
            <div class="{css_class}">
                <div class="section-label">Risk Assessment</div>

                <h2>{emoji} {risk} RISK</h2>

                <strong>Risk Score:</strong> {risk_score}/100
                <br>

                <strong>Likely type:</strong>
                {result.get("scam_type", "Unknown")}
            </div>
            """
        ),
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown("### Why?")
    st.write(
        result.get(
            "explanation",
            "No explanation was provided."
        )
    )

    st.write("")

    left, right = st.columns(2)

    with left:
        st.markdown("### 🚩 Red Flags")

        red_flags = result.get("red_flags", [])

        if red_flags:
            for flag in red_flags:
                st.write(f"• {flag}")
        else:
            st.write("No major red flags detected.")

    with right:
        st.markdown("### 🛡️ What You Should Do")

        recommended_action = result.get(
            "recommended_action",
            "Use caution and verify the sender."
        )

        st.write(recommended_action)

    st.info(
        "AI can make mistakes. Verify important emails through the organization's official website."
    )
