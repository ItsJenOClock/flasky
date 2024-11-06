from flask import Blueprint, abort, make_response, request, Response
from ..db import db
from app.models.cat import Cat
from .route_utilities import validate_model

# curl -X POST -H 'Content-Type: application/json' -d '{"name":"Felix","color":"black and white","personality":"wonderful"}' 'http://localhost:5000/cats' | json_pp

bp = Blueprint("cats_bp", __name__, url_prefix="/cats")

@bp.post("")
def create_cat():
    request_body = request.get_json()
    try: 
        new_cat = Cat.from_dict(request_body)
    except KeyError as e:
        response = {"message": f"Invalid Request: missing {e.args[0]}"}
        abort(make_response(response, 400))
    
    db.session.add(new_cat)
    db.session.commit()
    response = new_cat.to_dict()
    return response, 201

@bp.get("")
def get_all_cats():

    query = db.select(Cat)

    name_param = request.args.get("name")
    if name_param:
        query = query.where(Cat.name == name_param)

    color_param = request.args.get("color")
    if color_param:
        query = query.where(Cat.color.ilike(f"%{color_param}%"))

    personality_param = request.args.get("personality")
    if personality_param:
        query = query.where(Cat.personality.ilike(f"%{personality_param}%"))

    query = query.order_by(Cat.id)

    cats = db.session.scalars(query)

    cats_response = [cat.to_dict() for cat in cats]
    return cats_response

@bp.get("/<cat_id>")
def get_single_cat(cat_id):
    cat = validate_model(Cat, cat_id)

    return cat.to_dict()

@bp.put("/<cat_id>")
def update_cat(cat_id):
    cat = validate_model(Cat, cat_id)
    request_body = request.get_json()

    cat.name = request_body["name"]
    cat.personality = request_body["personality"]
    cat.color = request_body["color"]

    db.session.commit()

    return Response(status=204, mimetype="application/json")

@bp.delete("/<cat_id>")
def delete_cat(cat_id):
    cat = validate_model(Cat, cat_id)

    db.session.delete(cat)
    db.session.commit()

    return Response(status=204, mimetype="application/json")
