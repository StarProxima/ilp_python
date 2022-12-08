
import sys
import os
import inspect

import db

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))

parentdir = os.path.dirname(currentdir)

sys.path.insert(0, parentdir)

items = db.get_all_remarks_joined()

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
            <h1>Remarks:</h1>
            <a class="h3 link-primary" href="/">Go back</a>
            <br>
            <table class="table w-100 mx-4">
                <tr>
                    <th>RemarkID</th>
                    <th>Guard</th>
                    <th>Post</th>   
                    <th>Chief</th> 
                    <th>Remark</th>                  
                </tr>
                {rows_html}
            </table>
        </body>
    </html>
'''

rows_html = ""
for item in items:
    rows_html += "<tr>"
    for i in range(0, len(item)):
        rows_html += f"<td>{item[i]}</td>"
    rows_html += "</tr>"

print("Content-Type: text/html\n")
print(template.format(rows_html=rows_html))