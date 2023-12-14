from data_processor import DataProcessor
from bcolors import bcolors

dp = DataProcessor()
doc_size_test = 4
for i in range(doc_size_test):
    dp.add_file(f"tests/doc{i}")
dp.generate()
def test_occur_dict():
    # testing the validity edge cases
    tests = [(dp.occur_dict["lorem"],{1:[1, 0, 0], 3:[2, 0, 1, 0, 1, 1, 0, 0]}),
             (dp.occur_dict["test"], {0:[1,0,1,0], 1:[0,1,1]}),
             (dp.occur_dict["the"], {2:[0,2,0]}),
             (dp.occur_dict["this"], {0:[2,1,1,1],1:[0,1,0],2:[0,0,1]}),
             ]
    for actual,test in tests:
        # t sands for test, a stands for actual
        for adict, tdict in zip(actual.items(), test.items()):
            akey, aarray = adict
            tkey, tarray = tdict
            assert aarray.tolist() == tarray
            assert akey == tkey

def test_document_occurences():
    assert(dp.document_occurences("lorem", 1) == 1)
    assert(dp.document_occurences("lorem", 3) == 5)
    assert(dp.document_occurences("this", 3) == 0)
    assert(dp.document_occurences("this", 0) == 5)

def test_occurences():
    assert(dp.occurences("this") == 7)
    assert(dp.occurences("lorem") == 6)

def test_error_handling():
    # error handling
    try:
        dp.occurences("madeupword")
        assert(False)
    except(RuntimeError):
        pass
    try:
        dp.document_occurences("test",doc_size_test)
        assert(False)
    except(RuntimeError):
        pass
    try:
        dp.document_occurences("test",-1)
        assert(False)
    except(RuntimeError):
        pass

test_occur_dict() 
test_document_occurences()
test_occurences()
test_error_handling()
print(bcolors.BOLD+bcolors.GREEN+"Tests are completed successfully!"+bcolors.ENDC)
