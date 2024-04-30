def solution(tickets):
    answer = []
    # 간선의 개수
    N = len(tickets)
    # 인접 리스트를 딕셔너리 형태로 하자! (문자열이므로)
    adj = {}

    # 인접 리스트 작성하기
    # 이게 되네 (애용할 듯)
    for ticket in tickets:
        adj[ticket[0]] = adj.get(ticket[0], []) + [ticket[1]]

    # 알파셋 순서의 역순으로 정렬 - 리스트여서 pop으로 뺄 것임
    # 즉, 뒤에서부터 뺄 것임
    for a in adj:
        adj[a].sort(reverse=True)

    Q = []
    Q.append("ICN")  # 항상 ICN 공항에서 시작

    while Q:
        # 지금 놈 파악
        now = Q[-1]

        # 지금 놈이 있는 애이고 인접한 애가 있다면
        if now in adj and adj[now]:
            Q.append(adj[now].pop())
        else:
            answer.append(Q.pop())


    # 뒤집어주기
    answer.reverse()

    return answer


print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))