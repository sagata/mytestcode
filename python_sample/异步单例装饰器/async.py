#coding=utf-8
import time
import functools
import threading
lock = threading.Lock()
def async(func):                                                                                                                                                                                                                     
    '''
    异步装饰器
    '''
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
    #print ">>>%s"%func
        my_thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        my_thread.start()
        return my_thread
    return wrapper

@async
def gogo(str_tmp):
    #lock.acquire()
    with open(str_tmp,'w') as f:
        f.write('test')
        f.close()
    import time
    time.sleep(10)
    with open(str_tmp + '2222','w') as f:
        f.write('test')
        f.close()
    #lock.release()

if __name__ == "__main__":
    thread1 = gogo('1')
    time.sleep(15)
    print thread1.is_alive()
    #gogo('2')