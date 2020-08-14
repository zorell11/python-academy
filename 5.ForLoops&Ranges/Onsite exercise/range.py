




def main():
    print(list(range(20)))
    print(list(range(15, 20)))
    print(list(range(10,20,3)))

    nums = []
    nums1 = []
    for i in range(1,101):
        #nums.append(i) if (i%5 == 0)
        if i%5 == 0:
            nums.append(i)

        #nums1.append(i) if (i%5)==0 else break
    #print(nums1)
    print(nums)


if __name__ == "__main__":
    main()
