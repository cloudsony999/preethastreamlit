import streamlit as st
import seaborn as sns

st.title('Lets learn STREAMLIT!!!!')
st.write('Hello How are U Ahana and family???')

st.markdown('**Hello How are U Preetha and family???**')

st.markdown('# I am Streamlit ')

st.markdown('''
            1. Pen
            2. Pencil
            3. Computer
            ''')
st.markdown('''
            - Pen
            - Pencil
            - Computer
            ''')

st.title('Streamlit rocks :100: :umbrella_with_rain_drops:')

st.title(':green[Streamlit] :violet[rocks]')

st.subheader('Hello Pari!!!')

st.divider()

st.code("""
        //Hello world in java
        class A
        {
        public static void main(String args[])
        {
        System.out.println("HI Preetha\n");
        }
        }      
        
        """,language='java')

st.text('Hello Sayantani',help='I am your help....')

df=sns.load_dataset('mpg')
st.title('SEABORN MPG DATASET')
st.dataframe(df.style.highlight_max(axis=0,color='green'))
st.title('SEABORN MPG DATASET in table form')
st.table(df.head(15))


st.subheader('Current Wind Speed')

st.metric("Wind","6kmph","6%")

st.divider()
st.subheader('JSON DATA...')
df=sns.load_dataset('mpg')
st.json(
    {
    'first_20_hp':list(df['horsepower'][:20])
    }
)

st.line_chart(df,x='weight',y='horsepower')

st.area_chart(df,x='weight',y='horsepower')


st.bar_chart(df,x='origin',y='cylinders')

if st.button('Click Me'):
    st.write('U have clicked me!!!')

df=sns.load_dataset('tips')

mycsv=df.to_csv(index=False)

st.download_button(
    label='CSV DOWNLOAD',
    data=mycsv,
    file_name='amitava.csv',
    mime='text/csv'
)

x=st.checkbox('click to activate')
if x:
    st.write('Hi Trisha!!!')

choice=st.radio('Male/Female',('Male','Female'))

if choice:
    st.write(f'your gender is:  **{choice}**')

z=st.selectbox('please select favourite languages',('java','sql','python','javascript','go'))


if z:
    st.write(f'the chosed language is: **{z}** ')


z=st.multiselect('please select favourite languages',('java','sql','python','javascript','go'))


if z:
    d=','
    m=d.join(z)
    st.write(f'the chosed language is: **{m}** ')










