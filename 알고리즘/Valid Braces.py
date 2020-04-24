'''
Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
'''

def validBraces(s):
    # 올바른 brace의 경우엔 두개의 값이 붙어 있을 수 밖에 없다. (숫자가 중간에 없다고 치면)
    # 쌍처리 된것을 ''없애다 보면 s가 비게 될 것 이다.
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','').replace('[]','').replace('()','')
  return s==''


def validBraces(s):
    # brace의 순서를 고려해야 한다는 것을 인지하지 못했는데 dictionary로 정의한 것이 인상적
    braces = {"(": ")", "[": "]", "{": "}"}
    stack  = []
    for character in s:
        if character in braces:
            stack.append(character)
            # 위의 알고리즘과 같이 쌍이 되는 것들은 pop을 해서 확인함으로 stack이 비게 된다.
        elif stack == [] or braces[stack.pop()] != character:
            return False
    return stack == []