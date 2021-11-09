class AddCORSHeaders(object):
    def process_response(self, proxy, request, upstream_response, response):
        response.headers['Access-Control-Allow-Origin'] = "*"
        response.headers["Vary"] = "Origin"

        return response