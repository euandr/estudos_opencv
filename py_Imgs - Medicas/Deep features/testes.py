import pandas as pd


file_path = r'C:\Users\andre\Documents\atividades\estudos_opencv\py_Imgs - Medicas\Deep features\testand0.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')


metric_columns = ['accuracy', 'specificity', 'recall', 'precision', 'f1-score', 'kappa', 'auc-roc']
weight = 1 / len(metric_columns)

# Calcular a média ponderada de todas as métricas
df['Weighted_Score'] = df[metric_columns].apply(lambda row: row * weight).sum(axis=1)

# Encontrar o classificador com o melhor desempenho
best_classifier = df.loc[df['Weighted_Score'].idxmax()]

print(f"O melhor classificador é: {best_classifier['Classificador']}")
print(f"Métricas do melhor classificador:\n{best_classifier}")
