# weather

This app illutrates the use of a weather API provided by openweathermap.org.
Given a city, the app calls the API to retrieve the current temperature in the 
city.  This is displayed in the browser.

1. To use the API, you must request an API key.  Go to https://openweathermap.org/price
and request a key under the free tier.  The API key will be emailed to you.  It's a 
long string of characters.   Hold on to that.  

2. Now clone the repo to your VM.  In the home directory on the VM type:
git clone https://github.com/csc330/weather.git

3. This creates a directory called weather.  Go into it by typing: cd weather

4. Now edit main.py using micro (micro main.py).  Modify line 11 to include your API 
key in the appropriate place. 

5. Install the module requests. In a terminal window, type: sudo pip3 install requests

6. Now you're ready to run the app:  flask run

7. In the address bar of a browser, type the following URL to retrieve the current 
temperature in London:

http://VM_External_IP_Address:8080/temperature/London

The current temperature in London should display in the browser.  
