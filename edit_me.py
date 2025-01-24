
def monotonic(lst):
    """Return True if lst is monotonic; return False, otherwise."""
    if not lst or len(lst) == 1:
        return  True
    
    increasing = True
    decreasing = True

    for i in range(1, len(lst)):
        if lst[i]>lst[i-1]:
            decreasing = False
        elif lst[i]<lst[i-1]:
            increasing = False
            
        
    return increasing or decreasing 
    
  
print(monotonic([1,2,3,4,5,5,6,7]))
print(monotonic([7,6,5,4,3,2,1]))
print(monotonic([11,8,20,7,6,5,100]))
print(monotonic([100]))
print(monotonic([]))
print(monotonic([1,3,1,3,4,5,32,1]))





#
# Feel free to replace these comments with
# code that tests your function monotonic.
#
