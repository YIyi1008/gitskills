

import codecs

def userinfo(path):
    file = codecs.open(path,'r','utf-8')
    user_list = []
    for line in file:
        user_dict = {}
        result = [ele.strip() for ele in line.split(';')]
        for sult in result:
            re_sult = [ele.strip() for ele in sult.split('=')]
            user_dict.update(dict([re_sult]))
        user_list.append(user_dict)
    return user_list

if __name__ == '__main__':
    user_list = userinfo(r'D:\pythoncode\userinfo.txt')
    print(user_list)