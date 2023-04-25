from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.controllers import 

location_views = Blueprint('location_views', __name__, template_folder='../templates')