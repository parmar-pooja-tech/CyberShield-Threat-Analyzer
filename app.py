from flask import Flask, render_template, request, jsonify
from flask_bcrypt import Bcrypt
from cryptography.fernet import Fernet
from dotenv import load_dotenv
from google import genai
import re
import os


# ==========================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# ==========================================
# FLASK APPLICATION
# ==========================================

app = Flask(__name__)

app.secret_key = "cybershield-secret-key"

bcrypt = Bcrypt(app)


# ==========================================
# GEMINI AI CLIENT
# ==========================================

if not GEMINI_API_KEY:

    print("WARNING: Gemini API key not found.")

    gemini_client = None

else:

    gemini_client = genai.Client(
        api_key=GEMINI_API_KEY
    )


# ==========================================
# ENCRYPTION KEY
# ==========================================

KEY_FILE = "secret.key"


if not os.path.exists(KEY_FILE):

    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as file:
        file.write(key)

else:

    with open(KEY_FILE, "rb") as file:
        key = file.read()


cipher = Fernet(key)


# ==========================================
# RULE-BASED THREAT ANALYSIS
# ==========================================

def analyze_rules(message):

    message_lower = message.lower()

    score = 0

    indicators = []

    threat_types = []


    # --------------------------------------
    # URGENCY / PRESSURE
    # --------------------------------------

    urgency_words = [
        "urgent",
        "immediately",
        "act now",
        "within 24 hours",
        "last warning",
        "account suspended",
        "final notice"
    ]

    for word in urgency_words:

        if word in message_lower:

            score += 1

            indicators.append(
                f"Urgency or pressure: '{word}'"
            )

            break


    # --------------------------------------
    # LOGIN / VERIFICATION
    # --------------------------------------

    login_words = [
        "login",
        "log in",
        "sign in",
        "verify your account",
        "verify account",
        "confirm your identity",
        "authentication",
        "account verification"
    ]

    for word in login_words:

        if word in message_lower:

            score += 2

            indicators.append(
                f"Login/verification request: '{word}'"
            )

            threat_types.append(
                "Phishing"
            )

            break


    # --------------------------------------
    # PASSWORD / CREDENTIAL REQUEST
    # --------------------------------------

    credential_words = [
        "password",
        "username",
        "credentials",
        "otp",
        "one time password",
        "security code"
    ]

    for word in credential_words:

        if word in message_lower:

            score += 2

            indicators.append(
                f"Credential-related request: '{word}'"
            )

            threat_types.append(
                "Credential Theft"
            )

            break


    # --------------------------------------
    # SUSPICIOUS LINK
    # --------------------------------------

    if re.search(r"https?://", message_lower):

        score += 2

        indicators.append(
            "URL/link detected in the message"
        )

        threat_types.append(
            "Malicious Link / Phishing"
        )


    # --------------------------------------
    # SUSPICIOUS DOMAINS
    # --------------------------------------

    suspicious_domains = [
        "bit.ly",
        "tinyurl.com",
        "login-verify",
        "secure-login",
        "free-money"
    ]

    for domain in suspicious_domains:

        if domain in message_lower:

            score += 2

            indicators.append(
                f"Suspicious domain/pattern: '{domain}'"
            )

            threat_types.append(
                "Suspicious Link"
            )

            break


    # --------------------------------------
    # SOCIAL ENGINEERING / CASE STUDY TERMS
    # --------------------------------------

    social_engineering_words = [
        "code of conduct",
        "compliance",
        "review materials",
        "policy violation",
        "internal regulatory",
        "workforce communications"
    ]

    for word in social_engineering_words:

        if word in message_lower:

            score += 1

            indicators.append(
                f"Social-engineering context: '{word}'"
            )

            threat_types.append(
                "Social Engineering"
            )

            break


    # --------------------------------------
    # FINAL RISK LEVEL
    # --------------------------------------

    if score >= 5:

        risk = "HIGH"

    elif score >= 3:

        risk = "MEDIUM"

    else:

        risk = "LOW"


    # --------------------------------------
    # FINAL THREAT STATUS
    # --------------------------------------

    if score >= 3:

        status = "THREAT"

    else:

        status = "SAFE"


    # --------------------------------------
    # REMOVE DUPLICATE THREAT TYPES
    # --------------------------------------

    threat_types = list(
        dict.fromkeys(threat_types)
    )


    if not threat_types:

        threat_types = [
            "No specific threat type detected"
        ]


    return {

        "status": status,

        "risk": risk,

        "score": score,

        "indicators": indicators,

        "threat_types": threat_types

    }


