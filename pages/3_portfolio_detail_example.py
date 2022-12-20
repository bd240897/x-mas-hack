import streamlit as st
import json
import matplotlib.pyplot as plt

st.title('Пример страницы с более подробным описанием портфеля')

# ГРУЗИМ ДАННЫЕ ИЗ JSON

with open('example.json', encoding='utf-8') as f_in:
    portfolio_1 = json.load(f_in)

# СТРОИМ ГРАФИК

st.write()
values = [a.get("count") for a in portfolio_1.get("structure")]
labels = [a.get("name") for a in portfolio_1.get("structure")]
fig1, ax1 = plt.subplots()
ax1.pie(values, labels=labels)
ax1.axis('equal')
plt.show()
st.pyplot(fig1)

# ПОДРОБНОЕ ОПИСАНИЕ

st.header("Подробное описание")

# количество групп компаний
count_group = len(portfolio_1.get("structure"))
# создаем колонки
col_list = st.columns(3)

# пробегаем по всем группам
for i in range(count_group):
    # создаем колонки
    with col_list[i]:
        name_group = portfolio_1.get("structure")[i].get("name")
        name_company_list = portfolio_1.get("structure")[i].get("types")
        st.write(f"__{name_group}__")
        # достаем название каждой компании
        for j, name_company in enumerate(name_company_list):
                st.write(name_company)
