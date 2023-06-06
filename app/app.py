from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure the email notification system
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'username'
app.config['MAIL_PASSWORD'] = 'password'

mail = Mail(app)

# Create a route to handle user registration
@app.route('/register', methods=['POST'])
def register():
    # Get the user's email address from the request
    email = request.form['email']
    # Send a welcome email to the user
    msg = Message('Welcome!',
                  sender='support@example.com',
                  recipients=[email])
    msg.body = render_template('welcome_email.txt')
    mail.send(msg)
    # Return a success response
    return 'Registration successful!'

# Create a route to handle password reset requests
@app.route('/reset', methods=['POST'])
def reset():
    # Get the user's email address from the request
    email = request.form['email']
    # Send a reset password email to the user
    msg = Message('Password Reset Request',
                  sender='support@example.com',
                  recipients=[email])
    msg.body = render_template('reset_password.txt')
    mail.send(msg)
    # Return a success response
    return 'Password reset email sent!'

# Create a route to handle order confirmations
@app.route('/confirm', methods=['POST'])
def confirm():
    # Get the user's email address from the request
    email = request.form['email']
    # Send a order confirmation email to the user
    msg = Message('Order Confirmation',
                  sender='support@example.com',
                  recipients=[email])
    msg.body = render_template('order_confirmation.txt')
    mail.send(msg)
    # Return a success response
    return 'Order confirmation email sent!'

# Create a route to handle account activity alerts
@app.route('/alert', methods=['POST'])
def alert():
    # Get the user's email address from the request
    email = request.form['email']
    # Send a account activity alert email to the user
    msg = Message('Account Activity Alert',
                  sender='support@example.com',
                  recipients=[email])
    msg.body = render_template('account_activity_alert.txt')
    mail.send(msg)
    # Return a success response
    return 'Account activity alert email sent!'

if __name__ == '__main__':
    app.run(debug=True)