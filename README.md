# CyberShield – AI-Assisted Phishing & Cyber Threat Analyzer

CyberShield is a cybersecurity tool that analyzes suspicious emails, messages, and security notifications for common phishing and social engineering indicators.

The tool combines **rule-based threat detection** with **Google Gemini AI analysis** to identify possible phishing, credential theft, suspicious links, and social engineering attempts.

---

## 🎯 Objective

The main objective of CyberShield is to provide a simple security analysis tool that can help users identify suspicious messages before interacting with them.

The tool analyzes a message and provides:

- Threat status
- Risk level
- Risk score
- Threat type
- Detected indicators
- AI-based analysis
- Security recommendation

---

## 🔍 Key Features

### 1. Rule-Based Threat Detection

CyberShield checks messages for indicators such as:

- Urgency and pressure
- Login or verification requests
- Password and credential requests
- Suspicious URLs
- Suspicious domain patterns
- Social engineering terminology

### 2. AI-Assisted Analysis

Google Gemini AI is used to analyze suspicious messages for:

- Phishing
- Social engineering
- Credential theft
- Malicious links
- Account takeover attempts

### 3. Risk Classification

The tool classifies detected threats into:

- LOW
- MEDIUM
- HIGH

### 4. Message Encryption

The submitted message is encrypted using **Fernet symmetric encryption** before analysis and decrypted for processing.

### 5. Security Recommendations

After analysis, CyberShield provides a recommendation to help the user respond safely.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| Flask-Bcrypt | Password/security support |
| Cryptography / Fernet | Message encryption |
| Google Gemini API | AI-based threat analysis |
| HTML | Frontend |
| CSS | User interface |
| JavaScript | Frontend interaction |

---

## 🏗️ System Workflow

```text
User
  |
  v
Enter Suspicious Message
  |
  v
CyberShield Web Interface
  |
  v
Message Encryption
  |
  v
Rule-Based Threat Detection
  |
  +--------------------+
  |                    |
  v                    v
Threat Indicators   Gemini AI
  |                    |
  +---------+----------+
            |
            v
      Final Analysis
            |
            v
   Risk + Threat Type
            |
            v
 Security Recommendation

Example Detection

Example suspicious message:

Urgent! Your account will be suspended. Please click here to verify your password and login immediately.

CyberShield can detect indicators such as:

Urgency or pressure
Login/verification request
Credential-related request

Example result:

Status: THREAT
Risk: HIGH
Threat Type: Phishing, Credential Theft
📚 Real-World Case Study
Code of Conduct Phishing Campaign

CyberShield's detection logic includes indicators relevant to a documented phishing campaign reported by Microsoft.

The campaign involved messages using a Code of Conduct / compliance theme and techniques associated with phishing and Adversary-in-the-Middle (AiTM).

Observed: 14–16 April 2026

Reported by Microsoft: 4 May 2026

Reported target scale: 35,000+ users

Technique: Phishing + AiTM

CyberShield is a case-study-inspired detection tool. It does not reproduce or perform the actual Microsoft attack.

🚀 How to Run
1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL
2. Open the project
cd CyberShield-Threat-Analyzer
3. Create a virtual environment
python -m venv venv
4. Activate the virtual environment
Windows PowerShell
venv\Scripts\activate
5. Install dependencies
pip install -r requirements.txt
6. Create .env

Create a file named:

.env

Add:

GEMINI_API_KEY=your_actual_gemini_api_key

Never upload the actual .env file to GitHub.

7. Run the application
python app.py

Open:

http://127.0.0.1:5000
🔐 Security

The following files contain sensitive information and should not be uploaded to GitHub:

.env
secret.key
venv/

These files are excluded using .gitignore.

⚠️ Limitations
Rule-based detection depends on predefined indicators.
AI analysis depends on Gemini API availability and quota.
The tool cannot guarantee that every message classified as SAFE is actually safe.
Advanced phishing techniques may require additional analysis.
The current version is intended for educational and demonstration purposes.
🔮 Future Enhancements

Possible future improvements include:

URL reputation checking
Domain age and WHOIS analysis
Email header analysis
Attachment analysis
VirusTotal integration
ML-based phishing classification
Threat intelligence integration
Browser extension
Detailed security reports
Database-based threat history
🎓 Project Purpose

This project was developed as an academic cybersecurity project to demonstrate the practical application of:

Cyber threat detection
Phishing analysis
Social engineering detection
Encryption
Generative AI
Web application development
👩‍💻 Author

Pooja Parmar

B.Sc. Cyber & Digital Science

Cybersecurity | Cloud Security | Generative AI

📄 Disclaimer

CyberShield is an educational cybersecurity analysis tool.

It should not be considered a replacement for professional security tools, security teams, or threat intelligence platforms.