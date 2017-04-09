from wtforms import Form, BooleanField, TextField, PasswordField, validators
from wtforms.ext.appengine.db import model_form

from app.core.models import db, Post

MyForm = model_form(Post, Form, exclude=('title', 'slug', 'tags', 'category', 'body', ))
