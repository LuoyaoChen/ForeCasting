# Insurance Database Application

## 1. Introduction
We built a database web application using Flask and Python. The back-end database is stored in Azure Database. A machine learning model that predicts clients' risk level and their corresponding price is also integrated in this application.
Through this application, user can achieve multiple goals: 

        1) View the tables in the database
        2) Insert new data to the tables
        3) Update existing records in the tables
        4) Delete existing records in the tables
        5) Fill in personal information and get an estimated price for the insurance quote

### 1.1 Demo video: Table Insert, Update, Delete
<video src="Demo_videos/demo_table_operations.mov" controls="controls" style="max-width: 730px;">
</video>

### 1.2 Demo video: Use Machine Learning to Get Estimated Quote Price
<video src="Demo_videos/demo_ml.mov" controls="controls" style="max-width: 730px;">
</video>

## 2. Application Reference Architecture
<p align="center">
  <img src="Figures/reference_architecture.jpg" title="Business Reference Architecture"/>
</p>

## 3. Database Design
#### 3.1 Database Structure
<p align="center">
  <img src="Figures/database_structure.jpeg" title = "Database Structure"/>
</p>

#### 3.2 Database Logical Schema 
<p align="center">
  <img src="Figures/logical_schema.png" title = "Logical Schema of the Database"/>
</p>

## 4. How to run the web app
0. PreReq:git-lfs (install for mac):

        wget https://github.com/git-lfs/git-lfs/releases/download/v3.3.0/git-lfs-darwin-amd64-v3.3.0.zip
        unzip git-lfs-darwin-amd64-v3.3.0.zip
        cd ../../git-lfs-3.3.0/
        bash install.sh
1. git clone this repo
2. cd into this dir on your local computer
3. run (for macOS users):

        export FLASK_APP=app 
        export FLASK_ENV=development
        flask run

   run (for Windows users):

        set FLASK_APP=app 
        set FLASK_ENV=development
        flask run
4. access the homepage. 

   To view and modify tables, these steps:

        1.click the table name we want to view and/or modify
        2.access the table webpage
        3.select the operation: insert, update, or delete
        4.fill in the data we want to modify
        5.click inset/update/delete

   To get personalized insurance quote:

        1. fill in the personal information on the page
        2. click submit
        3. access the estimate_price page and view the predicted insurance quote.
 
## Reference
1. [Connect MS Azure with Python](https://learn.microsoft.com/en-us/azure/mysql/single-server/connect-python)
2. [Get all table names from MS Azure using python](https://stackoverflow.com/questions/3556305/how-to-retrieve-table-names-in-a-mysql-database-with-python-and-mysqldb)
3. [How to link two forms](https://stackoverflow.com/questions/18290142/multiple-forms-in-a-single-page-using-flask-and-wtforms) 
4. [Display Table with Headers and Contents](https://blog.miguelgrinberg.com/post/beautiful-interactive-tables-for-your-flask-templates)
     