# coding=utf-8

from flask import Blueprint, render_template, url_for, request, jsonify
# from .scripts.lesson import get_lesson_urls
from .scripts.lesson import get_urls


bp = Blueprint('lesson', __name__)

@bp.route('/', methods=('GET',))
def index():
    return render_template('index.html')


@bp.route('/lessonUrls', methods=('POST',))
def get_video_urls():
    if request.method == 'POST':
        lesson_key = request.form['key']
        # urls = get_lesson_urls(lesson_key)
        urls = get_urls(lesson_key)
        return jsonify(urls)