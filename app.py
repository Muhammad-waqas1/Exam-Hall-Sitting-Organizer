from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import os
import csv
import io
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///StudentSeating.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.secret_key = 'your_secret_key_here'  # Replace with a strong secret key

# Global variable to store seating data.
# Each entry will be a dictionary with keys: seat_no, student_name, roll_number, exam_hall.
seating_data = []

# Dummy admin credentials (update as needed)
ADMIN_EMAIL = ''
ADMIN_PASSWORD = ''


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Seat = db.Column(db.String(10), unique=True, nullable=False)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    RollNo = db.Column(db.String(50), nullable=False)
    HallNo = db.Column(db.String(10), nullable=False)

    def __repr__(self) -> str:
        return f"{self.Seat} - {self.fname} - {self.lname} - {self.RollNo} - {self.HallNo}"

# --------------------------
# ROUTES
# --------------------------

@app.route('/')
def index():
    """Render the Home (Index) page."""
    return render_template('index.html')


# @app.route('/student')
# def student():
#     return render_template('student.html')

@app.route('/hallmap')
def hallmap():
    return render_template('hallmap.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    """
    Render the Admin page.
    POST method is used for handling admin login.
    """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            flash('Logged in successfully.', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
            return redirect(url_for('admin'))
    return render_template('admin.html')


@app.route('/admin/dashboard')
def admin_dashboard():
    """Render the Admin Dashboard page. (You may reuse admin.html or create a separate dashboard.)"""
    if not session.get('admin_logged_in'):
        flash('Please login first.', 'warning')
        return redirect(url_for('admin'))
    # For simplicity, we reuse admin.html as the dashboard.
    return render_template('admin.html')


# @app.route('/upload', methods=['POST'])
# def upload():
#     """
#     Handle CSV file upload to process seating data.
#     Expects a CSV file with at least the following columns: student_name, roll_number, exam_hall.
#     """
#     if not session.get('admin_logged_in'):
#         flash('Please login first.', 'warning')
#         return redirect(url_for('admin'))

#     if 'csv_file' not in request.files:
#         flash('No file part in the request.', 'danger')
#         return redirect(url_for('admin'))
    
#     file = request.files['csv_file']
#     if file.filename == '':
#         flash('No file selected for uploading.', 'danger')
#         return redirect(url_for('admin'))

#     try:
#         stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
#         csv_input = csv.DictReader(stream)
#         global seating_data
#         seating_data = []  # Reset any existing data
#         seat_no = 1
#         for row in csv_input:
#             seating_data.append({
#                 'seat_no': seat_no,
#                 'student_name': row.get('student_name', 'N/A'),
#                 'roll_number': row.get('roll_number', 'N/A'),
#                 'exam_hall': row.get('exam_hall', 'N/A')
#             })
#             seat_no += 1
#         flash('CSV file uploaded and seating data processed successfully.', 'success')
#     except Exception as e:
#         flash(f'Error processing file: {e}', 'danger')
    
#     return redirect(url_for('seating'))


@app.route('/add-student', methods=['POST'])
def addingstudent():
    """
    Trigger seating plan generation.
    (For now, we assume that the seating plan is created as soon as CSV data is processed.
    This endpoint can later incorporate more complex seating algorithms.)
    """
    Seat = request.form['Seat']
    fname = request.form['fname']
    lname = request.form['lname']
    RollNo = request.form['RollNo']
    HallNo = request.form['HallNo']

    # Check if the seat is already occupied
    existing_seat = Todo.query.filter_by(Seat=Seat).first()

    if existing_seat:
        flash(f'Seat No. {Seat} is already occupied! Please choose another seat.', 'danger')
        return redirect(url_for('seating'))  # 

    StudentSeating = Todo(Seat=Seat, fname=fname, lname=lname, RollNo=RollNo, HallNo=HallNo)
    db.session.add(StudentSeating)
    db.session.commit()

    flash('Student added successfully!', 'success')
    return redirect(url_for('admin'))


@app.route('/seating')
def seating():
    """
    Display the seating arrangement.
    Pass the seating data to the seating.html template.
    """
    return render_template('seating.html', seating_data=seating_data)


@app.route('/search')
def search():
    """
    Handle search queries from the seating page.
    Filters seating data by roll number, student name, or exam hall.
    """
    query = request.args.get('query', '').lower()
    filtered_data = []
    for entry in seating_data:
        if (query in entry['roll_number'].lower() or 
            query in entry['student_name'].lower() or 
            query in entry['exam_hall'].lower()):
            filtered_data.append(entry)
    return render_template('seating.html', seating_data=filtered_data)


@app.route('/getSeat')
def get_seat():
    """
    Provide seating details for a student based on their roll number.
    Returns a JSON response that can be used by the student.html page.
    """
    roll = request.args.get('roll', '').strip()
    for entry in seating_data:
        if entry['roll_number'].lower() == roll.lower():
            return jsonify(entry)
    return jsonify({'error': 'Seat not found for the provided roll number.'}), 404


@app.route('/logout')
def logout():
    """Logout the admin user."""
    session.pop('admin_logged_in', None)
    flash('Logged out successfully.', 'info')
    return redirect(url_for('index'))


# --------------------------
# MAIN
# --------------------------

if __name__ == '__main__':
    # Run the app in debug mode for development
    app.run(debug=True)
