## 授業前課題_Python 演習_2


course_dict = {
     'AIコース': {'Aさん', 'Cさん', 'Dさん'},
     'Railsコース': {'Bさん', 'Cさん', 'Eさん'},
     'Railsチュートリアルコース': {'Gさん', 'Fさん', 'Eさん'},
    'JS': {'Aさん', 'Gさん', 'Hさん'},
     }

        def find_person(want_to_find_person):
        """
        受講生がどのコースに在籍しているかを出力する。
        まずはフローチャートを書いて、どのようにアルゴリズムを解いていくか考えてみましょう。
        """
        #a = 'want_to_find_person' & 'AIコース'
         b = 'want_to_find_person' & 'Railsコース'
         c = 'want_to_find_person' & 'Railsチュートリアルコース'
         d = 'want_to_find_person' & 'JS'

        def main():
        want_to_find_person = {'Cさん', 'Aさん'}
        print('探したい人: {}'.format(want_to_find_person))
        find_person(want_to_find_person)

        if __name__ == '__main__':
        main()
