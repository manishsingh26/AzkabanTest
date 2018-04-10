
import schedule
import time

from Azkaban.AzkabanJob import azkaban_mongo_job


def main():

    def job():
        azkaban_mongo_job()

    schedule.every(5).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
