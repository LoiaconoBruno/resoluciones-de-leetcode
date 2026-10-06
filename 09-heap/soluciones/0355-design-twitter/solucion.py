# 355. Design Twitter (Media)
# https://leetcode.com/problems/design-twitter/
#
# Idea: cada usuario guarda sus tweets con un contador global como "hora" y el set de a quién sigue;
#       el feed mezcla los últimos tweets de cada seguido con un heap y corta en 10.
# Tiempo: O(1) post/follow/unfollow; getNewsFeed O(f + 10 log f), con f los seguidos · Espacio: O(usuarios + tweets)

import heapq
from collections import defaultdict
from typing import List


class Twitter:
    def __init__(self):
        self.hora = 0
        self.tweets = defaultdict(list)
        self.sigue = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.hora -= 1
        self.tweets[userId].append((self.hora, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for u in self.sigue[userId] | {userId}:
            if self.tweets[u]:
                i = len(self.tweets[u]) - 1
                hora, tweet = self.tweets[u][i]
                heap.append((hora, tweet, u, i - 1))
        heapq.heapify(heap)
        feed = []
        while heap and len(feed) < 10:
            _, tweet, u, i = heapq.heappop(heap)
            feed.append(tweet)
            if i >= 0:
                hora, siguiente = self.tweets[u][i]
                heapq.heappush(heap, (hora, siguiente, u, i - 1))
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.sigue[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.sigue[followerId].discard(followeeId)


if __name__ == "__main__":
    t = Twitter()
    t.postTweet(1, 5)
    assert t.getNewsFeed(1) == [5]
    t.follow(1, 2)
    t.postTweet(2, 6)
    assert t.getNewsFeed(1) == [6, 5]
    t.unfollow(1, 2)
    assert t.getNewsFeed(1) == [5]
    for i in range(20):
        t.postTweet(3, 100 + i)
    t.follow(1, 3)
    assert t.getNewsFeed(1) == list(range(119, 109, -1))
    print("OK")
