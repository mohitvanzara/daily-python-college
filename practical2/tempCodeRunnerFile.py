ls = [1,1,1,1,4,4,4,3,3,1,2,2]
# for i in set(ls):
#     cnt =0
#     for j in ls:
#         if i==j:
#             cnt+=1
#     print(i,cnt)

# i and j is my value not index


# using frequency dictionary
freq = {}
for num in ls:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
for key ,value in freq.items():
    print(f'key:{key} value:{value}')
