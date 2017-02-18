from picamera import PiCamera
from time import sleep

MEDIUM = (1024, 758)
MEDIUM_WIDE = (1280, 720)

def record(duration=10):
    """Record video of specific duration"""
    print("Starting video recording...")
    camera.start_recording('/home/pi/Videos/test.h264')
    sleep(duration)
    camera.stop_recording()
    print("Stopped video recording...")

def burst(count=5, filename='image'):
    """Takes picture in burst mode"""
    print("Starting to capture pictures in burst mode...")
    for i in range(count):
        sleep(1)
        filename = '/home/pi/Pictures/{}_{}.jpg'.format(filename, i)
        print("Capturing picture {}".format(filename))
        camera.capture(filename)
    print("Stopped to capture pictures in burst mode...")

    
camera = PiCamera()
camera.resolution = MEDIUM_WIDE
camera.rotation = 180
camera.annotate_text = "Munchkins"
camera.start_preview(alpha=200)
sleep(5)

record(5)
#burst(1)

camera.stop_preview()
