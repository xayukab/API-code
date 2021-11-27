from flask import Flask, request
from service import AppService
import json

app = Flask(__name__)
appService = AppService();


@app.route('/')
def home():
    return "App Works!!!"


@app.route('/info')
def tasks():
    return appService.get_tasks()

