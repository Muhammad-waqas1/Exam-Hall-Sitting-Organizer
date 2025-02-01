# Exam Hall Sitting Organizer

![Exam Hall Organizer Banner](static/images/banner.jpg)

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Developer](#developer)
- [License](#license)

## Overview
**Exam Hall Sitting Organizer** is an innovative web application designed to streamline and automate the process of exam seating arrangements. Whether you're an administrator tasked with generating seating charts or a student looking for your assigned seat, this project provides an intuitive and interactive platform for managing exam hall logistics.

This project was developed as a Final Year Project by a team of 3 ADP CS students. It combines a modern, responsive frontend built with Bootstrap and a lightweight Flask backend to deliver a seamless user experience.

## Features
- **Home/Landing Page:** A professional and engaging landing page that introduces the system.
- **Admin Dashboard:** 
  - Secure login for administrators.
  - CSV file upload functionality to import student and exam hall data.
  - Seating plan generation with options to view and print the seating arrangement.
- **Seating Arrangement Display:** 
  - Responsive table view of the seating plan.
  - Search and filter capabilities by roll number, student name, or exam hall.
  - Options to edit or remove individual seat entries.
- **Student Portal:** 
  - A dedicated page for students to look up their seating details by entering their roll number.
  - Dynamic display of assigned seat details along with a print-friendly version.
- **Interactive Hall Map:** 
  - A visually interactive grid-based map of the exam hall.
  - Clickable seats with real-time status indicators (available, occupied, selected).
- **About Page:** 
  - Detailed overview of the project.
  - Introduction to the team members: Muhammad Haroon, Rehan Haider, and Muhammad Zohaib.

## Tech Stack
- **Frontend:** HTML, CSS (Bootstrap 5), JavaScript
- **Backend:** Python, Flask
- **Other:** CSV processing using Python's built-in libraries, session management for admin authentication

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Muhammad-waqas1/Exam-Hall-Sitting-Organizer.git
   cd Exam-Hall-Sitting-Organizer

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows use: venv\Scripts\activate

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt

_Note: Ensure you have Python 3 installed on your system._

4. **Run the Flask application:**
   ```bash
   python app.py

_The app should now be running in debug mode on http://127.0.0.1:5000._

## Usage
- **For Administrators:**  
1 Navigate to the Admin page to log in using your credentials.  
2 Upload the CSV file containing seating data. The CSV file should have columns such as student_name, roll_number, and exam_hall.  
3 Generate the seating plan and view the seating arrangement. You can also print the seating chart directly from the web interface.

- **For Students:**  
1 Go to the Student page and enter your roll number.  
2 View your seating details including your seat number and exam hall information.  
3 Print your seating slip if needed.

- **Interactive Hall Map:**  
1 Visit the Hall Map page to view an interactive grid representing the exam hall.  
2 Click on any seat to view its details. Occupied seats will be indicated and cannot be selected.

## Project Structure
   ```bash
   │── static/                   # Contains CSS, JS, and image assets
│   ├── css/
│   │   └── styles.css        # Custom styles
│   ├── js/
│   │   └── script.js         # Custom JavaScript functions
│   └── images/               # Banner and team member images
│── templates/                # HTML templates for all pages
│   ├── index.html            # Home/Landing Page
│   ├── admin.html            # Admin Dashboard/Login Page
│   ├── seating.html          # Seating Arrangement Page
│   ├── student.html          # Student Seating Info Page
│   ├── hallmap.html          # Interactive Hall Map Page
│   └── about.html            # About/Team Page
│── app.py                    # Flask application
│── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## Contributing
Contributions are welcome! If you have suggestions, improvements, or bug fixes, please feel free to create an issue or submit a pull request. Make sure to follow the standard GitHub workflow for contributions.

## Developer
Developed by [Muhammad Waqas](https://github.com/Muhammad-waqas1)

For any queries or further information, you can reach out via GitHub or create an issue in the repository.

## License
This project is licensed under the [MIT License]()


**_Happy organizing and coding!_**