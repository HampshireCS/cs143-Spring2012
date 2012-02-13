import tokenize

def method_for_it(token):
    return token.strip().replace(" ", "_").replace("\"", "") + "(self)"

def translate(line):
    prev = ""

    for typ, value, _,_,_ in tokenize.generate_tokens(line):
        if typ == tokenize.NAME and value == "describe":
            value = "class"
        elif typ == tokenize.NAME and value == 'it':
            value = "def"
        elif typ == tokenize.STRING and prev == "it":
            value = method_for_it(value)
        
        yield typ, value
        prev = value
            

import codecs, cStringIO, encodings

class StreamReader(utf_8.StreamReader):
    def __init__(self, *args, **kw):
        codecs.StreamReader.__init__(self, *args, **kwargs)
        data = tokenize.untokenize(translate(self.stream.readline))
        self.stream = cStringIO.StringIO(data)

def search_function(s):
    if s != "pyspec": return None

    utf8 = encodings.search_function("utf8")
    return codecs.CodecInfo(
        name = "pyspec",
        encode = utf8.encode,
        decode = utf8.decode,
        incrementalencoder = utf8.incrementalencoder,
        incrementaldecoder = utf8.incrementaldecoder,
        streamreader = StreamReader,
        streamwriter = utf8.streamwriter)

codecs.register(search_function)
