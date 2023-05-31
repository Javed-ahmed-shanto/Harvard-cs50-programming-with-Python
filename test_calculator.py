from calculator import sqaure

# def main():
#     test_sqaure()
    
def test_positive():
    assert sqaure(2) == 4
    assert sqaure(3) == 9

def test_negetive():
    assert sqaure(-2) == 4
    assert sqaure(-3) == 9

def test_zero():
    assert sqaure(0) == 0    
  
# if __name__ == "__main__":
#     main()
# using python -m pytest .\test_calculator.py