from flask import Flask, render_template, request, redirect, flash, url_for
import db

app = Flask(__name__)
app.secret_key = "nikita_secret_key" 
db.create_table()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    email = request.form['email']
    campus = request.form['campus']
    module = request.form['module']

    if db.add_student(name, email, campus, module):
        return redirect(url_for('show_students'))
    else:
        flash("Error: This email already exists!", "error")
        return redirect(url_for('home'))

@app.route('/students')
def show_students():
    students = db.get_all_students()
    return render_template('students.html', students=students)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    if request.method == 'POST':
        db.update_student(id, request.form['name'], request.form['email'], 
                          request.form['campus'], request.form['module'])
        flash("Student updated successfully!", "success")
        return redirect(url_for('show_students'))
    
    student = db.get_student_by_id(id)
    return render_template('edit.html', s=student)

@app.route('/delete/<int:id>')
def delete_student(id):
    db.delete_student(id)
    return redirect(url_for('show_students'))

if __name__ == '__main__':
    app.run(debug=True)


