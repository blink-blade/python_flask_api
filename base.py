
import requests
from flask import Flask, jsonify, request, render_template
from db import db_session, User

app = Flask(__name__)