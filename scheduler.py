# scheduler.py

from apscheduler.schedulers.blocking import BlockingScheduler
from main_mercury import main as mercury_main
from content_colector.api_connector_reddit import collect_reddit_posts

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    
    # Agendar o fluxo do Mercury a cada 3 horas
    scheduler.add_job(mercury_main, 'interval', hours=3, id='mercury_job')
    
    # Agendar a coleta do Reddit a cada 24 horas
    scheduler.add_job(collect_reddit_posts, 'interval', hours=24, id='reddit_job')
    
    print("Scheduler iniciado:")
    print("- Mercury postará a cada 3 horas.")
    print("- Coleta do Reddit ocorrerá a cada 24 horas.")
    
    scheduler.start()
