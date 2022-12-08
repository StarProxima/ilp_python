import db
import cgi
import sys
import os
import inspect
import xml.etree.ElementTree as ET
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


msg = ''

form = cgi.FieldStorage()

name = form.getfirst("Name")
location = form.getfirst("Location")

if (name is not None) and (location is not None):
    db.add_post(name, location)
    name = None
    location = None
    msg = '''
        <br>
        <div class="card">
            <div class="card-body">
                Success adding
            </div>
        </div>
    '''

template = '''
    <!DOCTYPE html>
    <html lang="en-US">
        <head>
            <meta charset="UTF-8">
            <!-- CSS only -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
            <!-- JavaScript Bundle with Popper -->
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
        </head>
        <body>
            <a href="/" class="button">Home page</a>
            <br>
            <br>
            <h1>Add chief</h1>
            <div class="ps-4 pe-4">
                <form method="GET">
                    <label class="form-label" for="Name">Name</label>
                    <input class="form-control" type="text" name="Name" required>
                    <br>
                    <label class="form-label" for="Location">Location</label>
                    <input class="form-control" type="text" name="Location" required>
                    <br>
                    <input type="submit" class="btn btn-primary" value="Add">
                </form>
                {msg}
        </body>
    </html>
'''


print("Content-Type: text/html\n")
print(template.format(msg=msg))
