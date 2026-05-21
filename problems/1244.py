import sys

def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    idx = 1
    
    for t in range(1, T + 1):
        if idx >= len(input_data):
            break
            
        num_str = input_data[idx]
        swaps = int(input_data[idx+1])
        idx += 2
        
        q = {num_str}
        
        for _ in range(swaps):
            next_q = set()
            for s in q:
                s_list = list(s)
                n = len(s_list)
                # Generate all possible strings by swapping two different positions
                for i in range(n):
                    for j in range(i + 1, n):
                        s_list[i], s_list[j] = s_list[j], s_list[i]
                        next_q.add("".join(s_list))
                        s_list[i], s_list[j] = s_list[j], s_list[i] # backtrack
            q = next_q
            
        # Find the maximum value among all possible results
        ans = max(int(x) for x in q)
        print(f"#{t} {ans}")

if __name__ == '__main__':
    solve()
