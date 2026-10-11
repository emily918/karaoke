import sounddevice as sd
from pygame import *


fs = 44100
chunk = 1024

width, height = 800, 400
init()
screen = display.set_mode((width, height))
display.set_caption("Karaoke")
clock = time.Clock()

data = [0.0] * chunk

def audio_callback(indata, frames, time_info, status):
    global data
    if status:
        print(status)
    data = [sample * (height // 2) for sample in indata[:, 0].tolist()]
stream = sd.InputStream(samplerate=fs, callback=audio_callback, channels=1, dtype='float32')
stream.start()

running = True
while running:
        for e in event.get():
            if e.type == QUIT:
                running = False

            screen.fill((0, 0, 0))

            points = []
            for i, simlle in enumerate(data):
                x = int(i * width / chunk)
                y = int(height / 2 + simlle)
                points.append((x, y))

                if len(points) > 1:
                    draw.lines(screen, (0, 255, 0), False, points, 2)
                display.update()
                clock.tick(60)
stream.stop()
quit()
