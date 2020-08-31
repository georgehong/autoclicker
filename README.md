# The 50 States Abbreviation Geography Game Auto-clicker

[Play the Game Here!](https://online.seterra.com/en/vgp/3002)   
[See the Autoclicker in Action](https://www.youtube.com/watch?v=OOgs88tzN5Y)    

Using Pytesseract Optical Character Recognition (OCR), this script is able to read state abbreviations and click on the corresponding locations in record time.  This script adapts to different window sizes, using three bounding clicks.  The first two clicks locate the textbox that generates the abbreviations, while the last click frames the map.  

In the video, the largest bottleneck is moving the cursor to bound the game window.  Afterwards, states can be clicked almost immediately after each abbreviation is generated.

The cursor directed OCR is easily adapted for other uses (such as copying images of text).  For use with similar games, edit the dictionary of relative positions of items within the image.
