import os
import csv

udemy_csv = os.path.join(".." , "web_starter.csv")

#lsits to store data
title = []
price = []
Subscribers = []
Reviews = []
Review_percent = []
Length = []



#with open (udemy_csv, newline='',encoding='utf-8') as csvfile 
with open (udemy_csv, newline='',encoding="utf-8") as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",") 
    #print (csvreader)
    for row in csvreader: 
        #add title 
        title.append(row[1])

        #add price 
        price.append(row[4])

        #add subscribers 
        Subscribers.append(row[5])

        #add reviews 
        Reviews.append(row[6])

        #detern=mine % of review left to decimal places 
        percent = round (int(row[6])/ int(row[5]), 2)
        Review_percent.append(percent)


        #get length of the course to just a nummber 
        new_length = row[9].split(" ")
        Length.append(float(new_length[0]))

 #zip lists together 
cleaned_csv = zip(title,price, Subscribers, Reviews, Review_percent, Length)
#set variable for output file 
output_file = os.path.join("web_Final.csv")
#open the output file 
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    #write the header row
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left", "Percet of Reviews", "Length of Course"])

    #write in zipped rows
    writer.writerows(cleaned_csv) 

    

 






