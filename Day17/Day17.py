class User:

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
count=0
Q1 = User("Con Cho co may chan ?", "4")
print("Q1: "+Q1.question)
A1=input("\nAnswer: ")
if (A1==Q1.answer):
    print("True")
    count+=1
    print(f"Score: {count}")
else:
    print("False")
    print(f"Score: {count}")
Q2 = User("Con meo co long khong ?", "khong")
print("Q2: "+Q2.question)
A2=input("\nAnswer: ").lower()
if (A2==Q2.answer):
    print("True")
    count+=1
    print(f"Score: {count}")
else:
    print("False")
    print(f"Score: {count}")

