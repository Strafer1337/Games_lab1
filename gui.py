# -*- coding: utf-8 -*-

############################# dataset #############################
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.metrics import precision_score
# from sklearn.metrics import recall_score
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.naive_bayes import MultinomialNB

# from sklearn.datasets import fetch_20newsgroups
# news = fetch_20newsgroups(subset='all')
#
#
# print('Количество классов: {}'.format(len(news.target_names)))
# print('Размер датасета data: {}'.format(len(news.data)))
# print('Тип данных data: {}'.format(type(news.data[0])))
###################################################################

# import sys
# import spacy
# import pandas as pd
# import numpy as np

import PySimpleGUI as sg

# from spacy.matcher import Matcher
# import nltk.data

################################# DecisionTreeClassifier #############################
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
##################################################################

# pip install spacy, pandas, numpy, PySimpleGUI, nltk, sklearn

import warnings
warnings.filterwarnings('ignore')

#pd.set_option('display.max_colwidth', 200)
TITLE = "Продукционные правила"

IRIS_FEATURES = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

EXPORT_FILE = 'export.txt'


def get_nsubj(doc, nlp):
    pattern = [
        {'DEP': 'amod', 'OP': "*"},
        {'DEP': 'compound', 'OP': "*"},
        {'DEP': 'nsubj'},
    ]
    matcher = Matcher(nlp.vocab)
    matcher.add("matching", [pattern])
    matches = matcher(doc)
    try:
        span = doc[matches[0][1]:matches[0][2]]
    except:
        return ''
    return span.lemma_


def get_root(doc, nlp):
    pattern = [
        {'DEP': 'ROOT'}
    ]
    matcher = Matcher(nlp.vocab)
    matcher.add("matching", [pattern])
    matches = matcher(doc)
    try:
        span = doc[matches[0][1]:matches[0][2]]
    except:
        return ''
    return span.lemma_


def get_pobj(doc):
    pobjs = []
    for tok in doc:
        if tok.dep_ == 'pobj':
            pobjs.append(tok.lemma_)
    return ' '.join(pobjs)


def print_text_description(doc):
    for tok in doc:
      print(tok.text, "-->",tok.dep_,"-->", tok.pos_)


