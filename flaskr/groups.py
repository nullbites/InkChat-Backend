import functools
import json

from flaskr import db
from flask import Blueprint, request
from flaskr.utils.responses import response

bp = Blueprint('groups', __name__, url_prefix='/groups')

@bp.route('all', methods=['GET'])
def get_all_groups():
	return db.get_all_groups()

@bp.route('', methods=['POST'])
def create_group():
	if 'name' in request.args:
		name = request.args['name']
		return db.create_group(name)
	return response(
		400,
		"name: name of group being created"
	)

@bp.route('', methods=['GET'])
def get_groupo():
	if 'name' in request.args:
		name = request.args['name']
		return db.get_group(name)
	return response(400, "name: name of requested group")
