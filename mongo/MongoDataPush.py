
import json
import warnings
import datetime, time
import pandas as pd
from pymongo import MongoClient
warnings.filterwarnings("ignore")


def mongo_data_stats():

    client = MongoClient('localhost', 27017)

    db1 = client.crmnext
    collection1 = db1.lead_data

    df = pd.DataFrame(list(collection1.find()))

    columns_list = list(df.columns.values)
    columns_list.remove('_id')
    columns_list.remove('createdonyear')

    df_data = df[columns_list]

    for each_header in columns_list:
        df_data[each_header] = df_data[each_header].astype('category')

    df_data_stats = df_data.describe()
    df_data_stats_json = json.loads(df_data_stats.to_json(orient='index'))

    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    df_data_stats_json['timestamp'] = timestamp

    db2 = client.crmnext
    collection2 = db2.data_stats
    collection2.insert(df_data_stats_json)

    print "Job Complete"


if __name__ == "__main__":
    mongo_data_stats()
