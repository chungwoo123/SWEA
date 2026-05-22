from collections import deque

def bfs(graph, start, visited):
    #큐 생성
    queue = deque([start])
    #현재 노드를 방문 처리
    visited[start] = True
    #큐가 빌 때까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end = '')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,6],
    [3,6],
    [4,5,7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

bfs(graph, 1, visited)