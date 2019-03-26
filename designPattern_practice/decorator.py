"""
Creates objects/function with wrapping classes/function

主要精神：wrapping (層層包裝)
若有需要共用之基本函式，且又要基於此去做修改，則可以此方式包裝並建立個別方法
寫 log 最常見  *避免過度包裝，降低可讀性*
"""

def printLog(msg):
    print(msg)

def starWrap(method, msg):
    print("******************")
    method(msg)
    print("******************")

def lineWrap(method, msg):
    print("------------------")
    method(msg)
    print("------------------")



if __name__ == "__main__":
    starWrap(printLog, "hihihihihih")
    print("")
    lineWrap(printLog, "hihihihihih")


