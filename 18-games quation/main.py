
# لعبة السؤال
secret_answer="cairo"
answer=""
count=0
limit=3
lose=False
while secret_answer != answer and not lose:
    if count < limit:
        answer=input("what's is capital of egypt ?")
        count +=1
    else:
        lose=True
if lose:
    print("you lose")
else:
    print("you win ")
