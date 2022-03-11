log_file = open("um-server-01.txt")   # this python's way of importing the .txt file and
                                    # assigning it to a variable 


def sales_reports(log_file):     #this is a fuction that takes a file as an argument
    for line in log_file: 
                                  #this is a loop that loops over each line in the file
        line = line.rstrip()         #this is assigning each line to line that removes the trailing characters 
        day = line[0:3]             #the [:] is similar to slice in js where it starts at index 0 stops at index 3
                                    #it creates a new varible that stores index 0,1,2 
    #    if day == "Tue":           #this is a if statement conditonal checking if the day is "Tue"
    #        print(line)            #this is similar to js console.log(line)
        if day == 'Mon':
            print(line);




def printTen(log_file):
    for line in log_file:
        line = line.rstrip()
        num = line[15:17]

        if num > 10:
            print(line)



printTen(log_file)

sales_reports(log_file)   #the function is being called with the file 
