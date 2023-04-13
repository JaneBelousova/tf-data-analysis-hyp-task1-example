import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 1124136722 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alfa=0.07
    threshold = x_success/x_cnt
    conversion = y_success/y_cnt # наше ограничение слева
    p = norm.cdf(np.sqrt(y_cnt) * (conversion - threshold) / np.sqrt(conversion * (1 - conversion)))
    return p >= (1 - alfa) # Ваш ответ, True или False
