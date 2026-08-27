from flask import Flask, jsonify, request
import psycopg2
import os

app = Flask(__name__)


def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5433"),
        database=os.getenv("DB_NAME", "assetdb"),
        user=os.getenv("DB_USER", "assetuser"),
        password=os.getenv("DB_PASSWORD", "assetpass")
    )


@app.route("/")
def home():
    return "Python Flask API is running"


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "flask-backend"
    })


@app.route("/assets", methods=["GET"])
def get_assets():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT id, asset_id, user_name, brand, model, status
            FROM assets
            ORDER BY id
        """)

        rows = cur.fetchall()

        cur.close()
        conn.close()

        assets = []

        for row in rows:
            assets.append({
                "id": row[0],
                "asset_id": row[1],
                "user_name": row[2],
                "brand": row[3],
                "model": row[4],
                "status": row[5]
            })

        return jsonify(assets)

    except Exception as error:
        return jsonify({
            "error": str(error)
        }), 500


@app.route("/assets", methods=["POST"])
def create_asset():
    try:
        data = request.get_json()

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO assets
            (asset_id, user_name, brand, model, status)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id
        """, (
            data["asset_id"],
            data.get("user_name"),
            data.get("brand"),
            data.get("model"),
            data.get("status")
        ))

        new_id = cur.fetchone()[0]

        conn.commit()
        cur.close()
        conn.close()

        return jsonify({
            "message": "Asset created successfully",
            "id": new_id
        }), 201

    except Exception as error:
        return jsonify({
            "error": str(error)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
