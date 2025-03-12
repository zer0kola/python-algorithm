def solution(nums):
    origin_len = len(nums)
    set_len = len(set(nums))
    return set_len if set_len < origin_len / 2 else origin_len / 2