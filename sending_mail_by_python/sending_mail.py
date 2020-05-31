from mailer import Mailer, Message
import smtplib



def build_email(from_address, to_address, subject, content): #attach_rpt, attach_pdf,
    #                    img_path):
    message = Message()

    message.From = from_address
    message.To = to_address
    # message.CC = cc
    #     message.charset = "utf-8"

    message.Subject = subject
    message.Body = content
    #     message.attach(attach_rpt, mimetype='text/csv', charset='utf-8')
    #     message.attach(attach_pdf, mimetype="application/pdf")
    #     message.attach(img_path, cid='image_cid')

    print('message type:', message)
    print('message\n:', message)

    return message

#     sender = Mailer(smtplib.SMTP(host='127.0.0.1', port=25, local_hostname="smtp.mydomain.com"))
#     sender.send(message)


def send_email(msg, host, port):
    s = smtplib.SMTP(host, port, local_hostname="smtp.mydomain.com")
    # s = smtplib.SMTP(host='127.0.0.1', port=25, local_hostname="smtp.mydomain.com")
    #     result = s.sendmail(msg["From"], msg["To"].split(","), msg.as_string())
    result = s.sendmail(msg.From, msg.To, msg.as_string())
    s.quit()

    return result