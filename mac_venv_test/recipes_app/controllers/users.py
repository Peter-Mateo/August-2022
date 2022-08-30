from flask import Flask, render_template, redirect, session, request
from recipes_app import app

@app.route('/')
def index():
    return 'Hello, world!'