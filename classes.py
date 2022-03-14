import re


class Item:

    def __init__(self, item_string):

        self.sign = str()  # '+' or '-'
        self.value = float()  # 3.99
        self.name = str()  # 'Chick Fil A'
        self.remainder = float()  # 96.01
        self.done = False  # '~'

        self.str = item_string
        self.item_from_string()

    def __repr__(self):

        item_repr = f'{self.sign} {abs(self.value):.2f} {self.name} {self.remainder:.2f}'

        if self.done:
            item_repr += ' ~'

        return item_repr

    def item_from_string(self):

        r = r'([+-])\s(\d+\.\d{2})\s([a-zA-Z &()\']+)\s?(\-?\d+\.\d{2})?\s?(~)?'

        pattern = re.compile(r)
        matches = pattern.finditer(self.str)

        for match in matches:

            self.sign = match.group(1)
            self.value = float(match.group(2))

            if self.sign == '-':
                self.value *= -1

            self.name = match.group(3).strip()

            if (type(match.group(4)) == str) or (type(match.group(4)) == float):
                self.remainder = float(match.group(4))

            if match.group(5) == '~':
                self.done = True


class Section:

    def __init__(self, section_string):

        self.title = str()
        self.allotment = float()
        self.items = list()
        self.remainder = float()
        self.done = bool()

        self.str = section_string
        self.section_from_string()

    def section_from_string(self):

        header = self.str.split('\n')[0]
        header_info = header.split(':')
        self.title = header_info[0]
        if header_info[1]:
            self.allotment = self.remainder = float(header_info[1].strip())

        for item_given in self.str.split('\n')[1:]:
            item = Item(item_given)
            self.items.append(item)


class Budget:

    def __init__(self, path):

        self.top_sections = dict()
        self.buy_sections = dict()
        self.credit_sections = dict()

        self.path = path
        self.file = open(path).read()
        self.budget_from_file()

    def budget_from_file(self):

        for section_given in self.file.split('\n\n'):
            section = Section(section_given)

            if section.title in ('Start', 'Deductions'):
                self.top_sections.update({section.title: section})

            elif section.title in ('Charges', 'Tabs'):
                self.credit_sections.update({section.title: section})

            else:
                self.buy_sections.update({section.title: section})

    def calculate_budget(self):

        sections = list()

        for super_section in (self.top_sections, self.buy_sections, self.credit_sections):

            for section in super_section.values():

                if section.title == 'Tabs':
                    section.christian = section.items[0].value
                    section.hayley = section.items[1].value

                    for charge in self.credit_sections['Charges'].items:

                        if '(H)' in charge.name:
                            section.hayley += charge.value

                        else:
                            section.christian += charge.value

                    section_lines = [
                        f'{section.title}:',
                        f'+ {section.items[0].value:.2f} Christian {section.christian:.2f}',
                        f'+ {section.items[1].value:.2f} Hayley {section.hayley:.2f}'
                    ]
                    sections.append('\n'.join(section_lines))

                else:
                    section_lines = [f'{section.title}: {section.allotment:.2f}']

                    if section.title == 'Deductions':

                        for item in section.items:
                            section_lines.append(str(item))

                    else:
                        remainder = section.allotment

                        for item in section.items:
                            remainder += item.value

                            section.remainder = item.remainder = remainder

                            if item.done:
                                section.done = True

                            section_lines.append(str(item))

                    sections.append('\n'.join(section_lines))

        calculated_budget = '\n\n'.join(sections)

        with open(self.path, 'w') as f:
            f.write(calculated_budget)

    def current_budget(self):

        for section in self.buy_sections.values():

            if not section.done:
                print(f'{section.title}: ${section.remainder:.2f}')

    def current_charges(self):
        print(f"Christian: ${self.credit_sections['Tabs'].christian}")
        print(f"Hayley: ${self.credit_sections['Tabs'].hayley}")
