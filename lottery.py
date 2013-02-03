# coding: utf-8

import math
import sys
import random

"""
Usage: python lottery.py <"digit,digit,digit,digit,digit"> <ticket_number>
ex) python lottery.py 5,10,20,30,40 5
カンマ区切りの5個の数字と、購入枚数。



1から40までの数字の中から、5つの数字を選んで、一口500円で購入します。

集まったお金の40％は主催者の取り分です。
残りの60％が当籤金として支払われます。

- 全体の売り上げ金額
- 主催者の取り分
- 当たりの数字
- 1等から3等までの当籤口数と当籤金額
- あらかじめ選んだ数字の当籤状況
"""
PRICE = 500
TICEKTS_SELL_RANGE = (200000, 300000)

def main(user_ticket, user_ticket_num):

    # エラーハンドリング
    user_ticket, user_ticket_num = sys.argv[1], sys.argv[2]
    for x in user_ticket.split(","):
        if not 1 <= int(x) <= 40:
            raise Exception(u"そんな数字は選べません")
    user_ticket = frozenset([int(x) for x in user_ticket.split(",")])

    # 販売
    bought_tickets, share = sell(user_ticket, user_ticket_num)

    # 1等抽選
    bingo = lottery()
    print "当たりの数字", ",".join([str(x) for x in bingo])

    # 配当数カウント
    prizes = count_prize(bought_tickets, bingo, share)

    # 自分の当たりくじ
    rank = check_user_ticket(prizes, user_ticket)
    if rank:
        print "User is {} prize".format(rank)


def check_user_ticket(prizes, user_ticket):
    for rank, prizes in enumerate(prizes):
        rank = rank + 1
        if user_ticket in prizes:
            return rank
            # print "User is {} prize".format(rank + 1)

def sell(user_ticket, user_ticket_num):
    ''' 発売と配当金額の決定'''
    ticket_num =  random.randint(*TICEKTS_SELL_RANGE)
    bought_tickets = make_dummy_ticket(ticket_num)
    bought_tickets = add_user_ticket(bought_tickets, user_ticket, user_ticket_num)
    sales = ticket_num * PRICE
    sponser_profit = int(math.ceil(sales * 0.6))
    share = sales - sponser_profit
    # print "発売枚数", ticket_num
    print "全体の売り上げ金額", sales
    print "主催者の取り分", sponser_profit
    return bought_tickets, share


def count_prize(bought_tickets, bingo, share):
    first_prizes = pickup_prize(bought_tickets, bingo, allow_diff=0)
    second_prizes = pickup_prize(bought_tickets, bingo, allow_diff=1)
    third_prizes = pickup_prize(bought_tickets, bingo, allow_diff=2)

    first_share = int(share / 2.0)
    second_share = int(share / 3.0)
    third_share = int(share / 6.0)
    print "1等", disp_prize(first_prizes, first_share)
    print "2等", disp_prize(second_prizes, second_share)
    print "3等", disp_prize(third_prizes, third_share)

    return [first_prizes, second_prizes, third_prizes]


def disp_prize(prizes, share):
    all_number = 0
    for tickets, number in prizes.items():
        # print ",".join([str(x) for x in tickets]), number,
        all_number += number
    if all_number:
        print "{}口,{}円".format(all_number, int(share / float(all_number))),
    else:
        print "なし",
    return ""


def pickup_prize(tickets, bingo, allow_diff=0):
    ''' 差集合が1なら1個だけズレてる。'''
    prizes = {}
    for ticket, number in tickets.items():
        diff = bingo - ticket
        if len(diff) == allow_diff:
            prizes[ticket] = prizes.get(ticket, 0) + number
    return prizes


def lottery():
    base_numbers = range(1, 40 + 1)
    ticket = frozenset(random.sample(base_numbers, 5))
    return ticket


def add_user_ticket(tickets, user_ticket, user_ticket_num):
    for _ in range(int(user_ticket_num)):
        tickets[user_ticket] = tickets.get(user_ticket, 0) + 1
        # print user_ticket, tickets[user_ticket]
    return tickets


def make_dummy_ticket(ticket_num):
    '''
    1から40までの数字の中から、5つの数字を選んで、
    当選番号と口数のdictで返す
    '''
    tickets = {}
    base_numbers = range(1, 40 + 1)
    for _ in range(ticket_num):
        ticket = frozenset(random.sample(base_numbers, 5))
        tickets[ticket] = tickets.get(ticket, 0) + 1
    return tickets


if __name__ == "__main__":
    #                   選択番号 口数
    # python lottery.py 5,10,20,30,40    5
    main(sys.argv[1], sys.argv[2])


import unittest
class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.bingo = frozenset([5, 10, 20, 30, 40])
        self.user_ticket_num = 1
        self.bought_tickets = make_dummy_ticket(10)
        self.share = 4000

    def test_first_prize(self):
        user_ticket = frozenset([5, 10, 20, 30, 40])
        self.bought_tickets[user_ticket] = 1
        prizes = count_prize(self.bought_tickets, self.bingo, self.share)
        rank = check_user_ticket(prizes, user_ticket)
        self.assertEqual(rank, 1)

    def test_second_prize(self):
        user_ticket = frozenset([1, 5, 10, 20, 30])
        self.bought_tickets[user_ticket] = 1
        prizes = count_prize(self.bought_tickets, self.bingo, self.share)
        rank = check_user_ticket(prizes, user_ticket)
        self.assertEqual(rank, 2)

    def test_third_prize(self):
        user_ticket = frozenset([1, 2, 5, 10, 20])
        self.bought_tickets[user_ticket] = 1
        prizes = count_prize(self.bought_tickets, self.bingo, self.share)
        rank = check_user_ticket(prizes, user_ticket)
        self.assertEqual(rank, 3)


# if __name__ == "__main__":
#     unittest.main()
