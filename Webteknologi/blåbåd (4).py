import reverse_geocoder
from orbit import ISS
from picamera import PiCamera
from time import sleep

camera = PiCamera()
while True:
coordinates = ISS.coordinates()
coordinate_pair = (
    coordinates.latitude.degrees,
    coordinates.longitude.degrees)
location = reverse_geocoder.search(coordinate_pair)
print(location)

locationISS = ISS.coordinates()
print(f'Latitude: {locationISS.latitude.degrees}')
print(f'Longitude: {locationISS.longitude.degrees}')
#locationISS.latitude.degrees
#print(locationISS.latitude.degrees- float(location[0]['lat']))
#locationISS.longitude.degrees
dy = abs(locationISS.longitude.degrees-float(location[0]['lon']))
dx = abs(locationISS.latitude.degrees-float(location[0]['lat']))
print(dy)
print(dx)


if (dy+dx < 2 and dy+dx>0):
    camera.start_preview()
    camera.start_recording('/home/pi/Desktop/video.h264')
    sleep(5)
    camera.stop_recording()
    camera.stop_preview()
else :
    print ("nej")








