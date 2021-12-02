import models
import geopandas
import geopy

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

from flask_login import current_user

favoriteplaces = Blueprint('favoriteplaces', 'favoriteplaces')

@favoriteplaces.route('/', methods=['POST'])
def create_favoriteplace():
    payload = request.get_json()
    print(payload)
    new_place = models.Favorite.create(username=current_user, city=payload['city'], country=payload['country'], type=payload['type'], latitude=payload['latitude'], longitude=payload['longitude'])
    
    print(new_place) 
    
    place_dict = model_to_dict(new_place)
    return jsonify(
        data = place_dict,
        message = "Successfully created a new favorite place",
        status = 201
    ), 201
    
@favoriteplaces.route('/<id>', methods=['GET'])
def get_one_place(id):
    place = models.Favorite.get_by_id(id)
    print(place)
    return jsonify(
        data = model_to_dict(place),
        message = 'Success!',
        status = 200
    ), 200
    
@favoriteplaces.route('/<id>', methods=['PUT'])
def update_place(id):
    payload = request.get_json()
    models.Favorite.update(**payload).where(models.Favorite.id==id).execute()
    
    return jsonify(
        data = model_to_dict(models.Favorite.get_by_id(id)),
        message = 'Resource updated successfully',
        status = 200,
    ), 200
    
