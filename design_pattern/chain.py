class Handler:

    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request):
        try:
            res = self.check_request(request)
        except:
            res = False
        if not res and self.successor:
            self.successor.handle(request)

    def check_request(self, request):
        raise NotImplementedError


class SuccessMessageHandler(Handler):

    def check_request(self, request):
        if request.startswith('success'):
            print('Task is finished')
            return True


class ErrorMessageHandler(Handler):

    def check_request(self, request):
        if request.startswith('error'):
            print('Task is failed')
            return True


class DefaultHandler(Handler):

    def check_request(self, request):
        print('default handler received', request)
        return True


h0 = SuccessMessageHandler()
h1 = ErrorMessageHandler()
h2 = DefaultHandler()
h0.successor = h1
h1.successor = h2

requests = ['success: hahaha', 'error: exception', 1]
for request in requests:
    h0.handle(request)
