import json
import os
module_dir = os.path.dirname(__file__)
file_path = os.path.join(module_dir, 'data.json')
def increment_counter(counter):
    for i in range(8):
        counter[i]+=1
        if(counter[i]==58):
            counter[i]=0
        else:
            break
    return counter

def generate_url():
    f=open(file_path,"r")
    data=json.load(f)
    counter=data['counter']
    # print(counter)
    f.close()

    fp=open(file_path,"w")
    ascii_list=data['lists']
    data['counter']=increment_counter(data['counter'])
    fp.write(json.dumps(data))
    fp.close()

    url_str=''.join([chr(ascii_list[i][counter[i]]) for i in range(8)])
    return url_str

# print(generate_url())

