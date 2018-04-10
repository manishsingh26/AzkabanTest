
from azkaban import Job, Project


def azkaban_mongo_job():

    project_2 = Project('LeadDataStats')
    project_2.add_job('UploadDataStats', Job({'type': 'command', 'command': 'python /home/msingh/Documents/'
                    'PycharmProjects/AzkabanTest/mongo/MongoDataPush.py'}, {'dependencies': 'MongoStart'}))

    project_3 = Project('MongoDataUpload')
    project_3.add_job('UploadDataStatus', Job({'type': 'command', 'command': 'echo "Data successfully  uploaded"'},
                                              {'dependencies': 'UploadDataStats'}))


if __name__ == "__main__":
    azkaban_mongo_job()