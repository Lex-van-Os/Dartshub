# modules for the rest api classes, model is imported to make connection with the sqlite tables and databases
from config import db
from sqlalchemy import exc
from flask_restful import Resource, reqparse