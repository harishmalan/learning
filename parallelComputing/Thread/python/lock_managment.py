import threading 
shared_resource_with_lock = 0
shared_resource_with_no_lock = 0
COUNT =10000
shared_resource_lock = threading.Lock()

def increment_with_lock():
	global shared_resource_with_lock
	for i in range (COUNT):
		shared_resource_lock.acquire()
		shared_resource_with_lock += 1
		shared_resource_lock.release()

def decrement_with_lock():
	global shared_resource_with_lock
	for i in range (COUNT):
		shared_resource_lock.acquire()
		shared_resource_with_lock -= 1
		shared_resource_lock.release()

"""[summary]

[description]
"""
def increment_without_lock():
	global shared_resource_with_no_lock
	for i in range(COUNT):
		shared_resource_with_no_lock +=1


def decrement_without_lock():
	global shared_resource_with_no_lock
	for i in range(COUNT):
		shared_resource_with_no_lock -=1


if __name__ == '__main__':
	t1= threading.Thread(target= increment_with_lock)
	t2= threading.Thread(target= decrement_with_lock)
	t3= threading.Thread(target= increment_without_lock)
	t4= threading.Thread(target= decrement_without_lock)
	t1.start()
	t2.start()
	t3.start()
	t4.start()
	t1.join()
	t2.join()
	t3.join()
	t4.join()
	print (f'the value of shared variable with lock management is {shared_resource_with_lock}')
	print (f'the value of shared variable with race condition  is {shared_resource_with_no_lock}')
