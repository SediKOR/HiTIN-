import json

f = open('text_total.json', 'r')
data = f.readlines()
f.close()

label_hierarchy = {'Root': []}

for line in data:
    line = line.rstrip('\n')
    line = json.loads(line)
    categories = line['doc_label']
    
    # example..
    #"doc_label": ["컴퓨터과학", "운영체제", "리눅스"]
    #"doc_label": ["컴퓨터과학", "데이터베이스", "SQL"]
    #"doc_label": ["의료학", "생리학", "신경계"]
    #"doc_label": ["의료학", "유전학", "유전자치료"
    #"doc_label": ["컴퓨터 과학", "운영체제", "리눅스", "커널"]
    
    # 하고자 하는 목표
    # {'Root': ['컴퓨터과학', '의료학', '컴퓨터 과학'], '컴퓨터과학': ['운영체제', '데이터베이스'], '운영체제': ['리눅스']}
    
    for i, category in enumerate(categories):
        if i == 0 :
            if category not in label_hierarchy['Root']:
                label_hierarchy['Root'].append(category)
                label_hierarchy[category] = []
                print(label_hierarchy)
            else:
                if category not in label_hierarchy[category[i-1]]:
                    print(label_hierarchy[categories[i]]).append(category)
                    print(label_hierarchy)
                #     label_hierarchy[categories[i]].append(category)
                #     print(category)
                #     print(categories[i])
                #     print(label_hierarchy)
                    
        
        
        
    
        
        # if i == 0 :
        #     print('root'+ categories[i])
        #     if category not in label_hierarchy['Root']:
                
        #         label_hierarchy[category].append(category)
        # else:
        #    if category not in label_hierarchy:
                
        #        label_hierarchy[category] = []
            #if categories[i] not in label_hierarchy[category]:
            
        #        label_hierarchy[].append(categories[i])
        #        print(categories[i])
                
    
                        
#label_hierarchy = remove_empty(label_hierarchy)
#print(label_hierarchy) 