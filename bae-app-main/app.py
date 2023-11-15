from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Use SQLite as the database
app.config['SECRET_KEY'] = '52413720'  # Add a secret key for flash messages
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define your model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    account_type = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.account_type}')"


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/users')
def list_users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            account_type = request.form.get('account_type')

            new_user = User(name=name, account_type=account_type)
            db.session.add(new_user)
            db.session.commit()

            flash('User created successfully', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            # Handle exceptions, for example, log the error
            print(f"Error creating user: {e}")
            db.session.rollback()
            flash('Error creating user', 'danger')
            return render_template('error.html')

    # Handle GET requests (display form)
    return render_template('create_user.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
