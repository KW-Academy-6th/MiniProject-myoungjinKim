def solution(nums):
    
    count = len(nums) #폰켓몬의 마릿루를 구한다.
    type = len(set(nums)) #폰켓몬의 종류의 개수를 구한다.
    
    return count//2 if count//2 < type else type #마릿수/2와 종류의 수 중 작은 쪽이 반환됩니다. 