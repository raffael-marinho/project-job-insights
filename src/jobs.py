from email import header
from functools import lru_cache
import csv

@lru_cache
def read(path):
    with open(path, encoding="utf-8") as file:
        reader= csv.reader(file, delimeter=",")
        header, *data=reader
    docs = []
    for line in data:
        dictWithReader = {}
        for row in range(len(header)):
            dictWithReader[header[row]] = line[row]
        docs.append(dictWithReader)
    return docs
