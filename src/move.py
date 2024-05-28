class Move:

    def __init__(app , initial , final):
        app.initial = initial
        app.final = final


    def __eq__(app , other):
        return app.initial == other.initial and app.final == other.final