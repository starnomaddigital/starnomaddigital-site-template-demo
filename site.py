import os
import glob
import shutil
import json
from jinja2 import Environment, FileSystemLoader

with open("site.json", 'r') as fin:
    site_config = json.load(fin)

if not os.path.exists("dist"):
    os.makedirs("dist")
if not os.path.exists(os.path.join("dist", "images")):
    os.makedirs("dist/images")
for filename in glob.glob(os.path.join("images", "*png")):
    shutil.copy2(filename, os.path.join("dist", "images"))

env = Environment(loader=FileSystemLoader([
    ".",
    "./site-templates/",
    "./jinja-components/"
]))

t = env.get_template("index.jinja")
with open(os.path.join("dist", "index.html"), 'w') as fout:
    fout.write(t.render(**site_config))

t = env.get_template("about.jinja")
with open(os.path.join("dist", "about.html"), 'w') as fout:
    fout.write(t.render(**site_config))

t = env.get_template("services.jinja")
with open(os.path.join("dist", "services.html"), 'w') as fout:
    fout.write(t.render(**site_config))

t = env.get_template("portfolio.jinja")
with open(os.path.join("dist", "portfolio.html"), 'w') as fout:
    fout.write(t.render(**site_config))
