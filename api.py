from flask import Flask, Response, stream_with_context, send_file
import psycopg2
import json

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect("dbname=stream user=postgres password=postgres host=localhost")

@app.route('/')
def index():
    return send_file('page.html')

@app.route('/stream')
def stream_people():
    def generate():
        conn = get_db_connection()
        try:
            cursor = conn.cursor(name='stream_cursor')
            cursor.itersize = 1
            cursor.execute("""
                SELECT pk, sk, fname, lname, dob, zipcode
                FROM people
                ORDER BY pk
            """)
            for row in cursor:
                person = {
                    "pk": row[0],
                    "sk": row[1],
                    "fname": row[2],
                    "lname": row[3],
                    "dob": str(row[4]),
                    "zipcode": row[5],
                }
                yield f"data: {json.dumps(person)}\n\n"
            cursor.close()
        finally:
            conn.close()

    return Response(stream_with_context(generate()), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