def split_text_to_sentences(doc):
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp("I. Introduction\nAlfred likes apples! A car runs over a red light.")
    """
    for sent in doc.sents:
        if sent[0].is_title and sent[-1].is_punct:
            has_noun = 2
            has_verb = 1
            for token in sent:
                if token.pos_ in ["NOUN", "PROPN", "PRON"]:
                    has_noun -= 1
                elif token.pos_ == "VERB":
                    has_verb -= 1
            if has_noun < 1 and has_verb < 1:
                print(sent.string)


def split_text_to_sentences_v2(text):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    return list((tokenizer.tokenize(text)))


def read_text_from_file(file_path):
    try:
        with open(file_path) as f:
            return f.read()
    except:
        print(f'Error reading file {file_path}')
        return ''


def nlp_class(text):
    nlp = spacy.load(r"en_core_web_sm-3.4.1")

    text_list = split_text_to_sentences_v2(text)
    # print(text_list)
    text_dict = {}
    for elem in text_list:
        doc = nlp(elem)
        if_text = f"{get_nsubj(doc, nlp)} {get_root(doc, nlp)}"
        then_text = get_pobj(doc)
        if if_text and then_text:
            text_dict[elem] = {
                'doc': doc,
                'if': if_text.strip(),
                'then': then_text.strip()
            }
        # print(f"IF {get_nsubj(doc, nlp)} {get_root(doc, nlp)} THEN {get_pobj(doc)}")

    for elem1 in text_dict:
        compares = dict()
        then_compares = dict()

        compares_sum = 0
        then_compares_sum = 0

        for elem2 in text_dict:
            compares[elem2] = text_dict[elem1]['doc'].similarity(text_dict[elem2]['doc'])
            then_elem1_doc = nlp(text_dict[elem1]['then'])
            then_elem2_doc = nlp(text_dict[elem2]['then'])
            then_compares[text_dict[elem2]['then']] = then_elem1_doc.similarity(then_elem2_doc)

            compares_sum += compares[elem2]
            then_compares_sum += then_compares[text_dict[elem2]['then']]

        text_dict[elem1]['compare'] = compares
        text_dict[elem1]['sum'] = compares_sum

        text_dict[elem1]['compare_then'] = then_compares
        text_dict[elem1]['sum_then'] = then_compares_sum

    text_dict = dict(sorted(text_dict.items(), key=lambda item: item[1]['sum_then']))

    text_res_list = []
    for elem in text_dict:
        text_res_list.append((text_dict[elem]['if'], text_dict[elem]['then'], text_dict[elem]['sum_then']))

    max_sum_then = text_res_list[-1][2]
    min_sum_then = text_res_list[0][2]
    sigma_step = round((max_sum_then - min_sum_then) / 3)
    top_res_list = []
    low_res_list = []

    top_if_bag = set()
    top_then_bag = set()
    low_if_bag = set()
    low_then_bag = set()

    for elem in text_res_list:
        if elem[2] <= min_sum_then + sigma_step:
            low_res_list.append(elem)
            low_if_bag.add(elem[0])
            low_then_bag.add(elem[1])
        elif elem[2] >= max_sum_then - sigma_step:
            top_res_list.append(elem)
            top_if_bag.add(elem[0])
            top_then_bag.add(elem[1])

    top_res_len = len(top_res_list)
    low_res_len = len(low_res_list)

    low_window_text = 'Продукционные правила нижнего приближения\n' + '-' * 70 + '\n'
    low_window_text = ""
    for elem in low_res_list:
        low_window_text += f"{elem[0]} -> {elem[1]}\n"
    # window['low'].update(low_window_text)

    top_window_text = 'Продукционные правила верхнего приближения\n' + '-' * 70 + '\n'
    top_window_text = ""
    for elem in top_res_list:
        top_window_text += f"{elem[0]} -> {elem[1]}\n"
    # window['top'].update(top_window_text)

    # for elem in text_res_list:
    #     print(elem)
    # print(top_res_list)
    # print(top_res_len)
    # window['low'].update(low_res_list)
    # print(low_res_len)
    # print(top_if_bag)
    # print(top_then_bag)
    # print(low_if_bag)
    # print(low_then_bag)
    # print(f"Точность апроксимации {len(low_then_bag) / len(top_then_bag)}")

    return len(text_res_list), low_window_text, top_window_text, len(low_then_bag) / len(top_then_bag)


def iris_class(df, y_lable=None, iris_flag=False):
    # attributes = list(df.columns)

    numeric_type = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    object_type = ['object']
    numeric_data = df.select_dtypes(include=numeric_type)

    attributes = list(numeric_data.columns)

    y_data = df.select_dtypes(include=object_type)
    y_data_cols = list(y_data.columns)
    if y_data_cols:
        y_lable = y_data_cols[0]
    else:
        y_lable = list(df.columns)[-1]
    x_attributes = attributes

    iris_classes = None
    if iris_flag:
        iris_classes = list(df[y_lable].unique())

    # if not y_lable:
    #     y_lable = attributes[-1]
    # x_attributes = [i for i in attributes if i != y_lable]

    train, test = train_test_split(df, test_size=0.4, stratify=df[y_lable], random_state=42)

    X_train = train[x_attributes]
    y_train = train[y_lable]
    X_test = test[x_attributes]
    y_test = test[y_lable]

    low_mod_dt = DecisionTreeClassifier(max_depth=None, random_state=1)
    low_mod_dt.fit(X_train, y_train)
    low_window_text = make_decision_tree_v2(low_mod_dt, iris_classes=iris_classes)

    top_mod_dt = DecisionTreeClassifier(max_depth=None, random_state=1, max_features='auto')
    top_mod_dt.fit(X_train, y_train)
    top_window_text = make_decision_tree_v2(top_mod_dt, iris_classes=iris_classes)

    precise = len(low_window_text.split('\n')) / len(top_window_text.split('\n'))

    return None, low_window_text, top_window_text, precise


def make_decision_tree_v2(clf, iris_classes=None):
    text = ''
    n_nodes = clf.tree_.node_count
    children_left = clf.tree_.children_left
    children_right = clf.tree_.children_right
    feature = clf.tree_.feature
    threshold = clf.tree_.threshold

    node_depth = np.zeros(shape=n_nodes, dtype=np.int64)
    is_leaves = np.zeros(shape=n_nodes, dtype=bool)
    stack = [(0, 0)]
    while len(stack) > 0:
        node_id, depth = stack.pop()
        node_depth[node_id] = depth

        is_split_node = children_left[node_id] != children_right[node_id]
        if is_split_node:
            stack.append((children_left[node_id], depth + 1))
            stack.append((children_right[node_id], depth + 1))
        else:
            is_leaves[node_id] = True

    # if iris_classes:
    #     print(iris_classes)

    for i in range(n_nodes):
        if is_leaves[i]:
            if iris_classes is not None:
                text += f"*** Vertex {i} is {iris_classes[i % len(iris_classes)]} class\n"
        else:
            feature_txt=feature[i]
            left=children_left[i]
            right=children_right[i]
            threshold_txt=threshold[i]
            if iris_classes is not None:
                text += f"If {IRIS_FEATURES[feature_txt]} <= {threshold_txt} then it's {left} vertex\n"
                text += f"If {IRIS_FEATURES[feature_txt]} > {threshold_txt} then it's {right} vertex\n"
            else:
                text += f"X[:, {feature_txt}] <= {threshold_txt} -> {left}\n"
                text += f"X[:, {feature_txt}] > {threshold_txt} -> {right}\n"

    return text


def main_window():
    layout = [
        [sg.Text(TITLE, justification='center', font=("Helvetica", 24))],
        [sg.Text('_' * 92)],
        [sg.Text('Выберите файл (.txt, .data)', font=("Helvetica", 16))],
        [sg.InputText(size=(45, 1), key='file_path'), sg.FileBrowse('Обзор'), sg.Submit('Загрузить')],
        [sg.Text('Если NLP задача, то введите текст в поле', font=("Helvetica", 16))],
        [sg.Multiline(size=(90, 3), key='text')],
        # [sg.InputText(size=(45, 1), key='names_file'), sg.FileBrowse('Обзор')],
        # [sg.InputText(2, size=(5, 1), key='num'), sg.Text('Число повторов косвенного синонима для попадния в колонку М2')],
        # [sg.Text('Иначе введите имя колонки Y'), sg.InputText(size=(10, 1), key='y_name')],
        [sg.Text('_' * 92)],
        [sg.Submit('Обработать')],
        [sg.Output(size=(90, 5), key='-OUTPUT-')],
        [sg.Text('_' * 92)],
        [sg.Multiline(size=(42, 5), key='low'), sg.Multiline(size=(42, 5), key='top')],
        [sg.Text('_' * 92)],
        [sg.Submit('Экспорт'), sg.Cancel('Выход')]
    ]

    window = sg.Window(TITLE, layout)
    text = ''
    df_flag = False
    iris_flag = False
    export_text = ''
    while True:
        event, values = window.read(timeout=400)
        if event in (None, 'Выход', sg.WIN_CLOSED):
            window.close()
            return None
        if event == 'Загрузить':
            iris_flag = False
            df_flag = False
            window['text'].update('')
            window['-OUTPUT-'].update('')
            file_path = values.get('file_path')
            if not file_path:
                sg.popup_error('Выберите путь к файлу')
                continue
            if file_path.endswith('.txt'):
                text = read_text_from_file(file_path)
                window['text'].update(text)
                print("Получен корпус текста")
            elif file_path.endswith('.data'):
                try:
                    df = pd.read_csv(file_path)
                    # numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
                    # df = df.select_dtypes(include=numerics)
                except Exception as e:
                    print(str(2))
                    sg.popup_error('Ошибка чтения датафрейма')
                    continue
                window['text'].update(df.describe)
                print('Получен числовой датафрейм')
                df_flag = True
                if 'iris' in file_path:
                    iris_flag = True
            else:
                sg.popup_error('Поддерживаются только .txt или .data')

        if event == 'Обработать':
            if not df_flag and text:
                print("Старт обработки ...")
                print('-' * 150)
                len_text_res_list, low_window_text, top_window_text, precise = nlp_class(text)
                print(f'Всего получено {len_text_res_list} продукционных правил')
                print('-' * 150)
                window['low'].update(low_window_text)
                window['top'].update(top_window_text)
                print(f"Точность апроксимации {precise}")
                export_text = f"Точность апроксимации {precise}\n\n" + "*" * 100 + '\n' + low_window_text + '\n' + "*" * 100 + '\n' + top_window_text
            elif df_flag:
                # y_name = values.get('y_name')
                # if not y_name:
                #     sg.popup_error('Введите имя поля Y')
                #     continue
                print("Старт обработки ...")
                print('-' * 150)
                len_text_res_list, low_window_text, top_window_text, precise = iris_class(df, iris_flag=iris_flag)
                window['low'].update(low_window_text)
                window['top'].update(top_window_text)
                print(f"Точность апроксимации {precise}")
                export_text = f"Точность апроксимации {precise}\n\n" + "*" * 100 + '\n' + low_window_text + '\n' + "*" * 100 + '\n' + top_window_text
            else:
                sg.popup_error('Введите входные данные')
                continue

        if event == 'Экспорт':
            if not export_text:
                sg.popup_error('Сначала сделайте Загрузку/Обработку')
                continue
            try:
                with open(EXPORT_FILE, 'w') as f:
                    f.write(export_text)
            except:
                sg.popup_error(f'Ошибка сохранения в файл {EXPORT_FILE}')
            else:
                sg.popup(f"Результат сохранен в {EXPORT_FILE}")


if __name__ == "__main__":
    main_window()
    sys.exit()
