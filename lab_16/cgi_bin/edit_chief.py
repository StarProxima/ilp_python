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

id = form.getfirst("ChiefId")
fio = form.getfirst("FIO")
work_experience = form.getfirst("WorkExperience")

if (id is not None) and (fio is not None) and (work_experience is not None):
    if work_experience.isdigit():
        db.edit_chief(id, fio, work_experience)
        id = None
        fio = None
        work_experience = None
        msg = '''
            <br>
            <div class="card">
                <div class="card-body">
                    Success editing
                </div>
            </div>
        '''
    else:
        msg = '''
            <br>
            <div class="card">
                <div class="card-body">
                    WorkExperience should be a number
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
                <form method="PUT">
                    <label class="form-label" for="ChiefId">ChiefId</label>
                    <input class="form-control" type="text" name="ChiefId" required>
                    <br>
                    <label class="form-label" for="FIO">FIO</label>
                    <input class="form-control" type="text" name="FIO" required>
                    <br>
                    <label class="form-label" for="WorkExperience">WorkExperience</label>
                    <input class="form-control" type="text" name="WorkExperience" required>
                    <br>
                    <input type="submit" class="btn btn-primary" value="Edit">
                </form>
                {msg}
        </body>
    </html>
'''


print("Content-Type: text/html\n")
print(template.format(msg=msg))
