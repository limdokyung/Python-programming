#12
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h"]
nums = [i for i in range(20)]
answer = [alpha+str(num) for alpha in alphabet for num in nums if num%2==0]
print(len(answer))
#a~h를 각 값으로 하는 알파벳 리스트를 생성하고, 0~19까지를 값으로하는
#넘스 리스트를 생성한다. 
#알파벳의 리스트의 크기만큼 for문을 만들어 그 안에 넘스크기만큼의 for문을 삽입하고
#짝수 num과 알파벳을 조합하여 알파+넘을 새로운 앤써 리스트에 저장한다.
#넘을 문자열형태로 만들어야 문자열인 알파에 붙일수있다.
#그러므로 알파 8개의 값에 각각 10개의 짝수들이 조합되어 8*10, 즉 80개의 
#값이 앤써에 생성된다. 그러므로 len(answer) == 80