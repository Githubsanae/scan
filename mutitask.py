import time

from scaner import scaner
import time
import multiprocessing
def start_mutitask(tx,name,min_price):
    copy_process = multiprocessing.Process(
        target=scaner, args=(tx, name, min_price))
    copy_process.start()
if __name__ == '__main__':
    start_mutitask("64c2d95a052cfaebd96bf9ea9c0b011edb70bec95ecbe51d820e799c1af0a4d2","小柯基",300)
    time.sleep(2)
    start_mutitask("6b42c03ec280cafc0dd53aad50c3da16f6907e1b64199ae06b58615f35af3757","幸运勋章",100)
    time.sleep(2)
    start_mutitask("9873e87ebc3d8d29fb4a277ca133e2d48163bd0ccd847c30032601e386092770","相依",200)
    time.sleep(2)
    # start_mutitask("e318e781bc3119e957640495e507e3235b05a781147ff48400cdeb4a2f2bd6db","自由勋章",50)
    # time.sleep(2)
    # start_mutitask("2903222c6392a02bb48a87947f1ccaa725120176027ed6fc678607fa02392776","快乐勋章",50)
    # time.sleep(2)
    # start_mutitask("72207db9ce4bfab4c37d1494eb2bbf546c0bfeefff91fefec5369746a1b057cf","理性勋章",50)
    # time.sleep(2)
    # start_mutitask("78f1f362ae4b617c430c8fa584762597349c489cbff069499b14afc699e26888","守护勋章",50)
    # time.sleep(2)
    # start_mutitask("d9278343884c0f82c54e9c9ab8e420757dab5b54b761c5dc6578c23e45b22fa4","团结勋章",50)
    # time.sleep(2)
    # start_mutitask("333e994f49ef48310534373e594a5fb8f4d90ab039f0b1b223adbf34dc1eb012","自律勋章",50)
    # time.sleep(2)
    start_mutitask("9426d086b23a8def4d88bb6d019a9a5fde7944972d8b361a8be9bdbec146db62","权益值双倍券",200)
    time.sleep(2)
    start_mutitask("ecee80c49310a727ff28fd2bd2c7f5263c7da022dfc63b1908e2237267252f4d","恒境返利券",200)
    time.sleep(2)
    start_mutitask("cb26047beaa92fb8fc0f39beb903f0edbbca80a5e52bfcb44d1e58698cee4287","优先券",100)
    time.sleep(2)
    start_mutitask("4f7a6d4c24aef53bc8ad033d84aa3552daf7c044eb5430a7f06202992b2c9800","十二生肖全家福",7000)
    time.sleep(2)
    start_mutitask("02770eb5e65844a8d84a6012ce67ed86e7a30f0b806c95a7ddffdc81f7b55f26","水中花",1000)
    time.sleep(2)
    start_mutitask("3a43cbce789c144af1c77a6b900ba0bda62ed68668c206383fceb5876076dead","花猫儿",1000)
