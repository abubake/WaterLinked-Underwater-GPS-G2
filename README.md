# WaterLinked-Underwater-GPS-G2

Instructions on the set up and use of the Waterlinked Underwater GPS G2 with the antenna configuration with the GOPRO Hero 9 to create georeferenced Mosaics in ArcGIS.

Materials Needed:
* Lectron Pro 14.8V 5200 mAh Battery
* Outside location with clear view of the sky
* WaterLinked Topside Unit
* WaterLinked Antenna
* WaterLinked Locator U1
* GOPRO Pole (length dependent on application)
* GOPRO and Mountable underwater GOPRO Light
* GOPRO with waterproof housing
* GOPRO battery and microSD card
* MicroSD card reader
* Laptop Computer
* Smartphone with Compass app or actual compass
* Rubber or elastic band for simple mounting. If mounting on boat, use a more secure method

First we will set up the GPS itself, followed by the GOPRO, and then the data collection process. 

Here are an outline of the steps in the process:

### Section 1 GPS Setup 
* Power the Topside unit
* Connect to the GUI
* Power the locator
* Calibrate IMUs
* Deploy the antenna
* Connect the locator
* Edit configuration settings in GUI

### Section 2 GOPRO Setup
* GOPRO and light Setup
* Mounting the Light and GOPRO
* GOPRO Operation

### Section 3 Data Collection
* Setup Instructions
* Data Collection
* Data Processing

# Section 1 GPS Setup 

## Power the Topside unit

The topside unit (pictured below) can be powered several different ways. The easiest is to use a battery, as it is inside the case of the topside unit and safe from water.

