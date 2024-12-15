import streamlit as st

st.set_page_config(
    page_title='포켓몬 도감',
    page_icon='./images/monsterball.png'
)

st.title('streamlit 포켓몬 도감')
st.markdown('**포켓몬**을 하나씩 추가하여 도감을 채워 보세요!')

type_emoji_dict = {
    "노말": "⚪",
    "불꽃": "🔥",
    "물": "💧",
    "풀": "🍃",
    "전기": "⚡",
    "얼음": "❄️",
    "격투": "✊",
    "독": "☠️",
    "땅": "🌋",
    "비행": "🕊",
    "에스퍼": "🔮",
    "벌레": "🐛",
    "바위": "🪨",
    "고스트": "👻",
    "드래곤": "🔷",
    "악": "😈",
    "강철": "💎",
    "페어리": "🩷"
}

# st.subheader(type_emoji_dict['드래곤'])

initial_pokemons = [
    {
        'name': '솔가레오',
        'types': ['강철'],
        'image_url': 'https://images.gameinfo.io/pokemon/256/p791.png'
    },
    {
        'name': '피카츄',
        'types': ['전기'],
        'image_url': 'https://i.namu.wiki/i/bTca2nNtVRjrLf08CrKv8fvVluVKWOjv-V3xyFEtvkKDs_yEP0h5nnjr_OYDax80NhKM8kriNO73DU6YDgRHMA.webp'
    },
    {
        'name': '망나뇽',
        'types': ['드래곤'],
        'image_url': 'https://i.namu.wiki/i/vEcT1migAadfyRShzZCAyImwR1WJp5u6mXXEUC_hYQ1A8G3Qe3i4EyUuYEkh05-vTuj7G_XNAm_69DkqAcpTbw.webp'
    },
    {
        'name': '칠색조',
        'types': ['불꽃'],
        'image_url': 'https://i.namu.wiki/i/qHoxGtaOaS_w975pfEjGPqSvHu2ersxWlQEw7tbtrUY8PlEuYvSHJBEhpEWVHizT6DgWAl0wyCt6pv0lwDemBw.webp'
    },
    {
        'name': '뮤',
        'types': ['에스퍼'],
        'image_url': 'https://i.namu.wiki/i/-4E6V5ThdKH8pwtEQE1agME-EXunTxFDtrg2WbfxNWzOec_bTdwIgzo0FZn9yDiwRnNpmbxlxiSjBCTNPhkW8g.webp'
    }
]

example_pokemon = {
    "name": "알로라 디그다",
    "types": ["땅", "강철"],
    "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/alora_digda.webp"
}

if "pokemons" not in st.session_state:
    st.session_state.pokemons = initial_pokemons

auto_complete = st.toggle("예시 데이터로 채우기")
print("page_reload, auto_complte", auto_complete)
with st.form(key='form'):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(
            label='포켓몬 이름',
            value=example_pokemon["name"] if auto_complete else "")
    with col2:
        types = st.multiselect(
            label='포켓몬 속성',
            options=list(type_emoji_dict.keys()),
            max_selections=2,
            default=example_pokemon["types"] if auto_complete else []
        )
    image_url = st.text_input(label='포켓몬 이미지 URL',
                              value=example_pokemon["image_url"] if auto_complete else "")
    submit = st.form_submit_button('Submit')
    if submit:
        if not name:
            st.error("포켓몬의 이름을 입력해주세요")
        elif len(types) == 0:
            st.error("포켓몬의 속성을 적어도 한개 선택해주세요")
        else:
            st.success("포켓몬을 추가 할 수 있습니다")
            st.session_state.pokemons.append({
                "name": name,
                "types": types,
                "image_url": image_url if image_url else "./images/monsterball.png"
            })

for j in range(0, len(st.session_state.pokemons), 3):
    row_pokemons = st.session_state.pokemons[j:j + 3]
    cols = st.columns(3)
    for i in range(len(row_pokemons)):

        with cols[i]:
            pokemon = row_pokemons[i]
            with st.expander(label=f'**{i + j + 1}. {pokemon['name']}**', expanded=True):
                st.image(pokemon['image_url'])
                emoji_types = []
                for type in pokemon['types']:
                    emoji_types.append(f'{type_emoji_dict[type]} {type}')
                st.subheader(' / '.join(emoji_types))
                delete_button = st.button(label="삭제", key=i + j, use_container_width=True)
                if delete_button:
                    print("delete button clicked!")
                    del st.session_state.pokemons[i + j]
                    st.rerun()