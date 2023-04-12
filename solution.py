import pandas as pd
import numpy as np


chat_id = 1124136722 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return (y_success/y_cnt - x_success/x_cnt) > 0.07 # Ваш ответ, True или False
