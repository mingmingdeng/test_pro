import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html

class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)

renderer = HighlightRenderer()
markdown = mistune.Markdown()
aa='''
# Query: C06CF2AA23DD10DB

★ ★ ★ ☆ ☆ 75分

```sql

SELECT
  *
  FROM
    mysql. USER
    ```

    ##  最外层 SELECT 未指定 WHERE 条件

    * **Item:**  CLA.001

    * **Severity:**  L4

    * **Content:**  SELECT 语句没有 WHERE 子句，可能检查比预期更多的行(全表扫描)。对于 SELECT COUNT(\*) 类型的请求如果不要求精度，建议使用 SHOW TABLE STATUS 或 EXPLAIN 替代。

    ##  不建议使用 SELECT * 类型查询

    * **Item:**  COL.001

    * **Severity:**  L1

    * **Content:**  当表结构变更时，使用 \* 通配符选择所有列将导致查询的含义和行为会发生更改，可能导致查询返回更多的数据。
'''
print(markdown(aa))
