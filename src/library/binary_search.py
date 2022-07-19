from typing import Any
# これらの関数はmain関数の内側で定義し、judge関数の中で使うものも引数にとらなくて済むようにする


def binary_search_int(ok: int, ng: int) -> int:
    """二分探索を行い、条件を満たす最小/最大の整数を返す

    Args:
        ok (int): 必ず条件を満たす値
        ng (int): 条件を満たすことがあり得ない値

    Returns:
        int: 条件を満たす最小/最大の整数
    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if judge(mid):
            ok = mid
        else:
            ng = mid
    return ok


def judge(mid: Any) -> bool:
    """条件を満たすかどうか判定する関数

    Args:
        mid (Any):

    Returns:
        bool: 条件を満たすならTrue
    """
    return True
