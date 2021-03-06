#!/usr/bin/env python

from seesaw.externalprocess import *
from seesaw.pipeline import *
from seesaw.project import *

if downloader:
    username = downloader
else:
    username = "warrior"

pipeline = Pipeline(
    ExternalProcess("TinyBack", ["./run.py",
        "--tracker=http://tracker.tinyarchive.org/v1/",
        "--sleep=60",
        "--one-task",
        "--temp-dir=./data",
        "--username", username
        ])
)

project = Project(
    title = "URLTeam",
    project_html = """
    <h2>URLTeam <span class="links"><a href="http://urlte.am/">Website</a></span></h2>
    <p>The URLTeam is a project to preserve shorturls from various URL shorteners.</p>
    """
)
