# Query: 935A8B9278172F77

★ ★ ★ ★ ☆ 95分

```sql

SELECT  
  * 
FROM  
  mysql. USER  
WHERE  
  id= 1
```

##  不建议使用 SELECT * 类型查询

* **Item:**  COL.001

* **Severity:**  L1

* **Content:**  当表结构变更时，使用 \* 通配符选择所有列将导致查询的含义和行为会发生更改，可能导致查询返回更多的数据。

