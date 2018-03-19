"""
Chef Judges a Competition Problem Code: CO92JUDG

Chef is the judge of a competition. There are two players participating in this competition — Alice and Bob.

The competition consists of N races. For each i (1 ≤ i ≤ N), Alice finished the i-th race in Ai minutes, while Bob finished it in Bi minutes. The player with the smallest sum of finish times wins. If this total time is the same for Alice and for Bob, a draw is declared.

The rules of the competition allow each player to choose a race which will not be counted towards their total time. That is, Alice may choose an index x and her finish time in the race with this index will be considered zero; similarly, Bob may choose an index y and his finish time in the race with this index will be considered zero. Note that x can be different from y; the index chosen by Alice does not affect Bob's total time or vice versa.

Chef, as the judge, needs to announce the result of the competition. He knows that both Alice and Bob play optimally and will always choose the best option. Please help Chef determine the result!

"""

t=int(input())
 
while(t!=0):
    t=t-1
    n=int(input())
    alice=[int(x) for x in input().strip().split()]
    bob=[int(x) for x in input().strip().split()]
    x=alice.index(max(alice))
    y=bob.index(max(bob))
    del(alice[x])
    del(bob[y])
    sum_alice=sum(alice)
    sum_bob=sum(bob)
    if(sum_alice<sum_bob):
        print("Alice")
    elif(sum_bob<sum_alice):
        print("Bob")
    else:
        print("Draw")  