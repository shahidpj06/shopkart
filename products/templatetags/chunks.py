from django import template

register = template.Library()

@register.filter(name='chunks')
def chunks(list_data, chunk_size):
    chunk = []
    count = 0
    for data in list_data:
        chunk.append(data)
        count += 1
        if count == chunk_size:
            yield chunk
            count = 0
            chunk = []
    if chunk:        
        yield chunk