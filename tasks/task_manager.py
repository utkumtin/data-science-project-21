import numpy as np
from scipy import stats

# Açıklama: Verilen büyü başarı sonuçlarının (1=başarılı, 0=başarısız) 
# ortalama başarı oranını döndürür.
# Input: spell_results: List[int]
# Output: float (0 ile 1 arasında)
# Örnek:
# calculate_mean_success_rate([1, 0, 1, 1]) → 0.75
def calculate_mean_success_rate(spell_results):
    pass

# Açıklama: İki büyü grubunun başarı oranlarının farkını Z-Test ile karşılaştırır.
# Input: sample1: List[int], sample2: List[int]
# Output: (z_stat: float, p_value: float)
# Örnek:
# perform_z_test([1,0,1,1], [0,1,0,0]) → (z_stat=1.41, p_value=0.15)
def perform_z_test(sample1, sample2):
    pass

# Açıklama: İki grubun başarı oranları arasındaki farkı T-Test ile karşılaştırır.
# Input: sample1: List[int], sample2: List[int]
# Output: (t_stat: float, p_value: float)
# Örnek:
# perform_t_test([3,4,5], [2,3,2]) → (1.5, 0.18)
def perform_t_test(sample1, sample2):
    pass

# Açıklama: Büyü türleri ve başarı durumları arasındaki bağımsızlığı test eder.
# Input: contingency_table: List[List[int]]
# Örnek: [[10, 5], [6, 9]] (2x2 tablo)
# Output: (chi_stat: float, p_value: float)
# Örnek:
# perform_chi_square_test([[10, 5], [6, 9]]) → (1.20, 0.27)
def perform_chi_square_test(contingency_table):
   pass

# Açıklama: 3 veya daha fazla büyü grubunun başarı oranlarını ANOVA testi ile karşılaştırır.
# Input: *groups: List[List[int]]
# Output: (f_stat: float, p_value: float)
# Örnek:
# perform_anova_test([1,2,3], [2,2,2], [3,3,3]) → (4.5, 0.03)
def perform_anova_test(*groups):
    pass

# Açıklama: Verilen başarı oranıyla n adet rastgele 1/0 sonucu döndürür.
# Input: n: int, success_rate: float (0-1 arası)
# Output: List[int]
# Örnek:
# generate_random_spell_results(5, 0.6) → [1,0,1,1,0]
def generate_random_spell_results(n, success_rate):
    pass


# Açıklama: İki büyüyü Z-Test ve T-Test ile karşılaştırır ve sonucu döndürür.
# Input: spell1_results: List[int], spell2_results: List[int]
# Output: Dict (z ve t test sonuçları)
# Örnek:
# compare_spells([1,1,0], [0,0,1])  → {'z': (1.23, 0.21), 't': (1.10, 0.28)}
def compare_spells(spell1_results, spell2_results):
   pass

# Açıklama: İki büyü arasındaki fark anlamlı mı (p<0.05)?
# Input: spell1_results, spell2_results, alpha
# Output: bool
# Örnek:
# is_spell_significant([1,1,1], [0,0,0], alpha=0.05) → True
def is_spell_significant(spell1_results, spell2_results, alpha=0.05):
   pass


# Açıklama: İki büyü arasındaki fark anlamlı mı (p<0.05)?
# Input: spell1_results, spell2_results, alpha
# Output: bool
# Örnek:
# is_spell_significant([1,1,1], [0,0,0], alpha=0.05) → True
def generate_spell_summary_report(spell_results):
   pass