import re

letters = 'ЫбВЫуЯСдущДШНККАеЩЙФеРФО'
print(re.sub(r'[А-ЯЁ]', '', letters))
