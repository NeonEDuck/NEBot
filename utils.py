from typing import Iterator
from datetime import datetime, timedelta

def get_bit_positions(n: int) -> Iterator[int]:
    """分解二進位數字後將bit位置傳回
    
    主要用於設定資料上，例：
    13 -> 1101
    將傳回：
    1, 4, 8
    """
    while n:
        b: int = n & (~n+1) # 1101 AND ( NOT 0010 + 1 ) => 0001
        yield b
        n ^= b              # 1101 XOR 0001             => 1100

def utc_plus(hours: int) -> datetime:
    """回傳UTC+n的時間
    
    回傳UTC+n的時間。
    """
    return datetime.utcnow() + timedelta(hours=hours)