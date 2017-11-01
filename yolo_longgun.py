

# need to pip3 install darknetpy
# run on python3


from darknetpy.detector import Detector

detector = Detector('dev/darknet',
                    'ds/swx_longgun.data',
                    'ds/swx-yolo-voc.2.0.cfg',
                    'swx-yolo-voc_18000.weights')


results = detector.detect('data/gun.jpg')

print(results)
