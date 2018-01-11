# smeetv

`smeetv` was a hastly written script from 2016 for digital slideshows on a recycled laptop screen using a Raspberry Zero. Below was notes on how to set the scripts to run during the Raspi's power up.


#### How to run python script on StartX boot
Make file executable:  
    `chmod +x run_smeetv.py`\
Open one of three different spots where code should be written:
    `sudo nano ~/.config/lxsession/LXDE-pi/autostart`\
Add to the end of the file:
    `@sudo python /home/pi/run_smeetv.py`

#### How to kill processes
Check running programs
    `ps axg`\
Find its process ID
    `ps -9 ID`    (9 for example)\
    `sudo kill -9 ID`\
    `sudo startx`