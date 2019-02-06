class WebsocketState:

    def __init__(self, ws_conn):
        self.conn = ws_conn

    def keep_connection(self):
        raise NotImplementedError


class ConnectingState(WebsocketState):

    def keep_connection(self):
        # set to open state
        pass


class OpenState(WebsocketState):

    def keep_connection(self):
        # send ping pong
        pass


class ClosingState(WebsocketState):

    def keep_connection(self):
        # wait close
        # set closed
        pass


class ClosedState(WebsocketState):
    def keep_connection(self):
        # reconnect
        pass


class WebsocketConnection:

    def __init__(self):
        self.state = ClosedState(self)

    def keep_connection(self):
        self.state.keep_connection()
