def is_vampire(hour, awake) :
    if ((hour<6 or hour>22) and awake)or(hour>=6 and hour<22and awake==False) :
        print("vampire")
        return True
        
    else:
        print("human")
        return False
        
def test_is_vampire(hour, awake, expected) :    
    if is_vampire(hour, awake) == expected:
        print("pass!")
    else:
        print("FAILLLLL")
        
#test_is_vampire(6.5, True, False) test_is_vampire(6.5, False, True) test_is_vampire(3, True, True) test_is_vampire(3, False, False)


def good_deal(ogPrice, salePrice) :
    if (salePrice<.75*ogPrice) :
        print("Buy!")
        return True
    print("Bad deal!")
    return False

def test_good_deal(ogPrice, salePrice, expected) :
    if(good_deal(ogPrice, salePrice)==expected) :
        print("pass")
        return True
    print("Fail!")

test_good_deal(100,50,True)
test_good_deal(100,90,False)
