# -*- coding:utf-8 -*-

from _api import API


class Public(API):
    '''
    DNSPod Public Information.
    '''
    def InfoVersion(self):
        '''
        DNSPod Version.
        '''
        path = 'Info.Version'
        params = ''

        ret = self.request(path, params)

        return ret


if __name__ == '__main__':
    raise SystemExit()
