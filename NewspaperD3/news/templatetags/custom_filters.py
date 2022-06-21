from django import template

register = template.Library()

@register.filter(name='Censor')
def Censor(input_text):
    bad_words = ['базы', 'легче', 'влиять']
    if isinstance(input_text, str):
        a = input_text.split()
        for i in a:
            if i in bad_words:
                a.remove(i)
        return ' '.join(a)
    else:
        raise ValueError(f'{input_text} не является строкой или текстом')