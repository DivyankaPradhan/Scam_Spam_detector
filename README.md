# 🛡️ Spam & Scam Message Detector (Version 1)

A rule-based Spam & Scam Message Detector built with Python.

This project analyzes a user-provided message and determines whether it is **Safe**, **Suspicious**, or **Likely Scam** by detecting suspicious keywords and scam-related patterns. It also calculates a risk score and provides explanations for every detected pattern.

This project was built as a learning project to practice Python fundamentals such as functions, loops, dictionaries, JSON handling, modules, and regular expressions.

---

# 📌 Features

- Detects suspicious scam-related keywords
- Detects URLs using Regular Expressions (Regex)
- Calculates a cumulative risk score
- Classifies messages into:
  - 🟢 Safe
  - 🟡 Suspicious
  - 🔴 Likely Scam
- Displays every detected pattern
- Explains why each pattern was flagged
- Loads detection rules from a JSON file
- Modular project structure for easy expansion

---

# 🛠️ Technologies Used

- Python 3
- JSON
- Regular Expressions (`re` module)

---

# 📂 Project Structure

```
Spam-Scam-Detector/
│
├── main.py                 # Main program
├── detector.py             # Detection engine
├── scan_keywords.json      # Detection rules and keyword database
├── README.md               # Project documentation
|__test_messages.txt        # Messages examples
|__demo.mp4                 # Video demo
```

---

# ⚙️ How It Works

1. The program loads all detection rules from `scan_keywords.json`.
2. The user enters a message.
3. The detector scans the message for:
   - Suspicious keywords
   - Scam-related phrases
   - URLs (using Regex)
4. Every detected pattern contributes to a risk score.
5. Based on the total score, the message is classified as:
   - Safe
   - Suspicious
   - Likely Scam
6. The program displays:
   - Detected patterns
   - Reasons
   - Risk score
   - Final verdict

---

# 📊 Risk Score

| Risk Score | Verdict |
|------------|---------|
| 0 - 19 | 🟢 Safe |
| 20 - 49 | 🟡 Suspicious |
| 50+ | 🔴 Likely Scam |

---

# ▶️ How to Run

### Clone the repository

```bash
git clone https://github.com/yourusername/Spam-Scam-Detector.git
```

### Open the project

```bash
cd Spam-Scam-Detector
```

### Run

```bash
python main.py
```

---

# 📚 Concepts Practiced

This project helped practice:

- Functions
- Modules
- Lists
- Dictionaries
- Loops
- Nested Loops
- JSON File Handling
- Regular Expressions (Regex)
- Risk Scoring
- Modular Programming
- Rule-Based Detection Systems

---

# 🚀 Future Improvements (Version 2)

Planned improvements include:

- Detect all URLs using `re.findall()`
- Email detection
- Phone number detection
- Money amount detection
- Shortened URL detection
- Fake company name detection
- Context-aware scoring
- Scan history
- Batch message scanning
- Streamlit web interface

---

# 🎯 Learning Objective

The goal of this project was **not to build a production-ready spam detector**, but to understand how rule-based detection systems work and strengthen core Python programming skills by building a practical cybersecurity-inspired application.

---

# 📄 License

This project is intended for educational and learning purposes.