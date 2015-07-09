__author__ = 'purv'
from urllib import request
import logging
import sys
import json
import time
from stop_watch.stop_watch import StopWatch


class ScopeContentResolver:
    _log = logging.getLogger('ScopeContentResolver')

    @property
    def log(self):
        return self._log

    def __init__(self, node):
        logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                            format='%(levelname)s:%(asctime)s:%(message)s')
        self.node = node

    def resolve_scope(self, scope_id):
        url = 'http://%s:9080/ScopeRegistryService/v1/scopes/%s/resolvedElements' % (self.node, scope_id)
        req = request.Request(url, method='GET')
        # make a request & read the response
        self._log.info("scope content request start")
        res = request.urlopen(req)
        data = json.loads(res.read().decode('utf-8'))
        print(data)
        self._log.info("scope content request end")


if __name__ == '__main__':
    scope_resolver = ScopeContentResolver('clab934node02.netact.nsn-rdnet.net')
    with StopWatch() as sw1:
        scope_resolver.resolve_scope(2)
    print("Time taken considering wall clock ", sw1.elapsed)

    with StopWatch(time.process_time) as sw2:
        scope_resolver.resolve_scope(2)
    print("Time taken considering only CPU time ", sw2.elapsed)
    # scope_resolver.resolve_scope(43)
