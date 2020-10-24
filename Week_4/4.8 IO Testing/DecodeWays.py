def numDecodings(s: str) -> int:
    if s[0] == '0':
        return 0

    dp = [0 for i in range(len(s) + 1)]

    dp[0] = 1
    dp[1] = 1

    for i in range(2, len(s) + 1):
        curr = int(s[i - 1:i])
        curr_last = int(s[i - 2:i])
        if curr >= 1 and curr < 10:
            dp[i] += dp[i - 1]

        if curr_last >= 10 and curr_last < 27:
            dp[i] += dp[i - 2]

    return dp[len(s)]
if __name__ == "__main__":

    numDecodings(s="121215353")