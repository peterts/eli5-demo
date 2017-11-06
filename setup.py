import os
import sys
import re

project_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
if project_dir not in sys.path:
    sys.path.append(project_dir)


def read_documents_in_dir(dir_path, has_labels):
    file_names = sorted(os.listdir(dir_path), key=lambda x: int(re.search("\d+", x).group()))
    documents, labels = [], []
    for file_name in file_names:
        with open(os.path.join(dir_path, file_name), encoding='utf8') as f:
            if has_labels:
                labels.append(int(next(f)))
            documents.append(f.read())
    if has_labels:
        return documents, labels
    return documents