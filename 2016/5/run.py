from shared import *
import hashlib
import re
input = 'ugkcyxxp'

def starts_with_5_zeros(s):
    return re.match('^00000.*', s)

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# password = ''
# for i in range(0, 99999999):
#     m = hashlib.md5(input+str(i)).hexdigest()
#
#     if starts_with_5_zeros(m):
#         password += m[5]
#         if len(password) > 7:
#             print 'Part 1:'
#             print password
#             break;


password = ['_'] * 8
for i in range(0, 99999999):
    m = hashlib.md5(input + str(i)).hexdigest()

    if starts_with_5_zeros(m):
        if isInt(m[5]):
            if (0 <= int(m[5]) <= 7):
                if password[int(m[5])] == '_':
                    password[int(m[5])] = m[6]
                    print ''.join(password)
                    if '_' not in password:
                        break