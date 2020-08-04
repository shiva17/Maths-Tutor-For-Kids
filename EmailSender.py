# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 02:26:00 2020

@author: kolhe
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def emailsender(name, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
    html = """\
    <html>
    <head>
    
    </head>
    <body>
    
    <h2>{} Test Results</h2>
    
    <h3>Incorrect Answers</h3>
    <table>
      <tr>
        <th>No.</th>
        <th>Question</th>
      </tr>
      <tr>
        <td>1</td>
        <td>{}</td>
      </tr>
      <tr>
        <td>2</td>
        <td>{}</td>
      </tr>
      <tr>
        <td>3</td>
        <td>{}</td>
      </tr>
      <tr>
        <td>4</td>
        <td>{}</td>
      </tr>
      <tr>
        <td>5</td>
        <td>{}</td>
      </tr>
      <tr>
        <td>6</td>
        <td>{}</td>
      </tr>
      <tr>
        <td>7</td>
        <td>{}</td>
      </tr>
      <tr>
        <td>8</td>
        <td>{}</td>
      </tr>
      <tr>
        <td>9</td>
        <td>{}</td>
      </tr>
      <tr>
        <td>10</td>
        <td>{}</td>
      </tr>
    </table>
    
    <br><br>
    
    </body>
    </html>
    """.format(name, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10)
    
    
    # senders address
    fromaddr = "kolhe.shivam1997@gmail.com"
    
    # receivers address
    toaddr = "kolhe.shivam1997@gmail.com"
    
    # Create a multipart message and set headers
    msg = MIMEMultipart()
    
    # senders address
    msg['From'] = fromaddr 
    # receivers address
    msg['To'] = toaddr
    # subject of the email
    msg['Subject'] = "{} Test Scores".format(name)
    
    part1 = MIMEText(html, 'html')
    msg.attach(part1)
    
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login(fromaddr, "jumboshree@1997")
    
    # convert message to string
    text = msg.as_string()
    
    s.sendmail(fromaddr, toaddr, text)
    s.quit()