#Now, we know the basics of webpages and servers.
#Now, we're going to build our own website portfolio

#I will follow along with the 'Hyperspace' html template found here: https://html5up.net/
#I have unzipped the files. I am moving all the html files into 'templates' and moving the js, css and jpg files into the 'static' file
#We have to ensure all the references to file in the html files have a modified file location to ensure they are referecing the
#correct location.
#After modifying the html documents a bit, it appears that all functionality has been achieved

# from flask import Flask, render_template, url_for
# app = Flask(__name__)

# @app.route("/")
# def my_home():
#     return render_template('index.html') #Just testing our index doc

# @app.route("/generic.html")
# def generic():
#     return render_template('generic.html')

# @app.route("/elements.html")
# def elements():
#     return render_template('elements.html')

# if __name__ == "__main__":
#     app.run()

#For each of the template documents we have, we are manually creating new app.route blocks of code. Perhaps we can make a function?
#We want them to dynamically accept a page name. So, we will use the <>

# from flask import Flask, render_template, url_for
# app = Flask(__name__)

# @app.route("/")
# def my_home():
#     return render_template('index.html')

# @app.route("/<string:page_name>")
# def html_page(page_name):
#     return render_template(page_name) #This works somehow and there doesn't appear to be any bugs

# if __name__ == "__main__":
#     app.run()

#Next, we are going to explore the contact data such that we can actually receive data in the back-end. 
#We will make a new route

# from flask import Flask, render_template, url_for
# app = Flask(__name__)

# @app.route("/")
# def my_home():
#     return render_template('index.html')

# @app.route("/<string:page_name>")
# def html_page(page_name):
#     return render_template(page_name)

# #For the below to work, I've added 'submit_form' in the 'action' command in the index.html document (with a method of 'post'). This is
# #found when searching for 'Send Message', as seen on the main page of the html template.

# #For the server to be able to read the data, we have to also give variable names for the inputs for email, text and textarea.
# #They have already been named as "name", "email" and "message".

# #To check that the server is reading it, we go to inspect elements > network > submit_form > Payload field. Our message
# #should actually appear there.

# @app.route('/submit_form', methods = ['POST','GET'])
# def submit_form():
#     return 'The form has been Submitted!'

# #^This works!

# if __name__ == "__main__":
#     app.run()

#Now, we can access these values using request.form. We will alter our submit_form block:

# from flask import Flask, render_template, url_for, request
# app = Flask(__name__)

# @app.route("/")
# def my_home():
#     return render_template('index.html')

# @app.route("/<string:page_name>")
# def html_page(page_name):
#     if page_name == 'favicon.ico':
#         return "" #These two lines are to stop errors occuring when accessing the /submit_form pages
#     return render_template(page_name)

# @app.route('/submit_form', methods = ['POST','GET'])
# def submit_form():
#     if request.method == 'POST':
#         data = request.form.to_dict()
#         print(data)
#         return "Form submitted!"
#     else:
#         return "Error. Try again."

# if __name__ == "__main__":
#     app.run()

#Lastly, we want to give a thank you message when the information is submitted.

#First, we duplicate the html doc that takes the information. In this case, that's index. We'll call it thankyou.html
#So, we will replace the block of code within the 'form' method that's found in index and instead replace it with a
#thank you. We will then redirect them to this page from the index page. We will import the 'redirect' module

# from flask import Flask, render_template, url_for, request, redirect
# app = Flask(__name__)

# @app.route("/")
# def my_home():
#     return render_template('index.html')

# @app.route("/<string:page_name>")
# def html_page(page_name):
#     if page_name == 'favicon.ico':
#         return "" 
#     return render_template(page_name)

# @app.route('/submit_form', methods = ['POST','GET'])
# def submit_form():
#     if request.method == 'POST':
#         data = request.form.to_dict()
#         print(data)
#         return redirect("/thankyou.html")
#     else:
#         return "Error. Try again." #this displays the message in thankyou.html (but you do have to scroll down)

