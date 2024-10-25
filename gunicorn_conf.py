import multiprocessing

max_requests = 1000

max_requests_jitter = 50

loglevel="info"

accesslog = "/home/ubuntu/api_automacao_sinapse/logs/access.log"
errorlog = "/home/ubuntu/api_automacao_sinapse/logs/error.log"

bind = "0.0.0.0:8000"

worker_class = "uvicorn.workers.UvicornWorker"

workers = (multiprocessing.cpu_count() * 2) + 1
