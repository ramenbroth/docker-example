from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'postgresql+psycopg2://postgres:test@db:5432/test'
db = SQLAlchemy(app)


class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)


@app.route('/test', methods=['GET'])
def customers():
    query = Customers.query.all()
    return jsonify({'customers': [i.nome for i in query]})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8000)
