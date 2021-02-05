from flask import Blueprint, current_app, request
from .model import Card
from .serializers import CardSchema
from marshmallow.exceptions import ValidationError
from app.creditcard import CreditCard
from .utils import format_date
from app.creditcard.exceptions import BrandNotFound


bp_cards = Blueprint('cards', __name__)


@bp_cards.route('/register', methods=['POST'])
def register():
    cs = CardSchema()
    payload = request.json
    try:
        card_data = cs.load(payload)  # informações tradatas/validadas
    except ValidationError as e:
        return e.args[0]

    card_number = card_data['number']

    cc = CreditCard(card_number)

    if not cc.is_valid():
        return "Número de cartão de crédito inválido"

    exp_date = format_date(card_data["exp_date"])

    card = Card()
    card.number = card_data["number"]
    card.cvv = card_data["cvv"]
    card.holder = card_data["holder"]
    card.exp_date = exp_date
    try:
        card.brand = cc.get_brand()
    except BrandNotFound:
        return {
            "message": "Card brand not found"
        }

    current_app.db.session.add(card)
    current_app.db.session.commit()

    return {
        "message": "Card saved"
    }


@bp_cards.route('/show', methods=['GET'])
def show():
    result = Card.query.all()
    return CardSchema(many=True).dumps(result), 200
