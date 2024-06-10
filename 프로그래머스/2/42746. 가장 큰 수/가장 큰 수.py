def solution(nums) :
    def expand_str(st: str) :
        exp_s = st * 4
        return exp_s[:4]
    str_arr = map(str, nums)
    sotred_str_nums = sorted(str_arr, key = expand_str, reverse = True)
    answer = ''.join(sotred_str_nums)

    return str(int(answer)) 