from threading import Lock, Thread, Event

user1 = Lock()
user2 = Lock()

def task(event, timeout, user1, user2):
    print("Started thread but waiting for event:")
    event_set = event.wait(timeout)
    if event_set:
        print("Event received, releasing thread:")
        transfer_do(user1, user2)
    else:
        print("Time out, moving ahead without event...")

def transfer(user1, user2):
    user1.acquire()
    user2.acquire()
    print("Transaction completed")
    user1.release()
    user2.release()

def transfer_do(user1, user2):    
        transfer(user1, user2)
        transfer(user2, user1)

if __name__ == '__main__':
    e = Event()
    p1 = Thread(target=task, args=(e, 1, user2, user1)) 
    p2 = Thread(target=transfer_do, args=(user2, user1)) 
    p1.start()
    p2.start()
    p2.join()
    e.set()
    print("Event is set")
    p1.join()