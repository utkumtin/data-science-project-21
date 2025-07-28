import numpy as np
from scipy import stats

# Açıklama: Verilen büyü başarı sonuçlarının (1=başarılı, 0=başarısız) 
# ortalama başarı oranını döndürür.
# Input: spell_results: List[int]
# Output: float (0 ile 1 arasında)
# Örnek:
# calculate_mean_success_rate([1, 0, 1, 1]) → 0.75
def calculate_mean_success_rate(spell_results):
    return np.mean(spell_results)

# Açıklama: İki büyü grubunun başarı oranlarının farkını Z-Test ile karşılaştırır.
# Input: sample1: List[int], sample2: List[int]
# Output: (z_stat: float, p_value: float)
# Örnek:
# perform_z_test([1,0,1,1], [0,1,0,0]) → (z_stat=1.41, p_value=0.15)
def perform_z_test(sample1, sample2):
    mean1 = np.mean(sample1)
    mean2 = np.mean(sample2)
    n1 = len(sample1)
    n2 = len(sample2)
    error = np.sqrt((mean1 * (1 - mean1) / n1) + (mean2 * (1 - mean2) / n2))
    z_stat = (mean1 - mean2) / error
    p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))

    return z_stat, p_value

# Açıklama: İki grubun başarı oranları arasındaki farkı T-Test ile karşılaştırır.
# Input: sample1: List[int], sample2: List[int]
# Output: (t_stat: float, p_value: float)
# Örnek:
# perform_t_test([3,4,5], [2,3,2]) → (1.5, 0.18)
def perform_t_test(sample1, sample2):
    t_stat, p_value = stats.ttest_ind(sample1, sample2)
    return t_stat, p_value

# Açıklama: Büyü türleri ve başarı durumları arasındaki bağımsızlığı test eder.
# Input: contingency_table: List[List[int]]
# Örnek: [[10, 5], [6, 9]] (2x2 tablo)
# Output: (chi_stat: float, p_value: float)
# Örnek:
# perform_chi_square_test([[10, 5], [6, 9]]) → (1.20, 0.27)
def perform_chi_square_test(contingency_table):
    chi2, p, dof, e = stats.chi2_contingency(contingency_table)
    return chi2, p

# Açıklama: 3 veya daha fazla büyü grubunun başarı oranlarını ANOVA testi ile karşılaştırır.
# Input: *groups: List[List[int]]
# Output: (f_stat: float, p_value: float)
# Örnek:
# perform_anova_test([1,2,3], [2,2,2], [3,3,3]) → (4.5, 0.03)
def perform_anova_test(*groups):
    f_stat, p_value = stats.f_oneway(*groups)
    return f_stat, p_value

# Açıklama: Verilen başarı oranıyla n adet rastgele 1/0 sonucu döndürür.
# Input: n: int, success_rate: float (0-1 arası)
# Output: List[int]
# Örnek:
# generate_random_spell_results(5, 0.6) → [1,0,1,1,0]
def generate_random_spell_results(n, success_rate):
    return np.random.binomial(1, success_rate, n).tolist()


# Açıklama: İki büyüyü Z-Test ve T-Test ile karşılaştırır ve sonucu döndürür.
# Input: spell1_results: List[int], spell2_results: List[int]
# Output: Dict (z ve t test sonuçları)
# Örnek:
# compare_spells([1,1,0], [0,0,1])  → {'z': (1.23, 0.21), 't': (1.10, 0.28)}
def compare_spells(spell1_results, spell2_results):
   mean1 = np.mean(spell1_results)
   mean2 = np.mean(spell2_results)
   n1 = len(spell1_results)
   n2 = len(spell2_results)
   error = np.sqrt((mean1 * (1 - mean1) / n1) + (mean2 * (1 - mean2) / n2))
   z_stat = (mean1 - mean2) / error
   p_value_z = 2 * (1 - stats.norm.cdf(abs(z_stat)))

   t_stat, p_value_t = stats.ttest_ind(spell1_results, spell2_results)

   return {'z': (z_stat, p_value_z), 't': (t_stat, p_value_t)}


# Açıklama: İki büyü arasındaki fark anlamlı mı (p<0.05)?
# Input: spell1_results, spell2_results, alpha
# Output: bool
# Örnek:
# is_spell_significant([1,1,1], [0,0,0], alpha=0.05) → True
def is_spell_significant(spell1_results, spell2_results, alpha=0.05):
   t, p = stats.ttest_ind(spell1_results, spell2_results)
   return p < alpha


"""
    Bu fonksiyon, büyü (spell) sonuçlarını içeren bir liste veya sözlükten,
    özet istatistiksel bilgiler çıkararak okunabilir bir rapor üretmek için kullanılır.

    Parametre:
    ----------
    spell_results : list[dict] veya dict
        Her bir büyüye (spell) ait başarı, hasar, mana kullanımı, isabet oranı gibi
        bilgileri içeren veri yapısıdır.

        Örnek giriş (list biçiminde):
        [
            {"name": "Fireball", "damage": 150, "mana": 40, "hit": True},
            {"name": "Ice Spike", "damage": 100, "mana": 30, "hit": False},
            {"name": "Ice Spike", "damage": 100, "mana": 30, "hit": True}}
            ...
        ]

    Fonksiyonun Görevi:
    -------------------
    - Her büyünün kaç kez kullanıldığını,
    - Toplam ve ortalama hasarını,
    - Toplam mana tüketimini,
    - Başarı oranlarını (kaç kez isabet etti),
    - En etkili büyüleri belirleyerek

    güzel formatlanmış bir şekilde ekrana yazdırmak veya döndürmek olabilir.

    Dönüş:
    ------
    str veya dict
        Rapor stringi veya özet bilgileri içeren sözlük dönebilir.
"""
def generate_spell_summary_report(spell_results):
    if isinstance(spell_results, dict):
        spell_results = [spell_results]
        
    report = {}
    for i in spell_results:
        name = i['name']
        if name not in report:
            report[name] = {
                'count': 0,
                'total_damage': 0,
                'total_mana': 0,
                'hits': 0,
                'hit_rate': 0.0,
                'average_damage': 0.0
            }
        report[name]['count'] += 1
        report[name]['total_damage'] += i['damage']
        report[name]['total_mana'] += i['mana']
        report[name]['hits'] += 1 if i['hit'] else 0
        
    for name, stats in report.items():
        stats['hit_rate'] = (stats['hits'] / stats['count']) * 100
        stats['average_damage'] = stats['total_damage'] / stats['count']
        
    return report