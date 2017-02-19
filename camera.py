from picamera import PiCamera
from time import sleep
import time
import os.path
import math

MEDIUM = (1024, 758)
MEDIUM_WIDE = (1280, 720)
SMALL = (640, 480)

VIDEO_DIR = "/home/pi/Videos"
PHOTO_DIR = "/home/pi/Pictures"

INIT_SLEEP = 0
RECORDING_TIME_SECS = 3
PREVIEW = True
VIDEO_CHUNK_SIZE_MINUTES = 1
DEBUG = True

def record(duration=5, filename="video", extension="h264"):
    """Record video of specific duration"""
    chunks = math.ceil(duration/(VIDEO_CHUNK_SIZE_MINUTES*60.0))
    print("Video will be split in {} chunk(s).".format(chunks))
    for i in range(chunks):
        segment_duration = min((duration - VIDEO_CHUNK_SIZE_MINUTES*60*i), VIDEO_CHUNK_SIZE_MINUTES*60)
        print("Starting video recording for {} seconds...".format(segment_duration))
        filename = add_timestamp(filename, extension)
        camera.start_recording('{}/{}'.format(VIDEO_DIR, filename))
        camera.wait_recording(segment_duration)
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
    if PREVIEW:
        if DEBUG:
            camera.start_preview(fullscreen=False, window=(100, 20, 640, 480))
        else:
            camera.start_preview()
    sleep(INIT_SLEEP)

    record(RECORDING_TIME_SECS)
    #burst(1)

    if PREVIEW:
        camera.stop_preview()
        
    camera.close()
