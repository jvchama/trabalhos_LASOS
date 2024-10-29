import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
test = pd.read_excel("BANCO_LIMPO_INT.xlsx")
numeric_var = ['age', 'height', 'weight', 'bmi', 'income', 'score_food_smile', "score_subs_smile", "score_PA_smile", "score_stress_smile", "score_social_smile", "score_sleep_smile", "score_envir_smile", "scoretot_smile"]
categorical_var = ["university", "sex", "gender_identity", "sexual_orientation", "ethnic_group", 'marital_status', 'student_accommodation', "work", 'RENDA_categorias', 'student_of', 'sedentary_behavior', "sedentary_2", "PHQ9_CLASS_COM OU SEM SINTOMAS_ABAIXO ACIMA DO PONTO DE CORTE >9", "PHQ9_CLASSIFICAÇÃO SEVERIDADE", "GAD7_class__COM OU SEM SINTOMAS_ABAIXO ACIMA DO PONTO DE CORTE >9", "GAD7_CLASSIFICAÇÃO SEVERIDADE" ]
corr_matrix_num_pearson = test[numeric_var].corr(method = 'pearson')
corr_matrix_num_kendall= test[numeric_var].corr(method = 'kendall')
corr_matrix_num_spearman= test[numeric_var].corr(method = 'spearman')
print(corr_matrix_num_pearson)

print(corr_matrix_num_kendall)
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix_num_spearman, annot=True, cmap='coolwarm', center=0, linewidths=0.5)
plt.title('Correlation Matrix (Spearman))')
plt.show()