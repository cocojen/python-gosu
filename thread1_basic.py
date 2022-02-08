import logging
import threading
import time

# 스레드 실행 함수
def thread_func(name, sec):
    logging.info("Sub-Thread %s: starting", name)
    
    time.sleep(sec)
    
    logging.info("sub-Thread %s: finishing", name)
    

# 메인 영역
if __name__ == "__main__":
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: before creating thread")    

    # 함수 인자 확인
    # Daemon 은 Default 값이 False 임.
    x = threading.Thread(target=thread_func, args=('First', 3), daemon=True)
    y = threading.Thread(target=thread_func, args=('Second', 2))
    
    # 데몬 스레드 확인
    print(x.isDaemon())
    
    logging.info("Main-Thread: before running thread")
    
    # 서브 스레드 시작
    x.start()
    y.start()
    # thread_func('first')
    
    logging.info("Main-Thread: wait for the thread to finish")
    
    logging.info("Main-Thread : all done")