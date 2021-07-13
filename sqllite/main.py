import sqlite3

# Create database in techblog.db
conn = sqlite3.connect('gcsにアップロードしたdbのPATH')

curs = conn.cursor()

# 初期設定
curs.execute('''CREATE TABLE post
             (entry_id integer, hatena_url text, file_path text, user real, created_at text, update_at text)''')

curs.execute('''CREATE TABLE user
             (user text, cosumer_key text, cosumer_key_secret text, created_at text, update_at text)''')


# insertの場合
## post
curs.execute("INSERT INTO post VALUES ('aa', 'bb', 'cc', 'dd', 'ee','ff')")
## user
curs.execute("INSERT INTO user VALUES ('aa', 'bb', 'cc', 'dd', 'ee')")

# Save (commit) the changes
conn.commit()

#Browse inserted data
A = curs.execute("SELECT * FROM post")
for row in A:
    print(row)