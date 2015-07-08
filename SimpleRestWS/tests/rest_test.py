__author__ = 'purv'
from urllib import request, parse


class RestTest:
    def http_get(self, song_id):
        url = "http://127.0.0.1:8081/api/songs/%s" % song_id

        req = request.Request(url, method='GET')

        # Make a request and read the response
        u = request.urlopen(req)
        resp = u.read()

        print(resp)

    def http_post(self, params):
        query_string = parse.urlencode(params)
        rest_url = "http://127.0.0.1:8081/api/songs/"

        req = request.Request(rest_url, query_string.encode('ascii'), method='POST')

        # Make a request and read the response
        u = request.urlopen(req)
        resp = u.read

        print(resp)

    def http_put(self, params, songs_id):
        query_string = parse.urlencode(params)
        rest_url = "http://127.0.0.1:8081/api/songs/%s" % songs_id

        req = request.Request(rest_url, query_string.encode('ascii'), method='PUT')

        # Make a request and read the response
        u = request.urlopen(req)
        resp = u.read
        print(resp)

    def http_delete(self, song_id):
        rest_url = "http://127.0.0.1:8081/api/songs/%s" % song_id

        req = request.Request(rest_url, method='DELETE')

        # Make a request and read the response
        u = request.urlopen(req)
        resp = u.read
        print(resp)


if __name__ == '__main__':
    rest_client = RestTest()
    rest_client.http_get(2)
    params = {
        'title': 'Xyx Xyxx...',
        'artist': 'ABC'
    }
    rest_client.http_post(params)
    # rest_client.http_put(params, 4)
    rest_client.http_get(4)
    # rest_client.http_delete(4)
    rest_client.http_get(4)