<img>![image](https://user-images.githubusercontent.com/32299736/143919023-df2543e1-810c-4e54-bd45-dd4e761831b7.png)

Plug in the battery as pictured, and press the power button located on the side of the topside unit to start it up.

![image](https://user-images.githubusercontent.com/32299736/143944877-303ddeab-0130-4c38-a0e1-02a8fd911f2f.png)

## Connect to the GUI

The next step is to connect to the online GUI. To do this, you first need to connect to the Topside unit's Wi-Fi on your laptop. You should see it appear in your Wi-Fi options now that the unit is powered. The password is "waterlinked." Once you connect, you can now access the GUI. To do this, enter http://192.168.7.1/ in your browser. Chrome or Firefox are recommended, and it will not work with internet explorer.

## Power the Locator

We will now step away from the GUI briefly to connect our locator. The locator (pictured below) is what the antenna is finding the location of, and it will only function properly once underwater. The locator needs to connect to the topside unit, which may take a few minutes. 

![image](https://user-images.githubusercontent.com/32299736/143930380-c1398871-39fc-4b04-a3dd-ba8798872810.png)

To begin the connection process, screw the seal on the back of the locator until a green light comes on and begins to flash. Once the light becomes solid green a connection is established. While the back cap is off the locator, please take note of the number on that the little arrow is pointing to, as this indicates a configuration setting (the locator channel number) for our GUI. Set the locator aside while it is connecting and move on to the next step.

![image](https://user-images.githubusercontent.com/32299736/143945323-ff9bbda4-f663-443a-ad8d-8216d3e2a3ae.png)

## Calibrate IMUs

The topside unit requires some calibration. In the GUI, navigate to settings in the menu, which is on the left side of the screen. In settings, go ahead and set the locator type to Locator-U1 and the channel to the value you wrote down that was on the locator.

Now scroll down to "Topside Setup" and click "Onboard IMU calibration".

![image](https://user-images.githubusercontent.com/32299736/143930108-782ba48e-299e-4004-bb8c-2541f98cd6f3.png)

This will open a menu where you will follow the three steps provided to ensure your topside unit will function properly. This should be done each time the topside unit is moved to a new location.

## Deploy the antenna

Now connect the antenna cable to the topside unit connector labeled Reciever D1/Antenna. To connect make sure the three prongs of the connector are aligned properly, and once plugged in, twist the connector to the right to lock it in.

![image](https://user-images.githubusercontent.com/32299736/143932132-caec6259-e917-48bc-a509-d434b4d61c6c.png)

Now the antenna can be placed in the water. Mount in whatever way works for your situation. Zipties or elastic/ excercise bands work well, and have the benefit of not requiring permanent mounting. It is recommended to have the bottom of the antenna reach 1 meter below the surface for optimum measurements, although it will work at any depth.

## Connect the locator

Now the locator needs to be connected to whatever you will be tracking the location of. For our case, it is the GOPRO Hero 9 that we are tracking the location of as we record video. So, The locator needs to be mounted on a GOPRO pole near where the GOPRO will be mounted. I recommend for easy mounting using zipties and or elastic bands to ensure it stays connected. See image below for example.

![image](https://user-images.githubusercontent.com/32299736/143945390-177a552b-26db-450d-b898-5e442dc0139e.png)

## Edit configuration settings in GUI
  
Navigate to "baseline" in the GUI menu. You should see a screen like below. This is where you can adjust the range the system will work within. Limiting the range increases the accuracy.
  
![image](https://user-images.githubusercontent.com/32299736/143933524-5426c926-8ba4-4608-b4a5-234f58119d34.png)
  
Once the locator is placed underwater, your system should now work properly. A proper working system will display checkmarks for everything in the system status. If there is an issue, it will tell you what to do to resolve it.
  
![image](https://user-images.githubusercontent.com/32299736/143934420-a0e25a7c-ad77-4c3c-9af7-11d66cced993.png)
  
To see the GPS data, navigate to the diagnostic tab under menu. This will show the locator's position relative to the topside unit. 

![image](https://user-images.githubusercontent.com/32299736/143934436-eacccf6c-d4db-4362-a50a-1066b9209cb1.png)

You can also see this data graphically in 2D under the position tab of the menu.

# Section 2 GOPRO Setup

For the GOPRO for best clarity in murky conditions I experimentally determined an attachable "snorkeling filter" paired with an attached underwater light at full brightness to best enhance the clarity of the video. Second to this was the pairing of the light with no filter. The light iteself seemed to have the greatest effect on visibilty, enabling more of the lake bottom where testing was done to be seen, with greater clarity.
  
## GOPRO and light Setup

Next we will set up the GOPRO. For this project, the GOPRO Hero 9 was used, but should work with any other GOPRO. If a microSD card and or charged battery is not already inserted, insert one into the battery/MicroSD port located on the left side of the GOPRO. To open the port, pull down on the protruding piece of plastic until the door of the port pops open. Insert the MicroSD first, followed by the battery.
  
![image](https://user-images.githubusercontent.com/32299736/143936236-51ae6ada-8cc4-424d-8951-12d1cc54ec59.png)
  
The GOPRO can now be inserted to the waterproof casing, insert it and lock the top latch.
 
The light is mounted on the back of the GoPro, to turn it on simply press the button on top 3 times to get it to the brightest setting. TO shut it off, hold down the button.
  
## Mounting the Light and GOPRO
  
If not already mounted, place a GOPRO mount on the back part of the waterproof casing as shown below. This allows the underwater light to be mounted as shown.
  
![image](https://user-images.githubusercontent.com/32299736/143945508-34ffdc97-157d-4948-ab68-e6b2f32e32a8.png)

![image](https://user-images.githubusercontent.com/32299736/143945577-8d2a1162-7cb7-4a50-85d1-e62dced27816.png)

    
Now take the GOPRO and connect it to the GOPRO pole using a GOPRO screw as seen in the image with the light mounting. Align the holes of the top of the pole and the underwater casing so that the screw can fit through. Force the screw through until it reaches the other side, and then proceed to screw it in until tight by hand.
  
## GOPRO Operation
  
At this point you are set up but need to know how to properly record and access video you take. To power on the GOPRO, press and hold the button on the side (the power/select button) until a red light flashes. It is now on, and you should be able to see the what the camera sees via an screen on the back of the GOPRO. To set it to video mode, press and release the power button to switch between time lapse, video, and photo. We want to have it in video mode. Sometimes if left unused the GOPRO will go into power saving mode and shut off the LCD screen. To wake it up, simply press the power button.
  
To record video, press and release the button on the top of the top of the GOPRO. To stop recording, do the same. To power off, again press and hold the button on the side.
  
# Section 3 Data Collection
  
## Setup Instructions
 
To collect GPS data from the locator, setup the python file "tracking_gps.py" from this repository in your favorite code editor or IDE. The orignal version of this code is available at https://github.com/waterlinked/examples along with several other useful examples depending on your needs. I recommend using the IDE spyder to run the code. Once it starts running, it will begin recording datapoints from the locator, so when you are ready for it to stop recording press control-C on the keyboard. This will generate a .gpx (GPS data) file in whatever folder the program "tracking_gps.py" is located. This file contains the latitude, longititude, depth, and a timestamp for each datapoint.

Make sure the GUI is still running, as the code will only run when the GUI is active.

I recommend trying to start the GOPRO and the tracking_gps file at close to the same time, as this in benefical later in processing the data.
  
## Data Collection

For this step begin recording with the GOPRO as well as running the tracking_gps file, while moving the GOPRO through the water with the GOPRO aimed at the area you wish to make a georeferenced mosaic of. Once you have covered the full area you wish to mosaic, stop recording and stop the code from running.

  
## Data Processing
 
In this step we will take the video you recorded and extract 6 frames for each second of recording, each of which will be compiled into a folder with a time stamp in the name of each, in the jpeg format.

Remove the micro SD card from the goPro and insert it into your computer using a microSD to SD converter if needed. Create a folder named videos and a folder named save, moving the video you are using into the "videos" folder you created. Make sure you trim/ edit the video in some way or it will not work with the code. I just take a tiny ammount of time off the end of the video.

Next we will be making some changed to the python file "gopro_to_timestamped_frame.py".
Open the python file, and change the files paths of the variables "video_paths" and "save_dir" on lines 112 and 113 of the file to match the path to your "videos" and "save" folders (example below).

![image](https://user-images.githubusercontent.com/32299736/146601060-b0d028ed-1246-469e-8c9a-0122c3cba07f.png)

Next go to line 23 and begin filling out the information shown in the image below. The time values set here should match the starting time you wish to take both the underwater GPS and GOPRO footage from. On that note I recommend starting to record with the GOPRO first,
and using the starting time of the first Underwater GPS data point as these intital values for increased accuracy.

![image](https://user-images.githubusercontent.com/32299736/146601432-b3a452ac-ee1a-45a1-b0a5-d537db3614fc.png)

Run the "gopro_to_timestamped_frame.py" script using your favorite IDE or text editor. I recommend Jupyter notebooks or Spyder, as I verifed the code to work in both. Running the code will generate another folder called "videos" inside of the "save" folder you created. Inside this newly generated "videos" folder will be another folder with the same name as your GOPRO video. When you open that folder, you will see all of your frames, like in the example below. Each frame has its own timestamp, a second apart. So 1 frame are generated every second. This could be changed on future iterations of the code, but would take some additional work.

![image](https://user-images.githubusercontent.com/32299736/146602098-f1d414da-a589-414e-9ed2-959b8c6b4361.png)

Now we need to access our navigation data. find your "tracklog.gpx" file that was generated by the "tracking_gps.py" script and open it using excel. You should now have access to the latitude, longitude, and depth data. Since the time you began tracking should be the same time you entered into "gopro_to_timestamped_frame.py" for the starting time, all data points up until the time you trimmed the camera to should be used from this file.

You must take the latitude, longitude, and depth and put them into the "navigation.csv" file in their respective columns. You can leave everything else the same. Here is an example of the completed navigation.csv for a short video. As you can see the first column also includes the filename of each of the frames you are using.

![image](https://user-images.githubusercontent.com/32299736/146603536-1a65984f-265e-4e6b-a8f7-2262db7c1030.png)

To copy the frame names into the navigation file, I recommend the following steps. Go to the folder that contains the images, and copy its filepath. Enter the file path into your favorite browser. You should see a view like this:

![image](https://user-images.githubusercontent.com/32299736/146603813-30253899-d57b-43ed-9b20-aa04c521bd98.png)

Now CTRL-A to copy all, and paste it into a text file. Once in the text file, get rid of the additional information so that it looks like this:

![image](https://user-images.githubusercontent.com/32299736/146603928-1081b781-03b9-414e-89e6-6cf74458a017.png)

Now copy this into an excel sheet, and delete the 2nd and 3rd columns which will just contain the data size and time. Copy the list of just filenames and save this file with the name "image_sequence.csv" as well. Now you can paste the filename column into the first column of the navigation.csv file.

We are now ready to generate a GeoTiff Mosaic from the video.

Mosaicking:

Note: If you would just like to create an ungeoreferenced mosaic, this can be easily accomplished using the free program "autostitch" which you can download online. It simply takes all the images you wish to mosaic, and generates it in a few seconds. The method about to be described takes over an hour to complete. I had difficulty finding options that could both create a mosaic and georeference it, as although there were plenty of papers claiming they did so, they did not have their code publicly available. There was a github repository that had a project for georeferencing mosaics, but I found it to be too complicated to work with. I eventually settled with LAPMv2, which was from one of the  only papers I found that created a finished product, or that did not charge for their service. A user manual for LAPMv2 is included in the files for additional support or for information on using more advanced features.

Download LAPMv2 on your computer. This is the software package we will use to produce a GeoTiff from the files we have created. 

There are a few additional times to complete before we launch LAPMv2. We first need to consolidate all of our data to be used. Create a folder and place "navigation.csv", "image_sequence.csv", "sensor_list.csv", and all the images being used inside of it.

Now open LAPMv2. It will prompt you to select a folder. Select the folder you just created. Next it will ask for a sequence file. Select "image_sequence.csv". Now a GUI will open.

![image](https://user-images.githubusercontent.com/32299736/146604618-1579ea1b-39b0-4a65-8c8f-4ab29f38fd6d.png)

The process to generate the GeoTiff is as follows: First upload the "navigation.csv" file by clicking "Navigation data & Input Files" in the GUI. Next click "detect and match features". Set it to automatic if the option is presented. Next do "find sidelinks". Again, set to automatic if it gives the option. Then click "refresh file system". Then "Global registration (linear)". After this, "plot topology" and then "assemble mosaic". This process will take a long time, but once completed a GeoTiff will be generated in a new folder within the main folder you made for using LAPMv2 originally.

You can now open this generated GeoTiff file in ArcMap!

