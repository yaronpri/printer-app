import sys, datetime, logging
import os
import asyncio
import datetime


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

logger.addHandler(logging.StreamHandler(sys.stdout))

process_sec = int(os.environ.get("PROCESS_SECOND", "30"))

async def main():
  
  before = datetime.datetime.utcnow()
  counter = 0
  while True:  
    current =  datetime.datetime.utcnow()    
    if (current - before < datetime.timedelta(days=0, hours=0, minutes=0, seconds=process_sec)): 
      counter = counter + 1
      logger.info(current.strftime("%a, %d %b %Y %H:%M:%S GMT"))    
      logger.info("counter = " + str(counter) + " span = " + str(current - before))
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())