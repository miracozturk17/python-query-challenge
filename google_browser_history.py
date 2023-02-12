import sqlite3
import re
conn = sqlite3.connect('C:/Users/.../AppData/.../Chrome/UserData/Default/History')
cur = conn.cursor()
print("history length",cur.execute('SELECT count(1) FROM urls').fetchone([0])
domainPattern = re.compile(r"https?://([^/]+)/") #(r"http?://([^/]+)/") == http?
domains{}
result = True
id=0
while result:
    result False
    ids []
for row in cur.execute('SELECT id, url, title FROM urls WHERE id>? LIMIT 1000',(id,)):
result True
match = domainPattern.search(row[1] )
id row[0]
if match:
    domain = match.group(1)
    domains[domain]	= domains.get(domain, 0) + 1
    if "imgur" in domain:
    ids.append((id,))
 cur.executemany('DELETE FROM urls WHERE id=?',ids)
 conn.commit() 
conn.close()