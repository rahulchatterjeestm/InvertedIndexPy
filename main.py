from Classes import Database, InvertedIndex
db = Database()
inverted =InvertedIndex(db)
document1 = {
    'id':1,
    'text':'The big sharks of Belgium drink beer.'
}
document2 = {
    'id':2,
    'text': 'Belgium has great beer. They drink beer all the time.'
}
inverted.IndexDocument(document1)
inverted.IndexDocument(document2)

term = "beer"
result = inverted.LookUp(term)
print(result)
