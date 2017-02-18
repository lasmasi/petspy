from picamera import PiCamera
from time import sleep
import time
import os.path

MEDIUM = (1024, 758)
MEDIUM_WIDE = (1280, 720)
SMALL = (640, 480)

VIDEO_DIR = "/home/pi/Videos"
PHOTO_DIR = "/home/pi/Pictures"

INIT_SLEEP = 3
RECORD_FOR = 5
PREVIEW = True

def record(duration=5, filename="video", extension="h264"):
    """Record video of specific duration"""
    print("Starting video recording for {} seconds...".format(duration))
    filename = add_timestamp(filename, extension)
    camera.start_recording('{}/{}'.format(VIDEO_DIR, filename))
    sleep(duration)
    camera.stop_recording()
    print("Stopped video recording: {}".format(filename))

def burst(count=5, filename='image'):
    """Takes picture in burst mode"""
    print("Starting to capture pictures in burst mode...")
    for i in range(count):
        sleep(1)
        filename = '{}/{}_{}.jpg'.format(PHOTO_DIR, filename, i)
        print("Capturing picture {}".format(filename))
        camera.capture(filename)
    print("Stopped to capture pictures in burst mode...")

def add_timestamp(filename, extension):
    """Add timestamp to given filename, e.g. video-2017-02-18T00-09-20.h264"""
    import datetime
    suffix = datetime.datetime.now().isoformat()
    suffix = suffix.split(".")[0]
    suffix = suffix.replace(":","-")
    updated_filename = "{}-{}.{}".format(filename, suffix, extension)
    print("Using file '{}'".format(updated_filename))
    return updated_filename


if __name__ == "__main__":    
    camera = PiCamera()
    camera.resolution = MEDIUM_WIDE
    camera.framerate = 25
    camera.rotation = 180
    #camera.annotate_text = "{}".format(time.time())
    #camera.start_preview(alpha=200)
    if PREVIEW:
        camera.start_preview()
    sleep(INIT_SLEEP)

    record(RECORD_FOR)
    #burst(1)

    if PREVIEW:
        camera.stop_preview()
        
    camera.close()
