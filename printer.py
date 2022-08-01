import sys, logging, time
import os
import asyncio
import datetime


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

logger.addHandler(logging.StreamHandler(sys.stdout))

process_sec = int(os.environ.get("PROCESS_SECOND", "30"))

#print("PRINTER APP - " + datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
async def main():
  #print("PRINTER APP MAIN - " + datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
  before = datetime.datetime.utcnow()
  counter = 0
  while True:  
    current =  datetime.datetime.utcnow()    
    if (current - before < datetime.timedelta(days=0, hours=0, minutes=0, seconds=process_sec)): 
      counter = counter + 1
      logger.info("counter = " + str(counter) + " span = " + str(current - before))
      time.sleep(0.0000001)
if __name__ == '__main__':
    #print("PRINTER APP IF - " + datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())