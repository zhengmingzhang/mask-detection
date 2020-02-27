import wave
import pyaudio
import matplotlib.pyplot as plt
import time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 2


def record(filename='output.wav'):
    """官方录音教程
    """
    
    p = pyaudio.PyAudio()
    
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    
    print("* recording")
    
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    
    print("* done recording")
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def multi_record(num=3):
    """implement 多次录音"""
    for i in range(1,num+1):
        print('第{}次录音准备'.format(i))
        filename = 'record_{}.wav'.format(i)
        record(filename)
        time.sleep(second)
        _ = input('进行下一次录音？')


def main():
    record(filename='mask_on.wav')

if __name__ == '__main__':
    main()

