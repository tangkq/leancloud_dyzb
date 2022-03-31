# coding: utf-8
import random
import time

from leancloud import Engine
from leancloud import LeanEngineError
import leancloud

engine = Engine()


@engine.define
def get_server_time(**params):
    return int(time.time())

@engine.define
def match_player_record(**params):
    heronum = params.get("heronum") #随从个数
    version = params.get("version") #版本号
    findnum = params.get("findnum") #需要记录条数
    print("match_player_record",heronum,version,findnum)
    query = leancloud.Query("RecordList")
    query.equal_to("heronum",heronum)
    query.equal_to("version",version)
    query.descending("createdAt")
    query.limit(100)
    results = query.find()
    retcount= len(results)
    findnum = min(findnum, retcount)
    matches = []
    for i in range(findnum):
        ran = random.randint(1,len(results))
        ret = results.pop(ran-1)
        matches.append(ret)
    return matches

@engine.define
def match_todo(**params):
    query = leancloud.Query("Todo")
    query.descending("createdAt")
    query.limit(100)
    results = query.find()
    return results