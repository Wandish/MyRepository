filosof = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren’t special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one — and preferably only one — obvious way to do it.
Although that way may not be obvious at first unless you’re Dutch.
Now is better than never.
Although never is often better than 'right now'.
If the implementation is hard to explain, it’s a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea — let’s do more of those!"""

print(filosof.count("better")) #Знайти кіл-ть входжень - better

print(filosof.upper()) #Верхній регістр

print(filosof.replace("i","&")) #Замінити символ і на &
#- - -#
chislo = "1534" #Добуток чисел

print(int(chislo[1])*int(chislo[2])*int(chislo[3])) #Добуток чисел

print(chislo[::-1]) #Реверсний порядок

print ("".join(sorted(chislo))) #Посортувати цифри, що входять в дане число

A=5 
B=10
print(A,B)
A,B=B,A #Поміняти між собою значення двох змінних, не використовуючи третьої змінної.
print(A,B)

print(0 and 1)
print(1 and 0)
print("f" and 1)
print(1 and "f")
print(1 and 2 and 0 and False)