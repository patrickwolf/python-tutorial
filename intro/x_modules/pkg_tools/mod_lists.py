def get_unique_list(lst):
    tmpset=set(lst)
    tmplist = list(tmpset)
    return tmplist
    
if __name__ == '__main__':
    print get_unique_list([1,2,1,3,5])