# ==========================================
# GEMINI AI ANALYSIS
# ==========================================

def analyze_with_ai(message):

    if gemini_client is None:

        return {

            "status": "AI UNAVAILABLE",

            "reason": "Gemini API key was not found."

        }


    prompt = f"""
You are a cybersecurity threat analysis assistant.

Analyze this message for phishing, social engineering,
credential theft, malicious links, scams, or account
takeover attempts.

Message:
{message}

Return exactly in this format:

STATUS: SAFE or THREAT
TYPE: short threat type
RISK: LOW, MEDIUM, or HIGH
REASON: one short sentence
RECOMMENDATION: one short safety recommendation

Do not provide extra text.
"""


    try:

        interaction = gemini_client.interactions.create(

            model="gemini-3.6-flash",

            input=prompt

        )


        result = interaction.output_text.strip()


        if "STATUS: THREAT" in result.upper():

            status = "THREAT"

        elif "STATUS: SAFE" in result.upper():

            status = "SAFE"

        else:

            status = "UNKNOWN"


        return {

            "status": status,

            "reason": result

        }


    except Exception as error:

        print()
        print("========================================")
        print("GEMINI AI ERROR")
        print("========================================")
        print(repr(error))
        print("========================================")
        print()


        return {

            "status": "AI ERROR",

            "reason": "Gemini AI analysis failed."

        }


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# ==========================================
# ANALYZE MESSAGE API
# ==========================================

@app.route(
    "/analyze",
    methods=["POST"]
)
def analyze_message():

    data = request.get_json()


    if not data:

        return jsonify({

            "error": "No data received."

        }), 400


    message = data.get(
        "message",
        ""
    ).strip()


    if not message:

        return jsonify({

            "error": "Please enter a message."

        }), 400


    # ======================================
    # ENCRYPT MESSAGE
    # ======================================

    encrypted_message = cipher.encrypt(

        message.encode()

    )


    print()
    print("Encrypted Message:")
    print(encrypted_message)


    # ======================================
    # DECRYPT MESSAGE
    # ======================================

    decrypted_message = cipher.decrypt(

        encrypted_message

    ).decode()


    # ======================================
    # RULE-BASED ANALYSIS
    # ======================================

    rule_result = analyze_rules(

        decrypted_message

    )


    # ======================================
    # AI ANALYSIS
    # ======================================

    ai_result = analyze_with_ai(

        decrypted_message

    )


    # ======================================
    # FINAL RESULT
    # ======================================

    final_status = rule_result["status"]

    final_risk = rule_result["risk"]


    # If AI detects threat, increase final result

    if ai_result["status"] == "THREAT":

        final_status = "THREAT"

        final_risk = "HIGH"


    # ======================================
    # RECOMMENDATION
    # ======================================

    if final_status == "THREAT":

        recommendation = (
            "Do not click suspicious links, "
            "share passwords, OTPs, or credentials. "
            "Verify the request through an official source."
        )

    else:

        recommendation = (
            "No strong threat indicators were detected. "
            "Still avoid sharing sensitive information."
        )


    # ======================================
    # RETURN RESULT
    # ======================================

    return jsonify({

        "status": final_status,

        "risk": final_risk,

        "score": rule_result["score"],

        "indicators": rule_result["indicators"],

        "threat_types": rule_result["threat_types"],

        "ai_analysis": ai_result["reason"],

        "recommendation": recommendation

    })


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(

        debug=True

    )