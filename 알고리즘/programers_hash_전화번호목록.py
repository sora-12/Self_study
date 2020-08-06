'''
나의풀이

다른 단어의 접두사로 온다는 것은 list목록 중 길이가 짧은 즉, 숫자로 치면 길이가 가장 짧은 요소일거라 판단하여 min을 사용
'''def solution(phone_book):
    answer = True
    mins=min(phone_book)
    del phone_book[phone_book.index(mins)]
    for i in phone_book:
        if i.startswith(mins):
            answer=False

    return answer


'''
sorted에 기준값을 줄 수 있다는 점.
가장 작은 요소를 제외하고 모든 케이스에 검정을 한다는 점.

'''
def solution(phoneBook):
    phoneBook = sorted(phoneBook,key=len)
    # phoneBook.sort(key=lambda x: len(x))

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return Fal
