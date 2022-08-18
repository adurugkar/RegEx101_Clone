
import re
from unittest import result
from flask import Flask, render_template, request

#create the object
app = Flask(__name__)

#Define the Routes and bind it with a function
@app.route('/', methods = ['GET', 'POST'])
def regex101():
    if request.method=='POST':
        xprsn = request.form['xpn']
        tststrng = request.form['tst']
        cnt = 0
        if (len(xprsn)==0 or len(tststrng)==0):
            cnt = -1
            return render_template("regex.html", result = "Pleace provid input", count = cnt)
        else:
            lst = []
            for match in re.finditer(r'{}'.format(xprsn), tststrng):
                stn = ''
                cnt = +1
                stn = stn+"match {} \"{}\" at start and end indices[{}, {}]".format(cnt, match.group(), match.start(),match.end())
                lst.append(stn)
            return render_template("regex.html" ,result ="Matches found", xpn=xprsn, tst=tststrng, lsts=lst, count=cnt)

    return render_template("regex.html", count=-1)


if __name__ == '__main__':
    app.run(debug=True)