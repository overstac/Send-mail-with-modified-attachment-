import yagmail
import os
import pandas


sender= "pintilei92@gmail.com"
subject= "This is the subject!"

df = pandas.read_csv("contacts.csv")

yag= yagmail.SMTP(user= sender, password=os.environ['PASS'])

def generate_file(filename, content):
  with open (filename, "w") as file:
    file.write(str(content))
  

for index, row in df.iterrows():
  receiver_mail= row["email"]
  name= row["name"]
  filename= name + ".txt"
  amount= row["amount"]
  generate_file(filename, amount)
  contents= [f"Hey, {name} you have to pay {amount} dolars! Bill is attached!", filename]
  yag.send(to= receiver_mail, subject= subject, contents= contents)
  print("Email sent!")    
