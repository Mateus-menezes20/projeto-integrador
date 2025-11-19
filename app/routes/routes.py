from flask import Blueprint, jsonify, request
from app.utils.logger import log

example_bp = Blueprint('example', __name__)

@example_bp.route('/')
def index():
    log(
        user="anonymous",                # se quiser depois trocamos por usuário logado
        action=f"Acessou rota / (IP={request.remote_addr})"
    )

    return jsonify({"message": "API funcionando!"})
