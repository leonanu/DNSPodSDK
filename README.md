# DNSPodSDK

DNSPodSDK is a DNSPod API SDK library, written in Python. 


**Requirement**

Python 2.6/2.7



**Install**
```
python setup.py install
```


                                                                              
**Example:**
```
>>> import DNSPodSDK
>>> dnspod = DNSPodSDK.API(token_id, token_code)
>>> ret = dnspod.request('Domain.Info', domain_id=20899954)
>>> pprint.pprint(ret)


{u'domain': {u'cname_speedup': u'enable',
             u'created_on': u'2015-02-02 18:30:21',
             u'ext_status': u'',
             u'grade': u'DP_Free',
             u'grade_title': u'\u65b0\u514d\u8d39\u5957\u9910',
             u'group_id': u'1',
             u'id': u'20899954',
             u'is_mark': u'yes',
             u'is_vip': u'no',
             u'name': u'inanu.net',
             u'owner': u'nanu@qq.com',
             u'punycode': u'inanu.net',
             u'records': u'7',
             u'remark': u'',
             u'searchengine_push': u'no',
             u'status': u'enable',
             u'ttl': u'600',
             u'updated_on': u'2015-12-23 12:29:03',
             u'user_id': u'1139407'},
 u'status': {u'code': u'1',
             u'created_at': u'2016-11-30 13:02:57',
             u'message': u'Action completed successful'}}
```
