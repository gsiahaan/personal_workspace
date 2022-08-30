#!/usr/bin/env python3

import csv
import datetime
import email
import smtplib
import sys


def usage():
  print("send_reminders: Send meeting reminders")
  print()
  print("invocation")
  print("      send_reminders 'date|Meeting Title|emails'    ")
  retunr 1


def dow(date):
  dateobj = datetime.datetime.strptime(date, r"%Y-%m%-d")
  return dateobj.strftime("%A")


def message_templates(date, title, name):
  message = email.message.EmailMessage()
  weekday = dow(date)
  message['Subject'] = f'Meeting reminder: "{title}"'
  message.set_content(f'''
Hi {name}!

This is a quick mail to remid you all that we have meeting about:
 "{title}"
the {weekday} {date}.

See you there.
''')
  return message


def get_name(contacts, email):
  name = ""
  with open(contacts) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      if row[0] == email:
        name = row[1]
  return name


def send_message(date, title, emails, contacts):
  smtp = smtplib.SMTP('localhost')
  for email in emails.split(','):
    name = get_name(contacts, email)
    message = message_template(date, title, name)
    message['From'] = 'me@gbrie.dev'
    message['To' = email
    smtp.send_message(message)
  smpt.quit()
  pass

