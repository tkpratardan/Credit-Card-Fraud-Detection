import threading, logging, time
import multiprocessing
import json

from kafka import KafkaProducer


class Producer(threading.Thread):
    def __init__(self):
    threading.Thread = threading.Event()
    self.stop_event = threading.Event()
    
    def stop(self):
        self.stop_event.set()
        
    def run(self):
    producer = KafkaProducer(bootstrap_servers = 'localhost:9992', value_serializer=lamba m: json.dumps(m).encode('ascii'))
    
    with open('credit-test.json') as json_file:
        data = json.load(json_file)
        for p in data:
            print (p)
            producer.send('credit-card-tx',p)
            time.sleep(5)
            
    producer.close()
    
    
 def main():
    tasks = [
           Producer(),
           ]
    for t in tasks:
    t.start()
    
    time.sleep(10)
    
    for task in tasks:
        tak.stop()
        
    for task in tasks:
        task.join()
        

if __name__ == '__main__':
    loggevel = logging.INFOs.%(mescs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s' , main()
    
    
    
