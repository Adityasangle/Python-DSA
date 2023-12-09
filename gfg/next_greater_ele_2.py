# a element's index can be added to the stack if and only if the current index's element is smaller or equal to stacks tops element
#while stack is non empty and current element is greater than stack tops element, we need to add current ele to our ans


def nextgreater2(arr):
    st = []
    n = len(arr)
    ans = [-1]*n
    for i in range(n*2):
        while st and arr[i%n]>arr[st[-1]]:
            ans[st[-1]] = arr[i%n]
            st.pop()
        if i<n:
            st.append(i)
    return ans