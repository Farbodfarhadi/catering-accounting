
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import os

app = Flask(__name__, template_folder='templates')

transactions = []

@app.route('/')
def index():
    balance = sum([t['amount'] for t in transactions])
    return render_template('index.html', transactions=transactions, balance=balance)

@app.route('/add', methods=['POST'])
def add():
    description = request.form.get('description')
    amount = float(request.form.get('amount'))
    date = request.form.get('date') or datetime.now().strftime('%Y-%m-%d')
    type_ = request.form.get('type')
    amount = amount if type_ == 'income' else -amount

    transactions.append({
        'description': description,
        'amount': amount,
        'date': date,
        'type': type_
    })

    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
