import time

def conta_tempo():
    relogio = 1
    start = time.time()
    while (relogio != 0):
        time.sleep(5)
        counter = -1

        secondsPause = 5

        printerLooper = True
        while printerLooper == True:
            print("Sleeping for ", secondsPause, " seconds")
            counter += 1
            print(counter)
            printerLooper = False


        #
        print("total time taken this loop: ", time.time() - start)
        
if __name__ == '__main__':
    impressora()
