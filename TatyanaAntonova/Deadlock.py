from threading import Lock, Thread

user1 = Lock()
user2 = Lock()

def transfer(user1, user2):
    user1.acquire()
    user2.acquire()
    print("Transaction completed")
    user1.release()
    user2.release()

def transfer_do(user1, user2):
    while True:
        transfer(user1, user2)
        transfer(user2, user1)

p1 = Thread(target=transfer_do, args=(user1, user2)) 
p2 = Thread(target=transfer_do, args=(user2, user1)) 
p1.start()
p2.start()
p1.join()
p2.join()