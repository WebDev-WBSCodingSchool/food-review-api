from flask import Blueprint, request, jsonify, g
from ..utils.auth_utils import require_auth
from ..db import get_connection

restaurants_bp = Blueprint('restaurants', __name__, url_prefix='/restaurants')

@restaurants_bp.get('/')
@require_auth
def get_restaurants():
    try:
        conn = get_connection()
        cur = conn.cursor()
        # Fetch all restaurants
        cur.execute("SELECT id, name, description, owner_id FROM restaurants")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        # Convert result to JSON-friendly format
        restaurants = []
        for row in rows:
            restaurants.append({
                'id': row[0],
                'name': row[1],
                'description': row[2],
                'owner_id': row[3]
            })
        return jsonify(restaurants), 200
    except Exception as e:
        return jsonify({'error': 'Server error', 'details': str(e)}), 500

@restaurants_bp.post('/')
@require_auth
def create():
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description', '')
        if not name:
            return jsonify({'error': 'Restaurant name is required'}), 400
        user_id = g.get('user_id')
        conn = get_connection()
        cur = conn.cursor()
        # Insert the restaurant into the DB
        cur.execute(
            "INSERT INTO restaurants (name, description, owner_id) VALUES (%s, %s, %s) RETURNING id",
            (name, description, user_id)
        )
        restaurant_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({
            'id': restaurant_id,
            'name': name,
            'description': description,
            'owner_id': user_id,
        }), 201
    except Exception as e:
        return jsonify({'error': 'Server error', 'details': str(e)}), 500
