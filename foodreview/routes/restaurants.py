from flask import Blueprint, request, jsonify, g
from ..utils.auth_utils import require_auth
from ..db import get_connection

restaurants_bp = Blueprint('restaurants', __name__, url_prefix='/restaurants')

@restaurants_bp.post('/')
@require_auth
def create():
    user_id = g.pop('user_id')
    username = g.pop('username')
    return jsonify({'message': f"User {username} with id {user_id} created a restaurant"})