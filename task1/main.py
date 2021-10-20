

import re
import string as _str
import pickle

def wordss(txt):  #Выбираем слова из предложения.
    res = {}
    for p in _str.punctuation:# Знаки препинания не входят в слова.
        txt = txt.replace(p, ' ')
    words = txt.split()
    for wor in words:
        res[wor] = len(wor)
    return res

def wordskol(s):
    for p in _str.punctuation:
        s = s.replace(p, ' ')
    return len(s.split())

def sentencess(txt):    #Выбираем предожения.
    res= {}
    sentence = re.split(r'(?<=[.!?]) ', txt)
    for sen in sentence:
        k = wordskol(sen)
        if (k != 0):
            res[sen] = k
    return res

def symbolss(txt): #Выбираем знаки
    res = {}
    for sy in _str.punctuation:
        k = txt.count(sy)
        if k != 0:
            res[sy] = k
    return res

def saveres(res, path):
    with open(path, 'wb') as f:
        pickle.dump(res, f)

def savetext(res, path):
    with open(path, 'w', encoding='UTF-8') as f:
        for r in res:
            f.write(r + '\n')


def printres(res):
    for key in res:
        if isinstance(res[key], dict):
            print(key, '', sep=': ')
            for sub in res[key]:
                print('\t' + sub, res[key][sub], sep=': ')
        else:
            print(key, res[key], sep=': ')
        print("\n")

def dopar(items, n):
    res = []
    i = 0
    c = 0

    for s in items:
        if c == 0:
            res.append(s)
        else:
            res[i] += ' ' + s
        c += 1

        if c == n:
            c = 0
            i += 1
    return res

def inputing(text):
    while 1:
        n = input(text)
        try:
            n = int(n)
        except ValueError as ex:
            print("Введено не число, повторите попытку.", sep="\n")
            continue
        return n

def sortpar(par):
    return sorted(par, key=lambda x: len(wordss(x)))

def printpar(sortedpar, n):
    print("Текст после разбиения на абзацы по "+str(n)+" предложения и сортировки их по числу слов:")
    for s in sortedpar:
        print(s)


def inputtext(txt):
    print('Исходный текст: ' + txt)

    res = {"Всего слов": 0, "Всего предложений": 0, "Предложения": 0, "Слова": 0, "Знаки препинания": 0}

    res['Предложения'] = sentencess(txt)
    res['Всего предложений'] = len(res['Предложения'])

    res['Слова'] = wordss(txt)
    res['Всего слов'] = len(res['Слова'])

    res['Знаки препинания'] = symbolss(txt)

    printres(res)

    saveres(res, 'output.pickle')

    n = inputing("Необходимо разбить текст на преложения.\n Введите значение количества преложений: (n): ")
    par = dopar(res['Предложения'], n)

    sortedpar = sortpar(par)
    printpar(sortedpar, n)
    savetext(sortedpar, 'output.txt')

if __name__ == '__main__':
    string = ''
    from pathlib import Path
    while 1:
        path = input("Введите путь к файлу, где хранится исходный текст: ")
        f = Path(path)
        if f.is_file():
            string = f.read_text(encoding="UTF-8")
            if len(string) > 1:
                # Чтобы можно было спокойно записать текст по строкам, просто для удобства
                string = string.replace('\n',' ')
                inputtext(string)
                break
            else:
                print("Ваш файл пустой")
                break
        else:
            print("Вы ввели неверный путь, попробуйте снова")
            continue

input("Введите ENTER, чтобы завершить работу")