from wimbd.es import es_init, get_indices, count_documents_containing_phrases, get_documents_containing_phrases
import json
from pathlib import Path


es = es_init(config=Path('es_config_dolma_1_7_2.yml'))

# cnts = count_documents_containing_phrases("docs_v1.7_2024-06-04", ["AMA", "against medical advice"], all_phrases=True, es=es) # 6494
# cnts = count_documents_containing_phrases("docs_v1.7_2024-06-04", ["AMA", "'against medical advice'"], all_phrases=True, es=es) # 6494
# docs = get_documents_containing_phrases("docs_v1.7_2024-06-04", ["AMA", "against medical advice"], all_phrases=True, num_documents=10000, es=es)  # 6494

# OP, 'oblique presentation'
cnts = count_documents_containing_phrases("docs_v1.7_2024-06-04", ["OP", "'oblique presentation'"], all_phrases=True, es=es) # 23
docs = get_documents_containing_phrases("docs_v1.7_2024-06-04", ["OP", "oblique presentation"], all_phrases=True, num_documents=10000, es=es)  # 23

# docs = get_documents_containing_phrases("c4", ["AMA", "against medical advice"], all_phrases=True, num_documents=500, es=es)  # single term

urls = []
for doc in docs:
    text = doc['_source']['text']
    url = doc['_source']['url']
    if 'oblique presentation' not in text:
        print("url: ", url)
        # print("text: ", text)
    urls.append(url)
print(urls)
print(f"duplicates: {len(urls) - len(set(urls))}") # 618
# import collections
# print([item for item, count in collections.Counter(urls).items() if count > 1])

