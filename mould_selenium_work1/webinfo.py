
import codecs

def webinfo(path):
    file = codecs.open(path,'r','gbk')
    ele_dict = {}
    for line in file:
        result = [ele.strip() for ele in line.split('=')]
        ele_dict.update(dict([result]))
    return ele_dict

if __name__ == '__main__':
    ele_dict = webinfo(r'D:\pythoncode\webinfo.txt')
    for key in ele_dict:
        print(key,ele_dict[key])