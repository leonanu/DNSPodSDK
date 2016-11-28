# -*- coding:utf-8 -*-

from _api import API


class Account(API):
    '''
    DNSPod Account.
    '''
    def UserDetail(self):
        '''
        User Detail Information.
        '''
        path = 'User.Detail'
        params = ''

        ret = self.request(path, params)

        return ret

    def UserLog(self):
        '''
        User Log.
        '''
        path = 'User.Log'
        params = ''

        ret = self.request(path, params)

        return ret


if __name__ == '__main__':
    raise SystemExit()
