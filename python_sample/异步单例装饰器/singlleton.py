#encoding=utf-8
import urllib,httplib
import traceback


#使用QA提醒发popo消息
def popo_to(popo_list,title,message):
    message = message.replace('\n','\r\n')
    message='%s:\r\n%s'%(title,message)
    message = message.decode('utf8').encode("gbk")
    params = urllib.urlencode({'users':popo_list, 'message':message})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = httplib.HTTPConnection("qa.nie.netease.com", 80, timeout=30)
    conn.request("POST", "/interface/popo", params, headers)
    response = conn.getresponse()
    conn.close()

def singleton(cls):
    '''单例装饰器
    usage: @singleton, 这种方式不太好，会把一个类变成一个func, 会导致super不能用
    '''
    instances = {}
    def _singleton(*args, **kwargs):
        print 'args, kw',cls, args, kwargs
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return _singleton

def enum(**enums):
    return type('Enum', (), enums)

class Singleton(type):
    '''单例类
    usage: class A():   __metaclass__ = Singleton
    '''
    def __init__(cls, name, bases, dict):  
        super(Singleton, cls).__init__(name, bases, dict)  
        cls._instance = None  
    def __call__(cls, *args, **kw):  
        if cls._instance is None:  
            cls._instance = super(Singleton, cls).__call__(*args, **kw)  
        return cls._instance

def catch(return_value=None, popo_list=None):
    '''函数报错catch装饰器
    usage: @catch(return_value={},popo_list='gzmaruijie')
    params:
        return_value: return return_value if trace, or return real ret of func()
        popo_list: send popo msg to popo_list when traced
    '''
    def real_wraper(func):
        def _wraper(*args, **kwargs):
            try:
                ret = func(*args, **kwargs)
                return ret
            except:
                msg = traceback.format_exc()
                if popo_list:
                    popo_to(popo_list, 'catch', msg)
                
                return return_value
        return _wraper
    return real_wraper

if __name__ == "__main__":
    '''
    @catch(return_value={},popo_list='gzmaruijie')
    def test():
        print 'test'
        raise
    print 'test', test()
    '''

    class Test(object):
        def __init__(self, x, y):
            print 'Test __init__'
            self.x, self.y = x, y

    
    class Test2(Test):
        __metaclass__ = Singleton
        def __init__(self, x, y, z):
            print 'Test2 __init__'
            #print 'self', self
            #print 'Test2', Test2
            #print 'super', super(Test2, self)
            super(Test2, self).__init__(x, y)
            #Test.__init__(self, x, y)
            self.z = z
        def get_z(self):
            return self.z
    
    t = Test2(1,2,4)
    b = Test2(2,3,5)
    c = Test(3,5)
    print t, b
    
    print t.x, t.y, t.z
    print b.x, b.y, b.z
    '''
    print t.get_z()
    print c.x, c.y
    '''
    



