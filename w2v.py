from gensim.models.word2vec import KeyedVectors

model = KeyedVectors.load_word2vec_format("/Users/zhung/py/meeting/tmunlp_1.6B_WB_300dim_2020v1.bin.gz",
                                                            unicode_errors='ignore', 
                                                            binary=True)

def help():
    print("press h call help")
    print("press q quit process")

def similar (s1:str,s2:str):
    ## Cosine similarity Value 1 to -1 heighest value more similarity
    print(f"{s1},{s2} Cosine similarity Value")
    print(model.similarity(s1,s2))

def most_similar(s:str,top):
    print(f"{s} 相似詞")
    for w, sim in model.most_similar(s,topn=top):
        print((w,sim))

def main():
    help()
    while 1:
        cmd = str(input())
        match cmd:
            case "s":
                print("Input similar word")
                arg = input()
                similar(arg)
            case "m":
                print("Input similar word to List")
                arg = input()
                arr = arg.split(" ")
                most_similar(arr[0],arr[1])
            case "q":
                break
            case _:
                print("You have some err")
                help()

main()
