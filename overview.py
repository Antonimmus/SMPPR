import streamlit as st
st.markdown(
        """
       <style>
                       
            [data-testid="stMarkdownContainer"]{
                text-align :justify;
            }
            
    
            
        </style>

        
        """,
        unsafe_allow_html=True,
    )
st.write('\n')


# Project Introduction
st.markdown(
        f"<h5 style='text-align: left; letter-spacing:1px;font-size: 23px;color: #3b3b3b;padding:0px'><i>Вступ</i></h5><hr style='margin-top:15px; margin-bottom:10px'>", unsafe_allow_html=True)
st.write('\n')
st.write("""
Зміни економічного середовища, спричинені інфляцією та коливанням споживчих цін, створюють складні виклики для стабільності національної економіки. 
Для їх вирішення необхідно забезпечити інструменти, що дозволяють ефективно аналізувати та прогнозувати ці тенденції, допомагаючи державним органам і 
бізнесу ухвалювати обґрунтовані рішення.
""")
st.write('\n')
st.write('\n')

# Expertise
st.markdown(
        f"<h5 style='text-align: left; letter-spacing:1px;font-size: 23px;color: #3b3b3b;padding:0px'><i>Напрямки можливого використання</i></h5><hr style='margin-top:15px; margin-bottom:10px'>", unsafe_allow_html=True)
st.write('\n')
st.write("""
         <ul>
<li><b>Data Analytics:</b>Перетворення "сирих" даних в значущий аналіз.
<li><b>Machine Learning:</b> Створення моделей прогнузування.
<li><b>Business Intelligence:</b> Допомога при створенні бізнес стратегій.
<li><b>Innovation:</b> Використання креативних підходів до реальних проблем.
<li><b>Excellence:</b> Ми прагнемо надавати високоякісні результати та рішення.</ul>""", unsafe_allow_html=True)
st.write('\n')
st.write('\n')

# Consumer Price Index (CPI) Section
st.markdown(
        f"<h5 style='text-align: left; letter-spacing:1px;font-size: 23px;color: #3b3b3b;padding:0px'><i>Індекс споживчих цін (ІСЦ)?</i></h5><hr style='margin-top:15px; margin-bottom:10px'>", unsafe_allow_html=True)
st.write('\n')

st.write("""
Індекс споживчих цін (ІСЦ) характеризує зміни у часі загального рівня цін на товари та послуги, які купує населення для невиробничого споживання.
Він є показником зміни вартості фіксованого набору споживчих товарів та послуг у поточному періоді до його вартості у базисному періоді.

ІСЦ є найважливішим показником, який характеризує інфляційні процеси в економіці країни і використовується для вирішення багатьох питань 
державної політики, аналізу і прогнозу цінових процесів в економіці, перегляду розмірів грошових доходів та мінімальних соціальних гарантій 
населення, рішення правових спорів, перерахунку показників системи національних рахунків у постійні ціни.
""")
st.write('\n')
st.write('\n')

# Inflation and Cost Pressure Section
st.markdown(
        f"<h5 style='text-align: left; letter-spacing:1px;font-size: 23px;color: #3b3b3b;padding:0px'><i>Інфляція та тиск витрат</i></h5><hr style='margin-top:15px; margin-bottom:10px'>", unsafe_allow_html=True)
st.write('\n')
st.write("""
Через складність інфляційних процесів існують суперечності між різними економічними школами щодо пояснення причин її виникнення. 
Наприклад, згідно з монетарною теорією «інфляція завжди і всюди є грошовим феноменом» (Мілтон Фрідман). При цьому, визначення процесу 
зростання цін як грошового явища можливе лише за умови безперервності і тривалості в часі процесу зростання цін. Збільшення грошової 
маси (створення нових грошей) може призводити до зростання цін, однак цілком очевидним цей взаємозв'язок стає лише за високого зростання
пропозиції грошей. Окрім збільшення пропозиції грошей, існує досить багато причин виникнення і розвитку інфляційних процесів.
""")
st.write('\n')
st.write('\n')

# Role of Forecasting in Policy Making Section
st.markdown(
        f"<h5 style='text-align: left; letter-spacing:1px;font-size: 23px;color: #3b3b3b;padding:0px'><i>Роль прогнозування</i></h5><hr style='margin-top:15px; margin-bottom:10px'>", unsafe_allow_html=True)
st.write('\n')
st.write("""
Прогнозування майбутніх значень ІСЦ має важливе значення для проактивного управління економікою. Прогнозуючи тенденції інфляції, політики можуть вживати попереджувальних заходів 
керувати тиском витрат і забезпечувати економічну стабільність. Точне прогнозування дозволяє Міністерству статистики та реалізації програм (МНСІ) 
Національному статистичному управлінню (NSO) і Центральному статистичному управлінню (CSO) розробляти та впроваджувати політику, спрямовану на 
вирішення потенційних економічних проблем до їх загострення.
""")
st.write('\n')
st.write('\n')

# Decision Support System Using ARIMA and SARIMA Models Section

st.markdown(
        f"<h5 style='text-align: left; letter-spacing:1px;font-size: 23px;color: #3b3b3b;padding:0px'><i>Система Підтримки Прийняття Рішень з використанням ARIMA та SARIMA моделей</i></h5><hr style='margin-top:15px; margin-bottom:10px'>", unsafe_allow_html=True)
st.write('\n')

st.markdown(
        f"<h5 style='text-align: left; letter-spacing:1px;font-size: 21px;color: #3b3b3b;padding:0px'>Модель ARIMA</h5>", unsafe_allow_html=True)
st.write('\n')
st.write("""
ARIMA (авторегресійне інтегроване ковзне середнє) використовується для несезонних даних, що робить його ідеальним для прогнозування тенденцій інфляції, які не демонструють чітких 
сезонні моделі. Він розглядає минулі значення та зв’язок між ними для прогнозування майбутніх значень CPI.
""")
st.write('\n')
st.write('\n')

st.markdown(
        f"<h5 style='text-align: left; letter-spacing:1px;font-size: 21px;color: #3b3b3b;padding:0px'>Модель SARIMA</h5>", unsafe_allow_html=True)
st.write('\n')
st.write("""
SARIMA (Seasonal ARIMA) розширює модель ARIMA, враховуючи сезонність. Це особливо корисно під час роботи з даними, які демонструють регулярні моделі 
з часом, наприклад, сезонні коливання цін на продукти харчування. Враховуючи як тренд, так і сезонність, SARIMA надає точніші прогнози для сезонних даних.
""")
st.write('\n')
st.write('\n')

