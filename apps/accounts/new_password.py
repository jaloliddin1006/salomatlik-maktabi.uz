from random import sample
elements=['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

code_length=8
def new_password(elements):
    random_code=sample(elements, k=code_length)
    
    result=''.join(random_code)
    return result

eee=new_password(elements)
print(eee)