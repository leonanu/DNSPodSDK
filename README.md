# DNSPodSDK [![Build Status](https://travis-ci.org/leonanu/DNSPodSDK.svg?branch=master)](https://travis-ci.org/leonanu/DNSPodSDK)

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
>>> ret = dnspod.request('Info.Version')
>>> pprint.pprint(ret)


{u'status': {u'code': u'1',
             u'created_at': u'2016-11-27 20:07:52',
             u'message': u'4.6'}}
```
