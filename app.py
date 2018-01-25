"""contains backend logic for the web app"""
from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message


app = Flask(__name__)

# email configuration when running locally
app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = '587'
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = 'faustiesbakery@gmail.com'
app.config["MAIL_PASSWORD"] = 'password'


mail = Mail(app)


@app.route('/')
def index():
    """displays the home page"""
    return render_template('index.html')

@app.route('/about')
def about():
    """renders the about page"""
    return render_template('about.html')

@app.route('/prices')
def prices():
    """renders the prices page"""
    return render_template('prices.html')


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    """renders the contact page and receives data from the contact form"""
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        site_message = request.form['site_message']

        content = """ Name: {} \n Email: {} \n Phone: {} \n Message: {} \n
                  """.format(name, email, phone, site_message)

        msg = Message("NEW CLIENT MESSAGE",
                      sender='faustiesbakery@gmail.com',
                      body=content,
                      recipients=['faustiesbakery@gmail.com'])
        mail.send(msg)

        return redirect(url_for('index'))

    return render_template('contact.html')


@app.route('/order', methods=['POST', 'GET'])
def order():
    """renders the order page and receives data from the order form"""
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cake_type = request.form['cake_type']
        shape = request.form['shape']
        weight = request.form['weight']
        cake_message = request.form['cake_message']
        instructions = request.form['instructions']

        content = """ Name: {} \n Email: {} \n Phone: {} \n Cake_type: {} \n Shape: {} \n Weight: {} \n Cake_message: {} \n Instructions: {} \n
                  """.format(name, email, phone, cake_type, shape, weight, cake_message, instructions)

        msg = Message("NEW CLIENT ORDER",
                      sender='faustiesbakery@gmail.com',
                      body=content,
                      recipients=['faustiesbakery@gmail.com'])
        mail.send(msg)

        return redirect(url_for('index'))

    return render_template('order.html')


if __name__ == '__main__':
    app.run(debug=True)
