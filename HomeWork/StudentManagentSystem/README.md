# python学生信息管理系统

## 基于面向对象设计

### 分为三层架构

1. Dao（数据层）：负责数据的存储和读取，暂时使用内存变量。
2. Service（业务逻辑层）：负责业务逻辑的处理，包括数据的增删改查等。
3. View(视图层)：负责数据的展示，暂时使用控制台输出。

### 实现功能

1. 学生信息管理：增删改查

### 项目目录

```
├── Dao
│ └── StudentDao.py
├── Pojo
│ └── Student.py
├── Service
│ └── StudentService.py
├── Utils
│ └── ListUtils.py
│ └── ResultUtils.py
├── View
│ └── StudentView.py
├── main.py
```
