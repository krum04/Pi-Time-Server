# Raspberry Pi Time Sync

This app will allow you to sync time between a single Raspberry Pi and multiple linux devices using crontab at set intervals

## Server Setup

Bellow we will install the server side flask script that will be the endpoint for computers requesting the date and time. We will use the crontab feature to have our script startup at boot.

- Copy serverApp.py and serverApp.sh to the root directory of your Raspberry Pi

- Edit your crontab by "entering crontab -e" and choosing nano as your editor. Enter the following to the end of the file.

- ```@Reboot 
  @reboot sleep 30 && /home/pi/serverApp.sh
  ```

- Hit 'CTRL + O' and then 'CTRL+X' to save and exit from nano

- run the following command to set the permissions for the bash script "sudo chmod a+x "serverApp.sh""

- Reboot the Pi

- Once booted you can use 'ifconfig' in the terminal to see your IP Address

- We can test your time server by opening up a browser on another computer on the same network and enter the server's address followed by ':5000', the server should return the current date and time 

  