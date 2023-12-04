from gensim.models.word2vec import KeyedVectors

print("Load Model...")
model = KeyedVectors.load_word2vec_format("/Users/zhung/py/meeting/tmunlp_1.6B_WB_300dim_2020v1.bin.gz",
                                                            unicode_errors='ignore', 
                                                            binary=True)
print("Load Model Complete!!")
print("===========================================")

def help():
    print("press h call help")
    print("press s search two similar cosine similarity value")
    print("press m search similar term for top n")
    print("press g judge two term are similar ?")
    print("press q quit process")

def vector(s:str):
    print(model[s])

def similar (s1:str,s2:str) -> float:
    ## Cosine similarity Value 1 to -1 heighest value more similarity
    return model.similarity(s1,s2)

def most_similar(s:str,top:int):
    print(f"{s} 相似詞")
    for w, sim in model.most_similar(s,topn=top):
        print((w,sim))

def main():
    help()
    print("===========================================")
    while 1:
        print("Input your command")
        cmd = str(input())
        match cmd:
            case "s":
                print("Input similar word")
                arg = input()
                arr = arg.split(" ")
                if len(arr) != 2:
                   print("Not have enough parameter。")
                   print("parameter1 : similar term 1 ,parameter2 : similar term 2")
                else:
                    print(f"{arr[0]},{arr[1]} Cosine similarity Value")
                    print(similar(arr[0],arr[1]))
            case "m":
                print("Input similar word to List")
                arg = input()
                arr = arg.split(" ")
                if len(arr) != 2:
                    print("Not have enough parameter。")
                    print("parameter1 : similar term,parameter2 : topNum")
                else:
                    most_similar(arr[0],int(arr[1]))
            case "q":
                print("program complete")
                break
            case "v":
                print("Input you want to search vector str")
                arg = input()
                vector(arg)
            case "g":
                print("Input str to judge similar")
                arg = input()
                arr = arg.split(" ")
                if similar(arr[0],arr[1]) > 0.5:
                    print(f"True {arr[0]},{arr[1]} similar")
                else:
                    print(f"False {arr[0]},{arr[1]} not similar")
            case _:
                print("You have some err")
                help()
        print("===========================================")

main()

