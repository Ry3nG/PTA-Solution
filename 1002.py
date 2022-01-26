n = input("")
i_sum = 0
pinyin = ["ling", "yi", "er", "san", "si", "wu","liu", "qi", "ba", "jiu"]
for i in range(len(n)):
    i_sum += int(n[i])
i_sum_string = str(i_sum)
for i in range(len(i_sum_string)-1):
    print(pinyin[int(i_sum_string[i])], end=" ")

print(pinyin[int(i_sum_string[-1])], end="")
