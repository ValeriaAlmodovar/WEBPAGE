from flask import Flask, request

app = Flask(__name__)

@app.route('page3.html', methods=['POST'])
def submit():
    # Get form data
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    phone = request.form['phone']
    payment = request.form['payment']

    # You can now process/save this data (for example, write it to a file or database)
    with open('order_data.txt', 'a') as file:
        file.write(f"Name: {name}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Address: {address}\n")
        file.write(f"Phone: {phone}\n")
        file.write(f"Payment: {payment}\n")
        file.write("-" * 20 + "\n")

    return "Thank you for your purchase!"

if __name__ == '__main__':
    app.run(debug=True)
