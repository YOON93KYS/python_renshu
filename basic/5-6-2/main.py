'''
5-6-2. 実践演習
実践演習５－３－２で作成したadd関数は引数が数値でなかった場合に例外を発生する可能性があるため、
その場合は0を返すようにせよ（目標１０分）
'''


def add_2(aa, bb):
    try:
        return(aa + bb)
    except ValueError:  # https://monozukuri-c.com/python-pep8-e722/
        return(0)
