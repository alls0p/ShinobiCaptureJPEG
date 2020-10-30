import urllib.request
import os

def file_name_counter():
  counter = 0
  filename = (input("put the path to the directory where you would like to store the jpeg files ") + '/' + input("what is the name of the camera? ")+ '{}' + '.jpeg') 
      counter += 1
  filename = filename.format(counter)
  return filename

filename = file_name_counter()
def grab_jpeg():
  imgURL = input("Enter your jpeg api url EG <http://shinobiIP:8080/apiKey/jpeg/apiuser/CameraID/s.jpg> ")
  urllib.request.urlretrieve(imgURL, filename)
  print(filename)
  sleep(100)
  
grab_jpeg()


# working currently out of directory that .py file is in
""" todo:
      - clean up files after x number of files exist
      - Create user input for both output file path and name, maybe camera name? - DONE
      - change api url to user input, but find a way to make the variable persistent 
      - save filename variable to memory


"""