# if __name__ == "__main__":
#     app.run()

#One issue with this is that our field data is stored on the server but isn't stored locally - data is lost if the server goes down
#We will store it on 'database.txt'

# from flask import Flask, render_template, url_for, request, redirect
# app = Flask(__name__)

# @app.route("/")
# def my_home():
#     return render_template('index.html')

# @app.route("/<string:page_name>")
# def html_page(page_name):
#     if page_name == 'favicon.ico':
#         return "" 
#     return render_template(page_name)

# def write_to_file(data):
#     with open('Building_a_Portfolio/database.txt', mode='a') as database:
#         name = data['name']
#         email = data['email']
#         message= data['message']
#         file = database.write(f"\n{name},{email},{message}")

# @app.route('/submit_form', methods = ['POST','GET'])
# def submit_form():
#     if request.method == 'POST':
#         data = request.form.to_dict()
#         write_to_file(data)
#         return redirect("/thankyou.html")
#     else:
#         return "Error. Try again." 

# if __name__ == "__main__":
#     app.run()

#Now, we want to write csv files rather than text documents

# from flask import Flask, render_template, url_for, request, redirect
# import csv

# app = Flask(__name__)

# @app.route("/")
# def my_home():
#     return render_template('index.html')

# @app.route("/<string:page_name>")
# def html_page(page_name):
#     if page_name == 'favicon.ico':
#         return "" 
#     return render_template(page_name)

# def write_to_file(data):
#     with open('Building_a_Portfolio/database.txt', mode='a') as database:
#         name = data['name']
#         email = data['email']
#         message= data['message']
#         file = database.write(f"\n{name},{email},{message}")

# def write_to_csv(data):
#     with open('Building_a_Portfolio/database.csv', newline ='', mode='a') as database2:
#         name = data['name']
#         email = data['email']
#         message= data['message']
#         csv_writer = csv.writer(database2, delimiter = ",", quotechar="'", quoting = csv.QUOTE_MINIMAL)
#         csv_writer.writerow([name,email,message])

# @app.route('/submit_form', methods = ['POST','GET'])
# def submit_form():
#     if request.method == 'POST':
#         try:
#             data = request.form.to_dict()
#             # write_to_file(data)
#             write_to_csv(data)
#             return redirect("/thankyou.html")
#         except:
#             return "Did not save to the database."
#     else:
#         return "Error. Try again." 

# if __name__ == "__main__":
#     app.run()

#Databases exist for ous to store data that 'persists' - i.e as long as we need it. With web development, there is the front-end
#which deals with the css, javascript and html. The backend is the server-side of things. We also have the database in the back-end
#as well. E.g we can store it on an actual database like MongoDB.

#Now, our address is the local host (with 127.0.0.1) but we want this to be accessible to the internet
#We want to deploy this. We will use pythonanywhere.com (with a free server). 
#We have to upload the files for this via GitHub.
#We create a repository and clone it with HTTPS.
#In the python command line, we put 'pip freeze > requirements.txt' to take a snapshot of all the required modules for the 
#code to work

from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    if page_name == 'favicon.ico':
        return "" 
    return render_template(page_name)

def write_to_file(data):
    with open('Building_a_Portfolio/database.txt', mode='a') as database:
        name = data['name']
        email = data['email']
        message= data['message']
        file = database.write(f"\n{name},{email},{message}")

def write_to_csv(data):
    with open('Building_a_Portfolio/database.csv', newline ='', mode='a') as database2:
        name = data['name']
        email = data['email']
        message= data['message']
        csv_writer = csv.writer(database2, delimiter = ",", quotechar="'", quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])

@app.route('/submit_form', methods = ['POST','GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return redirect("/thankyou.html")
        except:
            return "Did not save to the database."
    else:
        return "Error. Try again." 

if __name__ == "__main__":
    app.run() #Fuckin bullshit with github repositories I don't understand - I'm just going to upload the files

    