

# Raspberry Pi Time Sync

This app will allow you to sync time between a single Raspberry Pi and multiple Linux devices using crontab at set intervals

## Server Setup

Bellow we will install the server side flask script that will be the endpoint for computers requesting the date and time. We will use the crontab to run the flask app at startup.

- Copy serverApp.py and serverApp.sh to the root directory of your Raspberry Pi

- Edit your crontab by "entering crontab -e" and choosing nano as your editor. Enter the following to the end of the file.

  - ```
    @reboot sleep 30 && /home/pi/serverApp.sh
    ```

- Hit 'CTRL + O' and then 'CTRL+X' to save and exit 
- Enter "sudo chmod a+x "serverApp.sh" to set permissions for the shell script
- Reboot the Pi
- Once booted you can use 'ifconfig' in the terminal to see your IP Address
- We can test the time server by opening up a browser on another computer on the same network and enter the server's address followed by ':5000', the server should return the current date and time 

## Client Setup

Now we can setup the client side to request and sync the date and time from the server. We will set the crontab to sync up the time at reboot and every 30 minutes. 

- Copy timeSync.py  and timeSycn.sh to the root directory of your Raspberry Pi

- We need to edit the sudo version of crontab to apply date and time changes by "entering sudo crontab -e" and choosing nano as the editor. Enter the following to the end of the file.

  - ```
    @reboot sleep 30 && /home/pi/timeSync.sh
    30 * * * * /home/pi/timeSync.sh
    ```

- Hit 'CTRL + O' and then 'CTRL+X' to save and exit 
-  Enter "sudo chmod a+x "timeSync.sh" to set permissions for the shell script.
- Reboot your Pi and use "date" to check the time and date, it should now be synced up with the server Pi. 