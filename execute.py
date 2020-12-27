import exam as e
import threading

e.create("vamp",25)
e.create("src",70,3600)
e.read("vamp")
e.read("src")
e.create("vamp",50)
e.modify("vamp",55)
e.delete("vamp")
t1= threading.Thread(target=(e.create or e.read or e.delete), args=(key_name, value, timeout))
t1.start()
t1.sleep()
t2=threading.Thread(target=(e.create or e.read or e.delete), args=(key_name, value, timeout))
t2.start()
t2.sleep()
