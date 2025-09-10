import hashlib
s='deltabridge'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
