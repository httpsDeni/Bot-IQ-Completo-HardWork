import base64, re, time

def checkEmail(email):
    regex = '\\S+@\\S+\\.\\S+'
    valid = re.search(regex, email, re.IGNORECASE)
    if valid:
        return True
    return False


def isFloat(value: str):
    try:
        val = float(value.replace(',', '.'))
        return (
         True, val)
    except:
        return (False, 0)


def isTimeFormat(value: str):
    try:
        time.strptime(value, '%H:%M')
        return True
    except ValueError:
        return False


def Cripto64(Value: str, Decripto: bool):
    KEY = '#3U0'
    ret = ''
    if not Decripto:
        ret = base64.b64encode(Value.encode('UTF-8'))
        ret = ret.decode('UTF-8')
        ret = ret[:3] + KEY + ret[3:]
        ret = base64.b64encode(ret.encode('UTF-8'))
        ret = ret.decode('UTF-8')
    else:
        ret = base64.b64decode(Value)
        ret = ret.decode('UTF-8')
        ret = ret.replace(KEY, '')
        ret = base64.b64decode(ret)
        try:
            ret = ret.decode('UTF-8')
        except:
            ret = ret.decode('latin-1')

    return ret