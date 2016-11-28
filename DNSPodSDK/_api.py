# -*- coding:utf-8 -*-

import urllib
import urllib2
import time
import datetime
import json


API_URL = 'https://dnsapi.cn/'
DEBUG = False

LOG_FILE = './DNSPodSDK.log'
REQUEST_RETRY = 3
REQUEST_RETRY_INTERVAL = 3


class API(object):
    '''
    DNSPod Python SDK.
    '''
    def __init__(self, token_id, token_code):
        '''
        Generate Token data.
        '''
        self.token_id = token_id
        self.token_code = token_code

        try:
            token_id = int(token_id)
        except ValueError as e:
            print '{0} was not a valid Token ID.'.format(token_id)
            raise SystemExit(e)

        self.token = str(token_id) + ',' + str(token_code)
        self.token = self.token.strip()


    # API Log
    def _api_log(self, log_content):
        '''
        API Log
        '''
        datetime_now = str(datetime.datetime.now())

        try:
            log_fd = open(LOG_FILE, 'a+')

        except Exception as e:
            raise SystemExit(e)

        try:
            log_fd.write(datetime_now + '\n')
            log_fd.write('='*len(datetime_now) + '\n')
            for i in log_content:
                log_fd.write(str(i) + '\n')
            log_fd.write('\n'*2)

        except Exception as e:
            print e

        finally:
            log_fd.close()


    def make_request(self, params=''):
        '''
        Generate request URL.
        '''
        post_data = {
                     'login_token':self.token,
                     'format':'json',
                     'lang':'en',
                     'error_on_empty':'no'
                    }

        if params:
            for key in params.keys():
                post_data[key] = params[key]

        post = urllib.urlencode(post_data)

        return post


    def request(self, path, params=''):
        '''
        Do request.
        '''
        req_url = API_URL + str(path)

        req_headers = {
                       'Connection':'keep-alive',
                       'User-Agent':'Nanu DNSPodSDK/1.0.0 (nanu@qq.com)'
                      }

        attempt = 1
        retry = True
        while retry:
            try:
                post_data = self.make_request(params)

                if DEBUG:
                    handler=urllib2.HTTPSHandler(debuglevel=1)
                    opener = urllib2.build_opener(handler)
                    urllib2.install_opener(opener)

                req = urllib2.Request(req_url, post_data, req_headers)

                conn = urllib2.urlopen(req)
                response = conn.read()

                obj = json.loads(response)

                retry = False

            except Exception as e:
                log = []
                log.append('Request URL: ' + str(req_url))
                log.append('Got Error: ' + str(e))
                log.append('Retry ... ' + '[' + str(attempt) + '/' + str(REQUEST_RETRY) + ']')
                self._api_log(log)

                time.sleep(REQUEST_RETRY_INTERVAL)
                attempt += 1
                if attempt == REQUEST_RETRY + 1:
                    raise SystemExit(e)

        return obj


if __name__ == '__main__':
    raise SystemExit()
