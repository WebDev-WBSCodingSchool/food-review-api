from flask import Blueprint, request, jsonify
from ..db import get_connection

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.post('/register')
def register():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT NOW()")
        result = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({'server_time': result[0].isoformat()}), 200
    except Exception as e:
        return jsonify({'Error': str(e)}), 500