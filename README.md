
# pyHub

A modern, beginner-friendly Python learning and coding platform built to help students explore Python, solve problems, and build real skills.

## 🚀 Overview

pyHub offers a clean, dark-themed interface with interactive problem sets, a simple course browser, and a smooth learning flow. It’s designed for learners of all ages to practice Python in a friendly environment.

This repository currently contains the latest site files (see the `pyhub-newest/` directory).

## 🌟 Features

- User authentication: Sign up, log in, and session-based access
- Profile dashboard: Track your username and solved problems
- Problems library: 50+ challenges (easy, medium, hard) with instant feedback
- Courses section: Browse/search curated Python courses and videos
- Live code runner: Execute Python snippets in-browser
- Progress tracking: Persist solved progress to your profile
- Responsive design: Works on desktop and mobile
- Modern UI: Dark theme, animated backgrounds, and interactive elements

## 🛠️ Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python (Flask)
- Icons: Font Awesome
- Styling: Custom CSS, responsive layouts

## 📁 Repository Structure

The repository’s latest iteration is in the `pyhub-newest/` directory. A typical layout looks like:

```
pyhub-newest/
├─ app.py                  # Flask backend (if running the server)
├─ Landing_page.html       # Entry point for the UI
├─ Courses.html
├─ home.html
├─ question_page.html
├─ login.html
├─ signup_page.html
├─ About_us/
│  └─ about_us.html
├─ assets/                 # Images, icons, etc.
├─ css/                    # Stylesheets
└─ js/                     # Frontend scripts
```

Note: Exact filenames/folders may vary slightly; use `Landing_page.html` as a starting point if browsing statically, or `app.py` if running the backend.

## ⚡ Getting Started

You can either open the static pages directly, or run the Flask backend.

### Option A: Browse the static site
1. Clone the repository:
   ```bash
   git clone https://github.com/TurjoRahman-afk/pyHub_web.git
   cd pyHub_web/pyhub-newest
   ```
2. Open `Landing_page.html` in your browser.

### Option B: Run with Flask backend
1. Clone the repository:
   ```bash
   git clone https://github.com/TurjoRahman-afk/pyHub_web.git
   cd pyHub_web/pyhub-newest
   ```
2. (Recommended) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   # If a requirements.txt exists, prefer:
   # pip install -r requirements.txt

   # Otherwise, install the known dependencies:
   pip install flask flask-cors
   ```
4. Run the server:
   ```bash
   python app.py
   ```
5. Open your browser at:(or you can open the HTML files from the folder on your laptop)
   ```
   http://127.0.0.1:5000
   ```

## 📸 Screenshots

Add screenshots or GIFs here to showcase the UI (e.g., landing page, problem page, profile).

## 🗺️ Roadmap Ideas

- More problem sets and categories
- User streaks and achievements
- Hints and editorial solutions
- Richer course discovery filters
- Offline/desktop mode

## 👥 About

This was a course project. I worked on both the frontend and backend. It took around one and a half weeks to build and fix small issues.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Open an issue for bugs and ideas
- Submit a pull request for fixes or features

Please keep PRs focused and include a clear description of the change.

## 📄 License

This project is open source under the MIT License. See the License section in this README or the repository for details.

Copyright (c) 2025 TurjoRahman-afk

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

pyHub — Explore, Learn, and Build with Python!
