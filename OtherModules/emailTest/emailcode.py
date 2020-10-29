import mysql.connector
import smtplib
from collections import defaultdict
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="admin1234",
    database="wdrDb"

)

mycursor = mydb.cursor()
mycursor.execute(
    "SELECT d.id,d.Problem, d.valueid, s.StationName, d.outvalue,d.when_reported    FROM DetectedAnalyzerProblems d join stations s on s.station_id=d.stationId WHERE d.emailed <4 ")
gather = defaultdict(list)
for w, x, y, z, p,o in mycursor.fetchall():
    gather[z].append((w, x, y, p,o))

    mycursor.execute("UPDATE  DetectedAnalyzerProblems SET emailed =emailed+1  where id ={}".format(w))
    mydb.commit()





def send_mail(email):
    for k, v in gather.items():
        # print(k)
        # print(v)
        # # print(email)

        msg = MIMEMultipart()

        msg['From'] = 'mickeygerman1@gmail.com'
        msg['To'] = email
        msg['Subject'] = 'Problem on Station:' + k

        text = """Hello,The AWS has reported %s Problems on Station %s""" % (len(v), k)
        html = """\
            <html>
             <head>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

            <!-- Bootstrap CSS -->

          </head>
              <body>
              <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">


                <table class="table table-bordered" border="1">

                  <thead class="thead-dark">
                    <tr>
                      <th scope="col">id</th>
                      <th scope="col">Problem</th>
                      <th scope="col">Valueid</th>
                      <th scope="col">outvalue</th>
                      <th scope="col">when_reported</th>
                    </tr>
                  </thead>
                  <tbody>""" + "".join(
            ["<tr><th>{0}</th><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td</tr>".format(*a) for a in v]) + """</tbody></table>
                  </body></html>"""
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        msg.attach(part1)
        msg.attach(part2)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('mickeygerman1@gmail.com', 'mickeygerman1')
        server.sendmail('mickeygerman1@gmail.com', email, msg.as_string())


mycursor.execute("SELECT email  FROM users  WHERE emails='yes' ")
for x in mycursor.fetchall():
    send_mail(*x)

