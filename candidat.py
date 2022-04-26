class Candidates:

    def __init__(self, ident, name, picture, position, skills):
        self.ident = ident
        self.name = name
        self.pictures = picture
        self.position = position
        self.skills = skills

    def __repr__(self):
        return f"{self.name}\n{self.position}\n{self.skills}\n\n"

    

    def get_candy_info(self):
        """
        метод возвращает данные кандидата в запланированном виде
        :return:
        """
        return f"<pre>\n" \
               f"<h3>Имя кандидата - {self.name}\n" \
               f"Позиция {self.position}\n" \
               f"Навыки: {self.skills}\n</h3>" \
               f"</pre>\n\n"

    def get_foto_candy(self):
        """
        Возвращает фото кандидата
        :return:
        """
        return f"\n<img src={self.pictures}>\n"

    def chek_candy_from_id(self, input_id):
        """
        Метод проверяет вхождение ID и при наличии ID формирует фото и данные кандитата
        :param input_id: Входящий ID
        :return: возвращает фото и данные в нужном формате
        """
        if int(input_id) == int(self.ident):
            return self.get_foto_candy() + self.get_candy_info()

    def chek_candy_skill(self, input_skill):
        """
        Метод проверяет навык в списке и при совпадении возвращает данные кандидата
        :param input_skill: входящий проверяемый навык
        :return: данные кандидата с запрашиваемым навыком
        """
        temp_skills = self.skills.split(", ")
        for skill in temp_skills:
            if input_skill.lower() == skill.lower():
                get_candy_with_skill = self.get_candy_info()
            else:
                continue
            return get_candy_with_skill
