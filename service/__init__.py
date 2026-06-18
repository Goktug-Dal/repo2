from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

app = Flask(__name__)

# Security headers with Talisman
Talisman(app)

# Enable CORS
CORS(app)

from service import routes
