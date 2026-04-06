from flask import Flask, render_template, request, jsonify
import mysql.connector
from config import db_config

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(**db_config)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():

    data = request.json

    full_name = data.get("full_name")
    event_name = data.get("event_name")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO registrations (full_name, event_name)
        VALUES (%s, %s)
        """

        cursor.execute(query, (full_name, event_name))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"message": "Registration successful!"})

    except Exception as e:
        return jsonify({"message": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)