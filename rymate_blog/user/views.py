# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask.ext.login import login_required

blueprint = Blueprint("user", __name__, url_prefix='/admin',
                        static_folder="../static")


@blueprint.route("/new_post")
@login_required
def new_post():
    return render_template("users/new_post.html")
  
@blueprint.route("/")
@login_required
def admin_home():
    return render_template("users/home.html")