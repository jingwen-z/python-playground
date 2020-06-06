from mailer import Mailer, Message
import smtplib
import smtpd


def build_email(from_address, to_address, subject, content,
                attach_rpt=None):
    message = Message()

    message.From = from_address
    message.To = to_address
    # message.CC = cc
    # message.charset = "utf-8"

    message.Subject = subject
    message.Body = content
    if attach_rpt != None:
        message.attach(attach_rpt, mimetype='text/csv',
                       charset='us-ascii')
    # message.attach(attach_pdf, mimetype="application/pdf")
    # message.attach(img_path, cid='image_cid')

    print('message:', message)

    return message


def send_email(msg, host='', port=0):
    s = smtplib.SMTP(host=host, port=port, local_hostname="smtp.mydomain.com")
    result = s.sendmail(msg.From, msg.To, msg.as_string())
    s.quit()

    return result
